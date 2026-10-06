# 12 · Learnings Trybe Onboarding Call — Oct 6, 2026

**Participantes:** Marcel Lopez (MLO Growth), Adrian Waga (Waga Limited, mentor), Berta Vallmajor (MLO)  
**Duración:** 72 minutos  
**Contexto:** Primera call de onboarding de Trybe para marcas del portfolio MLO. Adrian ha lanzado programas en ES/FR/PL con Trybe.  
**Fireflies:** https://app.fireflies.ai/view/01M48FMKXQVM2DYSBTYNKXKMHZ  

---

## REGLA #1 — CRÍTICA: SIEMPRE CREAR LA CUENTA DE MARCA VÍA REFERRAL LINK MLO

**Marcel creó la cuenta de 8hours directamente en Trybe → se perdió el bonus de $10.000.**

La regla del partner referral de Trybe:
- Si una marca llega a $10.000 GMV en los primeros 100 días desde el referral link del partner → MLO recibe $10.000
- Este bonus SOLO se activa si la marca fue creada usando el referral link de MLO
- Crear la cuenta directamente (como hizo Marcel con 8hours) = $0 de bonus, aunque la marca supere el objetivo

**Procedimiento correcto:**
1. MLO tiene su link de partner en la cuenta de Trybe (Partnerships / Partner Dashboard)
2. Antes de que la marca haga NADA en Trybe, enviarles ese link
3. La marca se registra desde ese link
4. Si no está seguro, pedir que borren la cuenta y se re-registren vía el link

**Para 8hours:** investigar si se puede borrar la cuenta y re-crear vía referral (Adrian dice que Trybe Support puede gestionar esto en algunos casos).

---

## SETUP OPERATIVO DEL CGP (Creator Growth Program)

### La página de brief — infraestructura central

Adrian gestiona **una página de brief pública por marca**, alojada en **Netlify** (gratis):
- Se construye con Claude (skill mlo-creator-coordinator) como HTML estático
- Contiene: pitch de la marca, productos, ángulos que están funcionando, hooks actuales, ejemplos de vídeos ganadores, CTA con el invite link de Trybe
- Se actualiza **quincenalmente** (biweekly) con los hooks y formatos que están convirtiendo esa semana
- La página tiene **selector de idioma** y **geolocator** para mostrar el idioma correcto al creador
- Diseño: **mobile-first, scroll vertical** (los creadores la ven en el móvil)
- El creador la usa para entender la marca y orientar su creatividad — sin guiones, solo principios

**Por qué Netlify y no Notion/Google Doc:**
- URL limpia y compartible (no requiere login)
- Se puede trackear quién la visita (Netlify Analytics)
- Se puede actualizar sin reenviar links
- Aspecto profesional para los creadores

### Checklist de kickoff para una nueva marca en CGP

**Semana 0 — antes de arrancar:**
- [ ] Trybe partner account MLO configurado para la marca
- [ ] Marca creada VÍA referral link MLO (nunca directamente)
- [ ] Shopify conectado a Trybe
- [ ] Meta Ad Account conectado a Trybe
- [ ] Método de pago configurado en Trybe

**Semana 1:**
- [ ] Programa de comisión creado (15% GMV orgánico + configurar Partnership Ads)
- [ ] Catálogo de productos importado en Trybe
- [ ] Allow Sample Requests activado
- [ ] Página de brief construida en Netlify con Claude
- [ ] Grupo WhatsApp top performers creado (vacío hasta mes 2-3)
- [ ] Loom de onboarding grabado para creadores (2-3 min: qué es el programa, cómo funciona, qué esperamos)
- [ ] Invite link del programa configurado y testeado

**Semana 2-3:**
- [ ] Primeros 10-15 creadores invitados (usar créditos diarios)
- [ ] Primeros samples aprobados y enviados (el mismo día)
- [ ] Sistema de naming convention en el Ad Builder configurado (creator-first)
- [ ] Carpeta de Drive para brutos/submissions configurada

---

## LOS TRYBE IDs — REGLA CRÍTICA PARA MEDIA BUYERS

**Cada submission aprobada tiene un submission ID único** en Trybe (últimos 8 caracteres del código `trybe=`).

Cuando la marca lanza el ad desde el Ad Builder de Trybe, la URL de destino queda automáticamente como:
`tienda.com/products/hero?trybe=a1b2c3d4`

**NUNCA cambiar ni eliminar el parámetro `?trybe=XXXX` en un ad que está corriendo.**

Consecuencias de borrar el Trybe ID:
- Trybe pierde la atribución de ese ad → el creador no cobra comisiones de ese ad
- El dashboard de Trybe no muestra los datos de ese ad
- El creador ve $0 en su cuenta y pierde motivación

**Si el media buyer necesita cambiar la landing page de un ad activo:**
1. El nuevo URL debe incluir el mismo `?trybe=XXXXXXXX` del ad original
2. Si el media buyer duplica un ad en Ads Manager (no desde Trybe), el Trybe ID NO se copia automáticamente → hay que añadirlo a mano
3. Si hay dudas, crear un nuevo ad desde el Ad Builder de Trybe en vez de duplicar en Ads Manager

**Proceso de verificación semanal (checklist):**
- [ ] Ningún ad activo del programa tiene URL de destino sin `?trybe=`
- [ ] Todos los nuevos ads del media buyer incluyen el Trybe ID del creador correspondiente

---

## ATRIBUCIÓN TRYBE vs TRIPLE WHALE — CÓMO EXPLICARLO A CLIENTES

Los clientes van a ver diferencia entre lo que reporta Trybe y lo que reporta Triple Whale / Meta. Esto es normal y esperado. Comunicarlo así:

**Trybe usa server-side last-click** (sin view-through):
- Solo cuenta ventas donde hubo un clic real en el link de Trybe → compra
- Es el número más conservador y el más "limpio" de la industria
- Similar a cómo funciona Northbeam en modo last-click

**Triple Whale usa modelo blended** (MTA + determinístico):
- Incluye view-through, múltiples touchpoints
- Número más alto, más cercano al "total de ventas"
- El NCPA de Triple Whale que MLO usa para reportes incluye Meta + Google

**Por qué Trybe sale más bajo:**
- Correcto — es el número de ventas directamente atribuibles a creadores vía clic
- Los creadores también generan ventas que Trybe no ve (búsqueda directa, conversión tardía)

**Qué comunicar al cliente:**
> "El GMV de Trybe es el piso conservador del impacto del programa — lo que podemos probar con certeza. El número real suele ser 1,5-2× mayor cuando se incluye el efecto halo (búsquedas, conversiones tardías, seeding orgánico)."

---

## OUTREACH Y WARM-UP DE CUENTA TRYBE

Adrian reporta límites de outreach en Trybe que suben progresivamente:
- **Inicio:** 10 mensajes salientes/día
- Después de X días de actividad: 25/día
- Cuenta caliente: 50/día
- Cuenta veterana: 100/día

**Táctica de Adrian para acelerar el warm-up:**
- No agotar los créditos de invitación los primeros días — ir gradual
- Priorizar la calidad sobre la cantidad en las primeras semanas (creadores con >60% approval rate)
- Poner programas como "discoverable" para recibir inbound mientras se agota el outbound

**Para una cuenta nueva de marca MLO:**
- Semana 1-2: 10/día, priorizar los mejores perfiles del directorio Discovery
- Semana 3-4: subir a 25/día cuando la cuenta caliente
- Mes 2+: ritmo de crucero

---

## CADENCIA OPERATIVA SEMANAL

### Lunes
- Revisar submissions pendientes (objetivo: 0 submissions sin revisar al cierre)
- Verificar que todos los samples aprobados esta semana tienen envío confirmado
- Revisar Inbox de join requests (caducan a 30 días → oldest-first)

### Miércoles
- Actualizar página de brief Netlify si hay nuevos hooks/ángulos ganadores
- Enviar brief update al grupo WhatsApp de top performers
- Revisar leaderboard de la semana → candidatos a retainer

### Viernes
- Verificar estado Partnership Ads (icono verde en todos los activos)
- Confirmar que Integrations muestra Meta "Active" y tienda "Connected · Receiving data"
- Auditar ads activos: ¿todos tienen `trybe=` en la URL? Si alguno no tiene → añadir inmediatamente

### Mensual
- Pull del spend por creador desde el dashboard de Trybe (Analytics → Group by Creator)
- Revisar leaderboard → candidatos a Smart Retainer
- Preparar reporte GMV: orgánico vs Partnership Ads, CPA, hit rate, coste por winner
- Decisión: renovar / churn / escalar por creador

---

## TIMING DE LANZAMIENTO DE ADS

**Regla de Adrian: lanzar los ads 2 días antes del día pico de la semana de la marca.**

Por qué:
- Los primeros 48h del creador son la "ventana de dopamina" → si ve sus comisiones subir rápido, publicará más
- Los ads necesitan 1-2 días de aprendizaje antes de llegar al rendimiento pico
- Lanzar el viernes = el creador ve resultados el lunes = ciclo de motivación perfecto

**Aplicación práctica:**
- Si el día pico de la marca es el domingo (ej: wellness, suplementos) → lanzar ads el viernes
- Si es el miércoles → lanzar el lunes
- Si no se conoce el día pico: revisar los datos de la cuenta Meta (insights por día de la semana) → siempre hay un pico

---

## DATOS QUE NO COMPARTIR CON CREADORES

Los creadores trabajan con múltiples marcas que compiten entre sí y hablan en grupos de WhatsApp.

**NUNCA compartir con un creador:**
- ROAS de sus ads
- CAC de la marca
- Presupuesto de gasto mensual de la cuenta
- Datos de otros creadores (ni de forma anonimizada si es identificable)
- Información sobre la estrategia de targeting

**SÍ compartir:**
- Su GMV atribuido (solo el suyo)
- Sus comisiones ganadas (solo las suyas)
- Qué hooks/ángulos están funcionando en general (sin datos numéricos específicos)
- Qué tipos de vídeos están convirtiendo esta semana (dirección creativa, no métricas)

---

## PRÓXIMOS PASOS ACORDADOS (Oct 6, 2026)

### Adrian enviará a Marcel:
- [ ] Template de outreach que usa su equipo para reclutar en Trybe
- [ ] Carpeta Google Drive con Q&A de creadores (las preguntas más frecuentes y cómo responderlas)
- [ ] Loom sobre cómo gestionar los Trybe IDs correctamente
- [ ] Playbook de reclutamiento fuera de plataforma (cómo hizo su agencia en Polonia con creadores externos a Trybe)

### MLO en las próximas 2 semanas:
- [ ] Investigar si la cuenta de 8hours en Trybe puede ser borrada y re-creada vía referral link MLO
- [ ] Construir la primera brief page de Netlify para la primera marca CGP
- [ ] Configurar el Trybe partner account con el referral link correcto
- [ ] Finalizar y firmar el addendum CGP para MUTO (Marcel → DocuSign)
- [ ] Enviar el email de onboarding CGP a MUTO una vez firmado

---

## RESUMEN DE REGLAS OPERATIVAS CLAVE (destilado de la call)

| Regla | Detalle |
|---|---|
| Referral SIEMPRE | Toda marca nueva en Trybe = vía referral link MLO, nunca directo |
| Trybe ID intocable | No cambiar/borrar `?trybe=XXXX` en ads activos |
| Outreach gradual | 10/día → 25 → 50 → 100 (warm-up de cuenta) |
| Brief biweekly | Actualizar Netlify cada 2 semanas con hooks frescos |
| Lanzar 2 días antes del pico | Para maximizar la "ventana de dopamina" del creador |
| No compartir datos internos | ROAS, CAC, spend con creadores = nunca |
| Atribución Trybe = conservadora | Es el piso; el número real es 1,5-2× mayor |
| Samples = enviar el mismo día | Aprobar y no enviar destruye el sample score del creador |
| Partnership Ads = siempre en verde | Verificar icono cada semana |
