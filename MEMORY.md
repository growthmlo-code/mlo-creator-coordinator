## Briefing

- [NOW — Briefing de sesion](NOW.md) — estado actual de clientes, pendientes, decisiones recientes; LEER SIEMPRE al arrancar

## Clientes activos

- [COEUS Retroaging](Clientes/project-coeus-retroaging.md) — suplementos, paid+creative; CEO Diego Suarez; Meta Ads 841305872095419
- [Skindion](Clientes/project-skindion-onboarding.md) — dispositivo skincare, paid foco ES; founders Mau/Max Azcona; contrato firmado 26-ago
- [Doctor Lazarraga](Clientes/project-lazarraga-web-redesign.md) — rediseno web (NO paid); fase muestra Home+PDP; Marcos CRO lead
- [VECOS/Baikonicoceutical](Clientes/project-vecos-foundation-program.md) — consultoria Foundation Program 3 meses; kickoff 8-sep; contrato en prep
- [Merus Nutrition](Clientes/project-merus-nutrition.md) — gut health supplements, pre-revenue, propuesta Tier 1 enviada Sep-2026; contacto Cesar Estevez
- [Petite Meal Co.](Clientes/project-petite-meal-co.md) — Creative Scale; contact Abby; ALWAYS English; kickoff 17-sep-2026; web launching imminently
- [BEALGND](Clientes/project-bealgnd.md) — streetwear/fashion paid desde Jul-2026; Adria Serra Vila; crisis IOSS; fee adjustment en negociacion
- [Box Hero](Clientes/project-boxhero.md) — men's boxers dropshipping; paid+creative; contacto Ollie Aplin; alta Oct-2026

## Marcas gestionadas (21)

- [Indice completo con Shopify handles y brand brain skills](Marcas/coeus-retroaging.md) — ver carpeta Marcas/
- Marcas con brand brain: Nurse is Love, QiHealth, 8hours, Alma, Ancestra, Bala di Gala, Bridge, Chic Love, Cidrera, English Path, Hobbit.Alf, Huiike, I-Energy, Moncho Moreno, MUTO, V-UP, ZZEN
- Marcas sin brand brain aun: COEUS, Henric Fuster, Fajitex, Bealegend
- Solo ZZEN y Ancestra en Triple Whale MCP; resto por Chrome/ShopifyQL

## Skills (47)

- [Catalogo completo de skills](Skills/indice-skills.md) — que hace cada una, cuando invocarla, organizado por area

## Operaciones

- [Ecosistema agentes ChatGPT](Operaciones/project-chatgpt-agent-ecosystem.md) — organigrama de agentes IA (COO/CMO/analysts); skill `mlo-agent-architect`; Luke activo, resto pendiente
- [Fireflies→Notion llamadas+recaps](Operaciones/project-fireflies-notion-calls-system.md) — subir todas las calls de cada cliente a su portal (DB central Calls 6692a55d, categorizada por Cliente) + noticia-recap; DB estaba en papelera; ZZEN piloto hecho
- [BUG portal DEMO arrastra ANCESTRA](Operaciones/feedback-portal-demo-arrastra-ancestra.md) — al duplicar se copian ~31 anuncios + ~10 links; limpiar siempre
- [Wizard onboarding Framer](Operaciones/project-onboarding-wizard-framer.md) — 5 pasos HTML-embed en mlo-growth.com/onboarding/bienvenido; variante consultoria en /creative-scale/
- [Agente CRO Listicle/Advertorial](Operaciones/project-cro-listicle-agent.md) — nuevo agente: winning ad → listicle/advertorial LP; research en curso
- [Agente Page Cooker (Fable)](Operaciones/project-page-cooker-agent.md) — skill+agente mlo-page-cooker: cocina landings CRO/listicles/advertoriales en código con look de marca y los publica en Shopify (pageCreate/themeFilesUpsert)
- [Agente Creator Coordinator (Fable)](Operaciones/project-creator-coordinator-agent.md) — skill+agente mlo-creator-coordinator: creadores UGC/afiliados, Roster+Colaboraciones, contratos A/B/C, Trybe (jointrybe.com ≠ TRIBE), comisiones y ofertas, playbooks de grandes DTC
- [💼 Legal Marvin (abogado MLO)](Operaciones/project-legal-marvin.md) — skill mlo-legal + archivo de ~30 contratos + reglas de redacción; Boxhero pendiente de generar
- [Email onboarding agencia — flujo y templates](Operaciones/feedback-onboarding-email-flow.md) — secuencia contrato→bienvenida, URL bienvenida por marca, contactos Supralash/Box Hero/Harry's
- [Proceso lead magnet SIEMPRE acaba en Kit](Operaciones/feedback-lead-magnet-proceso-kit.md) — 1) carpeta Drive → 2) estructurar dentro → 3) subir a Kit (form dedicado, descargable); no termina en Drive
- [Links obligatorios en volumen creativo](Operaciones/feedback-volume-links-obligatorios.md) — Slack y Announcement siempre con link al HTML y link cruzado
- [Adjuntar HTML embebido en la noticia del Tablero](feedback-adjuntar-html-en-noticia-tablero.md) — al publicar la noticia semanal de performance, subir e incrustar SIEMPRE el HTML del reporte en el cuerpo
- [COEUS fuera del reporte para siempre](Operaciones/feedback-coeus-fuera-reporte-siempre.md) — nunca incluir COEUS en el weekly performance report (regla permanente)
- [Rutina: Weekly Creative Report](project-weekly-creative-report-routine.md) — cron lunes 7am; 9 marcas; deck HTML + Slack por canal de marca
- [Filtro board Notion solo por Chrome](Operaciones/feedback-notion-board-filter-solo-chrome.md) — el MCP NO aplica filtros de vistas board; cambiar chip Cliente por Chrome UI (+usar refs de find)
- [notion-create-pages crea huérfanas → flujo fix](Operaciones/feedback-notion-create-pages-orphan-fix.md) — crear → move-pages a DB (type:database_id) → update_properties; IDs DB de los 3 portales CS incluidos
- [Fireflies link SIEMPRE en announcements](Operaciones/feedback-fireflies-link-en-announcements.md) — todo announcement post-call debe incluir el enlace Fireflies al principio, obligatorio
- [LinkedIn posts → Estado Pendiente](Operaciones/feedback-linkedin-estado-pendiente.md) — copy listo = "🕐 Pendiente de publicar"; siempre completar todos los campos (Creador, Oferta, Formato, ICP, Semana, Funnel Stage)
- [notion-move-pages formato](Operaciones/feedback-notion-move-pages-format.md) — new_parent requiere objeto JSON {"type":"database_id","database_id":"UUID"}; strings no funcionan
- [Creative Scale — primeras tareas](Operaciones/reference-creative-scale-primeras-tareas.md) — 5 tareas estándar consultoría (Plan de Acción/Research/CRO/Email/Oferta); board propio por cliente; Marcel supervisa, cliente ejecuta
- [Consultoría = done with you](Operaciones/feedback-consultoria-done-with-you.md) — cliente ejecuta TODO; MLO solo dirige y da referencias; nunca poner ejecución bajo "MLO hace"
- [Creative Scale — databases independientes](Operaciones/feedback-creative-scale-independent-databases.md) — cada cliente CS DEBE tener task board y announcements propios; regla de Marcel
- [Web Capri Equity (LLC de Marcel)](Operaciones/project-capri-equity-website.md) — HTML en Cloudflare Pages, live en capri-equity.com; fuente en ~/claude/capri-equity/; re-deploy con wrangler@3
- [Script Scaling Agent](Operaciones/project-script-scaling-agent.md) — proyecto Claude Code en ~/script-scaling/; agente experto del programa consultorial; todas las skills, onboarding, diagnostico, sesiones
- [Playbook Creative Scale](Operaciones/reference-playbook-creative-scale.md) — proceso completo Foundation Program: pre-kickoff → research → entregables → delivery; checklist por fase
- [SOP Fase 0: Pre-kickoff](Operaciones/sop-creative-scale-fase0-prekickoff.md) — discovery call, Typeform, contrato, accesos; prompts incluidos
- [SOP Fase 1: Setup](Operaciones/sop-creative-scale-fase1-setup.md) — kick-off, portal Notion, Slack Connect, calendario; prompts y errores comunes
- [SOP Fase 2: Research](Operaciones/sop-creative-scale-fase2-research.md) — Nathan Audit, Brand DNA 14 secciones, productos, competencia, personas, social listening; prompts completos
- [SOP Fase 3: Entregables](Operaciones/sop-creative-scale-fase3-entregables.md) — Research HTML, Context Deck, Notion, Slack delivery; design system y reglas de comunicación
- [SOP Fase 4: Seguimiento](Operaciones/sop-creative-scale-fase4-seguimiento.md) — calls semanales, roadmap por bloques (CRO → email → oferta → paid); prompts de feedback
- [SOP: Panel de KPIs Semanal](Operaciones/sop-kpis-panel-mentoria.md) — puntero a los SOPs oficiales de Notion: M01.B (construcción onboarding) + KPI Panel & Unit Economics Calculator; plantilla Excel KPI_Panel_[MARCA]
- [SOP: Skills MLO en GitHub](Operaciones/sop-mlo-skills-github.md) — catálogo de 19 skills cliente-facing + instrucciones de instalación (GitHub/Proyecto/pegado) y flujos de uso semanal
- [Playbook 01: Números y Rentabilidad](Operaciones/playbook-01-numeros-rentabilidad.md) — P&L, unit economics, Break-Even ROAS, MER, LTV:CAC; documentos Drive + skill mlo-ecom-financials-2026
- [Playbook 02: Oferta](Operaciones/playbook-02-oferta.md) — Offer Architecture Scorecard, economía de ofertas, niveles de consciencia; skills mlo-offer-simulator + mlo-cro-2026
- [Playbook 03: Creative Strategy](Operaciones/playbook-03-creative-strategy.md) — Matriz conceptos, scorecard creativo, brief estratégico, loop semanal, teardown; 9 skills creativos
- [Playbook 04: Testing Paid y Escalado](Operaciones/playbook-04-testing-paid-escalado.md) — auditoría estructura cuenta, ABO vs CBO, Keep/Kill, escalar sin romper señal; skills mlo-media-buying + mlo-winner-strategist
- [Playbook 05: CRO y Conversión](Operaciones/playbook-05-cro-conversion.md) — RPV, 5 palancas landing, quiz funnel, checkout checklist, banco ofertas; skills mlo-cro-2026
- [Playbook 06: Retención y Email](Operaciones/playbook-06-email-retencion.md) — welcome flow, stack 5 flows, Klaviyo; skill mlo-klaviyo-email-report; métricas LTV
- [Playbook 07: Herramientas IA](Operaciones/playbook-07-herramientas-ia.md) — Kit 11 skills, Meta Ads Agent System (14 agentes), Simulador Ofertas; cómo integrar Claude en el flujo semanal
- [Reporte Google Ads estándar](Operaciones/project-google-ads-report-system.md) — skill mlo-google-ads-report; deck pestañas; cross-check Triple Whale; nCAC D2C = solo Meta+Google (fuera Amazon/TikTok)

## Referencias

- [Link de agenda MLO](Referencias/mlo-link-agenda.md) — CTA fijo: metodolgia-mlo (errata real en el slug)
- [Proceso Creativo & Feedback Loop](Referencias/reference-onboarding-feedback-loop-doc.md) — anexo onboarding para clientes
- [Typeform onboarding maestro](Referencias/reference-typeform-onboarding-migration.md) — form.typeform.com/to/EHEUswHd
- [Skill auditoria ecommerce](Referencias/reference-skill-auditoria-ecommerce.md) — skill en ~/.claude/skills/mlo-auditoria-ecommerce/
- [Handles Shopify por marca](Referencias/reference-shopify-handles-marcas.md) — admin handles para reporte semanal
- [Google Ads vía Windsor + fórmula NCPA](Referencias/reference-google-ads-windsor-reporte.md) — Google del reporte por MCP Windsor.ai; NCPA/NCROAS = (Meta+Google)/nuevos tienda; marcas con Google
- [Metodo Nathan audit](Referencias/reference-nathan-audit-method.md) — skill audit con acceso real; 3 pilares Data/Structure/Creative; bottleneck diagnosis
- [Servicios MLO (lista cerrada)](Referencias/reference-mlo-servicios.md) — solo 6: Meta Ads / Google Ads / Estrategia Creativa / Produccion Creativa / CRO / Email; no inventar en webs/casos

## Objetivos mensuales

- [Objetivos Sep 2026](project-objetivos-septiembre-2026.md) — targets por marca para forecast volumen creativo

## Plantillas

- [Template cliente](_plantillas/template-cliente.md) — frontmatter estandar para ficha de cliente nuevo
