# 07 · Legal, rights y disclosure (ES / EU / UK / US) — QA legal antes de publicar

No es asesoramiento jurídico: es el mapa para preparar contratos y el QA legal (Módulo 11). La redacción la valida Néstor / asesor. Regla MLO: **sin rights vigentes por escrito no se corre el ad** (campo `Rights hasta` en Colaboraciones).

## 1. Cláusulas estándar de mercado 2026 (para negociar y para las plantillas A/B/C)
| Cláusula | Término estándar | Default MLO |
|---|---|---|
| Spec de entregable | formato, duración, nº, aspect ratio, hooks, adherencia a brief, deadline, caption/hashtag/@mención, spec técnica | ~30 s vertical, VO, sin subtítulos quemados, encuadre centrado, raw + editado |
| Revisiones | 2 rondas (feedback consolidado en 5 días hábiles); extra +10-20% del base | **2 rondas**; la 3ª se re-cotiza |
| Ventana de aprobación | 3-5 días hábiles; silencio = aprobado | feedback <24h (SLA MLO) |
| Usage rights | plataformas, territorios, duración, exclusivo/no; default = creador es dueño, marca licencia no exclusiva; 6 m social +20-30%; perpetuo +50-100%; transferencia IP +50-100% sobre licencia | 3 m (8hours) · 6-12 m Meta exclusivo (ZZEN) · **siempre con fecha fin** |
| Paid media / whitelisting | línea aparte; +50-100% o fee mensual por handle; duración del permiso Spark/Partnership | anexo aparte con premium y duración |
| Edición/derivados | la marca puede recortar, subtitular, hacer variaciones; no tergiversar la opinión del creador | sí + raw footage a petición |
| Exclusividad | solo categoría; 30-90 d; con precio | opcional, compensada |
| Disclosure | FTC #ad al inicio y verbal/en pantalla; EU: etiqueta de plataforma + texto por país | ver §3 |
| Moralidad / brand safety | terminación mutua por conducta que dañe reputación; retirada | sí |
| Pago | 50% anticipo / 50% aprobación, o 3 tramos; **net 15-30**; 1,5%/mes demora | MLO: fin de mes + 7 días Wise; cliente directo 30 d |
| Kill fee | 25-50% si se cancela tras brief antes de producir; 50-75% empezada; 100% entregado y aprobado sin usar | incluir en B/C |
| Terminación | 30 d preaviso; retirada de contenido; la licencia de paid sobrevive | MLO 15 d; licencia sobrevive |
| Penalización por borrar contenido | (ZZEN) si el creador retira contenido en vigencia → paga el pack íntegro | opcional |
| Revisión legal | abogado en deals >$25k | Néstor siempre en C |

## 2. Rights: qué cerrar SIEMPRE
¿Cede cuenta (whitelisting)? · ¿Plataformas? · ¿Territorio? · **¿Hasta cuándo?** · ¿Premium? · ¿Puede la marca editar/derivar? · ¿Raw footage? · ¿Qué pasa si el creador borra el post? · ¿Renovación (precio y aviso 30 d antes de caducar)? → todo al Anexo de Whitelisting y a `Rights hasta`.
Mecánica de plataformas: **TikTok Spark Ads** = código de autorización del creador por 7/30/60/365 días. **Meta Partnership Ads** = permiso a nivel de contenido (código de ad) o de cuenta (Business Suite / ajustes IG), revocable en cualquier momento, sin caducidad fija → el contrato pone la caducidad.

## 3. Disclosure y normativa por país
### España
- **Ley 13/2022 (LGCA) + RD 444/2024:** "usuario de especial relevancia" (UER) si ≥300.000 € ingresos brutos/año por la actividad **y** ≥1M seguidores en una plataforma o ≥2M agregados **y** ≥24 vídeos en el año anterior → registro estatal, supervisión y sanción de la **CNMC** (ya ha emitido requerimientos por publicidad encubierta).
- **Código de Conducta AUTOCONTROL de publicidad a través de influencers, 2ª ed. (vigor 1-oct-2025; AEA + AUTOCONTROL + IAB Spain):** aplica a adheridos de cualquier tamaño; la empresa adherida debe informar al influencer e **incluir el cumplimiento en el contrato** (existe contrato modelo AEA de servicios + derechos de imagen).
  - Es publicidad si hay contraprestación de **cualquier tipo**: dinero, producto gratis, eventos, servicios, **links de afiliado**, tarjetas regalo, viajes. Indicadores: códigos de descuento, precios, llamadas a comprar, control editorial de la marca, afiliación.
  - Etiqueta explícita, inmediata, **al inicio**, visible durante todo el vídeo/foto; **preferente la herramienta de plataforma** ("colaboración pagada con [marca]" IG, "contenido promocional" TikTok, "incluye contenido promocional" YT). Aceptado: "publicidad", "publi", "en colaboración con", "colaboración pagada", "Embajador de [marca]", "patrocinado por". **No aceptado:** "Colab", "Sponso", "sp", "Gracias a [marca]", "Regalo de [marca]", "Viaje patrocinado", "Ad"/"Advertising" en inglés; hashtag de marca solo; etiqueta entre hashtags o tras "ver más". Persiste al repostear.
  - Menores: consentimiento parental escrito + firma del menor desde 14 años. IA: generación/modificación sustancial debe cumplir transparencia y no engañar.
  - Responsabilidad de todas las partes; el anunciante se exonera si prueba que el influencer incumplió instrucciones claras → **poner las instrucciones de disclosure por escrito en brief y contrato**. Copy Advice® de AUTOCONTROL permite pre-validar briefs.
- Guardrails por marca (QA de palabras): p.ej. Henric Fuster no menciona Dutasteride/Minoxidil; suplementos (ZZEN, COEUS, Merus) sin claims de salud no autorizados (Reglamento 1924/2006).
### Francia
Loi 2023-451: "publicité" o "collaboration commerciale" visible todo el contenido; etiquetas "images retouchées/virtuelles"; **contrato escrito obligatorio por encima de 1.000 €/año por anunciante** (cash + especie); sanciones hasta 2 años / 300.000 €.
### Italia
AGCOM 2025: "influencers relevantes" ≥500k seguidores o ≥1M views/mes → registro AGCOM; multas hasta 250.000 € (600.000 € menores).
### Alemania
Sin ley específica: UWG + MStV; "Werbung"/"Anzeige"; sin etiqueta solo si no hay contraprestación y no es primordialmente comercial (UWG §5a(4) 2021).
### UE
DSA art. 26: toggle de autodeclaración comercial en plataformas (auditoría 2025: 38% de influencers no lo usa; 358 investigados). UCPD: el influencer compensado es "trader". Digital Fairness Act (propuesta 2026) armonizará [pendiente].
### UK (Bridge, 8hours)
ASA/CAP Code + CMA: "#ad" o "Ad" al inicio, claro sin abrir el post; aplica también a gifting y afiliación; la marca es corresponsable. (Verificar guía ASA vigente antes de cada campaña UK.)
### US
FTC Endorsement Guides (rev. jun-2023, 16 CFR 255): disclosure "clear and conspicuous" e inevitable; en vídeo, **dentro del vídeo** (no solo descripción); cada post sin disclosure = infracción; sanción civil >$53.000 por infracción (2025); demandas colectivas H1-2025 (Celsius, Shein, Revolve) >$1,1B.

## 4. GDPR y whitelisting
Correr ads desde el handle del creador implica sus datos personales y los de su audiencia; marca/agencia actúan como responsable de la segmentación → el contrato debe incluir: cláusula de tratamiento de datos, limitación de finalidad (solo ads), retención y revocación, consentimiento explícito al uso de nombre/imagen/handle. EDPB Guidelines 3/2025 (DSA + GDPR). Garante italiano multó 50.000 € a un micro-influencer por recoger datos de audiencia sin consentimiento (2025). Los datos de envío (dirección, teléfono) del Roster son datos personales: acceso limitado, no compartir con el cliente más allá del envío.

## 5. Checklist QA legal antes de publicar (Módulo 11)
- [ ] Contrato + NDA firmados y archivados; `Rights hasta` informado y **no caducado**
- [ ] Anexo whitelisting (si aplica) con duración y premium; permiso Spark/Partnership activo
- [ ] Disclosure correcta por país (ES: herramienta de plataforma + "publicidad"/"colaboración pagada" al inicio; UK "#ad"; US in-video)
- [ ] Claims revisados contra la lista de palabras prohibidas de la marca y normativa de producto (salud/cosmética)
- [ ] Sin música/marcas de terceros sin licencia; sin menores sin consentimiento
- [ ] Si hay IA: etiquetado AIGC en plataforma
- [ ] Ad name con naming convention creator-first (para el spend report)
