# Attribution

This project contains original hardware, ESPHome configuration, documentation, original photographs and a clean-sheet mechanical design, together with one third-party open-source ESPHome dependency.

## Original project material

Original project material is copyright **kosla-dev, 2026** and is released under the scoped licenses described in [`LICENSES/README.md`](LICENSES/README.md):

- firmware/configuration: **MIT**
- PCB and mechanical design source/fabrication assets: **CERN-OHL-P-2.0**
- documentation and original project photographs: **CC BY 4.0**

These licenses apply only to original project material within their documented scope.

## ESPHome Qalcosonic NFC component

The firmware configuration uses the external [`dbmaxpayne/esphome_qalcosonicnfc`](https://github.com/dbmaxpayne/esphome_qalcosonicnfc) component by **dbmaxpayne**.

The production configuration pins the dependency to:

```text
bed6773b803a7ebf71613585aad8a73376d38b8e
```

The upstream repository is licensed under the **GNU Lesser General Public License v2.1 (LGPL-2.1)**. The component remains an external dependency and is not claimed as original work of this repository.

No copy of the component source is vendored here; ESPHome retrieves the pinned upstream revision during the build. Nothing in this repository's MIT license changes the upstream LGPL-2.1 terms.

The upstream component includes PN5180 driver code based on the [`ATrappmann/PN5180-Library`](https://github.com/ATrappmann/PN5180-Library) by **Andreas Trappmann**, licensed under **LGPL-2.1**. See the upstream component for the applicable copyright and license notices.

## Mechanical design

The current Production R1.0 geometry — meter collar/base, PN5180 carrier and upper retainer — was designed parametrically **from scratch** for this project.

The production hardware design assets are released under **CERN-OHL-P-2.0**.

## Custom adapter PCB

The PN5180 ↔ Seeed Studio XIAO ESP32-C3 adapter PCB is original project hardware. Its design/fabrication assets under `hardware/` are released under **CERN-OHL-P-2.0**. Human-readable documentation is CC BY 4.0.

## Documentation and photographs

Project-authored documentation and the photographs under `docs/images/` are original project material released under **CC BY 4.0**.

Suggested attribution:

> Qalcosonic W1 NFC Reader project by kosla-dev

## Product names and trademarks

Qalcosonic, Axioma, PN5180, ESPHome and Seeed Studio product names are used only to identify compatibility and the components used in the build.

This project is independent and is not affiliated with or endorsed by Axioma Metering, Seeed Studio, NXP or the ESPHome project.
