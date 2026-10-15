# Data pipeline — pulling the numbers from Atria

All numbers come from **Atria** (Meta ads analytics MCP, tools `mcp__4610d1aa-...`; load via ToolSearch if deferred). Never ask the user to type performance numbers. Use the brand's Atria **account_id** (internal UUID from `list_ad_accounts`; `config.atriaAccountId` in creators.json). The video CDN base is `https://cdn.tryatria.com/analytics/<account_id>/`.

## 1. Find the account
`list_ad_accounts` → match the brand → copy the internal `id` (UUID). That id goes in `config.atriaAccountId` and is used to build the CDN URL for every video/frame.

## 2. Account ROAS thresholds (for status + winner selection)
`get_ad_account_summary` for the last 90 days (`period=custom`, 92-day window ending yesterday) and `last_30d`, with `metrics=purchase_value`. ROAS = purchase_value ÷ spend. Keep both the 90d and 30d ROAS and the AOV.

## 3. List the ads with business + creative metrics
`list_ad_account_ads` (`period=custom` 90d, `sort_by=spend`, `limit=50`, `metrics=thumbstop_ratio,ctr_link,hold_rate,purchase_value`). The default set already includes spend, roas, purchases, impressions, ctr. This one call gives every metric you need per ad.

## 4. Identify the creators and their ads
- Creator UGC ads carry a **person's name** in `ad_name` (e.g. `CREATOR_PetePastides_...`, `OllieMorgan_...`, `FirstnameLastname_...`). **Exclude** founder videos, AI-animation, statics, and generic concept ads — a creator report is about real UGC creators.
- Group ads by creator. **Group the same video across placements** (same `thumbnail`/video id = one creative, sum its spend/GMV/orders).
- **Top creators** = those whose videos clear the bar: ≥10 orders in 90d AND grouped ROAS ≥ the account's 90d ROAS. (Below the bar = left out; say so to the user.)
- **All of a creator's ads** go in their report (active first). Mark each by status: ACTIVE vs PAUSED.

## 5. Per-ad creative detail (video + hook)
For each ad you'll feature, `get_ad_account_ad` returns `creative.videos[0].url` (the mp4) and `preview_image_url` (the frame) on the Atria CDN — use these **remote, never download**. `creative.body` is the caption.
- **Spoken hook** (talking-to-camera ads): `get_ad_account_video_transcript` (cache-first, free) → if empty, `transcribe_ad_account_video` (small credit). The opening line is the hook.
- **Faceless / text ads** (transcript empty or just "you"): the hook is the opening line of `creative.body`.

## 6. Metric mapping (Atria field → report field)
| Report | Atria field | Format |
|---|---|---|
| Ad spend | `spend` | `€1,234` |
| Conversion value (GMV) | `purchase_value` | `€1,234` |
| ROAS | `roas` (or gmv÷spend for a group) | `1.20x` |
| Orders | `purchases` | `56` |
| Impressions | `impressions` | `53.0K` |
| Hook rate | `thumbstop_ratio` | `43%` |
| CTR | `ctr_link` | `2.2%` |
| Hold 15s | `hold_rate` | `14%` |
| Earnings | computed by the generator = commission × GMV | — |

**Totals per creator** = sum across all their ads (ROAS = total GMV ÷ total spend). Account-average **benchmarks** (hook, CTR) go in `benchmarks` so each metric shows "vs X avg".

## Status mapping
ACTIVE + hook ≥ 30% → Scaling (🚀, class `scale`); ACTIVE otherwise → Testing (🧪, `test`); PAUSED → Paused (⏸, `pause`).
