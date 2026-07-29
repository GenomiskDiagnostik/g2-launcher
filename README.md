# G2 Launcher

G2 Launcher is a local-first app library, catalog client, and compatibility runtime for **Even Realities G2** smart glasses.

It lets users install launcher-compatible G2 app packages from a public catalog, keep those apps stored locally in the launcher, and open them from a compact glasses-first interface. The phone WebView is used for catalog browsing, importing, sorting, settings, and app management; the glasses HUD is optimized for the R1 ring and G2 touchpad.

> G2 Launcher does not modify the native Even Hub plugin list. Imported apps run inside the launcher's local compatibility runtime.

## Catalog

The default catalog used by G2 Launcher 0.4.13 and later is:

```text
https://github.com/GenomiskDiagnostik/g2-launcher/tree/main/catalog
```

The machine-readable manifest is [`catalog/g2-launcher.json`](catalog/g2-launcher.json). Launcher-ready packages are stored in [`catalog-packages/`](catalog-packages/) and protected by declared file sizes and SHA-256 checksums.

## Repository layout

```text
.
├── README.md
├── CONTRIBUTING.md
├── catalog/
│   ├── README.md
│   ├── g2-launcher.json
│   └── g2-launcher.schema.json
├── catalog-packages/
│   └── <app-slug>.zip
└── .github/
    └── PULL_REQUEST_TEMPLATE.md
```

## Using the launcher

1. Install G2 Launcher 0.4.13 or later in Even Hub.
2. Open **Catalog** in the launcher.
3. Refresh the catalog and select an app.
4. Install the package, then launch it from the local app library.

Installed apps and launcher settings remain local to the device/WebView storage unless an individual app explicitly implements another storage or network workflow.

## Package compatibility

The catalog distributes **launcher-compatible ZIP packages**. A standard binary `.ehpk` beginning with the `EHPK` container signature cannot currently be converted by the launcher runtime.

A compatible ZIP must contain:

```text
app.json
 dist/
   index.html
   assets/...
```

The files may be inside one top-level project directory. `package_root` can be declared in the catalog entry when the archive contains more than one app or has an unusual layout.

Minimum requirements:

- `app.json` with a stable `package_id`, app `name`, semantic `version`, and valid `entrypoint`;
- a built `dist/` or `web/` directory containing the entrypoint HTML and all runtime assets;
- package size no greater than **20 MiB**;
- no embedded credentials, private tokens, malware, hidden telemetry, or unauthorized recording/capture behavior;
- an explicit redistribution license or written permission to mirror the package;
- correct cooperative G2 teardown, including `bridge.shutDownPageContainer(1)` for the user-initiated exit path;
- hardware-tested R1/G2 navigation and startup rendering;
- every required external host documented. Apps needing hosts outside the launcher's current network whitelist require a launcher permission update before inclusion.

Source-only archives are not accepted. Build the app first and include `dist/` in the submitted ZIP.

## Add your app to the catalog

Catalog additions are made by pull request. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the complete procedure and review checklist.

External contributors who do not have write access should fork the repository and work in a branch in their fork. Repository collaborators with write access may instead create a branch directly in this repository. Both routes produce an ordinary pull request to `main`.

The practical sequence is:

1. Create a contribution branch: use a fork when you do not have write access, or branch directly in this repository when you do.
2. Add a versioned launcher-compatible ZIP to `catalog-packages/`.
3. Calculate its SHA-256 checksum and byte size.
4. Add or update one entry in `catalog/g2-launcher.json`.
5. Set the catalog's top-level `updated` value to the current UTC timestamp.
6. Open a pull request and complete the supplied checklist.

Example entry:

```json
{
  "name": "Example G2 App",
  "package_id": "com.example.g2app",
  "version": "1.0.0",
  "description": "A concise description of the app.",
  "download_url": "https://raw.githubusercontent.com/GenomiskDiagnostik/g2-launcher/main/catalog-packages/example-g2-app.zip",
  "file_name": "example-g2-app-v1.0.0-launcher.zip",
  "sha256": "<64 lowercase hexadecimal characters>",
  "size_bytes": 123456,
  "author": "Developer name",
  "tags": ["utility", "local-first"],
  "source_repository": "https://github.com/example/example-g2-app",
  "license": "MIT",
  "min_launcher_version": "0.4.13"
}
```

The catalog is curated rather than automatically indexed. Submission does not guarantee inclusion; packages are reviewed because they contain executable JavaScript and run inside the launcher.

## Updating an existing app

Use the same `package_id`, increase the app version, replace the package file, and update `download_url`, `file_name`, `sha256`, and `size_bytes`. Do not silently replace a package without changing the version and checksum.

## Security and privacy

Only install apps from developers you trust. Checksums verify that a downloaded file matches the catalog entry; they do not make unreviewed code safe. Repository maintainers may reject or remove packages that introduce undisclosed network traffic, credential handling, tracking, unsafe capture, license problems, or unstable G2 lifecycle behavior.

## Support

Development is maintained by [GenomiskDiagnostik](https://github.com/GenomiskDiagnostik). Ongoing work can be supported through [GitHub Sponsors](https://github.com/sponsors/GenomiskDiagnostik).
