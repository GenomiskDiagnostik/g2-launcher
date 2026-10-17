#!/usr/bin/env python3
import json
import pathlib
import sys

p = pathlib.Path(sys.argv[1])
data = json.loads(p.read_text())
perms = data.get("permissions", [])
if isinstance(perms, list):
    cleaned = []
    for perm in perms:
        if not isinstance(perm, dict):
            cleaned.append(perm)
            continue
        wl = perm.get("whitelist", [])
        if perm.get("name") == "network" and wl and all(
            host in {"https://fonts.googleapis.com", "https://fonts.gstatic.com"} for host in wl
        ):
            continue
        cleaned.append(perm)
    data["permissions"] = cleaned
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
