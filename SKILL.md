---
name: mlo-creator-report
description: "Build premium per-creator PERFORMANCE REPORTS for a DTC brand's top UGC creators — a private web page per creator showing their live videos, business results (ad spend, conversion value/GMV, ROAS, orders) plus a simulated/real commission, why their winner works, keep/push coaching and the next briefs. Pulls real data from Atria (Meta ads analytics), builds a static site (one private tokened URL per creator + a team overview), deploys to Cloudflare Pages, and refreshes on a schedule. Trigger: 'creator report', 'performance report for creators', 'report por creador', 'build creator reports for <brand>', '/mlo-creator-report'. NOT the creator onboarding BRIEF (that is the metric-free `creator-brief` skill), NOT the internal weekly performance deck, NOT ad copy."
---

# MLO Creator Report

Builds the **premium, per-creator performance report** that a top UGC creator opens on a private link. One scrolling page per creator:

| # | Section | Built from |
|---|---|---|
| Cover | Status + business totals: ad spend, conversion value (GMV), earnings (commission), ROAS, orders, impressions | Atria 90d totals across the creator's ads |
| 01 | Your videos | Every one of the creator's ads (active first), real video playing, business row (GMV · earnings · ROAS · orders) + creative row (hook · CTR · hold, vs account avg) |
| 02 | Why it works | The structure/beats of their winning ad (from transcript/copy) |
| 03 | Keep doing / push further | Per-creator coaching grounded in their real metrics |
| 04 | Film these next | 3 briefs built from what's working for them + a "Shoot by <date>" CTA |
| 05 | What happens next | Timeline; report refreshes on schedule |

Distinct from the **`creator-brief`** skill: that is a metric-free onboarding brief for ALL creators (Trybe). THIS is a premium 1-a-1 report for **best-performer creators on fixed contracts**, and it **does** show business metrics + the creator's commission — a deliberate, client-approved exception to the usual "no ROAS/spend to creators" rule. Keep the two separate; never put business metrics on the general brief.

## Quick run (one-shot)

When the user says **"créame el reporte de creadores para `<brand>`"** / **"build the creator report for `<brand>`"**, run this end to end without stopping to ask what you can look up:

1. **Config** — open `references/brands.md`, copy that brand's `config` block into `creators.json`. Not listed? Get the Atria id from `list_ad_accounts` and colours from `mlo-brand-brain-<brand>`, then add it to the registry.
2. **Pull + analyse everything** (`references/data-pipeline.md`): account 90d/30d ROAS; `list_ad_account_ads` (90d, all metrics); identify the real UGC creators (name in `ad_name`, exclude founders/AI/statics), group each creator's ads, keep those above the bar (≥10 orders AND ROAS ≥ account ROAS); per featured ad pull the video/poster/transcript for the hook. Never ask the user to type a number.
3. **Write `creators.json`** (schema in `references/build-deploy.md`): `config` + top-level `updated`/`angle`/`shootBy`/`benchmarks`, then per creator `status`/`totals`/`ads[]`/`callout`/`formula`/`keep`/`push`/`briefs`. Business numbers come from Atria; the analysis (why-it-works, keep/push, 3 briefs) you write from each creator's own real signals. Nothing invented, no placeholders.
4. **Build**: `python3 <skill>/assets/build_reports.py` from the brand's project folder (copy the generic generator in once — don't fork it per brand). It writes `dist/`: one private `slug-token` page per creator, a team overview at an unguessable path, a neutral private root.
5. **Preview** at phone width (videos play muted + sound button; metrics/commission/vs-avg/CTA render; root shows no list), then **report back** per creator: status, GMV, ROAS, earnings, and the headline of their coaching — so the user sees the analysis, not just links.
6. **Deploy on the user's go** (`deploy.sh` / `wrangler pages deploy dist --project-name=<brand>-creator-reports`), hand over each private link + the team overview, and offer the bi-weekly refresh task.

The generator is **config-driven**: `lang` (`es`/`en`), `showCommission` (on/off), `currency`, accent trio. One brand = one `creators.json`, no code edits. Default to `es` for MLO brands unless the brand is English (8hours, Bridge, MUTO, Box Hero).

## Files in this skill

| Path | Use |
|---|---|
| `references/brands.md` | **Brand registry** — ready-to-paste `config` per brand (Atria id, lang, colours, commission, salt) + Atria ids for the rest of the portfolio. Read this first on any "report for `<brand>`". |
| `references/data-pipeline.md` | How to pull winners + creator-safe-plus-business metrics from Atria, the selection rules, the metric mapping |
| `references/build-deploy.md` | `creators.json` schema, the generator, private tokened URLs, trend history, Cloudflare deploy, scheduled refresh |
| `references/best-practices.md` | Design system, the creator-safe-vs-premium rule, and the gotchas that will bite you |
| `assets/build_reports.py` | The generator. Reads `creators.json`, writes `dist/` (one private page per creator + a team overview). **Fully config-driven** — `lang` (es/en, full i18n), `showCommission` (on/off), `currency`, accent trio — so one brand = one `creators.json`. Don't edit or fork per brand. |
| `assets/creators.example.json` | A complete, valid example (8HOURS) — copy its structure |

Python 3.8+. Deploy needs `wrangler` (via `npx`) with the user's Cloudflare logged in. No ffmpeg/downloads — videos stay as remote Atria URLs.

## Workflow

1. **Scope.** Confirm the brand, its Atria ad-account id, who the "top creators" are (or derive them), the commission rate (real once their platform e.g. Trybe is wired, else simulated — label it), brand colours, and the deploy target (Cloudflare Pages project name). One project per brand.
2. **Pull the data** with `references/data-pipeline.md`: account ROAS thresholds, each creator's ads (all of them, active first) with business + creative metrics, and transcripts for hooks/why-it-works. Never ask the user to type performance numbers.
3. **Write `creators.json`** (schema in `references/build-deploy.md`): the `config` block (brand, atria account, colours, salt, commission rate, benchmarks, shootBy), then per creator: status, totals, ads[], callout, formula, keep/push, briefs. Business metrics come from Atria; coaching (keep/push/briefs) is written per creator from their real signals. Nothing invented.
4. **Build:** `python3 <skill>/assets/build_reports.py` pointed at the brand's project folder. It writes `dist/` with one private URL per creator (slug + token) and a team overview at an unguessable path; the public root is a neutral "your report is private" page.
5. **Preview** at phone width: every creator page reads well, the real videos play muted with a sound button, business metrics + commission + "vs avg" + CTA all render, and the root shows no list.
6. **Deploy** (user's go): `wrangler pages deploy dist --project-name=<brand>-creator-reports --branch=main --commit-dirty=true`. Give the user each creator's private link + the team overview link.
7. **Schedule the refresh** (bi-weekly by default): a task that saves the trend history, re-pulls Atria, updates `creators.json`, rebuilds, and notifies the user to publish (`deploy.sh`). It does NOT auto-publish.

## Hard rules

- **Two kinds of metric, by audience.** These premium reports show business metrics (ad spend, GMV, ROAS, orders) + the creator's commission ON PURPOSE, because the client pays creators on GMV and wants transparency. This is the exception, not the default — it applies only to premium 1-a-1 reports for trusted fixed-contract creators, confirmed by the user. The general `creator-brief` and anything broader stay metric-free.
- **Privacy.** One unguessable URL per creator; no public index; the root lists nothing. A creator must not be able to reach another creator's earnings. The team overview lives at its own unguessable path.
- **Commission is labelled.** While simulated, say so ("Simulated · live with <platform>"). Compute it in the generator from GMV (one rate constant), never hardcode per-creator earnings.
- **Nothing invented.** Every number comes from Atria; every claim/hook comes from the creator's real ads (transcripts/copy). No placeholders.
- **Videos stay remote.** Reference Atria's content-hashed CDN URLs (`cdn.tryatria.com/...`) directly — they're stable and play cross-origin. Never download/bundle.
- **Static page needs `<meta charset="utf-8">`** or emojis/×/·/→/€ render as mojibake (the host may not send a charset).
- **Writing spend/GMV/ROAS onto a published page can be gated** by the auto-mode safety classifier. It needs the user's explicit go (they confirm, or switch permission mode). Don't try to route around it.
- **Publishing is the user's step.** Never deploy without their go; the scheduled refresh prepares and notifies, it doesn't publish.
