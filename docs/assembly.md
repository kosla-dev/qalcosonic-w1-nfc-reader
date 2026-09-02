# Assembly

The production mechanical design consists of three printed parts:

1. **Base / meter collar**
2. **PN5180 carrier**
3. **Upper retainer**

> **Safety and responsibility:** Build and install this project at your own risk. Verify applicable local regulations and the requirements of your water utility or meter owner before installation. Do not disturb metrology seals, certified measurement functions or utility-owned equipment.

## Required parts

- Seeed Studio XIAO ESP32-C3
- PN5180 NFC reader
- custom adapter PCB
- R1.0 printed base / meter collar
- printed PN5180 carrier
- printed upper retainer
- 2 × M3 × 8 mm pan-head screws

Do not use a screw length that bottoms out before the retainer is seated or causes the PN5180 PCB to bow.

## 1. Assemble the electronics

1. Solder the Seeed Studio XIAO ESP32-C3 and PN5180 connections to the custom adapter PCB.
2. Inspect all solder joints for bridges or incomplete joints.
3. Check that 3.3 V, 5 V and GND are not shorted.
4. Confirm the XIAO and PN5180 orientation before applying power.
5. Power the assembly on the bench and verify that no component becomes abnormally hot.
6. Flash the production ESPHome configuration and confirm that the device connects normally.

## 2. Install the PN5180 in the carrier

1. Place the PN5180 module into the printed carrier.
2. Confirm that the PCB sits flat and no component or solder joint is pressed by the printed part.
3. Place the upper retainer over the PCB edge bands.
4. Insert the two M3 × 8 mm screws.
5. Tighten evenly only until the retainer is seated.
6. Confirm that the PN5180 PCB remains flat.
7. Attach the external XIAO ESP32-C3 Wi-Fi antenna flat to the side wing on the retainer using the antenna's adhesive backing or thin double-sided tape. The installed project photographs show the intended placement.

No nuts are required.

## 3. Install the reader on the Qalcosonic W1

1. Use the supplied R1.0 base / collar orientation.
2. Fit the collar onto the meter without forcing it over the meter protrusions.
3. Confirm that the modeled reliefs clear the meter correctly.
4. Keep the carrier and PN5180 in the orientation defined by the R1.0 assembly.
5. Check that the electronics and solder joints do not contact the meter body.
6. Confirm that USB access to the XIAO ESP32-C3 remains practical.

Do not mirror or arbitrarily rotate the printed assembly. NFC performance depends on the complete installed antenna position.

## 4. Functional check

After assembly:

1. Power the reader.
2. Open the ESPHome logs.
3. Confirm that `Inventory successful` appears on a normal read cycle.
4. Confirm that meter data is decoded and published to Home Assistant.
5. Verify that `Consecutive Errors` returns to `0` after successful reads.
6. Check that the PN5180 PCB remains flat and securely retained.
