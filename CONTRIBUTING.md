# Contributing apps to the G2 Launcher catalog

Thank you for contributing an Even Realities G2 app. The catalog contains executable packages, so additions are reviewed for reproducibility, permissions, licensing, and G2 lifecycle behavior before merge.

## 1. Prepare a launcher-compatible package

Create a ZIP containing a built Even Hub web app:

```text
app.json
 dist/
   index.html
   assets/...
```

A single top-level project directory is acceptable. For a non-standard archive layout, add `package_root` to the catalog entry.

The package must:

- contain `app.json` or, as a fallback, `package.json`;
- contain a built `dist/` or `web/` entrypoint; source-only ZIPs are rejected;
- use a stable reverse-domain `package_id`;
- use semantic versioning;
- be no larger than 20 MiB;
- include all assets needed at runtime;
- avoid secrets, private API tokens, hidden telemetry, malware, and unauthorized capture;
- have an explicit license that permits redistribution, or documented maintainer permission;
- perform cooperative shutdown with `bridge.shutDownPageContainer(1)` on the user exit path;
- render something on the G2 HUD shortly after startup;
- be tested on physical G2 glasses with the R1 ring or G2 touchpad.

The launcher cannot currently convert the official binary `EHPK` container format. Submit a ZIP with `app.json` and built `dist/`, even when the same app is also distributed as `.ehpk` through Even Hub.

## 2. Check network compatibility

List every external HTTP, HTTPS, WebSocket, or local service used by the app in the pull request.

Imported apps run under the launcher's own manifest permissions. A new domain that is not already in G2 Launcher's network whitelist cannot be approved merely by adding it to the submitted app's `app.json`; the launcher itself must be reviewed and released with the additional host permission.

Apps with user-configurable relay hosts, unrestricted endpoints, or unclear data flows may be deferred until a safe permission model exists.

## 3. Add the package

Place the ZIP in:

```text
catalog-packages/<stable-app-slug>.zip
```

Use a stable path. The version is recorded in the catalog entry and in `file_name`; changing the repository path for every patch release is optional.

Generate the checksum and exact byte size.

Linux/macOS:

```bash
sha256sum catalog-packages/example-g2-app.zip
wc -c < catalog-packages/example-g2-app.zip
```

PowerShell:

```powershell
(Get-FileHash catalog-packages/example-g2-app.zip -Algorithm SHA256).Hash.ToLower()
(Get-Item catalog-packages/example-g2-app.zip).Length
```

## 4. Add the catalog entry

Edit `catalog/g2-launcher.json` and add one object to `apps`:

```json
{
  "name": "Example G2 App",
  "package_id": "com.example.g2app",
  "version": "1.0.0",
  "description": "A concise description of the app.",
  "download_url": "https://raw.githubusercontent.com/GenomiskDiagnostik/g2-launcher/main/catalog-packages/example-g2-app.zip",
  "file_name": "example-g2-app-v1.0.0-launcher.zip",
  "sha256": "<sha256>",
  "size_bytes": 123456,
  "author": "Developer name",
  "tags": ["utility"],
  "source_repository": "https://github.com/example/example-g2-app",
  "license": "MIT",
  "min_launcher_version": "0.4.13"
}
```

Also update the top-level `updated` timestamp in UTC, for example:

```json
"updated": "2026-07-29T13:30:00Z"
```

### Required catalog fields

- `name`
- `package_id`
- `version`
- `file_name`
- one install source, normally `download_url`

### Strongly required for review

- `description`
- `sha256`
- `size_bytes`
- `author`
- `source_repository`
- `license`
- `min_launcher_version`
- concise `tags`

Alternative advanced install sources (`package_files`, `package_chunks`, or `bundled_path`) require prior maintainer agreement. Normal third-party submissions should use one ZIP and `download_url`.

## 5. Validate before opening the pull request

At minimum:

```bash
python -m json.tool catalog/g2-launcher.json > /dev/null
unzip -l catalog-packages/example-g2-app.zip
```

Confirm that:

- the checksum and byte size exactly match the ZIP;
- `app.json` is present and parses as JSON;
- the declared entrypoint exists in `dist/` or `web/`;
- no secret or environment file is included;
- the package starts, displays on G2, accepts input, and exits cleanly;
- repeated launch/exit cycles do not leave GPS, timers, workers, requests, sockets, or event handlers active.

## 6. Open a pull request

Include:

- app name, package ID, and version;
- source repository and license;
- build instructions or a reproducible release reference;
- every external host/service used;
- physical G2/R1 test results;
- privacy/data handling summary;
- confirmation that redistribution is allowed.

The pull request template contains the full checklist.

## Review and acceptance

Maintainers may inspect source, unpack the submitted ZIP, compare the built files with the source release, verify checksums, request changes, and hardware-test the package. Packages may be deferred when licensing, network permissions, teardown, privacy, or reproducibility are unresolved.

Accepted packages may later be removed or disabled if they become unsafe, unavailable, legally ambiguous, or incompatible with current launcher versions.

## Updating an existing catalog app

Keep the existing `package_id`. Increase `version`, replace the ZIP, recalculate `sha256` and `size_bytes`, and update the metadata. Mention breaking changes, new permissions, and new external hosts explicitly.
