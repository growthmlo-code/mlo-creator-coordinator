# Best practices & gotchas

## The metric rule (most important)
There are two creator deliverables, and they treat metrics oppositely:
- **General `creator-brief`** (onboarding, all creators, Trybe): **metric-free**. Never ad spend, ROAS, GMV or earnings.
- **This premium report** (1-a-1, top fixed-contract creators): **shows** ad spend, conversion value (GMV), ROAS, orders **and** the creator's commission — on purpose, because the brand pays creators on GMV and wants transparency to keep them.

This is a deliberate, client-confirmed exception. Apply it only to premium reports for trusted creators, and only when the user has confirmed it. Keep the two deliverables separate; never let business metrics leak onto the general brief.

## Commission
- Label it honestly while simulated: "Simulated · live with <platform>". The report's subtitle also says earnings are simulated.
- One rate constant (`config.commissionRate`), computed from GMV in the generator. Never hardcode per-creator earnings — they'd drift from the GMV.
- When the real payout platform (e.g. Trybe) is wired, switch to the real rate / real attributed GMV from that source. Note that platform GMV (last-click) differs from Meta-attributed `purchase_value`.

## Privacy
- One unguessable URL per creator; the public root lists nothing; the team overview sits at its own unguessable path. A creator must never reach another creator's earnings.
- The `salt` is what makes URLs unguessable — keep it private and stable (changing it changes every URL).

## Honesty / coaching
- Every number is real (Atria). Every hook/quote comes from the creator's actual ads (transcript or caption) — nothing invented.
- `keep`/`push`/`briefs` are real coaching grounded in that creator's signals: e.g. a low hook rate → "fix the first 2 seconds"; a short ad with low hold → "extend it"; paused ads → "shoot a relaunch cut". Supportive tone — the creator reads this.

## Design
- Dark, editorial, premium. Accent is brand-configurable (`config.accent*`). Playfair Display (serif, hooks/headlines) + DM Sans (body) + JetBrains Mono (labels).
- Mobile-first: creators open on phones. 9:16 videos autoplay muted/looped with a sound button (remote Atria mp4s play cross-origin).
- Sections, in order: cover (status + business totals + earnings) · your videos · why it works · keep/push · film these next (+ CTA) · what happens next.

## Gotchas that will bite you
- **`<meta charset="utf-8">` is mandatory** on every generated page — a static host may not send a charset, and then emojis / × / · / → / € become mojibake.
- **Videos are remote Atria URLs** (content-hashed, stable, no signature → don't expire). Reference them; never download/bundle. (This is the opposite of Meta's own CDN URLs, which do expire — the skill's selection step reads from Atria, not Meta.)
- **A local `python3 -m http.server` backgrounded with `&` dies when the shell exits.** Run it as its own backgrounded command (e.g. Bash `run_in_background`), or it won't stay up for preview.
- **Cloudflare Pages first deploy** may 522 for a few seconds while the production domain propagates — retry the root URL, or test the deployment-specific `*.pages.dev` URL.
- **The safety classifier** can block writing spend/GMV/ROAS to a published page until the user explicitly authorizes — surface it, don't work around it.
- **Verify in a real browser at phone width** before reporting done: videos playing, business metrics + earnings + "vs avg" + CTA rendering, root showing no list.
