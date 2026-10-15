#!/usr/bin/env python3
"""Build premium per-creator PERFORMANCE REPORTS (static) from creators.json.

  python3 build_reports.py            -> writes ./dist

Generic across brands: everything brand-specific lives in creators.json's "config" block.
Output: one PRIVATE page per creator (slug + unguessable token) + a team overview at an
unguessable path + a neutral public root (no creator list). Videos are remote Atria URLs
(no downloads). Commission is computed from each conversion value (one rate), labelled as
simulated until the real payout platform is wired. See the mlo-creator-report skill.
"""
import hashlib, html, json, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "creators.json")
HISTORY = os.path.join(HERE, "history.json")   # previous snapshot per slug, for ▲/▼ trend (written by the refresh task)
DIST = os.path.join(HERE, "dist")

# --- config (filled from creators.json["config"] in main) ---
CFG = {}
CDN = ""
SALT = ""
COMMISSION_RATE = 0.10
PLATFORM = "the platform"
BRAND = "Brand"
BENCH = {"hook": "", "ctr": ""}
LANG = "en"               # "en" or "es" (config.lang)
SHOW_COMMISSION = True     # config.showCommission — set False for brands paid outside the platform
CUR = "€"                 # currency symbol (config.currency)

# --- i18n: every creator-facing string. T("key") resolves in the configured language. ---
STRINGS = {
  "en": {
    "creator_report":"Creator Report","report_team":"Creator Reports · Team","reports_team_title":"Creator Reports",
    "private_badge":"🔒 Private · your personal report",
    "cover_h1":"Your work,<br><span class=\"serif\">and what’s next.</span>",
    "cover_sub":"What your content is doing right now, why it works, and what to film next.",
    "your_status":"Your status","conv_value":"Conversion value","your_earnings":"Your earnings","roas":"ROAS",
    "ad_spend":"Ad spend","orders":"Orders","sales_drove":"Sales your videos drove","ret_on_spend":"Return on ad spend",
    "behind_content":"Behind your content","impressions":"impressions","report":"Report","product":"Product","angle":"Angle",
    "sec01":"Your videos","sec01_sub":"Every creative of yours we’re running, and the sales it drove.",
    "sec01_sub_comm":" <b>Your earnings are simulated at {rate}%</b> — they go live once {platform} is set up.",
    "hook_rate":"Hook rate","ctr":"CTR","hold":"Hold 15s","vs_avg":"vs {v} avg","sound_on":"Sound on","sound_off":"Sound off",
    "sec02":"Why it works","sec02_sub":"The structure behind your winner — the skeleton to keep using.",
    "sec03":"Keep doing / push further","sec03_sub":"What’s working, and where the next gain is.",
    "keep_doing":"Keep doing","push_further":"Push further",
    "sec04":"Film these next","sec04_sub":"Three briefs built from what’s working for you. Start with #1.",
    "why":"Why:","cta_t":"Your next brief is ready","cta_s":"Pick one above, film it your way, and send us your raw footage — we handle the rest.","shoot_by":"Shoot by {date}",
    "sec05":"What happens next","sec05_sub":"From shoot to live — you’re always in the loop before anything runs.",
    "tl1_d":"This week","tl1_l":"Brief received","tl1_n":"Questions before you shoot? Reply any time.",
    "tl2_d":"+3 days","tl2_l":"Raw footage → Drive","tl2_n":"2–3 takes per video. No editing needed — we handle it.",
    "tl3_d":"+5 days","tl3_l":"Edited cuts for your review","tl3_n":"See the finished edits before they go live.",
    "tl4_d":"+1 week","tl4_l":"Live & into testing","tl4_n":"Tracked against your current winners.",
    "tl5_d":"Next refresh","tl5_l":"This report updates","tl5_n":"Fresh numbers and a new brief, on a regular cadence.",
    "sec05_note":"<b>Keep going.</b> Your content is one of the signals carrying the account. This report refreshes on a regular cadence so you always know what’s working.",
    "ov_sub":"Internal overview — all top {brand} creators. {updated}. Each creator gets only their own private link.",
    "earnings":"Earnings","open_report":"Open report →","sim_live":"Simulated · live with {platform}",
    "root_h1":"Your report is<br><span class=\"serif\">private.</span>",
    "root_sub":"Open the personal link we sent you to see your videos, results and next brief. If you don’t have it, message your {brand} contact.",
    "flat":"→ flat","vs_last":"vs last",
  },
  "es": {
    "creator_report":"Reporte de Creador","report_team":"Reportes de Creador · Equipo","reports_team_title":"Reportes de Creador",
    "private_badge":"🔒 Privado · tu reporte personal",
    "cover_h1":"Tu trabajo,<br><span class=\"serif\">y lo que viene.</span>",
    "cover_sub":"Qué está haciendo tu contenido ahora mismo, por qué funciona y qué grabar a continuación.",
    "your_status":"Tu estado","conv_value":"Valor de conversión","your_earnings":"Tus ganancias","roas":"ROAS",
    "ad_spend":"Inversión","orders":"Pedidos","sales_drove":"Ventas que generó tu contenido","ret_on_spend":"Retorno sobre inversión",
    "behind_content":"Detrás de tu contenido","impressions":"impresiones","report":"Reporte","product":"Producto","angle":"Ángulo",
    "sec01":"Tus vídeos","sec01_sub":"Cada creativo tuyo que tenemos activo, y las ventas que generó.",
    "sec01_sub_comm":" <b>Tus ganancias están simuladas al {rate}%</b> — se activan en cuanto montemos {platform}.",
    "hook_rate":"Hook rate","ctr":"CTR","hold":"Hold 15s","vs_avg":"vs {v} media","sound_on":"Sonido","sound_off":"Silencio",
    "sec02":"Por qué funciona","sec02_sub":"La estructura detrás de tu ganador — el esqueleto que debes seguir usando.",
    "sec03":"Mantén / mejora","sec03_sub":"Qué funciona, y dónde está la siguiente mejora.",
    "keep_doing":"Mantén","push_further":"Mejora",
    "sec04":"Graba esto a continuación","sec04_sub":"Tres briefs construidos sobre lo que te funciona. Empieza por el #1.",
    "why":"Por qué:","cta_t":"Tu próximo brief está listo","cta_s":"Elige uno de arriba, grábalo a tu manera y mándanos el bruto — del resto nos encargamos nosotros.","shoot_by":"Grábalo antes del {date}",
    "sec05":"Qué pasa ahora","sec05_sub":"De la grabación a estar live — siempre lo ves antes de que salga nada.",
    "tl1_d":"Esta semana","tl1_l":"Brief recibido","tl1_n":"¿Dudas antes de grabar? Escríbenos cuando quieras.",
    "tl2_d":"+3 días","tl2_l":"Bruto → Drive","tl2_n":"2-3 tomas por vídeo. Sin editar — de eso nos encargamos.",
    "tl3_d":"+5 días","tl3_l":"Cortes editados para tu revisión","tl3_n":"Ves los edits finales antes de que salgan.",
    "tl4_d":"+1 semana","tl4_l":"Live y en testing","tl4_n":"Medido contra tus ganadores actuales.",
    "tl5_d":"Próximo refresh","tl5_l":"Este reporte se actualiza","tl5_n":"Números frescos y un brief nuevo, con cadencia regular.",
    "sec05_note":"<b>Sigue así.</b> Tu contenido es una de las señales que sostienen la cuenta. Este reporte se actualiza con cadencia regular para que siempre sepas qué funciona.",
    "ov_sub":"Vista interna — todos los creadores top de {brand}. {updated}. Cada creador recibe solo su propio enlace privado.",
    "earnings":"Ganancias","open_report":"Abrir reporte →","sim_live":"Simulado · real con {platform}",
    "root_h1":"Tu reporte es<br><span class=\"serif\">privado.</span>",
    "root_sub":"Abre el enlace personal que te enviamos para ver tus vídeos, resultados y próximo brief. Si no lo tienes, escribe a tu contacto en {brand}.",
    "flat":"→ sin cambio","vs_last":"vs anterior",
  },
}

def T(key, **kw):
    s = STRINGS.get(LANG, STRINGS["en"]).get(key, STRINGS["en"].get(key, key))
    return s.format(**kw) if kw else s

def token(slug):
    return hashlib.sha1((slug + "|" + SALT).encode()).hexdigest()[:10]

def e(s): return html.escape(str(s if s is not None else ""))

def num(s):
    """Parse '€1,663' / '43%' / '1.20x' -> float, or None."""
    try:
        return float(str(s).replace("€", "").replace(",", "").replace("%", "").replace("x", "").strip())
    except (ValueError, AttributeError):
        return None

def comm(value_str):
    """Simulated creator payout = COMMISSION_RATE of the conversion value string (e.g. '€1,663')."""
    n = num(value_str)
    if n is None:
        return "—"
    return CUR + format(int(round(n * COMMISSION_RATE)), ",d")

def delta(cur, prev):
    """Small ▲/▼ chip vs previous period. Empty when there is no comparable history."""
    c, p = num(cur), num(prev)
    if c is None or p is None or p == 0:
        return ""
    pct = (c - p) / p * 100
    if abs(pct) < 1:
        return '<span class="delta flat">' + T("flat") + '</span>'
    arrow, cls = ("▲", "up") if pct > 0 else ("▼", "down")
    return '<span class="delta ' + cls + '">' + arrow + " " + format(abs(round(pct)), "d") + "% " + T("vs_last") + "</span>"

def hex_rgb(h):
    h = h.lstrip("#")
    return ",".join(str(int(h[i:i+2], 16)) for i in (0, 2, 4))

# Default amber theme. main() rebrands it by replacing the accent tokens from config.
CSS_TEMPLATE = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
:root{
  --bg:#0A0A0C; --bg-panel:rgba(255,255,255,0.038); --bg-panel-2:rgba(255,255,255,0.06); --panel-border:rgba(255,255,255,0.09);
  --accent:#E0A569; --accent-glow:rgba(224,165,105,0.28);
  --good:#7FD1A6; --warn:#E6C06A; --bad:#E08A7A;
  --text:#F3EFEA; --text-dim:#9A938A;
  --serif:"Playfair Display",Georgia,serif; --mono:"JetBrains Mono",monospace; color-scheme:dark;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:"DM Sans",system-ui,sans-serif;font-size:15px;line-height:1.5}
section{position:relative;width:100%;min-height:100vh;padding:52px 80px 76px;display:flex;flex-direction:column;justify-content:center;border-bottom:1px solid rgba(255,255,255,0.06);overflow:hidden}
@media(max-width:640px){section{padding:40px 20px 60px;min-height:auto}}
.glow{position:absolute;background:radial-gradient(circle,var(--accent-glow) 0%,transparent 65%);pointer-events:none;z-index:0}
section>*{position:relative;z-index:1}
section>.glow{position:absolute;z-index:0}
.logo-bar{display:flex;align-items:center;gap:8px;margin-bottom:30px}
.logo-dot{width:8px;height:8px;border-radius:50%;background:var(--accent);box-shadow:0 0 10px var(--accent-glow);flex-shrink:0}
.logo-text{font-size:11px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--text-dim)}
.sec-head{display:flex;align-items:baseline;gap:14px;margin-bottom:6px;flex-wrap:wrap}
.sec-num{font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:600}
h1{font-size:clamp(34px,5vw,50px);font-weight:800;line-height:1.08;letter-spacing:-0.5px;margin-bottom:14px;text-wrap:balance}
h1 .serif{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--accent)}
h2{font-size:27px;font-weight:800;letter-spacing:-0.3px;text-wrap:balance}
.subtitle{font-size:15px;color:var(--text-dim);line-height:1.55;max-width:640px;margin:8px 0 24px}
.subtitle b{color:var(--text)}
.read-badge{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:600;letter-spacing:0.5px;color:var(--text-dim);border:1px solid var(--panel-border);border-radius:999px;padding:5px 12px;margin-bottom:20px;align-self:flex-start}
.meta-row{display:flex;gap:44px;flex-wrap:wrap;margin-top:36px}
.meta-item{display:flex;flex-direction:column;gap:5px}
.meta-label{font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--text-dim)}
.meta-value{font-size:14px;font-weight:600}
.creator-badge{display:flex;align-items:center;gap:14px;margin-bottom:26px}
.creator-avatar{width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,var(--accent) 0%,#8a5a33 100%);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:800;color:#2a1708;flex-shrink:0;box-shadow:0 0 22px var(--accent-glow)}
.creator-name{font-size:17px;font-weight:700}
.creator-role{font-size:12px;color:var(--text-dim);margin-top:2px}
.pill{display:inline-flex;align-items:center;gap:5px;font-size:10.5px;font-weight:700;letter-spacing:0.4px;text-transform:uppercase;padding:5px 12px;border-radius:999px;white-space:nowrap}
.pill-scale{background:rgba(127,209,166,0.12);border:1px solid rgba(127,209,166,0.4);color:var(--good)}
.pill-test{background:rgba(230,192,106,0.1);border:1px solid rgba(230,192,106,0.35);color:var(--warn)}
.pill-pause{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.14);color:var(--text-dim)}
.metric-row{display:flex;gap:14px;flex-wrap:wrap;margin-top:14px}
.metric-chip{background:var(--bg-panel);border:1px solid var(--panel-border);border-radius:12px;padding:16px 20px;min-width:140px}
.metric-chip.hero{border-color:rgba(224,165,105,0.35);background:linear-gradient(135deg,rgba(224,165,105,0.1),rgba(224,165,105,0.03))}
.mc-label{font-size:10px;text-transform:uppercase;letter-spacing:0.8px;color:var(--text-dim)}
.mc-value{font-size:24px;font-weight:800;margin-top:4px;font-variant-numeric:tabular-nums}
.mc-note{font-size:11.5px;color:var(--text-dim);margin-top:3px}
.vid-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-top:18px}
@media(max-width:640px){.vid-grid{grid-template-columns:1fr}}
.vid-card{background:var(--bg-panel);border:1px solid var(--panel-border);border-radius:18px;overflow:hidden;display:flex;flex-direction:column}
.vid-card.scale{border-color:rgba(127,209,166,0.3)}
.vid-card.test{border-color:rgba(230,192,106,0.28)}
.vid-card.pause{border-color:var(--panel-border)}
.vid-thumb{position:relative;aspect-ratio:9/16;background:#14110d;display:flex;align-items:center;justify-content:center;overflow:hidden}
.vid-thumb video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vid-code{position:absolute;top:12px;left:12px;z-index:2;font-family:var(--mono);font-size:10px;color:rgba(255,255,255,0.55);background:rgba(0,0,0,0.55);padding:3px 8px;border-radius:6px}
.vid-status-badge{position:absolute;top:12px;right:12px;z-index:2}
.vid-sound{position:absolute;bottom:10px;right:10px;z-index:3;background:rgba(0,0,0,0.6);color:#fff;border:0;border-radius:999px;font:600 11px "DM Sans",sans-serif;padding:6px 11px;cursor:pointer}
.vid-hook-overlay{position:absolute;bottom:0;left:0;right:0;z-index:2;padding:46px 16px 14px;background:linear-gradient(to top,rgba(0,0,0,0.9) 0%,transparent 100%);font-family:var(--serif);font-style:italic;font-size:14px;line-height:1.4;color:rgba(255,255,255,0.92);pointer-events:none}
.vid-body{padding:14px 18px 18px}
.vid-angle{font-size:12px;color:var(--text-dim);margin-bottom:10px}
.vid-metrics{display:flex;border-top:1px solid rgba(255,255,255,0.07);padding-top:11px}
.vid-metric{flex:1;text-align:center;border-right:1px solid rgba(255,255,255,0.07);padding:0 8px}
.vid-metric:first-child{text-align:left;padding-left:0}
.vid-metric:last-child{border-right:none}
.vm-label{font-size:10px;text-transform:uppercase;letter-spacing:0.7px;color:var(--text-dim)}
.vm-value{font-size:17px;font-weight:800;margin-top:3px;font-variant-numeric:tabular-nums}
.up{color:var(--good)}.down{color:var(--bad)}.flat{color:var(--text-dim)}
.mc-note .delta,.vm-note .delta{font-weight:700}
.delta.up{color:var(--good)}.delta.down{color:var(--bad)}.delta.flat{color:var(--text-dim)}
.vm-note{font-size:10px;color:var(--text-dim);margin-top:2px;letter-spacing:0.2px}
.cta-block{display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;background:linear-gradient(135deg,rgba(224,165,105,0.12),rgba(224,165,105,0.03));border:1px solid rgba(224,165,105,0.35);border-radius:16px;padding:22px 26px;margin-top:22px}
.cta-block .cta-t{font-size:17px;font-weight:800}
.cta-block .cta-s{font-size:13px;color:var(--text-dim);margin-top:3px}
.cta-block .cta-btn{background:var(--accent);color:#2a1708;font-weight:800;font-size:14px;padding:12px 20px;border-radius:999px;white-space:nowrap}
.callout{background:var(--bg-panel);border-left:3px solid var(--accent);border-radius:10px;padding:15px 20px;margin-top:18px;font-size:13.5px;line-height:1.55}
.callout b{color:var(--text)}
.formula-strip{display:grid;grid-template-columns:repeat(var(--n,5),1fr);gap:10px;margin-top:20px}
@media(max-width:760px){.formula-strip{grid-template-columns:1fr;gap:8px}}
.fstep{background:var(--bg-panel);border:1px solid var(--panel-border);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:8px}
.fstep-top{display:flex;align-items:center;justify-content:space-between}
.fstep-time{font-family:var(--mono);font-size:10px;color:var(--text-dim)}
.fstep-no{width:20px;height:20px;border-radius:50%;background:var(--accent);color:#2a1708;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center}
.fstep-label{font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:0.4px}
.fstep-quote{font-family:var(--serif);font-style:italic;font-size:12.5px;line-height:1.4;color:rgba(224,165,105,0.85)}
.ki-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:18px}
@media(max-width:760px){.ki-grid{grid-template-columns:1fr}}
.ki-card{background:var(--bg-panel);border:1px solid var(--panel-border);border-radius:16px;padding:24px 26px}
.ki-card.keep{border-color:rgba(127,209,166,0.26)}
.ki-card.push{border-color:rgba(230,192,106,0.24)}
.ki-title{display:flex;align-items:center;gap:9px;font-size:15px;font-weight:800;margin-bottom:16px}
.ki-title .dot{width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.ki-card.keep .dot{background:rgba(127,209,166,0.15)}
.ki-card.push .dot{background:rgba(230,192,106,0.14)}
.ki-list{list-style:none;display:flex;flex-direction:column}
.ki-list li{padding:11px 0;border-bottom:1px solid rgba(255,255,255,0.06);display:flex;flex-direction:column;gap:3px}
.ki-list li:last-child{border-bottom:none;padding-bottom:0}
.ki-item{font-size:14px;font-weight:600}
.ki-why{font-size:12px;color:var(--text-dim);line-height:1.45}
.brief-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:18px}
@media(max-width:900px){.brief-grid{grid-template-columns:1fr}}
.brief-card{background:var(--bg-panel);border:1px solid var(--panel-border);border-radius:16px;padding:24px 22px;display:flex;flex-direction:column;gap:14px}
.brief-card.priority{border-color:rgba(224,165,105,0.3);background:linear-gradient(160deg,rgba(224,165,105,0.05),transparent 60%)}
.brief-top{display:flex;align-items:center;justify-content:space-between}
.brief-num{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent)}
.brief-hook{font-family:var(--serif);font-style:italic;font-size:18px;font-weight:700;line-height:1.35;color:var(--text)}
.brief-tags{display:flex;flex-wrap:wrap;gap:6px}
.brief-tag{font-size:11px;color:var(--text-dim);background:var(--bg-panel-2);border:1px solid var(--panel-border);border-radius:6px;padding:4px 10px}
.brief-goal{font-size:12px;color:var(--text-dim);line-height:1.5;border-top:1px solid rgba(255,255,255,0.07);padding-top:12px;margin-top:auto}
.brief-goal b{color:var(--text)}
.tl-row{display:flex;flex-direction:column;padding-left:22px;position:relative;margin-top:20px}
.tl-row::before{content:'';position:absolute;left:5px;top:8px;bottom:8px;width:2px;background:linear-gradient(to bottom,var(--accent),rgba(224,165,105,0.1))}
.tl-item{position:relative;padding:0 0 18px 18px}
.tl-dot{position:absolute;left:-18px;top:4px;width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 8px var(--accent-glow)}
.tl-dot.dim{background:rgba(255,255,255,0.2);box-shadow:none}
.tl-date{font-size:10.5px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--accent);margin-bottom:2px}
.tl-date.dim{color:var(--text-dim)}
.tl-label{font-size:14px;font-weight:700}
.tl-note{font-size:12.5px;color:var(--text-dim);line-height:1.45;margin-top:1px}
.footer-tag{position:absolute;bottom:22px;left:80px;right:80px;display:flex;justify-content:space-between;color:var(--text-dim);font-size:11px;letter-spacing:0.5px;z-index:1}
@media(max-width:640px){.footer-tag{left:20px;right:20px}}
.idx-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin-top:26px}
.idx-card{display:block;text-decoration:none;color:inherit;background:var(--bg-panel);border:1px solid var(--panel-border);border-radius:18px;padding:24px;transition:border-color .2s,transform .15s}
.idx-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.idx-head{display:flex;align-items:center;gap:12px;margin-bottom:16px}
.idx-av{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,var(--accent),#8a5a33);display:flex;align-items:center;justify-content:center;font-weight:800;color:#2a1708;flex-shrink:0}
.idx-name{font-size:16px;font-weight:700}
.idx-role{font-size:11.5px;color:var(--text-dim);margin-top:1px}
.idx-metrics{display:flex;gap:18px;border-top:1px solid rgba(255,255,255,0.07);padding-top:14px}
.idx-m .l{font-size:9.5px;text-transform:uppercase;letter-spacing:0.7px;color:var(--text-dim)}
.idx-m .v{font-size:17px;font-weight:800;margin-top:2px;font-variant-numeric:tabular-nums}
.idx-go{margin-top:14px;font-size:12.5px;font-weight:700;color:var(--accent)}
"""

def css():
    """Rebrand the default amber CSS to the configured accent."""
    c = CSS_TEMPLATE
    accent = CFG.get("accent", "#E0A569")
    accent_dark = CFG.get("accentDark", "#8a5a33")
    accent_ink = CFG.get("accentInk", "#2a1708")
    c = c.replace("#E0A569", accent).replace("#8a5a33", accent_dark).replace("#2a1708", accent_ink)
    c = c.replace("224,165,105", hex_rgb(accent))
    return c

def footer(label, upd):
    return '<div class="footer-tag"><span>'+e(label)+'</span><span>'+e(upd)+'</span></div>'

def earn_note():
    return T("sim_live", platform=PLATFORM)

def ad_card(a):
    earn_cell = ('<div class="vid-metric"><div class="vm-label">'+T("your_earnings")+'</div><div class="vm-value" style="color:var(--accent)">'+comm(a["gmv"])+'</div></div>') if SHOW_COMMISSION else ''
    return (
        '<div class="vid-card '+e(a["statusClass"])+'">'
        '<div class="vid-thumb">'
        '<div class="vid-code">'+e(a["code"])+'</div>'
        '<div class="vid-status-badge"><span class="pill pill-'+e(a["statusClass"])+'">'+e(a["statusEmoji"])+' '+e(a["statusLabel"])+'</span></div>'
        '<video muted loop playsinline preload="metadata" poster="'+CDN+e(a["poster"])+'" src="'+CDN+e(a["video"])+'"></video>'
        '<button class="vid-sound" type="button" onclick="var v=this.previousElementSibling;v.muted=!v.muted;v.play();this.textContent=v.muted?this.dataset.on:this.dataset.off" data-on="'+T("sound_on")+'" data-off="'+T("sound_off")+'">'+T("sound_on")+'</button>'
        '<div class="vid-hook-overlay">“'+e(a["hook"])+'”</div>'
        '</div>'
        '<div class="vid-body">'
        '<div class="vid-angle">'+e(a["angle"])+'</div>'
        '<div class="vid-metrics">'
        '<div class="vid-metric"><div class="vm-label">'+T("conv_value")+'</div><div class="vm-value up">'+e(a["gmv"])+'</div></div>'
        +earn_cell+
        '<div class="vid-metric"><div class="vm-label">'+T("roas")+'</div><div class="vm-value">'+e(a["roas"])+'</div></div>'
        '<div class="vid-metric"><div class="vm-label">'+T("orders")+'</div><div class="vm-value">'+e(a["orders"])+'</div></div>'
        '</div>'
        '<div class="vid-metrics">'
        '<div class="vid-metric"><div class="vm-label">'+T("hook_rate")+'</div><div class="vm-value up">'+e(a["hookRate"])+'</div>'+('<div class="vm-note">'+T("vs_avg", v=e(BENCH["hook"]))+'</div>' if BENCH["hook"] else '')+'</div>'
        '<div class="vid-metric"><div class="vm-label">'+T("ctr")+'</div><div class="vm-value">'+e(a["ctr"])+'</div>'+('<div class="vm-note">'+T("vs_avg", v=e(BENCH["ctr"]))+'</div>' if BENCH["ctr"] else '')+'</div>'
        '<div class="vid-metric"><div class="vm-label">'+T("hold")+'</div><div class="vm-value">'+e(a["hold"])+'</div></div>'
        '</div></div></div>'
    )

def report_html(c, meta, prev, stylesheet):
    upd = meta["updated"]; st = c["status"]; prev = prev or {}
    rate_pct = str(int(round(COMMISSION_RATE * 100)))
    earn_chip = ('<div class="metric-chip hero"><div class="mc-label">'+T("your_earnings")+' · '+rate_pct+'%</div><div class="mc-value" style="color:var(--accent)">'+comm(c["totals"]["gmv"])+'</div><div class="mc-note">'+e(earn_note())+'</div></div>') if SHOW_COMMISSION else ''
    cover = (
        '<section><div class="glow" style="bottom:-300px;left:-220px;width:1100px;height:1100px;opacity:0.5"></div>'
        '<div class="logo-bar"><div class="logo-dot"></div><span class="logo-text">'+e(BRAND)+' · '+T("creator_report")+'</span></div>'
        '<div class="read-badge">'+T("private_badge")+'</div>'
        '<div class="creator-badge"><div class="creator-avatar">'+e(c["initials"])+'</div>'
        '<div><div class="creator-name">'+e(c["name"])+'</div><div class="creator-role">'+e(c["role"])+'</div></div></div>'
        '<h1>'+T("cover_h1")+'</h1>'
        '<div class="subtitle">'+T("cover_sub")+'</div>'
        '<div class="metric-row">'
        '<div class="metric-chip hero"><div class="mc-label">'+T("your_status")+'</div><div class="mc-value" style="color:var(--accent)">'+e(st["emoji"])+' '+e(st["label"])+'</div><div class="mc-note">'+e(st["note"])+'</div></div>'
        '<div class="metric-chip"><div class="mc-label">'+T("conv_value")+'</div><div class="mc-value up">'+e(c["totals"]["gmv"])+'</div><div class="mc-note">'+(delta(c["totals"]["gmv"], prev.get("gmv")) or T("sales_drove"))+'</div></div>'
        +earn_chip+
        '<div class="metric-chip"><div class="mc-label">'+T("roas")+'</div><div class="mc-value">'+e(c["totals"]["roas"])+'</div><div class="mc-note">'+T("ret_on_spend")+'</div></div>'
        '<div class="metric-chip"><div class="mc-label">'+T("ad_spend")+'</div><div class="mc-value">'+e(c["totals"]["adspend"])+'</div><div class="mc-note">'+T("behind_content")+'</div></div>'
        '<div class="metric-chip"><div class="mc-label">'+T("orders")+'</div><div class="mc-value">'+e(c["totals"]["orders"])+'</div><div class="mc-note">'+e(c["totals"]["impressions"])+' '+T("impressions")+'</div></div>'
        '</div>'
        '<div class="meta-row">'
        '<div class="meta-item"><div class="meta-label">'+T("report")+'</div><div class="meta-value">'+e(upd)+'</div></div>'
        '<div class="meta-item"><div class="meta-label">'+T("product")+'</div><div class="meta-value">'+e(c["product"])+'</div></div>'
        '<div class="meta-item"><div class="meta-label">'+T("angle")+'</div><div class="meta-value">'+e(meta["angle"])+'</div></div>'
        '</div>'+footer(T("creator_report").upper()+" · "+c["name"].upper(), upd)+'</section>'
    )
    ads_sub = T("sec01_sub") + (T("sec01_sub_comm", rate=rate_pct, platform=e(PLATFORM)) if SHOW_COMMISSION else "")
    ads = (
        '<section><div class="glow" style="top:-260px;right:-200px;width:960px;height:960px;opacity:0.45"></div>'
        '<div class="sec-head"><span class="sec-num">01</span><h2>'+T("sec01")+'</h2></div>'
        '<div class="subtitle">'+ads_sub+'</div>'
        '<div class="vid-grid">'+''.join(ad_card(a) for a in c["ads"])+'</div>'
        '<div class="callout">'+e(c["callout"])+'</div>'
        +footer(T("creator_report").upper()+" · 01", upd)+'</section>'
    )
    steps = c["formula"]
    fsteps = ''.join(
        '<div class="fstep"><div class="fstep-top"><span class="fstep-time">'+e(s["time"])+'</span><span class="fstep-no">'+str(i+1)+'</span></div>'
        '<div class="fstep-label">'+e(s["label"])+'</div><div class="fstep-quote">“'+e(s["quote"])+'”</div></div>'
        for i,s in enumerate(steps))
    formula = (
        '<section><div class="glow" style="bottom:-200px;left:-160px;width:900px;height:900px;opacity:0.4"></div>'
        '<div class="sec-head"><span class="sec-num">02</span><h2>'+T("sec02")+'</h2></div>'
        '<div class="subtitle">'+T("sec02_sub")+'</div>'
        '<div class="formula-strip" style="--n:'+str(len(steps))+'">'+fsteps+'</div>'
        '<div class="callout">'+e(c["formulaNote"])+'</div>'
        +footer(T("creator_report").upper()+" · 02", upd)+'</section>'
    )
    keep = ''.join('<li><span class="ki-item">'+e(k["item"])+'</span><span class="ki-why">'+e(k["why"])+'</span></li>' for k in c["keep"])
    push = ''.join('<li><span class="ki-item">'+e(p["item"])+'</span><span class="ki-why">'+e(p["why"])+'</span></li>' for p in c["push"])
    kp = (
        '<section><div class="glow" style="top:-220px;right:-180px;width:900px;height:900px;opacity:0.4"></div>'
        '<div class="sec-head"><span class="sec-num">03</span><h2>'+T("sec03")+'</h2></div>'
        '<div class="subtitle">'+T("sec03_sub")+'</div>'
        '<div class="ki-grid">'
        '<div class="ki-card keep"><div class="ki-title"><span class="dot">✅</span> '+T("keep_doing")+'</div><ul class="ki-list">'+keep+'</ul></div>'
        '<div class="ki-card push"><div class="ki-title"><span class="dot">🔧</span> '+T("push_further")+'</div><ul class="ki-list">'+push+'</ul></div>'
        '</div>'+footer(T("creator_report").upper()+" · 03", upd)+'</section>'
    )
    bcards = ''
    for b in c["briefs"]:
        tag = '<span class="pill pill-scale">'+e(b["tag"])+'</span>' if b.get("tag") else ''
        cls = ' priority' if b.get("tag") else ''
        tags = ''.join('<span class="brief-tag">'+e(t)+'</span>' for t in b["tags"])
        bcards += ('<div class="brief-card'+cls+'"><div class="brief-top"><span class="brief-num">'+e(b["num"])+'</span>'+tag+'</div>'
                   '<div class="brief-hook">“'+e(b["hook"])+'”</div>'
                   '<div class="brief-tags">'+tags+'</div>'
                   '<div class="brief-goal"><b>'+T("why")+'</b> '+e(b["why"])+'</div></div>')
    briefs = (
        '<section><div class="glow" style="bottom:-220px;left:-160px;width:900px;height:900px;opacity:0.42"></div>'
        '<div class="sec-head"><span class="sec-num">04</span><h2>'+T("sec04")+'</h2></div>'
        '<div class="subtitle">'+T("sec04_sub")+'</div>'
        '<div class="brief-grid">'+bcards+'</div>'
        '<div class="cta-block"><div><div class="cta-t">'+T("cta_t")+'</div>'
        '<div class="cta-s">'+T("cta_s")+'</div></div>'
        '<div class="cta-btn">'+T("shoot_by", date=e(meta["shootBy"]))+'</div></div>'
        +footer(T("creator_report").upper()+" · 04", upd)+'</section>'
    )
    tl = (
        '<section><div class="glow" style="top:-200px;right:-160px;width:860px;height:860px;opacity:0.4"></div>'
        '<div class="sec-head"><span class="sec-num">05</span><h2>'+T("sec05")+'</h2></div>'
        '<div class="subtitle">'+T("sec05_sub")+'</div>'
        '<div class="tl-row">'
        '<div class="tl-item"><div class="tl-dot"></div><div class="tl-date">'+T("tl1_d")+'</div><div class="tl-label">'+T("tl1_l")+'</div><div class="tl-note">'+T("tl1_n")+'</div></div>'
        '<div class="tl-item"><div class="tl-dot"></div><div class="tl-date">'+T("tl2_d")+'</div><div class="tl-label">'+T("tl2_l")+'</div><div class="tl-note">'+T("tl2_n")+'</div></div>'
        '<div class="tl-item"><div class="tl-dot dim"></div><div class="tl-date dim">'+T("tl3_d")+'</div><div class="tl-label">'+T("tl3_l")+'</div><div class="tl-note">'+T("tl3_n")+'</div></div>'
        '<div class="tl-item"><div class="tl-dot dim"></div><div class="tl-date dim">'+T("tl4_d")+'</div><div class="tl-label">'+T("tl4_l")+'</div><div class="tl-note">'+T("tl4_n")+'</div></div>'
        '<div class="tl-item"><div class="tl-dot dim"></div><div class="tl-date dim">'+T("tl5_d")+'</div><div class="tl-label">'+T("tl5_l")+'</div><div class="tl-note">'+T("tl5_n")+'</div></div>'
        '</div>'
        '<div class="callout">'+T("sec05_note")+'</div>'
        +footer(T("creator_report").upper()+" · 05", upd)+'</section>'
    )
    body = cover+ads+formula+kp+briefs+tl
    return ('<meta charset="utf-8">'
            '<title>'+e(c["name"])+' · '+e(BRAND)+' '+T("report")+'</title>'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="robots" content="noindex, nofollow">'
            '<style>'+stylesheet+'</style>'+body)

def overview_html(data, links, stylesheet):
    cards = ''
    for c, folder in links:
        st = c["status"]
        earn_m = ('<div class="idx-m"><div class="l">'+T("earnings")+'</div><div class="v" style="color:var(--accent)">'+comm(c["totals"]["gmv"])+'</div></div>') if SHOW_COMMISSION else ''
        cards += ('<a class="idx-card" href="../'+e(folder)+'/">'
                  '<div class="idx-head"><div class="idx-av">'+e(c["initials"])+'</div>'
                  '<div><div class="idx-name">'+e(c["name"])+'</div><div class="idx-role">'+e(c["product"])+'</div></div></div>'
                  '<div style="margin-bottom:14px"><span class="pill pill-'+e(st["class"])+'">'+e(st["emoji"])+' '+e(st["label"])+'</span></div>'
                  '<div class="idx-metrics">'
                  '<div class="idx-m"><div class="l">'+T("conv_value")+'</div><div class="v up">'+e(c["totals"]["gmv"])+'</div></div>'
                  +earn_m+
                  '<div class="idx-m"><div class="l">'+T("roas")+'</div><div class="v">'+e(c["totals"]["roas"])+'</div></div>'
                  '</div><div class="idx-go">'+T("open_report")+'</div></a>')
    return ('<meta charset="utf-8">'
            '<title>'+e(BRAND)+' · '+T("report_team")+'</title>'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="robots" content="noindex, nofollow">'
            '<style>'+stylesheet+'</style>'
            '<section><div class="glow" style="bottom:-300px;left:-220px;width:1100px;height:1100px;opacity:0.5"></div>'
            '<div class="logo-bar"><div class="logo-dot"></div><span class="logo-text">'+e(BRAND)+' · '+T("report_team")+'</span></div>'
            '<h1>'+T("reports_team_title")+'<br><span class="serif">.</span></h1>'
            '<div class="subtitle">'+T("ov_sub", brand=e(BRAND), updated=e(data["updated"]))+'</div>'
            '<div class="idx-grid">'+cards+'</div>'
            '<div class="footer-tag"><span>'+e(BRAND)+' · '+T("report_team").upper()+'</span><span>'+e(data["updated"])+'</span></div>'
            '</section>')

def root_html(data, stylesheet):
    return ('<meta charset="utf-8">'
            '<title>'+e(BRAND)+' · '+T("reports_team_title")+'</title>'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="robots" content="noindex, nofollow">'
            '<style>'+stylesheet+'</style>'
            '<section style="text-align:center;align-items:center"><div class="glow" style="bottom:-300px;left:-220px;width:1100px;height:1100px;opacity:0.4"></div>'
            '<div class="logo-bar" style="justify-content:center"><div class="logo-dot"></div><span class="logo-text">'+e(BRAND)+' · '+T("creator_report")+'</span></div>'
            '<h1 style="max-width:620px">'+T("root_h1")+'</h1>'
            '<div class="subtitle" style="margin-left:auto;margin-right:auto">'+T("root_sub", brand=e(BRAND))+'</div>'
            '</section>')

def main():
    global CFG, CDN, SALT, COMMISSION_RATE, PLATFORM, BRAND, BENCH, LANG, SHOW_COMMISSION, CUR
    data = json.load(open(DATA, encoding="utf-8"))
    CFG = data.get("config") or {}
    BRAND = CFG.get("brand") or data.get("brand") or "Brand"
    CDN = "https://cdn.tryatria.com/analytics/" + CFG["atriaAccountId"] + "/"
    SALT = CFG.get("salt") or (BRAND + "-salt")
    COMMISSION_RATE = float(CFG.get("commissionRate", 0.10))
    PLATFORM = CFG.get("commissionPlatform", "the platform")
    LANG = (CFG.get("lang") or "en").lower()
    if LANG not in STRINGS: LANG = "en"
    SHOW_COMMISSION = bool(CFG.get("showCommission", True))
    CUR = CFG.get("currency", "€")
    bm = data.get("benchmarks") or {}
    BENCH = {"hook": bm.get("hook", ""), "ctr": bm.get("ctr", "")}
    stylesheet = css()
    meta = {"brand": BRAND, "updated": data["updated"], "angle": data.get("angle", ""), "shootBy": data.get("shootBy", "")}

    history = {}
    if os.path.isfile(HISTORY):
        try:
            history = json.load(open(HISTORY, encoding="utf-8"))
        except (ValueError, OSError):
            history = {}

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(root_html(data, stylesheet))
    open(os.path.join(DIST, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    open(os.path.join(DIST, "_headers"), "w").write("/*\n  X-Robots-Tag: noindex, nofollow\n")

    links = []
    for c in data["creators"]:
        folder = c["slug"] + "-" + token(c["slug"])
        d = os.path.join(DIST, folder)
        os.makedirs(d)
        prev = history.get(c["slug"]) or {}
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(report_html(c, meta, prev, stylesheet))
        links.append((c, folder))

    ov = "overview-" + token("overview")
    os.makedirs(os.path.join(DIST, ov))
    open(os.path.join(DIST, ov, "index.html"), "w", encoding="utf-8").write(overview_html(data, links, stylesheet))

    print("Built", len(links), "private reports + team overview in", DIST, "for", BRAND)
    print("  TEAM overview:  /" + ov + "/")
    for c, folder in links:
        print("  /" + folder + "/   " + c["name"] + "  [" + c["status"]["label"] + "]")

if __name__ == "__main__":
    main()
