# -*- coding: utf -*-

from elbase import EllipticCurve, PointOnEllipticCurve, describe_points_sum
from base import modinv

curve = EllipticCurve(a=-1, b=1, p=751)

G = PointOnEllipticCurve(0, 1, curve)


P = PointOnEllipticCurve(74, 170, curve)
Q = PointOnEllipticCurve(53, 277, curve)
R = PointOnEllipticCurve(86, 25, curve)

# 2P
print("\r\n\\textbf{Вычисляем $2P$}")

describe_points_sum(P, P)

print(f"\\textbf{{$2P={P+P}$}}")

# 2Q
print("\r\n\\textbf{Вычисляем $2Q$}")

describe_points_sum(Q, Q)

print(f"\\textbf{{$2Q={Q+Q}$}}")

# 3Q
print("\r\n\\textbf{Вычисляем $3Q$}")

describe_points_sum(2 * Q, Q)

print(f"\\textbf{{$3Q={2*Q+Q}$}}")

# 2P+3Q

print("\r\n\\textbf{Вычисляем $2P+3Q$}")

describe_points_sum(2 * P, 3 * Q)

print(f"\\textbf{{$2P+3Q={2*P+3*Q}$}}")

# 2P+3Q-R

print("\r\n\\textbf{Вычисляем $2P+3Q-R$}")

describe_points_sum(2 * P + 3 * Q, R.inverted())

print(f"\\textbf{{$2P+3Q-R={2*P + 3*Q + R.inverted()}$}}")
