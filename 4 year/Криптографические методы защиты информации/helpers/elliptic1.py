# -*- coding: utf -*-

import pdb, traceback, sys

from elbase import EllipticCurve, PointOnEllipticCurve
from base import modinv

curve = EllipticCurve(a=-1, b=1, p=751)

G = PointOnEllipticCurve(0, 1, curve)


def step(A: PointOnEllipticCurve, B: PointOnEllipticCurve, a, p, i):
    print(f"\r\nВычисляем {i}G:")

    if A == B:
        num = 3 * A.x ** 2 + a
        den = 2 * A.y

        if (num < 0) and (den < 0):
            num, den = -num, -den

        num_mod = num % p
        den_mod = modinv(den, p)

        alpha = (num_mod * den_mod) % p

        print(
            f"""
            \\[
            \\lambda = \\frac{{ 3 \\cdot {A.x}^2 + ({a}) }}{{2 \\cdot {A.y}}} = \\frac{{{num}}}{{{den}}} = {num} \\cdot {den}^{{-1}} = {num_mod} \\cdot {den_mod}\\mod{{{p}}} = {alpha}\\mod{{{p}}}
            \\]
            """
        )

    elif A != B:
        num = B.y - A.y
        den = B.x - A.x

        if (num < 0) and (den < 0):
            num, den = -num, -den

        num_mod = num % p
        den_mod = modinv(den, p)

        alpha = (num_mod * den_mod) % p

        print(
            f"""
            \\[
            \\lambda = \\frac{{{B.y}-{A.y}}}{{{B.x}-{A.x}}} = \\frac{{{B.y-A.y}}}{{{B.x-A.x}}} = {num} \\cdot {den}^{{-1}}\\mod{{{p}}} = {num_mod} \\cdot {den_mod}\\mod{{{p}}}
            \\]
            """
        )

    new_x = (alpha ** 2 - A.x - B.x) % p
    new_y = (alpha * (A.x - new_x) - A.y) % p

    print(
        f"""
        \\[
        x = {alpha}^2 - {A.x} - {B.x} \\mod{{{p}}} = {new_x}\\mod{{{p}}}
        \\]
        """
    )

    print(
        f"""
        \\[
        y = {alpha} \\cdot ({A.x} - {new_x}) - {A.y}\\mod{{{p}}} = {new_y}\\mod{{{p}}}
        \\]
        """
    )

    print(f"\\textbf{{{i}G = {new_x, new_y}}}")
    return PointOnEllipticCurve(new_x, new_y, A.curve)


# G2 = step(G, G, curve.a, curve.p, 2)
# G3 = step(G2, G, curve.a, curve.p, 3)
# G4 = step(G2, G2, curve.a, curve.p, 4)
# G5 = step(G3, G2, curve.a, curve.p, 5)
# G6 = step(G3, G3, curve.a, curve.p, 6)
# G7 = step(G4, G3, curve.a, curve.p, 7)
# G8 = step(G4, G4, curve.a, curve.p, 8)
# G9 = step(G5, G4, curve.a, curve.p, 9)
# G10 = step(G5, G5, curve.a, curve.p, 10)
# G11 = step(G10, G, curve.a, curve.p, 11)
# G12 = step(G6, G6, curve.a, curve.p, 12)
# G13 = step(G7, G6, curve.a, curve.p, 13)
# G14 = step(G7, G7, curve.a, curve.p, 14)
# G15 = step(G8, G7, curve.a, curve.p, 15)
# G16 = step(G8, G8, curve.a, curve.p, 16)
# G17 = step(G9, G8, curve.a, curve.p, 17)
# G18 = step(G9, G9, curve.a, curve.p, 18)
# G19 = step(G10, G9, curve.a, curve.p, 19)

# print("\r\n Вычисляем $Pm+kPb$ для каждой буквы в слове.")


def describe_points_sum(A: PointOnEllipticCurve, B: PointOnEllipticCurve):
    p = A.curve.p
    if A == B:
        num = 3 * A.x ** 2 + a
        den = 2 * A.y

        if (num < 0) and (den < 0):
            num, den = -num, -den

        num_mod = num % p
        den_mod = modinv(den, p)

        alpha = (num_mod * den_mod) % p

        print(
            f"""
            \\[
            \\lambda = \\frac{{ 3 \\cdot {A.x}^2 + ({a}) }}{{2 \\cdot {A.y}}} = \\frac{{{num}}}{{{den}}} = {num} \\cdot {den}^{{-1}} = {num_mod} \\cdot {den_mod}\\mod{{{p}}} = {alpha}\\mod{{{p}}}
            \\]
            """
        )

    elif A != B:
        num = B.y - A.y
        den = B.x - A.x

        if (num < 0) and (den < 0):
            num, den = -num, -den

        num_mod = num % p
        den_mod = modinv(den, p)

        alpha = (num_mod * den_mod) % p

        print(
            f"""
            \\[
            \\lambda = \\frac{{{B.y}-{A.y}}}{{{B.x}-{A.x}}} = \\frac{{{B.y-A.y}}}{{{B.x-A.x}}} = {num} \\cdot {den}^{{-1}}\\mod{{{p}}} = {num_mod} \\cdot {den_mod}\\mod{{{p}}}
            \\]
            """
        )

    new_x = (alpha ** 2 - A.x - B.x) % p
    new_y = (alpha * (A.x - new_x) - A.y) % p

    print(
        f"""
        \\[
        x = {alpha}^2 - {A.x} - {B.x} \\mod{{{p}}} = {new_x}\\mod{{{p}}}
        \\]
        """
    )

    print(
        f"""
        \\[
        y = {alpha} \\cdot ({A.x} - {new_x}) - {A.y}\\mod{{{p}}} = {new_y}\\mod{{{p}}}
        \\]
        """
    )


letters = [
    ("т", 17, (247, 266)),
    ("е", 5, (234, 587)),
    ("р", 4, (243, 87)),
    ("п", 17, (240, 442)),
    ("е", 13, (234, 587)),
    ("л", 2, (237, 454)),
    ("и", 17, (236, 39)),
    ("в", 14, (229, 151)),
    ("о", 19, (240, 309)),
]

Pb = PointOnEllipticCurve(725, 195, curve)

for l, k, point in letters:
    point = PointOnEllipticCurve(*point, curve)
    # print(
    # f"\\textbf{{$Pm(\\text{{{l}}})+k \\cdot Pb = {point} + {k} \\cdot {Pb} = {point} + {k*Pb} = {point + k*Pb}$}}"
    # )

    # describe_points_sum(point, k*Pb)

    print(f"{k*G, point + k*Pb}")
