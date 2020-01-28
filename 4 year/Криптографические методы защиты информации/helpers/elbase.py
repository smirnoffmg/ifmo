# -*- coding: utf -*-

from base import modinv
from functools import reduce


class EllipticException(Exception):
    pass


class Point:
    def __init__(self, x=float("inf"), y=float("inf")):
        self.x = x
        self.y = y

    def __str__(self):
        return f"point({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)


class EllipticCurve:
    """
        y^2 = x^3 + a * x + b
        """

    def __init__(self, a=0, b=0, p=None):
        self.a = a
        self.b = b
        self.p = p

    def __str__(self):
        return f"curve y^2 = x^3 + {self.a} * x + {self.b} (mod {self.p})"


class PointOnEllipticCurve(Point):
    def __init__(self, x: float, y: float, curve: EllipticCurve):
        self.x = x
        self.y = y
        self.curve = curve

    def inverted(self):
        return PointOnEllipticCurve(self.x, -self.y % self.curve.p, self.curve)

    def __str__(self):
        return f"{self.x, self.y}"

    def __eq__(self, other):
        return (
            (self.x == other.x) and (self.y == other.y) and (self.curve == other.curve)
        )

    def __add__(self, other):
        if not isinstance(other, PointOnEllipticCurve):
            raise EllipticException(
                f"{other} is {type(other)}, not PointOnEllipticCurve"
            )

        x1, x2, y1, y2 = self.x, other.x, self.y, other.y
        p = self.curve.p
        a = self.curve.a

        if self == other:
            num = 3 * x1 ** 2 + a
            den = 2 * y1
        else:
            num = y2 - y1
            den = x2 - x1

        if (num < 0) and (den < 0):
            num, den = -num, -den

        num_mod = num % p
        den_mod = modinv(den, p)

        alpha = (num_mod * den_mod) % p

        x_new = (alpha ** 2 - x1 - x2) % p
        y_new = (alpha * (x1 - x_new) - y1) % p

        return PointOnEllipticCurve(x_new, y_new, self.curve)

    def __radd__(self, other):
        print(f"radd self={self} other={other}")
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(other.inverted())

    def __mul__(self, other: int):
        other = int(other)
        r = [self for x in range(other)]
        return reduce(lambda a, b: a + b, r)

    def __rmul__(self, other: int):
        other = int(other)
        r = [self for x in range(other)]
        return reduce(lambda a, b: a + b, r)


def describe_points_sum(A: PointOnEllipticCurve, B: PointOnEllipticCurve):
    p = A.curve.p
    a = A.curve.a

    print("\\begin{equation*}\r\n\\begin{aligned}")
    if A == B:
        num = 3 * A.x ** 2 + a
        den = 2 * A.y

        if (num < 0) and (den < 0):
            num, den = -num, -den

        num_mod = num % p
        den_mod = modinv(den, p)

        alpha = (num_mod * den_mod) % p

        print(
            f"\\lambda &= \\frac{{ 3 \\cdot {A.x}^2 + ({a}) }}{{2 \\cdot {A.y}}} = \\frac{{{num}}}{{{den}}} = {num} \\cdot {den}^{{-1}} = {num_mod} \\cdot {den_mod}\\mod{{{p}}} = {alpha}\\mod{{{p}}} \\\\"
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
            f"\\lambda &= \\frac{{{B.y}-{A.y}}}{{{B.x}-{A.x}}} = \\frac{{{B.y-A.y}}}{{{B.x-A.x}}} = {num} \\cdot {den}^{{-1}}\\mod{{{p}}} = {num_mod} \\cdot {den_mod}\\mod{{{p}}} = {alpha}\\mod{{{p}}} \\\\"
        )

    new_x = (alpha ** 2 - A.x - B.x) % p
    new_y = (alpha * (A.x - new_x) - A.y) % p

    print(f"x &= {alpha}^2 - {A.x} - {B.x} \\mod{{{p}}} = {new_x}\\mod{{{p}}} \\\\")

    print(
        f"y &= {alpha} \\cdot ({A.x} - {new_x}) - {A.y}\\mod{{{p}}} = {new_y}\\mod{{{p}}}"
    )
    print("\\end{aligned}\r\n\\end{equation*}")
