#!/usr/bin/env python3
"""Check every graph6 line of FILE is srg(v,k,lam,mu): A^2 = kI + lam*A + mu*(J-I-A).
Usage: python3 verify_srg.py FILE v k lam mu      (plain Python 3, no packages)"""
import sys

def decode(s):                      # graph6, n < 258048
    d = [ord(c) - 63 for c in s.strip()]
    if d[0] < 63: n, d = d[0], d[1:]
    else: n, d = (d[1] << 12) | (d[2] << 6) | d[3], d[4:]
    bits = [(x >> (5 - i)) & 1 for x in d for i in range(6)]
    nb = [0] * n; t = 0             # neighbourhoods as int bitmasks
    for j in range(1, n):
        for i in range(j):
            if bits[t]: nb[i] |= 1 << j; nb[j] |= 1 << i
            t += 1
    return n, nb

def is_srg(nb, n, k, lam, mu):
    if any(bin(x).count("1") != k for x in nb): return False
    return all(bin(nb[i] & nb[j]).count("1") == (lam if nb[i] >> j & 1 else mu)
               for i in range(n) for j in range(i + 1, n))

f, v, k, lam, mu = sys.argv[1], *map(int, sys.argv[2:6])
lines = [l for l in open(f) if l.strip()]
bad = 0
for no, line in enumerate(lines, 1):
    n, nb = decode(line)
    ok = n == v and is_srg(nb, n, k, lam, mu)
    bad += not ok
    print(f"{f} line {no}: n={n}", "OK" if ok else "FAIL")
print(f"{f}: {len(lines) - bad}/{len(lines)} OK")
sys.exit(1 if bad or not lines else 0)
