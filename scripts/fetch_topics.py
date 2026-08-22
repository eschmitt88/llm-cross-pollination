"""Download the OpenAlex topic taxonomy into data/openalex_topics.json.
Re-run to refresh the sampling frame (the file is small enough for git)."""
import json, time, urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "openalex_topics.json"
out, cursor = [], "*"
while cursor:
    url = (f"https://api.openalex.org/topics?per-page=200&cursor={cursor}"
           "&select=id,display_name,description,keywords,domain,field,subfield,works_count")
    req = urllib.request.Request(url, headers={"User-Agent": "llm-cross-pollination (research)"})
    d = json.load(urllib.request.urlopen(req, timeout=60))
    for t in d["results"]:
        out.append({"id": t["id"].rsplit("/", 1)[1], "name": t["display_name"],
                    "description": t["description"], "keywords": t["keywords"],
                    "domain": t["domain"]["display_name"], "field": t["field"]["display_name"],
                    "subfield": t["subfield"]["display_name"], "works_count": t["works_count"]})
    cursor = d["meta"].get("next_cursor"); time.sleep(0.2)
OUT.parent.mkdir(exist_ok=True)
json.dump(out, OUT.open("w"), indent=0, ensure_ascii=False)
print(len(out), "topics ->", OUT)
