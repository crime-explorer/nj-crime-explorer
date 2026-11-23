import json, os, urllib.request
from datetime import datetime, timezone

API_KEY = os.environ["FBI_API_KEY"]
URL = f"https://api.usa.gov/crime/fbi/cde/estimate/state/NJ?from=2021&to=2026&API_KEY={API_KEY}"

req = urllib.request.Request(URL, headers={"User-Agent": "nj-crime-explorer-bot"})
with urllib.request.urlopen(req, timeout=30) as resp:
    raw = json.loads(resp.read().decode("utf-8"))

# Map API response into your site's structure (adjust keys if FBI updates schema)
payload = {
    "updated_utc": datetime.now(timezone.utc).isoformat(),
    "source": "FBI Crime Data Explorer API",
    "raw_estimates": raw,
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2)
