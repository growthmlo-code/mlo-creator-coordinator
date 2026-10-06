# 04c · Trybe Brand API — guía operativa + automatización MLO

Fuente: help center API Reference (capturado 18-sep-2026). Cliente listo: `scripts/trybe_api.py`.

## Lo esencial
- Base URL `https://api.jointrybe.com/v1` · versionado v1 (solo cambios aditivos) · **no es pública**: acceso por marca activado por el account manager de Trybe; grupos de endpoints activables por separado (`403 feature_not_enabled` si no).
- **Auth:** `Authorization: Bearer tk_live_<32 chars>`; clave por marca (Integrations → API Access → Create API key, se muestra UNA vez; solo owners/admins; 1 clave activa por marca; Rotate = revoca la anterior sin gracia; Trybe guarda solo SHA-256). Guardar en secrets manager; HTTPS only. Las reviews vía API se atribuyen en el audit trail al miembro que creó la clave.
- **Rate limits** por marca: burst **60 req/min**, sostenido **5.000/día** (ventanas fijas); reviews (approve/reject/request-revision) tienen bolsa aparte **2.000/día**. Headers `ratelimit-limit/remaining/reset`; en 429 `retry-after` (honrarlo, backoff exponencial). Pre-auth: IP limitada a 30/min y 300/día con claves inválidas.
- **Errores** (usar `error.type`, no el message): `validation_error` 400 · `invalid_request` 400 (p.ej. revisar una submission no pending) · `invalid_api_key` 401 (rotar) · `feature_not_enabled` 403 · `not_found` 404 · `rate_limit_exceeded` 429 · `internal_error` 500 (retry con backoff).
- **Convenciones:** recurso único con `object`; listas `{object:"list", data, has_more, next_cursor, previous_cursor}`; paginación por cursor: `limit` (20, máx 100) + `after` (= next_cursor) o `before` (mutuamente excluyentes; **no existe `cursor`** → 400). Dinero en **céntimos USD** enteros (`4280000` = $42.800). Fechas `YYYY-MM-DD` en UTC, timestamps ISO 8601 Z; rangos de rendimiento half-open, default últimos 30 días completos, máx 365 (90 si ranking por métrica o `active_only`); `end_date` ≤ ayer. IDs con prefijo (`creator_`, `program_`/`creator_program_`, `submission_`, `subgroup_`, `product_`), opacos, siempre completos.

## Endpoints
| Método | Ruta | Para qué |
|---|---|---|
| GET | `/creators` | roster activo (id, name, avatar_url, joined_at); sin PII ni username |
| GET | `/creators/{creator_id}` | + `programs[]` (id, name, enrolled_at, status, `commission.display_text` / `display_rules`, sin reglas raw) |
| GET | `/creator-performance` | **bulk BI**: por creador `programs`, `activity` (last_submission_at, last_ad_day all-time) y `performance` en el rango: `earnings_cents`, `trybe_conversions`, `trybe_gmv_cents` (neto de refunds), `new_submissions`, `active_submissions`, `ads`, `spend_cents`, `purchases`, `purchase_value_cents`, `roas` (Meta). Query: `start_date`, `end_date`, `creator_id`, `sort_by` (joined_at o cualquier métrica, desc), `program_id`, `managed_by` (partner/brand), `active_only`, `limit`, `after/before`. ⚠️ Nunca sumar métricas Trybe (link-attributed) con las de Meta (provider-reported). |
| GET | `/submissions` | newest-first; filtros `status` (pending/approved/rejected/revision_requested), `creator_id`, `group_id`, `angle`, `program_id`, `product_id`, `transcript_language`, `query` (substring en transcript/texto en pantalla/nota). Campos: media_type, version, revision_of, program, `ads{count,first_day,last_day}` (uso, no performance), thumbnail_url (estable), group, products, creator_comment, review_comment, `transcript{language,text}`, `angles[{name,source,confidence}]`, `asset{url,expires_at}` (**presigned ~20 min, no cachear**), `trybe_id` (8 chars → `trybe=<id>` en URL y ad name). |
| GET | `/submissions/{id}` | una submission (404 si borrada/superseded/en partner review) |
| POST | `/submissions/{id}/approve` · `/reject` · `/request-revision` | body `{"comment": "..."}` (obligatorio y no vacío en request-revision). **Efectos reales**: approve dispara earnings y notifica. Solo si `status == pending` (evita dobles reviews). |
No hay endpoints (v1) para crear programas, invitar creadores, lanzar ads ni pagos → eso se hace en el portal (o vía Chrome).

## Automatizaciones MLO (con `scripts/trybe_api.py`)
1. **Reporte semanal por creador** → `creator-performance` últimos 7/30 días, sort_by earnings, exportar CSV/xlsx a `REPORTING/` de la marca y tabla a Slack (complementa `mlo-creator-spend-report`).
2. **Cola de revisión** → `submissions?status=pending` con transcript y ángulos → resumen al canal `#creator-ads-[marca]` para revisar en <24h; aprobación/revisión vía API con comentario (siempre con OK humano).
3. **Descarga de aprobados** → `submissions?status=approved` → bajar `asset.url` en el momento (caduca) a Drive/sección UGC → ticket en Editors Hub si hace falta edición.
4. **Alertas** → creadores con `activity.last_submission_at` > 30 días (dormidos) · `active_submissions == 0` con `new_submissions > 0` (aprobados sin lanzar) · `roas` alto con pocos `ads` (candidato a escalar/retainer).
5. **Sync al Roster/Colaboraciones** de Notion: creador Trybe → fila del Roster (Fuente=Trybe, ID Trybe en Notas); cada submission aprobada → fila de Colaboraciones (Coste real = earnings, Winner si ROAS ≥ objetivo).
Env var: `TRYBE_API_KEY` (nunca en repo). Uso:
```bash
python3 ~/.claude/skills/mlo-creator-coordinator/scripts/trybe_api.py creators
python3 ~/.claude/skills/mlo-creator-coordinator/scripts/trybe_api.py performance --start 2026-08-01 --end 2026-08-31 --sort earnings --csv out.csv
python3 ~/.claude/skills/mlo-creator-coordinator/scripts/trybe_api.py submissions --status pending
python3 ~/.claude/skills/mlo-creator-coordinator/scripts/trybe_api.py review submission_xxx approve --comment "Great hook"
```
