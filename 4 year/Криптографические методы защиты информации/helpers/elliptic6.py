# -*- coding: utf -*-
from elbase import EllipticCurve, PointOnEllipticCurve, describe_points_sum
from base import modinv

curve = EllipticCurve(a=-1, b=1, p=751)
G = PointOnEllipticCurve(562, 89, curve)

e = 4
Q = PointOnEllipticCurve(384, 475, curve)
r, s = 11, 9
n = 13

X = 12 * G + Q

print(
    f"\r\nПроверка подписи начинается с проверки условий $ 1 \\leq r \\leq n−1, 1 \\leq s \\leq n−1 $."
)

print(f"\r\n$1 \\leq {r} \\leq {(n-1)}, 1 \\leq {s} \\leq {(n-1)}$.")

v = modinv(s, n)
u1 = e * v % n
u2 = s * v % n
print(f"\r\nВычисляем $v = s^{{-1}} \\mod(n) = {s}^{{-1}} \\mod({n}) = {v}$")
print(f"\r\nВычисляем $u_1 = e \\cdot v \\mod(n) = {e} \\cdot {v} \\mod({n}) = {u1}$")
print(f"\r\nВычисляем $u_2 = s \\cdot v \\mod(n) = {s} \\cdot {v} \\mod({n}) = {u2}$")
print(
    f"\r\nНаходим точку $X=u_1\\cdot G+u_2 \\cdot Q = {u1} \\cdot {G} + {u2} \\cdot {Q}$"
)

for i in [2, 4, 8]:
    print(
        f"\r\n Найдем ${i}G = {int(i/2)}*G+{int(i/2)}*G={int(i/2) * G} + {int(i/2) * G} = {i * G}$"
    )
    describe_points_sum(int(i / 2) * G, int(i / 2) * G)

print(f"\r\n Найдем $12G = 4*G+8*G={4 * G} + {8 * G} = {12 * G}$")
describe_points_sum(4 * G, 8 * G)

print(f"\r\n Найдем $12G + Q ={12 * G} + {Q} = {12 * G + Q}$")
describe_points_sum(12 * G, Q)

print(f"\r\n\\textbf{{X = {X}}}")

print(
    f"\r\nСравниваем значения $r$ и $x \\mod n$, если они совпадают, следовательно, подпись действительная."
)

print("\\begin{equation*}\r\n\\begin{aligned}")
print(f" r &= {r} \\")
print(f" x \\mod n &= {X.x % n} \\")
print("\\end{aligned}\r\n\\end{equation*}")
