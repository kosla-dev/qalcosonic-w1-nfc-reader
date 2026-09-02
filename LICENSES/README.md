# Licenses

This repository uses different licenses for software, open-hardware design material and documentation/media.

Copyright for original project material is held by **kosla-dev** unless a file states otherwise.

## Firmware — MIT

Original project software/configuration under `firmware/` is licensed under the **MIT License**, including:

- `firmware/qalcosonic-w1-nfc-reader.yaml`
- `firmware/secrets.example.yaml`

License text: [`MIT.txt`](MIT.txt)

The external `dbmaxpayne/esphome_qalcosonicnfc` component is not relicensed here and remains under its upstream LGPL-2.1 terms.

## PCB and mechanical design — CERN-OHL-P-2.0

Original hardware design and fabrication/print assets are licensed under the **CERN Open Hardware Licence Version 2 — Permissive (CERN-OHL-P-2.0)**.

This includes:

- `hardware/` fabrication assets, including Gerber/Excellon data and production archives
- `mechanical/source/`
- `mechanical/3mf/`
- mechanical production archives and validation data

Human-readable README/documentation files are covered by CC BY 4.0 instead.

License text: [`CERN-OHL-P-2.0.txt`](CERN-OHL-P-2.0.txt)

## Documentation and photographs — CC BY 4.0

Original project documentation and photographs are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

This includes the root documentation files, `docs/`, documentation README files and the original photographs under `docs/images/`.

Suggested attribution:

> Qalcosonic W1 NFC Reader project by kosla-dev — CC BY 4.0

License text: [`CC-BY-4.0.txt`](CC-BY-4.0.txt)

## Third-party dependency

The firmware uses [`dbmaxpayne/esphome_qalcosonicnfc`](https://github.com/dbmaxpayne/esphome_qalcosonicnfc), pinned to:

```text
bed6773b803a7ebf71613585aad8a73376d38b8e
```

The component remains under its upstream **LGPL-2.1** license and is not vendored into this repository.

See [`../ATTRIBUTION.md`](../ATTRIBUTION.md) for attribution details.
