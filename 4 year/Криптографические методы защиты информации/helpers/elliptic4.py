# -*- coding: utf -*-

from elbase import EllipticCurve, PointOnEllipticCurve, describe_points_sum
from base import modinv

curve = EllipticCurve(a=-1, b=1, p=751)

P = PointOnEllipticCurve(39, 580, curve)
N = 109

for n in [2, 4, 8, 16, 32, 64]:
    m = n // 2
    print(f"\r\n \\textbf{{Найдём ${n}P$}} \r\n")
    print(
        f"${n} \\cdot P = {m} \\cdot P + {m} \\cdot P = {m * P} + {m * P} = {n * P} \\mod {curve.p}$"
    )
    describe_points_sum(m * P, m * P)


start = 64
for n in [32, 8, 4, 1]:
    print(f"\r\n \\textbf{{Найдём ${start}P + {n}P = {start+n}P$}} \r\n")
    print(
        f"${start+n} \\cdot P = {start} \\cdot P + {n} \\cdot P = {start * P} + {n * P} = {(start+n) * P} \\mod {curve.p}$"
    )
    describe_points_sum(start * P, n * P)
    start += n


print(f"\r\n \\textbf{{Результат ${N}P = {N*P}$}} \r\n")
