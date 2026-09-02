# Home Assistant

The reader integrates through the standard ESPHome integration.

## Add the device

After the first successful ESPHome boot and Wi-Fi connection, Home Assistant should discover the device automatically. If it does not, add it manually through **Settings → Devices & services → Add integration → ESPHome** and enter the reader's hostname or IP address.

The default firmware configuration uses the hostname:

`qalcosonic-w1-nfc-reader-xiao`

## Entity reference

The tables below list the entities exposed by the production configuration in [`firmware/qalcosonic-w1-nfc-reader.yaml`](../firmware/qalcosonic-w1-nfc-reader.yaml).

Home Assistant entity IDs are generated from the device and entity names and may change if you rename the device. The names below are the display names defined by the shipped configuration.

### Primary water data

These entities are enabled by default.

| Entity | Type | Description |
|---|---|---|
| **Water Consumption** | Sensor | Cumulative water volume in m³ |
| **Water Flow** | Sensor | Current water flow in m³/h |
| **Water Temperature** | Sensor | Water temperature reported by the meter |
| **Battery Level** | Sensor | Meter battery level |
| **Consecutive Errors** | Sensor | Consecutive NFC/read error count |

### Secondary water data

These entities are available but disabled by default to keep the normal entity list clean.

| Entity | Type | Default | Description |
|---|---|---|---|
| **External Temperature** | Sensor | Disabled | External temperature value reported by the meter |
| **Volume (Only Positive)** | Sensor | Disabled | Positive-direction water volume |
| **Volume (Only Negative)** | Sensor | Disabled | Negative-direction water volume |

### Meter warnings and errors

The most useful warning entities are enabled by default.

| Entity | Type | Default | Description |
|---|---|---|---|
| **Leakage** | Binary sensor | Enabled | Meter leakage warning |
| **Pipe Burst** | Binary sensor | Enabled | Burst / unusually high-flow warning |
| **Low Battery Warning** | Binary sensor | Enabled | Meter low-battery warning |
| **Hardware Failure** | Binary sensor | Enabled | Meter hardware-failure flag |
| **Software Failure** | Binary sensor | Enabled | Meter software-failure flag |
| **No Flow Sensor Signal** | Binary sensor | Enabled | No flow-sensor signal warning |
| **Reverse Flow** | Binary sensor | Enabled | Reverse-flow warning |
| **Reconfiguration Warning** | Binary sensor | Disabled | Meter reconfiguration warning |
| **No Consumption** | Binary sensor | Disabled | No-consumption warning |
| **Damage of Meter Housing** | Binary sensor | Disabled | Meter-housing damage warning |
| **Calculator Hardware Failure** | Binary sensor | Disabled | Calculator hardware-failure flag |
| **Optical Communication Error** | Binary sensor | Disabled | Optical communication error flag |
| **Excessive Flow Rate** | Binary sensor | Disabled | Excessive-flow-rate warning |
| **Freeze Alert** | Binary sensor | Disabled | Freeze warning |

### Meter information

These identification fields are disabled by default.

| Entity | Type | Default | Description |
|---|---|---|---|
| **Meter ID** | Sensor | Disabled | Meter identifier |
| **Serial Number** | Sensor | Disabled | Meter serial number |
| **Manufacturer ID** | Sensor | Disabled | Manufacturer identifier |
| **Meter Version** | Sensor | Disabled | Meter version information |

### Timing and raw diagnostics

These lower-level fields are disabled by default and are mainly useful for troubleshooting or protocol inspection.

| Entity | Type | Default | Description |
|---|---|---|---|
| **Timepoint** | Sensor | Disabled | Meter timepoint converted using `Europe/Helsinki` |
| **Timepoint Raw** | Sensor | Disabled | Raw meter timepoint value |
| **Operating Time** | Sensor | Disabled | Meter operating-time value |
| **On Time** | Sensor | Disabled | Meter on-time value |
| **Error Flags Raw** | Sensor | Disabled | Raw meter error flags |
| **M-Bus Raw Data** | Sensor | Disabled | Raw M-Bus payload/data exposed by the component |

### Controls

| Entity | Type | Default | Description |
|---|---|---|---|
| **Force Sensor Update** | Button | Enabled | Immediately requests a new meter read |
| **Restart** | Button | Enabled | Restarts the ESP32-C3 |

### ESP32-C3 diagnostics

The production configuration creates a separate **ESP32-C3 Diagnostics** device for hardware/network diagnostics.

| Entity | Type | Default | Description |
|---|---|---|---|
| **Temperature** | Sensor | Enabled | ESP32-C3 internal temperature |
| **WiFi Signal** | Sensor | Enabled | Wi-Fi signal strength |
| **Uptime** | Sensor | Enabled | ESP32-C3 uptime |
| **Status** | Binary sensor | Enabled | ESPHome connection/status state |
| **Reset Reason** | Text sensor | Enabled | Reason for the most recent ESP32 reset |
| **ESPHome Version** | Text sensor | Disabled | ESPHome firmware version |
| **IP Address** | Text sensor | Disabled | Current network IP address |
| **Connected SSID** | Text sensor | Disabled | Connected Wi-Fi SSID |
| **Connected BSSID** | Text sensor | Disabled | Connected access-point BSSID |
| **MAC Address** | Text sensor | Disabled | ESP32-C3 MAC address |

Disabled entities can be enabled from the Home Assistant device's entity settings when they are needed.

## Energy dashboard / water tracking

`Water Consumption` is the cumulative meter value and is the appropriate source when a Home Assistant water-consumption dashboard expects a monotonically increasing total.

If replacing an existing water-meter reader and preserving long-term statistics is important, verify the old and new readers show the same physical meter reading before switching the dashboard/statistics source. Do not reset or artificially zero the meter value during migration.

## Manual read

The ESPHome device exposes a **Force Sensor Update** button. Use it to trigger an immediate read while testing antenna placement or after mechanical changes.

## Expected update interval

The production configuration polls the meter every **300 seconds (5 minutes)**. This is intentional; water-meter NFC data does not need high-frequency polling for normal Home Assistant use.
