#!/usr/bin/env python3
"""Trybe Brand API client (v1) for MLO Growth. Stdlib only.
Docs: https://jointrybe.com/help/api-reference/getting-started
Env: TRYBE_API_KEY=tk_live_...  (never commit). Usage: see references/04c-trybe-api.md
"""
import argparse, csv, json, os, sys, time, urllib.parse, urllib.request, urllib.error

BASE = "https://api.jointrybe.com/v1"

def _req(method, path, params=None, body=None, attempt=0):
    key = os.environ.get("TRYBE_API_KEY")
    if not key:
        sys.exit("Falta TRYBE_API_KEY en el entorno")
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        payload = e.read().decode()
        if e.code == 429 and attempt < 5:
            wait = int(e.headers.get("retry-after", "2") or 2)
            time.sleep(wait); return _req(method, path, params, body, attempt + 1)
        if e.code >= 500 and attempt < 3:
            time.sleep(2 ** attempt); return _req(method, path, params, body, attempt + 1)
        try:
            err = json.loads(payload)["error"]
            sys.exit(f"HTTP {e.code} {err.get('type')}: {err.get('message')}")
        except (ValueError, KeyError):
            sys.exit(f"HTTP {e.code}: {payload[:300]}")

def paginate(path, params=None, max_pages=200):
    params = dict(params or {}); params.setdefault("limit", 100)
    items, after = [], None
    for _ in range(max_pages):
        if after: params["after"] = after
        page = _req("GET", path, params)
        items.extend(page.get("data", []))
        if not page.get("has_more"): break
        after = page.get("next_cursor")
    return items

def cmd_creators(a):
    rows = paginate("/creators")
    if a.detail:
        rows = [_req("GET", f"/creators/{r['id']}") for r in rows]
    _out(rows, a)

def cmd_performance(a):
    params = {"start_date": a.start, "end_date": a.end, "sort_by": a.sort, "program_id": a.program,
              "managed_by": a.managed_by, "active_only": "true" if a.active_only else None, "creator_id": a.creator}
    rows = paginate("/creator-performance", params)
    flat = []
    for r in rows:
        p, act, c = r.get("performance", {}), r.get("activity", {}), r.get("creator", {})
        flat.append({"creator_id": c.get("id"), "name": c.get("name"),
                     "programs": "; ".join(x["name"] for x in r.get("programs", [])),
                     "last_submission_at": act.get("last_submission_at"), "last_ad_day": act.get("last_ad_day"),
                     "earnings_usd": (p.get("earnings_cents") or 0) / 100, "trybe_gmv_usd": (p.get("trybe_gmv_cents") or 0) / 100,
                     "trybe_conversions": p.get("trybe_conversions"), "new_submissions": p.get("new_submissions"),
                     "active_submissions": p.get("active_submissions"), "ads": p.get("ads"),
                     "meta_spend_usd": (p.get("spend_cents") or 0) / 100, "meta_purchases": p.get("purchases"),
                     "meta_purchase_value_usd": (p.get("purchase_value_cents") or 0) / 100, "meta_roas": p.get("roas")})
    _out(flat, a)

def cmd_submissions(a):
    params = {"status": a.status, "creator_id": a.creator, "program_id": a.program, "product_id": a.product,
              "angle": a.angle, "transcript_language": a.lang, "query": a.query}
    rows = paginate("/submissions", params)
    if a.download:
        os.makedirs(a.download, exist_ok=True)
        for r in rows:
            asset = r.get("asset") or {}
            if asset.get("url"):
                ext = ".mp4" if r.get("media_type") == "video" else ".jpg"
                dest = os.path.join(a.download, f"{r['creator']['name'].replace(' ', '')}_{r['id']}{ext}")
                urllib.request.urlretrieve(asset["url"], dest); print("saved", dest)
    _out(rows, a)

def cmd_review(a):
    if a.action == "request-revision" and not a.comment:
        sys.exit("request-revision requiere --comment")
    body = {"comment": a.comment} if a.comment else {}
    print(json.dumps(_req("POST", f"/submissions/{a.id}/{a.action}", body=body), indent=2))

def _out(rows, a):
    if getattr(a, "csv", None):
        keys = sorted({k for r in rows for k in r.keys()})
        with open(a.csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); [w.writerow({k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in r.items()}) for r in rows]
        print(f"{len(rows)} filas → {a.csv}")
    else:
        print(json.dumps(rows, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Trybe Brand API v1 client (MLO)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("creators"); s.add_argument("--detail", action="store_true"); s.add_argument("--csv"); s.set_defaults(fn=cmd_creators)
    s = sub.add_parser("performance"); s.add_argument("--start"); s.add_argument("--end"); s.add_argument("--sort", default="earnings")
    s.add_argument("--program"); s.add_argument("--managed-by", dest="managed_by"); s.add_argument("--active-only", action="store_true"); s.add_argument("--creator"); s.add_argument("--csv"); s.set_defaults(fn=cmd_performance)
    s = sub.add_parser("submissions"); s.add_argument("--status"); s.add_argument("--creator"); s.add_argument("--program"); s.add_argument("--product")
    s.add_argument("--angle"); s.add_argument("--lang"); s.add_argument("--query"); s.add_argument("--download", help="carpeta destino para bajar assets (URLs caducan en ~20 min)"); s.add_argument("--csv"); s.set_defaults(fn=cmd_submissions)
    s = sub.add_parser("review"); s.add_argument("id"); s.add_argument("action", choices=["approve", "reject", "request-revision"]); s.add_argument("--comment"); s.set_defaults(fn=cmd_review)
    args = ap.parse_args(); args.fn(args)
