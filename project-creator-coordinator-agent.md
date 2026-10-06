---
name: project-creator-coordinator-agent
description: "Skill + agente Fable mlo-creator-coordinator (creado 18-sep-2026): el cerebro de creadores UGC/afiliados de MLO; ojo Trybe (jointrybe.com) ≠ TRIBE"
metadata:
  type: project
---

Agente **mlo-creator-coordinator** (pedido por Marcel 18-sep-2026): "el mayor experto en gestión de creadores DTC" — opera el sistema real de MLO (playbook Creator Coordinator 0→100, Roster + Pipeline de Colaboraciones en Notion, canal #creator-ads-[marca], contratos A/B/C, pagos Wise) y conoce Trybe, plataformas, modelos de comisión/ofertas y cómo operan las grandes DTC.

Ubicación:
- Skill: `~/.claude/skills/mlo-creator-coordinator/` (SKILL.md router + `references/01-08` + `templates/` + `references/raw-trybe-transcripts/`).
- Agente: `~/.claude/agents/mlo-creator-coordinator.md` (`model: fable`).
- Sustituye en la práctica a la skill v1 del plugin `anthropic-skills:creator-coordinator` (solo SKILL.md, sin playbooks reales).

**Why:** la vertical de creadores es un revenue stream nuevo (piloto Bridge + 8hours, Alejandro Torres como coordinator) y Marcel quería un "bicho" con TODO el contexto (playbook Notion + contratos reales + mercado).

**How to apply:**
- **"Tribe" en boca de Marcel = TRYBE (jointrybe.com)**, la plataforma performance-based del Módulo 4.1 del playbook (creadores suben ads, la marca los lanza whitelisteados en Meta, cobran % ventas / % ad spend; fee 1,5%). NO es tribegroup.co. Trybe es US-first (0 marcas ES): encaja en Bridge/8hours, no en marcas ES.
- Contratos reales con números en `references/03`: 8hours = producto + 25% primera venta vía Upfluence (1 Reel 3 m rights + 2 Stories, 2 rondas, raw footage); ZZEN = 350 €+IVA / 5 vídeos + 20 €/hook, rights Meta 12 m (mín 6).
- Reglas de Marcel (llamada 03-ago-2026): 2-3 creadores/marca × 2 vídeos × 2-3 hooks; propuesta cerrada en frío; whitelisting add-on aparte; la marca envía el producto.
- Fuentes vivas: playbook Notion `3aa6c997-7eb7-81a2-a34b-d2d0c8ac2cad` (módulos 9-15 pendientes), SOPs roster/colaboraciones, Drive contratos. Actualizar la skill si el playbook cambia.
- **Trybe help center** (jointrybe.com/help, requiere login; SPA — se lee con Chrome de Marcel + iframes) capturado entero (27 artículos) en `references/raw-trybe-help/`; SOP lado marca en Notion `3df6c997-7eb7-8174-ac12-f72bf06bdd84` (Company SOP Hub, Approved) enlazado desde Módulo 4.1, playbook, onboardings y UGC Creation Hub; Brand API documentada en `04c` + `scripts/trybe_api.py` (falta la clave `TRYBE_API_KEY`: Integrations → API Access, la activa el account manager).
- Regla de Marcel (18-sep-2026): **todo el que trabaje con creadores se lee el SOP de Trybe + el help center entero, siempre**; los vídeos de YouTube son el lado creador (cómo piensan/qué buscan).
- Para guion/brief → `ugc-director`; spend por creador → `mlo-creator-spend-report`.
Relacionado: [[project_ugc_creator_system]], [[project-page-cooker-agent]], [[mlo-agent-architect]].
