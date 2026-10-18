# Self-contained construction of an srg(217,66,15,22).  Stdlib only.
# Vertices (j,x), j in 0..6, x in Z_31.  (j,x) ~ (j',y)  iff  y-x in S[j][j'] (mod 31).
# C = <2> = {1,2,4,8,16} is the subgroup of order 5 of Z_31^*; rC its cosets, r in {1,3,5,7,11,15}.
import hashlib, itertools
C = lambda r: {(r*c) % 31 for c in (1, 2, 4, 8, 16)}
Z = {0}
S = {}
S[0,1] = Z|C(5)|C(15);  S[0,2] = Z|C(7)|C(11);  S[0,3] = Z|C(1)|C(3)
S[1,1] = C(1)|C(15);    S[1,2] = Z|C(7);        S[1,3] = Z|C(11)
S[1,4] = Z|C(3)|C(7);   S[1,5] = Z|C(3)|C(5);   S[1,6] = Z|C(5)|C(15)
S[2,2] = C(5)|C(11);    S[2,3] = Z|C(1);        S[2,4] = Z|C(7)|C(11)
S[2,5] = Z|C(1)|C(15);  S[2,6] = Z|C(7)|C(15)
S[3,3] = C(3)|C(7);     S[3,4] = Z|C(1)|C(11);  S[3,5] = Z|C(1)|C(3);  S[3,6] = Z|C(5)|C(11)
for j in (1, 2, 3): S[0, j+3] = S[0, j]                 # the central involution swaps blocks 1,2,3 <-> 4,5,6
for i, j in [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]: S[i+3, j+3] = S[i, j]
S[0,0] = set()
for (i, j), s in list(S.items()):
    if i != j: S[j, i] = {(-d) % 31 for d in s}          # symmetry
V = [(j, x) for j in range(7) for x in range(31)]
idx = {v: n for n, v in enumerate(V)}
adj = {n: set() for n in range(217)}
for (j, x), (k, y) in itertools.combinations(V, 2):
    if (y - x) % 31 in S[j, k]:
        adj[idx[j, x]].add(idx[k, y]); adj[idx[k, y]].add(idx[j, x])
# exact SRG check
assert all(len(adj[v]) == 66 for v in adj)
for u in range(217):
    for v in range(u+1, 217):
        c = len(adj[u] & adj[v])
        assert c == (15 if v in adj[u] else 22), (u, v, c)
print("srg(217,66,15,22) verified")
# graph6
bits = [1 if idx[V[i]] in adj[idx[V[j]]] else 0 for j in range(1, 217) for i in range(j)]
bits += [0] * (-len(bits) % 6)
g6 = "~" + "".join(chr(63 + ((217 >> s) & 63)) for s in (12, 6, 0)) + "".join(chr(63 + int("".join(map(str, bits[k:k+6])), 2)) for k in range(0, len(bits), 6))
open("construct_srg217.g6", "w").write(g6 + "\n")
try:
    import pynauty
    g = pynauty.Graph(217, adjacency_dict={k: list(v) for k, v in adj.items()})
    print("|Aut| =", pynauty.autgrp(g)[1], " certificate sha256 =", hashlib.sha256(pynauty.certificate(g)).hexdigest())
except ImportError:
    print("pynauty not available here")
