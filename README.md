# mlo-creator-coordinator

Skill package completo del **Creator Coordinator de M.L.O Growth** — sistema operativo para gestionar creadores UGC, influencers y afiliados para marcas DTC, incluyendo el **Creator Growth Program (CGP)** con Trybe + Partnership Ads.

Repositorio vivo: se actualiza con cada nueva call, propuesta o aprendizaje operativo.

---

## Cómo instalar la skill

### Opción A — GitHub (recomendado)
```
Copiar la carpeta mlo-creator-coordinator/ completa a ~/.claude/skills/
```
Estructura de destino: `~/.claude/skills/mlo-creator-coordinator/`

### Opción B — Proyecto Claude
Subir como proyecto en claude.ai y añadir como skill del proyecto.

### Opción C — Pegado directo
Copiar el contenido de `SKILL.md` y pegarlo como instrucción de sistema en Claude.

---

## Estructura del paquete

```
mlo-creator-coordinator/
├── SKILL.md                    ← Router principal (instalar aquí)
├── README.md                   ← Este archivo
├── references/
│   ├── 01-playbook-operativo-mlo.md          ← Playbook 0→100, flujo, RACI, SLAs
│   ├── 02-sistema-notion-creadores.md         ← IDs Notion, esquemas, vistas
│   ├── 03-contratos-y-compensacion-mlo.md     ← Contratos A/B/C, contratos reales
│   ├── 04-trybe-y-plataformas.md             ← Trybe qué es + comparativa plataformas
│   ├── 04b-trybe-sop-marcas.md              ← SOP lado marca (27 artículos help center)
│   ├── 04c-trybe-api.md                      ← Brand API v1: endpoints y autenticación
│   ├── 04d-trybe-lado-creador-videos.md       ← Cómo piensan los creadores en Trybe
│   ├── 05-modelos-comision-y-ofertas.md       ← Rates, premiums, comisiones, tiers
│   ├── 05b-top-dtc-creator-programs.md        ← Ridge, Gymshark, Caraway, Halara...
│   ├── 06-sourcing-directorio.md              ← 4 canales, directorio Skool, por marca
│   ├── 07-legal-rights-eu.md                 ← Disclosure ES/EU, GDPR, cláusulas
│   ├── 08-scaling-economics.md               ← Hit rates, coste/winner, KPIs programa
│   ├── 09-perlas-calls-sep2026.md            ← Adrian Waga + Skindion México playbook
│   ├── 10-servicio-creator-growth-program.md  ← CGP: 9 pasos, pricing, benchmarks
│   ├── 11-cgp-propuestas-por-marca.md        ← 8hours, Moncho, MUTO: tiers y pricing
│   └── 12-trybe-onboarding-call-oct2026.md   ← ⚠️ Reglas críticas Oct 6, checklist
├── templates/
│   ├── outreach.md                           ← DMs, emails, job posts, propuesta cerrada
│   ├── oferta-creador.md                     ← Plantillas A/B/C/D/E (Smart Retainer)
│   ├── creator-call-semanal.md               ← Agenda 30-40 min, ritual semanal
│   ├── propuesta-servicio-creator-management.md ← Pitch UGC packs + CGP a cliente
│   ├── cuestionario-creador.md               ← Typeform para creadores (perfil, formatos)
│   ├── prelista-perfiles.md                  ← Tabla de candidatos para estratega
│   └── reporte-programa-creadores.md         ← Reporte mensual por marca
└── scripts/
    └── trybe_api.py                          ← Automatizaciones Trybe API (Python)
```

---

## Reglas críticas — NO OLVIDAR

### ⚠️ Trybe: siempre vía referral link MLO
Crear cuenta de marca directamente en Trybe = perder el bonus de $10.000 (si llega a $10K GMV en primeros 100 días). **SIEMPRE usar el partner referral link de MLO.**

### ⚠️ Trybe IDs: nunca tocar en ads activos
`?trybe=XXXXXXXX` en la URL del ad es intocable. Si el media buyer cambia la landing, debe mantener el mismo Trybe ID. Verificar semanalmente (viernes).

### ⚠️ Datos internos: nunca a creadores
ROAS, CAC, presupuesto de cuenta — nunca a creadores. Hablan con competidores en WhatsApp.

---

## Cronología del paquete

| Fecha | Evento | Archivos añadidos |
|---|---|---|
| Sep 22, 2026 | Call Adrian Waga (181 min) + Skindion weekly call | `09-perlas-calls-sep2026.md` |
| Sep-oct 2026 | Propuestas CGP 8hours + Moncho Moreno | `11-cgp-propuestas-por-marca.md` |
| Oct 6, 2026 | Call onboarding Trybe con Adrian Waga (72 min) | `12-trybe-onboarding-call-oct2026.md` |
| Oct 6, 2026 | Paquetización completa al repo GitHub | Todos los archivos |

---

## Contactos clave

| Persona | Rol | Contexto |
|---|---|---|
| **Adrian Waga** (Waga Limited) | Mentor creator management | Gestiona 5+ marcas × 50 creadores/marca con 1 persona; referente CGP en ES/FR/PL |
| **Berta Vallmajor** | Equipo MLO | Creator coordinator en entrenamiento |
| **Marcel Lopez** | Founder MLO | Decisiones de pricing, contratos y propuestas |

**Adrian enviará (pendiente):** template de outreach, Google Drive Q&A creadores, Loom Trybe IDs, playbook reclutamiento fuera de plataforma.

---

## Para actualizar este repo

Cuando llegue nueva información (call, propuesta, aprendizaje):
1. Añadir a `references/09-perlas-calls-*.md` si es de una call
2. Crear `references/12+.md` numerado si es un tema nuevo
3. Actualizar `SKILL.md` router si hay nuevas peticiones tipo
4. Actualizar `README.md` cronología

El repo es el registro permanente. La skill en `~/.claude/skills/` es la copia de trabajo activa.
