# G2 Launcher Community Catalog

This directory contains the public machine-readable catalog used by G2 Launcher.

Default repository address:

```text
https://github.com/GenomiskDiagnostik/g2-launcher/tree/main/catalog
```

Files:

- `g2-launcher.json` — catalog metadata and package download references;
- `g2-launcher.schema.json` — JSON Schema for catalog entries.

Launcher-ready ZIP packages are stored in `../catalog-packages/`. Each published package should be referenced by an exact byte size and immutable SHA-256 checksum.

## Catalog entry sources

The normal installation source is `download_url`, pointing to a ZIP that includes `app.json` and built `dist/` or `web/` output. The launcher also understands `package_files`, `package_chunks`, and maintainer-only `bundled_path`, but those formats require prior coordination.

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) for package requirements, metadata fields, validation commands, and the pull-request process.
