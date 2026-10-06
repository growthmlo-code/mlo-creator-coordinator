# 02 · Sistema Notion de creadores (Roster + Colaboraciones + Hub)

Arquitectura de 2 bases + hub (montada 3-ago-2026). Regla: **el Roster dice QUIÉN es la gente; Colaboraciones dice QUÉ hace cada uno, para QUIÉN y en qué PUNTO.** Se unen por el campo `Creador`. Si algo de un creador no está en su canal o en estas bases, no existe.

## IDs (usar tal cual con el MCP de Notion)
| Pieza | Página | Data source |
|---|---|---|
| 🎥 UGC Creator Database / **Roster de Creadores** | `a17ed77c-3037-47f0-a1cf-1c1043b3e4c7` | `collection://ac1ef0ab-1851-4f27-bd31-2e77de2f7c46` |
| 🤝 Colaboraciones UGC / **Pipeline de Colaboraciones** | `7e1ea4da-3cfd-470e-9020-c881dedf9a78` | `collection://2e5ff5ee-2296-49b9-8f4b-b8e5d12e10f1` |
| 🎬 UGC Creation Hub (interno, cross-marca; en Action Views del TEAM HUB) | `3b16c997-7eb7-81dc-b614-fb84552a5df9` | — |
| 🎥 Playbook Creator Coordinator | `3aa6c997-7eb7-81a2-a34b-d2d0c8ac2cad` | — |
| SOP roster | `3b16c997-7eb7-81e0-99d1-db3af3d95c55` | — |
| SOP colaboraciones | `3b16c997-7eb7-81ed-be05-df90c66daa79` | — |
| General Tasks (tareas UGC = `Área` = UGC) | — | `collection://1316c997-7eb7-81d6-a427-000b03b9e2d2` |
| Company SOP & PlayBooks Hub | — | `collection://1b76c997-7eb7-81e1-b986-000b833832ea` |
| Alejandro (guest, asignable) | user `3acd872b-594c-81ca-9855-0002a585b25a` | — |
| Base ANTIGUA "Creator Data Base" (backup, NO usar) | `24e6c997-7eb7-80e9-aace-000bc2d442a8` | — |

## Roster (1 fila = 1 creador; datos fijos de la persona)
Campos: Creador (title) · Foto · Estado (Prospecto/Contactado/En negociación/Activo/Pausado/Churn) · Plataforma (TikTok/IG/YouTube/Otro) · Handle/Link · Mercado (ES/EN/IT/FR/DE) · Estilo (Founder/Testimonial/Before-After/Storytelling/Unboxing/Voiceover) · Nivel (Gama baja/media/alta) · Coste por vídeo · Coste por paquete (texto) · Whitelisting (Sí/Con premium/No) · Marcas asignadas (texto; potencial) · Winners (número, a mano) · Contacto · Dirección de envío · Notas · Colaboraciones (relación automática).
Decisión Marcel 03-ago: quitar Cuestionario, Engagement %, Producto. Vistas: 📋 Todos · 🚦 Pipeline · 🖼️ Galería · 🌍 Por mercado.
Reglas: nunca crear sin Mercado + Handle; buscar antes de crear (no duplicar); estado siempre al día. ⚠️ 8 fichas migradas con "REVISAR IDENTIDAD" en Notas (Sofia↔Mora, Pamela↔Ilaria, Francesca↔Laia, Marta↔Eloy, Maria dels Angels=Danielah): verificar antes de contactar. 50 filas (49 migradas + "EJEMPLO — María UGC").

## Colaboraciones (1 fila = creador × marca × entrega)
Campos: Colaboración (title, ej. "Chloe × Bridge · Denim set") · Creador (relación DUAL al roster) · Marca (select: Bridge / 8hours; añadir marcas al entrar) · Estado colaboración (Brief enviado → Producto enviado → Grabando → En revisión → Entregado → Publicado) · Producto enviado (Pendiente → Dirección pedida → Enviado → Recibido) · Fecha brief · Fecha entrega · Coste real · Piezas entregadas · Winner ✓ · Rights hasta (fecha; si caduca, se deja de correr) · Link al brief (CE) · Notas.
Vistas: 🏷️ Por marca (board) · 🚦 Pipeline · 📦 Envíos de producto · 🏆 Winners (pendiente).
Reglas: trabajo nuevo = fila nueva · creador SIEMPRE elegido del roster · Winner solo si funciona en ads de verdad (criterio del KPI panel de la marca).

## Portales de cliente
En cada portal se incrusta una **vista enlazada de Colaboraciones filtrada por Marca** (Bridge ve Bridge). El roster (precios, otros clientes) **no se comparte**. Marcel ya metió en un portal una vista de tareas filtrada por "creadores UGC". Fase 2 pendiente: relación `Creador` → Roster en el Creative Engine de Bridge y 8hours (elegir creador al crear brief).

## Tareas UGC
Toda tarea de creadores va en General Tasks con `Área = UGC` (Assignee Alejandro, Supervisor Marcel) y cae sola en el espejo del Hub. Tareas batch 1: Bridge `3b36c997-7eb7-81a2-8c0e-d8d086c0c607`, 8HOURS `3b36c997-7eb7-8114-8e1b-c1de1d34af40`, dashboards Atria por creador `3b36c997-7eb7-8171-84d8-d46119de68aa`.

## Creadores 8HOURS conocidos (Meta, naming creator-first)
Maria Senatorova, Aaron Greenfield, Taylor Willis, Laura Cooney, Anna Keyserling, Steph Ingerman, Hannah Rinne, Louise Walkden, Brandon Ross, Jacob Ladouceur, Pete Pastides, Lucas Parker, Henrike Mauersberger, Erik Hansman. Contratos firmados en Drive: Bonnie Becker, Aaron Greenfield, Mary Senatorova. Cuenta Meta 8HOURS `1336199457035968` (EUR). El spend por creador se saca con la skill `mlo-creator-spend-report` (nombre del creador antes del primer `_` en el ad name).

## Gotchas del MCP de Notion
- `notion-create-database` usa `schema` con tipos RICH_TEXT / SELECT('x':color) / RELATION('ds', DUAL 'name'). `ADD COLUMN` por DDL puede no aplicarse (url/text) y `RENAME TABLE` tampoco → hacerlo por UI.
- `replace_content` usa `new_str`; para borrar linked views hijas `allow_deleting_content: true`.
- Páginas NO escribibles por API: Action Views `2486…198081` y la wrapper antigua `24e6…d317`.
- Filtros de vistas board no se aplican por MCP: cambiar por Chrome.
- Checklist limpio: no numerar `- [ ]` (mete "1." delante).

## Mejoras propuestas (auditoría jul-2026, no ejecutadas; proponer cuando Marcel lo pida)
Campos: Rights/Usage (multi) · Rights hasta en roster (ya está en Colaboraciones) · Idioma de grabación · Nicho · Rating A/B/C · Disponibilidad 🟢🟡🔴 · Retainer · TikTok Shop · Owner interno · Canal comunicación · Portfolio · Fuente sourcing · Contrato firmado ✓ · AI-UGC · País/TZ · Método de pago. Convertir Marcas asignadas → relación a DB Marcas; Winners → rollup desde Colaboraciones. Rollups: #Colabs, Winners, Gasto total, Última colab, Rights activos. Fórmulas: €/winner, días sin actividad, countdown rights. Avisos Make/Slack: activo→canal marca, dormido >60d, rights <30d. 8 vistas: Listos para brief · Por marca · Por whitelisting · A renovar/churn · Pipeline 3× · Rights expirando · Top performers · Por owner.
