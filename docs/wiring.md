# Wiring

The production reader uses a custom adapter PCB between the Seeed Studio XIAO ESP32-C3 and PN5180 NFC module.

## PN5180 signal mapping

| PN5180 signal | XIAO ESP32-C3 |
|---|---:|
| MOSI | GPIO6 |
| MISO | GPIO7 |
| SCK | GPIO21 |
| NSS / CS | GPIO5 |
| BUSY | GPIO20 |
| RST | GPIO4 |

These assignments are the same values used by `firmware/qalcosonic-w1-nfc-reader.yaml`.

## Power

Use the custom adapter PCB as the wiring reference rather than free-wiring the modules. Before first power-up:

1. inspect the 3.3 V and GND rails for solder bridges;
2. verify continuity only where expected;
3. confirm the XIAO orientation;
4. confirm the PN5180 orientation;
5. apply power while watching for abnormal heating.

## SPI / NFC notes

The PN5180 is used as an ISO15693 frontend. Keep the antenna side facing the water meter and avoid adding unnecessary metal directly in the antenna area.
