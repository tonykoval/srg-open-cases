#!/usr/bin/env python3
"""Builds the strongly regular graph srg(833,416,207,208) of the paper
"A strongly regular graph with parameters (833,416,207,208)" (A. Koval, October 2026) from its definition,
counts the common neighbours of every pair of vertices, and writes the graph in graph6 format.
Standard library only.  usage: python3 construct_srg833.py [outfile.g6]

Vertex set Z_17 x F_49, F_49 = F_7[w]/(w^2 - 3).  Fibre i: Paley(49).  The 136 edges of K_17 are covered by the 34
four-cycles below, written (a, b, c, d) with a, c the positive and b, d the negative vertices of the cycle;
every vertex is positive in four cycles and negative in four.  For the s-th positive occurrence of a vertex it uses
the s-th positive line, for the s-th negative occurrence the s-th negative line (lines = F_7-linear forms on F_49).
For an edge {a, b} of a cycle with a positive and b negative, (a, u) ~ (b, v) iff l_a(u) - l_b(v) in T_ab, where
T_ab = Q = {1, 2, 4} if a ~ b in Paley(17) and T_ab = {0, 3, 5, 6} otherwise."""
import sys, hashlib

CYCLES = [[0, 1, 15, 12], [0, 2, 9, 13], [3, 10, 15, 0], [4, 8, 7, 0], [0, 5, 12, 10], [6, 13, 8, 0], [9, 12, 16, 0],
          [0, 11, 1, 14], [1, 2, 14, 8], [3, 9, 6, 1], [1, 4, 9, 16], [1, 5, 11, 10], [7, 14, 13, 1], [9, 11, 12, 1],
          [2, 3, 11, 6], [4, 7, 13, 2], [2, 5, 10, 8], [2, 7, 11, 15], [10, 14, 16, 2], [2, 11, 13, 12], [4, 11, 14, 3],
          [3, 5, 8, 15], [6, 4, 12, 3], [7, 15, 13, 3], [3, 8, 11, 16], [5, 14, 15, 4], [4, 10, 16, 13], [14, 6, 16, 4],
          [5, 6, 8, 16], [5, 7, 6, 15], [5, 9, 10, 13], [10, 7, 12, 6], [7, 9, 15, 16], [8, 9, 14, 12]]
P, Q17 = 7, {x * x % 17 for x in range(1, 17)}
POS_LINES = [(1, 1), (1, 3), (1, 4), (1, 6)]   # forms x + y, x + 3y, x + 4y, x + 6y: kernel a non-square line of F_49
NEG_LINES = [(1, 0), (0, 1), (1, 2), (1, 5)]   # forms x, y, x + 2y, x + 5y: kernel a square line of F_49
Q7 = {1, 2, 4}; T_PLUS = Q7; T_MINUS = {0, 3, 5, 6}

def build(cycles=None, line_of=None):
    """cycles: list of (a,b,c,d) with a, c positive (default CYCLES); line_of(ci, pos, vertex) -> line for position pos
    of cycle ci (default: the s-th positive/negative occurrence of a vertex, in listing order, gets the s-th line)."""
    if cycles is None: cycles = CYCLES
    els = [(x, y) for x in range(P) for y in range(P)]                  # u = x + y w
    mul = lambda a, b: ((a[0] * b[0] + 3 * a[1] * b[1]) % P, (a[0] * b[1] + a[1] * b[0]) % P)
    squares = {mul(e, e) for e in els if e != (0, 0)}
    assert len(squares) == 24
    form = lambda l, u: (l[0] * u[0] + l[1] * u[1]) % P
    idx = lambda i, u: 49 * i + 7 * u[0] + u[1]
    n = 49 * 17; adj = [0] * n                                           # bitsets
    def add(a, b): adj[a] |= 1 << b; adj[b] |= 1 << a
    for i in range(17):
        for u in els:
            for w in els:
                if u != w and ((u[0] - w[0]) % P, (u[1] - w[1]) % P) in squares: add(idx(i, u), idx(i, w))
    cp = [0] * 17; cn = [0] * 17; used = set(); used_lines = set()
    for ci, (a, b, c, d) in enumerate(cycles):
        if line_of is None:
            lp = {a: POS_LINES[cp[a]], c: POS_LINES[cp[c]]}; ln = {b: NEG_LINES[cn[b]], d: NEG_LINES[cn[d]]}
        else:
            lp = {a: line_of(ci, 0, a), c: line_of(ci, 2, c)}; ln = {b: line_of(ci, 1, b), d: line_of(ci, 3, d)}
        cp[a] += 1; cp[c] += 1; cn[b] += 1; cn[d] += 1
        for v, l in list(lp.items()) + list(ln.items()):
            assert (v, l) not in used_lines, 'direction node used twice'; used_lines.add((v, l))
            assert l in (POS_LINES if v in lp else NEG_LINES)
        for x, y in ((a, b), (b, c), (c, d), (d, a)):
            pos, neg = (x, y) if x in lp else (y, x)
            e = frozenset((pos, neg)); assert e not in used; used.add(e)
            T = T_PLUS if (pos - neg) % 17 in Q17 else T_MINUS
            for u in els:
                fu = form(lp[pos], u)
                for w in els:
                    if (fu - form(ln[neg], w)) % P in T: add(idx(pos, u), idx(neg, w))
    assert len(used) == 136 and cp == [4] * 17 and cn == [4] * 17
    return adj

def check(adj, v=833, k=416, lam=207, mu=208):
    assert all(bin(r).count('1') == k for r in adj), 'degree'
    for i in range(v):
        assert not (adj[i] >> i) & 1
        for j in range(i + 1, v):
            c = bin(adj[i] & adj[j]).count('1')
            assert c == (lam if (adj[i] >> j) & 1 else mu), (i, j, c)
    return True

def graph6(adj):
    v = len(adj); bits = [(adj[i] >> j) & 1 for j in range(v) for i in range(j)]
    while len(bits) % 6: bits.append(0)
    s = '~' + chr(63 + (v >> 12)) + chr(63 + ((v >> 6) & 63)) + chr(63 + (v & 63))
    for t in range(0, len(bits), 6): s += chr(63 + int(''.join(map(str, bits[t:t + 6])), 2))
    return s + '\n'

if __name__ == '__main__':
    adj = build(); check(adj); print('srg(833,416,207,208): all degrees 416, every pair checked (207 / 208)')
    g6 = graph6(adj); out = sys.argv[1] if len(sys.argv) > 1 else 'construct_srg833.g6'
    open(out, 'w', newline='\n').write(g6)
    print('written', out, len(g6), 'bytes, SHA-256', hashlib.sha256(g6.encode()).hexdigest())
