## App submission

**App name:**

**Package ID:**

**Version:**

**Source repository:**

**License / redistribution permission:**

### Package

- [ ] The submitted ZIP contains `app.json` (or supported `package.json`) and a built `dist/` or `web/` directory.
- [ ] The catalog `sha256` and `size_bytes` match the uploaded package.
- [ ] The package is no larger than 20 MiB.
- [ ] No credentials, private tokens, build secrets, or environment files are included.
- [ ] The version was increased for an update to an existing `package_id`.

### G2 behavior

- [ ] Tested on physical Even Realities G2 hardware.
- [ ] Tested with R1 ring or G2 touchpad input.
- [ ] The app renders on the glasses shortly after startup.
- [ ] User exit calls `bridge.shutDownPageContainer(1)` and cleans up active resources.
- [ ] Repeated launch/exit cycles do not leave timers, GPS, workers, requests, sockets, or event handlers running.

### Network, privacy, and safety

List every external host/service used:

```text
none
```

Describe data stored, transmitted, recorded, or captured:

```text
local-only / describe here
```

- [ ] Network behavior and data handling are disclosed.
- [ ] The app contains no hidden telemetry, malware, or unauthorized capture functionality.
- [ ] The declared license permits catalog redistribution of the submitted package.

### Test notes

Describe tested phone/Even App/G2 versions and any known limitations.
