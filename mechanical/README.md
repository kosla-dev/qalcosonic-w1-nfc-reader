# Mechanical design

The production design is a clean-sheet, three-part mount for the Qalcosonic W1 and PN5180.

## Parts

### Base / meter collar

Clips around the Qalcosonic W1 and fixes the orientation of the complete reader assembly.

### PN5180 carrier

Locates the 70 × 39 mm PN5180 PCB by its perimeter while keeping the antenna area open.

### Upper retainer

Clamps the PN5180 gently at the PCB edges using two M3 screws and provides the electronics mounting land.

The side wing on the retainer also provides a convenient mounting surface for the external XIAO ESP32-C3 Wi-Fi antenna. The antenna can be attached flat to the wing using its adhesive backing or thin double-sided tape, as shown in the installed project photographs.

## Key dimensions

- Collar engagement: 11.0 mm
- PN5180 PCB reference outline: 70.0 × 39.0 mm
- PCB thickness used for the design: 1.65 mm
- Nominal PCB side clearance: 0.30 mm per side
- Nominal component-to-meter gap: 0.55 mm

## Editable source

The authoritative CadQuery source is:

```text
mechanical/source/qalcosonic_w1_pn5180_production_r1_0.py
```

It exports the base, carrier and retainer geometry.

## Ready-to-print file

The three-part print plate is:

```text
mechanical/3mf/qalcosonic-w1-pn5180-production-r1.0.3mf
```

## Production package

A user-facing package is included as:

```text
mechanical/qalcosonic-w1-pn5180-production-r1.0.zip
```

It contains:

```text
QALCOSONIC_W1_PN5180_R1.0_PRINT_PLATE.3mf
BASE.step
CARRIER.step
RETAINER.step
README.md
```

The 3MF is ready to print. STEP files are included for inspection and modification. The CadQuery source and validation data are also available in the repository.

## Print orientation

- Base: upright with the collar axis in Z
- Carrier: flat
- Retainer: flat
- Supports: **OFF**
- Brim: normally **OFF**

## Recommended settings

- PETG recommended for long-term installation
- PLA suitable for fit/function testing
- 0.4 mm nozzle
- 0.20 mm layer height
- 3 walls
- 5 top / 5 bottom layers
- 20% grid or gyroid infill
- Supports OFF

## Hardware

- 2 × M3 × 8 mm pan-head screws
- No nuts required

Tighten only until the retainer is seated. Do not bow the PN5180 PCB.
