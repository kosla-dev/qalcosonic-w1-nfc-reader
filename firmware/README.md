# Firmware

The production firmware is an ESPHome configuration for the **Seeed Studio XIAO ESP32-C3** and PN5180 NFC reader.

## Files

- `qalcosonic-w1-nfc-reader.yaml` — sanitized production configuration
- `secrets.example.yaml` — template for local ESPHome secrets

The configuration uses DHCP by default. If you want a static address, assign one in your router or add your own `manual_ip:` block locally.

## Requirements

- ESPHome **2026.8.2 or newer**
- Seeed Studio XIAO ESP32-C3
- PN5180 module
- Custom adapter PCB or equivalent wiring

## External component

The configuration uses:

`https://github.com/dbmaxpayne/esphome_qalcosonicnfc`

Pinned revision:

```text
bed6773b803a7ebf71613585aad8a73376d38b8e
```

Pinning the dependency keeps builds reproducible.

## Setup

1. Copy `qalcosonic-w1-nfc-reader.yaml` into your ESPHome configuration directory.
2. Copy `secrets.example.yaml` to `secrets.yaml`.
3. Replace all placeholder values in `secrets.yaml`.
4. Compile and flash the XIAO ESP32-C3.
5. Add the discovered ESPHome device to Home Assistant.

The configuration uses `Europe/Helsinki` for the optional meter timepoint sensor. Change it locally if needed.

See [`../docs/wiring.md`](../docs/wiring.md) for the pin mapping and [`../docs/esphome-installation.md`](../docs/esphome-installation.md) for flashing instructions.

## Production behavior

- Meter read interval: **300 s / 5 min**
- Five consecutive read failures are allowed before measurement sensors are treated as unavailable
- `Force Sensor Update` button for manual reads
- ESP32 diagnostics grouped into a separate Home Assistant device
- Primary water data and important error flags enabled by default
- Secondary/raw meter data and most network-identification diagnostics disabled by default
- Normal logging level: `INFO`
