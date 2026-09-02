# ESPHome installation

## Requirements

- ESPHome 2026.8.2 or newer
- Seeed Studio XIAO ESP32-C3
- PN5180 module connected through the project adapter PCB
- Wi-Fi credentials
- Home Assistant is optional but is the primary integration target

## Configuration

Copy `firmware/qalcosonic-w1-nfc-reader.yaml` to your ESPHome configuration directory and create a `secrets.yaml` based on `firmware/secrets.example.yaml`.

Required secrets:

- `wifi_ssid`
- `wifi_password`
- `fallback_password`
- `api_key`
- `ota_password`

The configuration uses DHCP by default.

The external component is pinned to:

`bed6773b803a7ebf71613585aad8a73376d38b8e`

from:

`https://github.com/dbmaxpayne/esphome_qalcosonicnfc`

## First flash

1. Connect the XIAO ESP32-C3 over USB.
2. Open ESPHome Device Builder or use the ESPHome CLI.
3. Compile the configuration.
4. Flash over USB for the first installation.
5. Open logs immediately after boot.
6. Confirm Wi-Fi and API connectivity.
7. Wait for the Qalcosonic NFC component to scan the meter.

A successful read cycle should include lines similar to:

```text
Scanning for water meter...
Inventory successful
Getting water meter infos
Water Usage: ...
Water Temperature: ...
Battery Percentage: ...
```

Do not copy meter UID, meter ID or network addresses from another installation into your configuration.

## Updates

After the device has joined Wi-Fi, normal ESPHome OTA updates can be used.

The configuration reads the meter every 300 seconds. A `Force Sensor Update` button is also exposed for manual testing.

## Diagnostics

The firmware exposes diagnostic entities for:

- Wi-Fi signal
- ESP32 internal temperature
- uptime
- device status
- reset reason
- optional ESPHome / Wi-Fi information

These are useful when commissioning the hardware or investigating intermittent reads.
