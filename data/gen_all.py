#!/usr/bin/env python3
import json

def gen():
    q = {}
    q["demo"] = [{"id":"demo","text":"sample","type":"sum"}]
    return q

q = gen()
with open("/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v10.json", "w") as f:
    json.dump(q, f, ensure_ascii=False, indent=2)
print(f"Generated: {len(q)} groups")
