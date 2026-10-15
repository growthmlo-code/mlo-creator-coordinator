# Brand registry — one-shot config per brand

When the user says **"create the creator report for <brand>"**, read this file, copy that brand's `config` block straight into `creators.json`, and go. Everything the generator needs is here. If a brand is not listed, build its config from `mlo-brand-brain-<brand>` (colours) + `list_ad_accounts` (Atria id) and **add it here** when done.

The generic generator (`assets/build_reports.py`) is now fully config-driven: `lang` (`en`/`es`), `showCommission` (bool), `currency`, and the accent trio. No per-brand code. (The three live reports — 8hours, ZZEN, Ancestra — still run on older forked `build_reports.py` copies in their project folders; when you next touch one, migrate it onto this config + the skill generator, don't fork again.)

## Config field reference
| Field | What | Example |
|---|---|---|
| `brand` | Display name | `"ZZEN"` |
| `atriaAccountId` | Internal Atria UUID (from `list_ad_accounts`) — builds the CDN URL | `"a5f02bfc509240c695329edd4fac1b12"` |
| `lang` | `"es"` or `"en"` — all creator-facing copy | `"es"` |
| `showCommission` | `true` shows each creator's earnings (GMV × rate); `false` hides every earnings line (brand pays outside the platform or commission not signed yet) | `false` |
| `currency` | Symbol for the earnings figure | `"€"` |
| `commissionRate` | Decimal; only used when `showCommission` | `0.10` |
| `commissionPlatform` | Named in "live with X" | `"Trybe"` |
| `accent` / `accentDark` / `accentInk` | Accent hex, a darker shade (avatar gradient end), and the ink that sits ON the accent (button/avatar text) | `#00DA8C` / `#0E7A5A` / `#06130E` |
| `salt` | Private random string — makes per-creator URLs unguessable. **Keep secret; never change once links are shared** (it would break every creator's URL). | `"zz3n-mlo-private-2026-q7w4"` |

Top-level (siblings of `config`, not inside it): `updated`, `angle`, `shootBy`, `benchmarks` (`{hook, ctr}` account averages for the "vs avg" notes), `creators[]`.

---

## Live brands (ready)

### 8HOURS  ·  en  ·  commission ON
```json
"config": {
  "brand": "8HOURS", "atriaAccountId": "2974be40b9764b00bcd0c5c75878e4f7",
  "lang": "en", "currency": "€",
  "showCommission": true, "commissionRate": 0.10, "commissionPlatform": "Trybe",
  "accent": "#E0A569", "accentDark": "#8a5a33", "accentInk": "#2a1708",
  "salt": "8h-mlo-private-2026-REPLACE"
}
```
Project `8hours-creator-reports` · live `8hours-creator-reports.pages.dev` · EUR. English. The one brand with the commission exception already live (10% Trybe, simulated until payouts wire).

### ZZEN  ·  es  ·  commission OFF (today)
```json
"config": {
  "brand": "ZZEN", "atriaAccountId": "a5f02bfc509240c695329edd4fac1b12",
  "lang": "es", "currency": "€",
  "showCommission": false, "commissionRate": 0.10, "commissionPlatform": "Trybe",
  "accent": "#00DA8C", "accentDark": "#0E7A5A", "accentInk": "#06130E",
  "salt": "zz3n-mlo-private-2026-q7w4"
}
```
Project `zzen-creator-reports` · live `zzen-creator-reports.pages.dev` · EUR. Spanish, dark green theme. Runs **sin comisión** today. The Oct-2026 creator proposal (jose@zzenlabs.com) proposes 10% via Trybe — flip `showCommission` to `true` once signed. Roster incl. René (internal), Isabel Belaustegui, Juan Pedro García, Jon, David Vaquero, Raquel Oliva, The Twibbles, Farmacia Teresa.

### Ancestra  ·  es  ·  commission OFF (today)
```json
"config": {
  "brand": "Ancestra", "atriaAccountId": "31102eb5058d46c3942cf94ba419e205",
  "lang": "es", "currency": "€",
  "showCommission": false, "commissionRate": 0.10, "commissionPlatform": "Trybe",
  "accent": "#E0A24E", "accentDark": "#8a6020", "accentInk": "#241803",
  "salt": "ancestra-mlo-private-2026-REPLACE"
}
```
Project `ancestra-creator-reports` · live `ancestra-creator-reports.pages.dev` · EUR. Spanish, gold theme. Sin comisión today; proposal (jorge@ancestra.es) proposes 10% Trybe. Roster: Saribor, Manu, Paula.

---

## Portfolio — Atria account ids ready (build the rest of the config from the brand brain)

Pull colours from `mlo-brand-brain-<brand>`; set `lang`/`currency`/`showCommission` as noted. Confirm commission with the user before switching it on for any brand.

| Brand | Atria account id | lang | currency | Notes |
|---|---|---|---|---|
| Bala di Gala | `a79bae3bcf16465a9793e189a3959c6c` | es | $ (MXN) | Mexico |
| The Bridge | `7a62292dac79415f9c7a2017292012d6` | en | £ | Apple-Watch strap specialist; navy/brass |
| MUTO | `49b1707075124dffa2b653dfe8aa8b95` | en | £ | UK |
| QiHealth | `3f65738fea674d2298071be1309c1743` | es | $ (MXN) | COFEPRIS claims apply; teal #0E8F9E |
| Box Hero | `a3eead9045a944b39c861c56c677f03e` | en | $ | Men's boxers |

> Currency note: the symbol is cosmetic (just the earnings figure). For MXN/USD stores the Atria figures are already in that currency — set `currency` to match what Atria returns, and don't convert.
