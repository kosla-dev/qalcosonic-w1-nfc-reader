# PCB manufacturing

The custom adapter PCB is prepared as an AISLER-compatible production package.

## Production specification

- 2 copper layers
- 1.6 mm board thickness
- 35 µm outer copper
- lead-free HASL finish
- green solder mask
- white silkscreen
- no stencil required for the hand-assembled build

## Revision 3

Revision 3 is the current production PCB revision.

## Production files

The complete board-house file set is checked into:

```text
hardware/gerbers/
```

It contains the board outline, top and bottom copper, solder masks, silkscreens and plated/non-plated drill data.

These checked-in Gerber/Excellon files are the PCB production source of truth.

## AISLER archive

The ready-to-upload archive is:

```text
hardware/manufacturing/qalcosonic-w1-nfc-reader-pcb-rev3-aisler.zip
```

You can upload this ZIP directly to AISLER or create an archive from the exact files under `hardware/gerbers/`.

## Before ordering

Always inspect the board-house preview, especially:

1. board outline and drill locations
2. top and bottom copper
3. solder-mask openings
4. top silkscreen orientation
5. bottom silkscreen orientation

PCB photographs elsewhere in the repository are illustrative; use the Revision 3 production files when ordering boards.
