import json
import os
import urllib.request
from datetime import datetime, timezone

API_KEY = os.environ["FBI_API_KEY"]
BASE = "https://api.usa.gov/crime/fbi/cde/summarized/state/NJ"

def fetch_offense(offense: str, start: str = "01-2021", end: str = "12-2025"):
    url = f"{BASE}/{offense}?from={start}&to={end}&API_KEY={API_KEY}"
    req = urllib.request.Request(url, headers={"User-Agent": "nj-crime-explorer-bot"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

payload = {
    "updated_utc": datetime.now(timezone.utc).isoformat(),
    "source": "FBI Crime Data Explorer (/cde/summarized/)",
    "violent_crime": fetch_offense("violent-crime"),
    "property_crime": fetch_offense("property-crime"),
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2)
print("Updated data.json successfully")
