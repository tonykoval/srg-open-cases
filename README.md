# Open cases of Brouwer's SRG table

https://tonykoval.github.io/srg-open-cases/

A small static website that explains results on parameter sets of strongly regular graphs that were marked open
("?") in A. E. Brouwer's table, settled in September–October 2026:

- **No graph exists**: srg(69,20,7,5), srg(99,42,21,15), srg(105,52,21,30), srg(154,72,26,40), srg(162,69,36,24),
  srg(288,105,52,30), srg(405,132,63,33).
- **New graphs** for nine parameter sets: (250,81,24,27), (300,69,18,15), (320,87,22,24), (320,88,24,24),
  (324,114,36,42), (324,133,52,56), (324,136,58,56), (486,97,16,20), (486,100,22,20).

All results are preprints, not yet peer-reviewed. The papers are the authoritative versions; the site states nothing
beyond them.

## Pages

| file | content |
|---|---|
| `index.html` | landing page: all sixteen results, methods, how they were checked |
| `srg69.html`, `srg99_42.html`, `srg105.html`, `srg154.html`, `srg162.html`, `srg288.html`, `srg405.html` | one page per nonexistence proof |
| `graphs.html` | the new graphs: counts, automorphism groups, sources, data files |
| `about.html` | method in plain words, verification standard, use of AI, licence, how to cite |
| `assets/site.css` | shared stylesheet (light and dark theme) |
| `data/` | graph6 files of the new graphs, the verifier `verify_srg.py`, `README.txt`, `SHA256SUMS` |

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
| No srg(288,105,52,30) | [10.5281/zenodo.23263506](https://doi.org/10.5281/zenodo.23263506) |
| No srg(405,132,63,33) | [10.5281/zenodo.23263684](https://doi.org/10.5281/zenodo.23263684) |
| New strongly regular graphs on open parameter sets of Brouwer's table | [10.5281/zenodo.23210829](https://doi.org/10.5281/zenodo.23210829) |

Brouwer's table: <https://aeb.win.tue.nl/graphs/srg/>

## Author and licence

Anton Kovaľ, AI Lead, VÚB banka, Bratislava. The work was done with substantial assistance from AI systems
(Claude, Codex), coordinated and checked by the author; see `about.html`.

Text: CC BY 4.0 (see `LICENSE`). Papers, code and data: CC BY 4.0, as published in their Zenodo records.
