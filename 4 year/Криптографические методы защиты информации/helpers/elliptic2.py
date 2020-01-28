# -*- coding: utf -*-

from elbase import EllipticCurve, PointOnEllipticCurve, describe_points_sum
from base import modinv

curve = EllipticCurve(a=-1, b=1, p=751)

G = PointOnEllipticCurve(0, 1, curve)

n_b = 12

points = [
    ((16, 416), (128, 672)),
    ((56, 419), (59, 386)),
    ((425, 663), (106, 24)),
    ((568, 355), (145, 608)),
    ((188, 93), (279, 398)),
    ((425, 663), (99, 295)),
    ((179, 275), (269, 187)),
    ((188, 93), (395, 337)),
    ((188, 93), (311, 68)),
    ((135, 82), (556, 484)),
    ((56, 419), (106, 727)),
    ((16, 416), (307, 693)),
]

for kG, P_m in points:
    kG = PointOnEllipticCurve(*kG, curve)
    P_m = PointOnEllipticCurve(*P_m, curve)
    print(
        f"$P_m + k \\cdot P_b - n_b \\cdot (kG) = {P_m} - {n_b} \\cdot {kG} = {P_m} + {(n_b * kG).inverted()}={P_m - n_b * kG}$"
    )

    # describe_points_sum(P_m, (n_b * kG).inverted())
