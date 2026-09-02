# Troubleshooting

## Meter is not detected

If `Inventory successful` never appears:

1. confirm the PN5180 is powered;
2. verify MOSI/MISO/SCK/NSS/BUSY/RST against `docs/wiring.md`;
3. confirm the PN5180 antenna faces the meter;
4. install the mechanical holder in the supplied R1.0 orientation;
5. avoid unnecessary metal or thick material in the antenna area;
6. press **Force Sensor Update** and watch the ESPHome logs.

Do not mirror or arbitrarily rotate the holder. NFC performance depends on the installed antenna position.

## `qalcosonicnfc took a long time` warning

A single timing warning around a successful NFC read can occur because the component performs a complete PN5180 transaction and meter decode in one update operation.

If meter data is published correctly and reads remain stable, an isolated warning is not considered a failed read. Repeated timing warnings together with missed reads should be investigated.

## ESP32-C3 gets hot

Disconnect power immediately if the board becomes abnormally hot or there is an electrical smell.

Before reconnecting:

- inspect soldering for bridges;
- check 3.3 V to GND for an unintended short;
- inspect XIAO orientation;
- inspect the PN5180 and adapter board for damaged pads or excess solder.

Normal internal ESP32-C3 diagnostic temperature readings are not the same as a physically overheating board.

## Wi-Fi is weak

Meter reads happen locally, so Wi-Fi does not need to be exceptionally strong. Repeated API disconnects should still be addressed by improving AP placement or reducing obstruction around the XIAO antenna.

## Home Assistant does not show entities

1. confirm the ESPHome API connection succeeds;
2. verify the device appears under the ESPHome integration;
3. check whether the desired entity is disabled by default;
4. inspect ESPHome logs to confirm the source value is being read.

## Mechanical fit is wrong

Do not force the meter collar or bend the PN5180 PCB. Printer calibration, elephant-foot, material shrinkage and hardware variants can affect fit.

Use the source model to adjust tolerances if needed, but keep the documented installed orientation unless you also revalidate NFC operation on the meter.
