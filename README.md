# Open cases of Brouwer's SRG table

https://tonykoval.github.io/srg-open-cases/

A small static website that explains results on parameter sets of strongly regular graphs that were marked open
("?") in A. E. Brouwer's table, settled in September–October 2026, and related uniqueness results:

- **No graph exists**: srg(69,20,7,5), srg(99,42,21,15), srg(105,52,21,30), srg(154,72,26,40), srg(162,69,36,24), srg(196,81,42,27),
  srg(288,105,52,30), srg(405,132,63,33), srg(476,133,60,28) (one paper each).
- **No graph exists, by one uniform condition**: 70 further open complementary pairs with 96 ≤ v ≤ 1288 (the
  Bannai–Munemasa–Venkov lattice method extended to all strongly regular graphs with integral eigenvalues; 28 pairs
  by hand, 42 by enumerations repeated by at least two independent programs), and every parameter set of
  negative-Latin-square type NL_m(q) with q a power of a prime ≡ 1 (mod 4) and m odd.
- **New graphs** for fourteen parameter sets: (250,81,24,27), (300,69,18,15), (320,87,22,24), (320,88,24,24),
  (324,114,36,42), (324,133,52,56), (324,136,58,56), (486,97,16,20), (486,100,22,20), and, in a second paper, (306,55,4,11), (400,171,74,72), (576,253,112,110),
  (784,351,158,156), (1296,595,274,272) (Bush-type Hadamard graphs with two orthogonal spreads deleted, and a
  pseudo-GQ(5,10) on Q(4,5); still "?" in Brouwer's table on 11 October 2026).
- **Uniqueness**: the regular two-graphs on 126 and 176 points are unique (equivalently, 126 equiangular lines in
  R^21 and 176 in R^22 at angle arccos 1/5 are unique; listed as unknown by Brouwer–Van Maldeghem 2022, §8.10.1).
  Hence srg(125,52,15,26), srg(125,72,45,36), srg(175,72,20,36) and srg(175,102,65,51) each have exactly one graph.
  By the same method, the Delsarte graph is the only srg(243,110,37,60) and the M23 graph the only
  srg(253,112,36,60) (no group assumed), so these two sets and their complements also have exactly one graph.

All results are preprints, not yet peer-reviewed. The papers are the authoritative versions; the site states nothing
beyond them.

## Pages

| file | content |
|---|---|
| `index.html` | landing page: all results, methods, how they were checked |
| `srg69.html`, `srg99_42.html`, `srg105.html`, `srg154.html`, `srg162.html`, `srg196.html`, `srg288.html`, `srg405.html`, `srg476.html` | one page per nonexistence proof |
| `bmv.html` | the uniform lattice condition: statement, parity corollary, NL_m(q) family, parity checker, sortable Table 1 of the 70 pairs, controls |
| `twographs.html` | uniqueness of the regular two-graphs on 126 and 176 points: statement, corollary for four srg parameter sets, switching classes, proof steps, case explorer, Leech enumeration, verification |
| `uniq243_253.html` | uniqueness of srg(243,110,37,60) (Delsarte graph) and srg(253,112,36,60) (M23 graph): statement, prior rank-3 results, proof steps, the 16 forms for 253, Leech counts, verification, controls |
| `graphs.html` | the new graphs of both construction papers: counts, automorphism groups, sources, data files, the two-spread construction, the 306-vertex graph |
| `about.html` | method in plain words, verification standard, use of AI, licence, how to cite |
| `assets/site.css` | shared stylesheet (light and dark theme) |
| `data/` | graph6 files of the new graphs, the verifier `verify_srg.py`, `README.txt`, `SHA256SUMS`; `bmv_table1.json` and `bmv_table1.csv` (Table 1 of the 70-pair paper) |
| `tools/bmv_table1.mjs` | regenerates the two Table 1 files from the paper's LaTeX source and embeds the JSON in `bmv.html` (Node 18+, no packages) |

## Viewing locally

The site is plain HTML, CSS and a little vanilla JavaScript, with no build step. Open `index.html` in a browser, or
serve the folder:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/
```

Fonts are loaded from Google Fonts; without a network connection the pages fall back to system fonts.

## Checking the graphs

```bash
cd data
python3 verify_srg.py srg324_136_58_56.g6 324 136 58 56
```

The verifier (plain Python 3, no packages) checks A² = kI + λA + μ(J − I − A) for every line of a file. The files in
`data/` are copies of the ancillary files of the construction paper; `SHA256SUMS` also lists programs and connection
sets of the full archive that are not copied here.

## Papers

| paper | DOI |
|---|---|
| No srg(69,20,7,5) | [10.5281/zenodo.23209705](https://doi.org/10.5281/zenodo.23209705) |
| No srg(99,42,21,15) | [10.5281/zenodo.23210773](https://doi.org/10.5281/zenodo.23210773) |
| No srg(105,52,21,30) | [10.5281/zenodo.23210908](https://doi.org/10.5281/zenodo.23210908) |
| No srg(154,72,26,40) | [10.5281/zenodo.23210954](https://doi.org/10.5281/zenodo.23210954) |
| No srg(162,69,36,24) | [10.5281/zenodo.23211005](https://doi.org/10.5281/zenodo.23211005) |
| No srg(196,81,42,27) | [10.5281/zenodo.23296112](https://doi.org/10.5281/zenodo.23296112) |
| No srg(288,105,52,30) | [10.5281/zenodo.23263506](https://doi.org/10.5281/zenodo.23263506) |
| No srg(405,132,63,33) | [10.5281/zenodo.23263684](https://doi.org/10.5281/zenodo.23263684) |
| No srg(476,133,60,28) | [10.5281/zenodo.23295959](https://doi.org/10.5281/zenodo.23295959) |
| The Bannai–Munemasa–Venkov lattice method for strongly regular graphs: a uniform discriminant-form condition and new nonexistence results | [10.5281/zenodo.23275433](https://doi.org/10.5281/zenodo.23275433) |
| The regular two-graphs on 126 and 176 points are unique | [10.5281/zenodo.23279444](https://doi.org/10.5281/zenodo.23279444) |
| The strongly regular graphs with parameters (243,110,37,60) and (253,112,36,60) are unique | [10.5281/zenodo.23296040](https://doi.org/10.5281/zenodo.23296040) |
| New strongly regular graphs on open parameter sets of Brouwer's table | [10.5281/zenodo.23210829](https://doi.org/10.5281/zenodo.23210829) |
| Strongly regular graphs on 306, 400, 576, 784 and 1296 vertices from multi-orbit coset fusion and Bush-type Hadamard matrices | [10.5281/zenodo.23296158](https://doi.org/10.5281/zenodo.23296158) |

Brouwer's table: <https://aeb.win.tue.nl/graphs/srg/>

## Author and licence

Anton Kovaľ, AI Lead, VÚB banka, Bratislava. The work was done with substantial assistance from AI systems
(Claude, Codex), coordinated and checked by the author; see `about.html`.

Text: CC BY 4.0 (see `LICENSE`). Papers, code and data: CC BY 4.0, as published in their Zenodo records.
