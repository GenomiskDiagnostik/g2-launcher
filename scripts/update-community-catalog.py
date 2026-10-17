#!/usr/bin/env python3
import datetime
import hashlib
import json
import pathlib

root = pathlib.Path(".")
catalog_path = root / "catalog/g2-launcher.json"
catalog = json.loads(catalog_path.read_text())

def meta(path):
    b = path.read_bytes()
    return hashlib.sha256(b).hexdigest(), len(b)

entries = [
    {
        "name": "My Pomodoro",
        "package_id": "com.tarumzu.mypomodoro",
        "version": "0.1.4",
        "description": "Customizable Pomodoro timer with work/break cycles, session persistence and full glasses controls.",
        "download_url": "https://raw.githubusercontent.com/GenomiskDiagnostik/g2-launcher/main/catalog-packages/my-pomodoro.zip",
        "file_name": "my-pomodoro-v0.1.4-launcher.zip",
        "author": "tarumzu",
        "tags": ["productivity", "timer", "pomodoro"],
        "source_repository": "https://github.com/tarumzu/my-pomodoro-even-g2",
        "license": "MIT",
        "min_launcher_version": "0.4.14",
        "upstream_commit": "89dea0e1877681a3b879a4ef64d667622741ba0a"
    },
    {
        "name": "Chess",
        "package_id": "com.harmon.chess",
        "version": "2.1.0",
        "description": "Chess for G2 with Stockfish play, Bullet Blitz and training modes, controlled from the R1/touchpad.",
        "download_url": "https://raw.githubusercontent.com/GenomiskDiagnostik/g2-launcher/main/catalog-packages/evenchess.zip",
        "file_name": "evenchess-v2.1.0-launcher.zip",
        "author": "Dustin Harmon",
        "tags": ["game", "chess", "offline"],
        "source_repository": "https://github.com/dmyster145/EvenChess",
        "license": "MIT",
        "min_launcher_version": "0.4.14",
        "upstream_commit": "426a689e94bcb4bfac2911a332b44e5614c1c371",
        "launcher_patch": "Google Fonts links were removed from the phone help page; the corresponding network permission was removed. G2 game code is otherwise built from the pinned upstream commit."
    },
    {
        "name": "Solitaire",
        "package_id": "com.harmon.solitaire",
        "version": "1.1.1",
        "description": "Klondike Solitaire for G2 with three-gesture controls, Move Assist and persistent save/resume.",
        "download_url": "https://raw.githubusercontent.com/GenomiskDiagnostik/g2-launcher/main/catalog-packages/evensolitaire.zip",
        "file_name": "evensolitaire-v1.1.1-launcher.zip",
        "author": "Dustin Harmon",
        "tags": ["game", "solitaire", "offline"],
        "source_repository": "https://github.com/dmyster145/EvenSolitaire",
        "license": "MIT",
        "min_launcher_version": "0.4.14",
        "upstream_commit": "ca823277842c16150cda3917da428131e6edc822",
        "launcher_patch": "Google Fonts links were removed from the phone help page; the corresponding network permission was removed. G2 game code is otherwise built from the pinned upstream commit."
    }
]

paths = {
    "com.tarumzu.mypomodoro": root / "catalog-packages/my-pomodoro.zip",
    "com.harmon.chess": root / "catalog-packages/evenchess.zip",
    "com.harmon.solitaire": root / "catalog-packages/evensolitaire.zip",
}
for entry in entries:
    sha, size = meta(paths[entry["package_id"]])
    entry["sha256"] = sha
    entry["size_bytes"] = size

ids = {entry["package_id"] for entry in entries}
catalog["apps"] = [entry for entry in catalog.get("apps", []) if entry.get("package_id") not in ids] + entries
catalog["updated"] = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
