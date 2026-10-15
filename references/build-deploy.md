# Build, deploy & refresh

## Project layout (one folder per brand)
```
~/claude/<brand>-creator-reports/
  creators.json      # the data (you edit)
  history.json       # previous snapshot per slug, for ▲/▼ trend (the refresh task maintains it)
  build_reports.py   # copy of assets/build_reports.py (don't edit per brand)
  deploy.sh          # build + wrangler deploy
  dist/              # generated output
```

## creators.json schema
Top level:
- `config` — `{ brand, atriaAccountId, salt, commissionRate, commissionPlatform, accent, accentDark, accentInk }`. `salt` keeps the per-creator URLs unguessable — set a private random string, keep it stable. `commissionRate` is a fraction (0.10 = 10%). Accent colours rebrand the (dark) theme.
- `updated` — report date string. `angle` — the brand's winning angle. `shootBy` — the CTA date. `benchmarks` — `{ hook, ctr }` account averages.
- `creators[]` — each: `slug`, `name`, `initials`, `role`, `product`, `status {label,emoji,class,note}`, `totals {adspend,gmv,roas,orders,impressions,bestHook,benchNote}`, `ads[]`, `callout`, `formula[] {time,label,quote}`, `formulaNote`, `keep[] {item,why}`, `push[] {item,why}`, `briefs[] {num,tag?,hook,tags[],why}`.
- `ads[]` — each: `code`, `statusLabel/statusClass/statusEmoji`, `angle`, `hook`, `video` (Atria filename, CDN prefixed at build), `poster` (Atria filename), `adspend`, `gmv`, `roas`, `orders`, `hookRate`, `ctr`, `hold`.

See `assets/creators.example.json` for a complete valid file.

## Build
```
python3 build_reports.py
```
Writes `dist/`:
- `index.html` — neutral private root (NO creator list).
- `<slug>-<token>/index.html` — one **private** page per creator (token = sha1(slug|salt)[:10]).
- `overview-<token>/index.html` — the **team** overview (lists everyone) at its own unguessable path.
The generator computes each creator's commission from GMV (`comm()`), renders trend deltas from `history.json`, benchmarks, and the CTA.

## Deploy (Cloudflare Pages — user's go)
`deploy.sh`:
```
cd ~/claude/<brand>-creator-reports
python3 build_reports.py
npx wrangler pages deploy dist --project-name=<brand>-creator-reports --branch=main --commit-dirty=true
```
First time: `npx wrangler pages project create <brand>-creator-reports --production-branch=main`. Needs the user's Cloudflare logged in (`npx wrangler whoami`). Production URL = `https://<brand>-creator-reports.pages.dev`. Hand the user **each creator's private link** + the team overview link (print them with the salt so they're reproducible).

## Scheduled refresh (bi-weekly default)
A scheduled task (cron `0 7 1,15 * *`) that:
1. **Saves history first** — writes `history.json` = `{ "<slug>": { "gmv": <current totals.gmv>, "bestHook": <current> } }` from the CURRENT creators.json, so the next build shows ▲/▼ "vs last".
2. Re-pulls Atria (data-pipeline.md), updates `creators.json` totals + per-ad metrics + status, bumps `updated` and `shootBy`.
3. Rebuilds locally and **notifies the user to publish** (`bash deploy.sh`) — it does NOT auto-publish.
Keep callout/formula/keep/push/briefs unless a creative changed.

## Gotcha: the safety classifier
Writing spend/GMV/ROAS onto a published page can be gated by the auto-mode classifier. It clears with the user's explicit go (they confirm, or change permission mode). Don't route around it; surface it and let them decide.
