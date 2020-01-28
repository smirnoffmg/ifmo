# -*- coding: utf -*-


def mpow(a, b, m):
    """a ^ b mod m"""
    r = 1
    for i in range(b):
        r *= a
        r %= m
    return r


def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def modinv(a, b):
    """return x such that (x * a) % b == 1"""
    if a < 0:
        a = a % b
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b
    raise Exception(f"Cannot find inverse for {a} mod {b}")


def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def fermat(n):
    t0 = isqrt(n) + 1
    counter = 0
    t = t0 + counter
    temp = isqrt((t * t) - n)
    while (temp * temp) != ((t * t) - n):
        counter += 1
        t = t0 + counter
        temp = isqrt((t * t) - n)
    s = temp
    p = t + s
    q = t - s
    return p, q
