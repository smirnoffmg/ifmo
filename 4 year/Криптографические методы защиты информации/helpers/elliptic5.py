# -*- coding: utf -*-
from elbase import EllipticCurve, PointOnEllipticCurve, describe_points_sum
from base import modinv

curve = EllipticCurve(a=-1, b=1, p=751)
G = PointOnEllipticCurve(416, 55, curve)
n = 13

e = 8
d = 5
k = 5


print(f"\r\nНайдём kG = {k}*{G}.\r\n")

print(f"\r\n\\textbf{{Найдём 2G.}}\r\n")
print(f"\r\n$2G = G + G = {G} + {G} = {G+G}$\r\n")
describe_points_sum(G, G)

print(f"\r\n\\textbf{{Найдём 4G.}}\r\n")
print(f"\r\n$4G = 2G + 2G = {2*G} + {2*G} = {4*G}$\r\n")
describe_points_sum(2 * G, 2 * G)

print(f"\r\n\\textbf{{Найдём 5G.}}\r\n")
print(f"\r\n$5G = 4G + G = {4*G} + {G} = {5*G}$\r\n")
describe_points_sum(4 * G, G)

_5G = 5 * G
r = _5G.x % n
print(f"\r\nНайдём $r = x \\mod(n) = {_5G.x} \\mod({n}) = {r}$.\r\n")

z = modinv(k, n)
print(f"\r\nНайдём $z = k^{{-1}} \\mod(n) = {k}{{-1}} \\mod({n}) = {z}$.\r\n")

s = z * (e + d * r) % n
print(
    f"\r\nНайдём $s = z \\cdot (e+ d \\cdot r)\\mod(n) = {z} \\cdot ({r}+ {d} \\cdot {r})\\mod({n})={s}$.\r\n"
)

print(f"\r\n\\textbf{{Цифровая подпись: $(r,s)={r, s}$}}\r\n")
