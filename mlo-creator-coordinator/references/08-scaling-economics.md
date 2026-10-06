# 08 · Economía de escalado: cuántos creadores, hit rate, coste por winner, churn

Conecta con `mlo-estratega-creativo` (forecast creativo: hit rate, churn, half-life, test tax) y `mlo-creator-spend-report` (spend por creador en Meta). Aquí: los números de mercado y las fórmulas para creadores.

## 1. Hit rates (qué % de lo lanzado se convierte en winner)
| Fuente | Dataset | Winner = | Hit rate |
|---|---|---|---|
| **Motion Creative Benchmarks 2026** | 578.750 creativos, $1,29B Meta, sep-25→ene-26 | ad que gasta ≥10× la mediana de la cuenta | **~5%** (3,8% <$10k/mes → 8,2% >$1M/mes); 50% de ads muertos antes de 28 d; UGC 7,56% vs text-only 11,6% |
| **Agentio (Partnership Ads)** | 8.696 ads, 56 marcas, 12 m | definido por marca | **mediana 20,4%**; 45% de winners parecen perdedores a $100 de spend, 26% a $1.000 |
| Auditorías (AdMake, 200+) | 250-612 ads/cuenta | — | 5-7% [unv] |
| Plofker | nivel creador | "rinde" | **3 de 10 creadores** |
| Post rate de gifting (input) | — | publica | 20-40% (nano 40-60%) |
Motion: hit rate alto suele significar under-testing. **Supuesto de trabajo MLO:** 5-10% de vídeos = winner escalable; 20% usables; 25-30% de creadores producen algo usable; 3/10 creadores rinden.

## 2. Coste por winner
`Coste por winner = (fees creadores + rights de los assets escalados + media de testing) ÷ nº winners`
- Solo producción: 10 vídeos × $600 = $6.000, 2 escalan → **$3.000/winner**.
- Marca $50k/mes, CPA $40: 20% testing = $10k media; 50 assets × $200 = $10k; rights top 20% (~10) ≈ $800 → $20,8k; hit 5-10% (2,5-5 winners) → **$4.200-8.300/winner**; hit 20% → ~$2.100.
- **España:** 30 vídeos × €125 = €3.750 + 10% rights + €3.000 media test ≈ €7.100; hit 6% (1,8 winners) → **≈ €3.900/winner**.
- **MLO pack tipo:** 3 creadores × 2 vídeos × 2-3 hooks = 12-18 piezas ≈ €700-1.000 (ZZEN-rate) + whitelisting + test €1.500-3.000 → con 1-2 winners ≈ €1.500-3.500/winner. Objetivo: bajar €/winner cada trimestre (rollup €/winner por creador en el Roster).
- Vida del winner: Agentio 36 d de media antes de que el CPA suba 1,4× (mediana)-1,8×; Motion: refrescar a frecuencia 2,5-3,0 (a 4: CTR −40%, CVR −60%); UGC de baja calidad decae en 10-14 d, estudio 18-25 [unv].

## 3. Cuántos creadores/vídeos al mes para alimentar una cuenta Meta
**Volumen Motion (creativos nuevos/semana, media vs top-25%):** <$10k: 2,8 / 4,8 · $10-50k: 4,1 / 8,1 · $50-200k: 6,7 / 16 · $200k-1M: 11,2 / 31,1 · $1M+: 18,9 / 54,6. Regla: **~20 ads por winner**.
**Fórmula back-solve:** `vídeos/mes = (spend mensual ÷ spend que absorbe un winner) ÷ vida del winner (meses) ÷ hit rate`. Ej.: $80k/mes, un winner absorbe ~$10k/mes, vida 1,2 m, hit 8% → 8 ÷ 1,2 ÷ 0,08 ≈ **83 vídeos/mes** (~7/semana; ~20 conceptos nuevos y el resto variaciones de hook/edición).
**Creadores:** si 30% de creadores entregan usable y cada activo rinde 3-5 vídeos/mes, para 30 assets UGC nuevos/mes → **~10 creadores activos y ~30 reclutados/mes** (pipeline 3× de MLO).
**CTC Creative Demand Score** (zero-spend rate, concentración top-5, degradación ROAS/spend, share evergreen 30+ d): >50 aguanta volumen, <50 necesita más ads; incluso cuentas a 75 necesitaron ~100 ads/mes; CTC habla de "200 o 400 ads/mes", no "20 o 60". Loop Earplugs: 500+ ads Meta concurrentes por "tribu".
Regla Marcel para arrancar una marca: 2-3 creadores × 2 vídeos × 2-3 hooks/mes; escalar creadores según hit rate real.

## 4. Churn y reactivación de creadores
- La mayoría de relaciones UGC one-off mueren tras 1 transacción; ~19% de programas de embajadores sobreviven al año 2 [unv]; 30-50% inactivos a 90 d sin cadencia [anecdótico]; TikTok Shop open-collab churn 58% en 90 d.
- Palancas con evidencia: call de onboarding 15 min · transparencia de performance (dashboard por creador, Atria) · newsletter mensual con talking points y calendario de lanzamientos · escalera pública de tiers (10% → 15% @2,5k → 20% @5k) · kickers por volumen (+1-3 pt a 5/8/12 vídeos) · leaderboards multi-categoría · **graduar al top ~10% a retainer** · re-regalar en cada lanzamiento (Caraway) · pago puntual (factor #1 de confianza).
- Cadencia MLO: review mensual de spend/winners por creador (skill `mlo-creator-spend-report` + Atria) · **review trimestral: renovar / churn / escalar** · aviso 30 d antes de caducar rights.

## 5. Decisión renovar / churn / escalar (criterio)
| Señal | Acción |
|---|---|
| ≥1 winner en 2 packs, entrega a tiempo, cede rights | **Escalar**: pack mayor o retainer; pasar a contrato B/C; más marcas |
| Usable pero sin winner en 2-3 packs | Cambiar ángulo/brief 1 vez; si no, **pausar** |
| 0 usable, retrasos, >2 rondas, no cede rights | **Churn** (documentar motivo en Notas) |
| Winner con rights a punto de caducar | **Renovar rights** (precio pactado, aviso 30 d) antes de que el ad muera |

## 6. KPIs del programa (reporte mensual por marca)
Outreach enviados · tasa de respuesta · cierres · creadores activos · piezas entregadas/mes · % piezas con rights vigentes · coste por pieza · **coste por winner** · hit rate de creador (winners/piezas) · spend por creador y % del total (naming creator-first) · ROAS/CPA por creador (Atria) · días medios brief→entrega · rondas medias.
