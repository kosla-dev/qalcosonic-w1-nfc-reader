"""Qalcosonic W1 + PN5180 clean-sheet production mount R1.0.

Parametric CadQuery source for the three physically validated production parts:
base/meter collar, PN5180 carrier and upper retainer.

Coordinate system: XY is the meter/PCB plane, +Z points away from the meter.
Requires CadQuery 2.6.x.
"""

from pathlib import Path
import cadquery as cq

REV = "QALCOSONIC_W1_PN5180_CLEANSHEET_PRODUCTION_R1.0"
OUT = Path(__file__).resolve().parent / "generated"

# Meter fit — physically validated on a Qalcosonic W1.
METER_INNER_R = 30.657
METER_HALF_STRAIGHT = 8.747
COLLAR_OUTER_R = 33.200
COLLAR_OUTER_HALF_STRAIGHT = 8.800
COLLAR_H = 11.000
LUG_Y = 6.500
LUG_W = 7.000
LUG_RELIEF_OUTER_X = 34.800
LUG_BOSS_OUTER_X = 36.800
LUG_BOSS_HALF_Y = 12.000

# PN5180 envelope and validated NFC position.
PCB_L = 70.000
PCB_W = 39.000
PCB_T = 1.650
PCB_CX = -5.000
PCB_CY = 0.000

# Carrier.
CARRIER_FLOOR = 1.200
PCB_CLEARANCE = 0.300
SUPPORT_OVERLAP = 1.300
SUPPORT_OUTBOARD = 1.800
LOCATOR_WALL = 1.100
LOCATOR_H = 2.750
CLAMP_SEAT_H = 2.820

# Fasteners.
SCREW_X = -5.000
SCREW_Y = 43.000
BASE_BOSS_R = 4.300
PILOT_D = 2.700
PILOT_DEPTH = 8.000
CLEARANCE_D = 3.400
PAD_R = 5.200
ARM_W = 8.000

# Retainer and XIAO/C3 mounting land.
RETAINER_T = 1.800
RETAINER_EDGE_OVERLAP = 1.600
RETAINER_SIDE_W = 2.600
RETAINER_X_START = -31.000
C3_PAD_X = 40.000
C3_PAD_Y = 20.000


def box(x0, x1, y0, y1, z0, z1):
    return (cq.Workplane("XY")
            .box(x1-x0, y1-y0, z1-z0, centered=(True, True, False))
            .translate(((x0+x1)/2, (y0+y1)/2, z0)))


def cyl(x, y, r, z0, h):
    return cq.Workplane("XY").center(x, y).circle(r).extrude(h).translate((0, 0, z0))


def capsule(r, half_straight, h, z0=0.0):
    return (box(-r, r, -half_straight, half_straight, z0, z0+h)
            .union(cyl(0, half_straight, r, z0, h))
            .union(cyl(0, -half_straight, r, z0, h)))


def pcb_bounds():
    return (PCB_CX-PCB_L/2, PCB_CX+PCB_L/2,
            PCB_CY-PCB_W/2, PCB_CY+PCB_W/2)


def build_base():
    outer = capsule(COLLAR_OUTER_R, COLLAR_OUTER_HALF_STRAIGHT, COLLAR_H)
    # Local external material behind the two meter-lug reliefs.
    outer = outer.union(box(METER_INNER_R-0.5, LUG_BOSS_OUTER_X,
                            -LUG_BOSS_HALF_Y, LUG_BOSS_HALF_Y, 0, COLLAR_H))
    for sy in (-SCREW_Y, SCREW_Y):
        outer = outer.union(cyl(SCREW_X, sy, BASE_BOSS_R, 0, COLLAR_H))

    inner = capsule(METER_INNER_R, METER_HALF_STRAIGHT, COLLAR_H+0.4, -0.2)
    shape = outer.cut(inner)

    half = LUG_W/2
    for cy in (-LUG_Y, LUG_Y):
        shape = shape.cut(box(METER_INNER_R-0.5, LUG_RELIEF_OUTER_X,
                              cy-half, cy+half, -0.2, COLLAR_H+0.2))

    for sy in (-SCREW_Y, SCREW_Y):
        shape = shape.cut(cyl(SCREW_X, sy, PILOT_D/2,
                               COLLAR_H-PILOT_DEPTH, PILOT_DEPTH+0.2))
    return shape.clean()


def build_carrier():
    x0, x1, y0, y1 = pcb_bounds()
    ov, out, zf = SUPPORT_OVERLAP, SUPPORT_OUTBOARD, CARRIER_FLOOR

    shape = box(x0-0.3, x1+0.3, y0-out, y0+ov, 0, zf)
    shape = shape.union(box(x0-0.3, x1+0.3, y1-ov, y1+out, 0, zf))
    shape = shape.union(box(x1-ov, x1+out, y0-out, y1+out, 0, zf))

    c, w = PCB_CLEARANCE, LOCATOR_WALL
    shape = shape.union(box(x0, x1+out, y0-c-w, y0-c, 0, LOCATOR_H))
    shape = shape.union(box(x0, x1+out, y1+c, y1+c+w, 0, LOCATOR_H))
    shape = shape.union(box(x1+c, x1+c+w, y0-out, y1+out, 0, LOCATOR_H))

    # Small corner stops at the electronics/header end.
    sx0, sx1 = x0-c-w, x0-c
    shape = shape.union(box(sx0, sx1, y0-c-w, y0+4.5, 0, LOCATOR_H))
    shape = shape.union(box(sx0, sx1, y1-4.5, y1+c+w, 0, LOCATOR_H))

    for sy in (-SCREW_Y, SCREW_Y):
        near_y = y0-out if sy < 0 else y1+out
        ay0, ay1 = sorted((near_y, sy))
        shape = shape.union(box(SCREW_X-ARM_W/2, SCREW_X+ARM_W/2,
                                ay0, ay1, 0, zf))
        shape = shape.union(cyl(SCREW_X, sy, PAD_R, 0, CLAMP_SEAT_H))
        shape = shape.cut(cyl(SCREW_X, sy, CLEARANCE_D/2, -0.1, CLAMP_SEAT_H+0.2))
    return shape.clean()


def build_retainer():
    x0, x1, y0, y1 = pcb_bounds()
    t, ov, w = RETAINER_T, RETAINER_EDGE_OVERLAP, RETAINER_SIDE_W

    shape = box(RETAINER_X_START, x1+0.2, y0-0.2, y0+w, 0, t)
    shape = shape.union(box(RETAINER_X_START, x1+0.2, y1-w, y1+0.2, 0, t))
    shape = shape.union(box(x1-ov, x1+0.2, y0-0.2, y1+0.2, 0, t))

    # 20 x 40 mm external XIAO/C3 mounting land.
    pad_x0 = RETAINER_X_START
    pad_x1 = pad_x0 + C3_PAD_X
    shape = shape.union(box(pad_x0, pad_x1, y1, y1+C3_PAD_Y, 0, t))

    # Original production R1.0 screw arms connect the retainer edge bands to
    # the two external screw pads. These are part of the physically validated
    # retainer geometry and must not be omitted from regenerated production files.
    for sy in (-SCREW_Y, SCREW_Y):
        near_y = y0 if sy < 0 else y1
        ay0, ay1 = sorted((near_y, sy))
        shape = shape.union(box(SCREW_X-ARM_W/2, SCREW_X+ARM_W/2,
                                ay0, ay1, 0, t))
        shape = shape.union(cyl(SCREW_X, sy, PAD_R, 0, t))
        shape = shape.cut(cyl(SCREW_X, sy, CLEARANCE_D/2, -0.1, t+0.2))
    return shape.clean()


def export(shape, name):
    OUT.mkdir(parents=True, exist_ok=True)
    cq.exporters.export(shape, str(OUT / f"{name}.step"))
    cq.exporters.export(shape, str(OUT / f"{name}.stl"),
                        tolerance=0.035, angularTolerance=0.08)


def main():
    export(build_base(), "base")
    export(build_carrier(), "carrier")
    export(build_retainer(), "retainer")
    print(f"Generated production geometry in {OUT}")


if __name__ == "__main__":
    main()
