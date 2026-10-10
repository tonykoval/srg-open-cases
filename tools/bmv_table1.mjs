// Build data/bmv_table1.json and data/bmv_table1.csv from Table 1 of the paper
// "The Bannai-Munemasa-Venkov lattice method for strongly regular graphs" (doi:10.5281/zenodo.23275433),
// and embed the JSON in bmv.html between the markers <!--T1:BEGIN--> and <!--T1:END-->.
//
// Usage (Node 18+, no packages), from the repository root:
//   node tools/bmv_table1.mjs PATH/TO/milgram_obstruction.tex [PATH/TO/table_summary.json]
//
// The table is read from the LaTeX source of the published paper (the longtable labelled tab:kills, which the
// paper's own generator out/milgram_paper/make_table.py wrote). Nothing is typed by hand. Checks: 70 pairs, the
// H/C2 split of table_summary.json, eigenvalues and complements recomputed from (v,k,lambda,mu).
import { readFileSync, writeFileSync } from 'node:fs';

const [texPath, sumPath] = process.argv.slice(2);
if (!texPath) { console.error('usage: node tools/bmv_table1.mjs milgram_obstruction.tex [table_summary.json]'); process.exit(2); }
const tex = readFileSync(texPath, 'utf8');
const start = tex.indexOf('\\label{tab:kills}');
const end = tex.indexOf('\\end{longtable}', start);
if (start < 0 || end < 0) throw new Error('table tab:kills not found');
const body = tex.slice(start, end).split('\\endfoot')[1];
const lines = body.split('\n').map(s => s.trim()).filter(Boolean);

function isqrt(n) { let r = Math.floor(Math.sqrt(n)); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++; return r; }
function eig(v, k, l, m) {
  const D = (l - m) ** 2 + 4 * (k - m), r0 = isqrt(D);
  if (r0 * r0 !== D) throw new Error('non-integral eigenvalues ' + [v, k, l, m]);
  const r = (l - m + r0) / 2, s = (l - m - r0) / 2, f = ((v - 1) * (-s) - k) / (r - s);
  return { r, s, f, g: v - 1 - f };
}
const SEC = { 'sec:hand': '§5', 'sec:four': '§5.4' };
function plain(t) {               // the few LaTeX constructs that occur in the reason column
  return t.replace(/\(\\S\\ref\{([^}]+)\}\)/g, (_, l) => '(' + (SEC[l] || '§?') + ')')
    .replace(/\\ph/g, 'ph').replace(/\\in/g, ' ∈ ').replace(/\\\{/g, '{').replace(/\\\}/g, '}')
    .replace(/\\ell/g, 'ℓ').replace(/\^2/g, '²').replace(/\$/g, '').replace(/=/g, ' = ')
    .replace(/\s+/g, ' ').replace(/ ,/g, ',').trim();
}
function reps(cell) {             // "proof $(3,-1,1)_{33}$ [V1,V4,V5]" | "V3 $(3,-1,2)_{33}$" | ""
  if (!cell) return [];
  const m = cell.match(/^(\w+) \$\((-?\d+),(-?\d+),(-?\d+)\)_\{(\d+)\}\$(?: \[([^\]]*)\])?$/);
  if (!m) throw new Error('representation cell not understood: ' + cell);
  return [{ by: m[1], rep: [+m[2], +m[3], +m[4]], d: +m[5], also: m[6] ? m[6].split(',') : [] }];
}
function power(cell) { const m = cell.match(/^\$(-?\d+)\^\{(\d+)\}\$$/); if (!m) throw new Error(cell); return [+m[1], +m[2]]; }

const rows = [];
for (let i = 0; i < lines.length; i++) {
  if (!lines[i].endsWith('\\\\*')) continue;
  const a = lines[i].replace(/\\\\\*$/, '').split('&').map(s => s.trim());
  const b = lines[i + 1].replace(/\\\\ \\midrule$/, '').split('&').map(s => s.trim());
  if (a.length !== 15 || b.length !== 15) throw new Error('bad row near: ' + lines[i]);
  const [v, k, l, m] = a.slice(0, 4).map(Number);
  const [r, f] = power(a[4]), [s, g] = power(a[5]);
  const e = eig(v, k, l, m);
  if (e.r !== r || e.s !== s || e.f !== f || e.g !== g) throw new Error('eigenvalue mismatch ' + [v, k, l, m]);
  const ck = +b[1], cl = +b[2], cm = +b[3];
  if (ck !== v - k - 1 || cl !== v - 2 * k + m - 2 || cm !== v - 2 * k + l) throw new Error('complement mismatch ' + v);
  const [cr, cg] = power(b[4]), [cs, cf] = power(b[5]);
  if (cr !== -1 - s || cs !== -1 - r || cg !== g || cf !== f) throw new Error('complement eigenvalues ' + v);
  const cnt = c => (c === '--' ? null : c.split('/').map(Number));
  rows.push({
    v, k, lambda: l, mu: m, r, f, s, g,
    comp: { k: ck, lambda: cl, mu: cm, r: cr, f: cg, s: cs, g: cf },
    V1: cnt(a[6]), V2: cnt(a[7]), V3: cnt(a[8]), V4: cnt(a[9]), V5: cnt(a[10]),
    P: a[11] === 'yes', grade: a[12],
    reps: reps(a[13]).concat(reps(b[13])),
    reason: plain(a[14]),
  });
}
// NL_m(q) family membership (Corollary 4.2), recomputed from the parameters
for (const R of rows) {
  R.nl = null;
  for (const P of [[R.v, R.k, R.lambda, R.mu], [R.v, R.comp.k, R.comp.lambda, R.comp.mu]]) {
    const q = isqrt(P[0]); if (q * q !== P[0] || P[1] % (q + 1)) continue;
    const mm = P[1] / (q + 1);
    if (P[2] === -q + mm * mm + 3 * mm && P[3] === mm * (mm + 1)) { R.nl = R.nl || []; R.nl.push([mm, q]); }
  }
}
const nH = rows.filter(r => r.grade === 'H').length, nC2 = rows.filter(r => r.grade === 'C2').length;
if (rows.length !== 70 || nH + nC2 !== 70) throw new Error(`counts ${rows.length} H=${nH} C2=${nC2}`);
if (sumPath) {
  const S = JSON.parse(readFileSync(sumPath, 'utf8'));
  if (S.n !== rows.length || S.nH !== nH || S.nC2 !== nC2) throw new Error('disagrees with table_summary.json');
  const c2 = S.C2.match(/\((\d+),(\d+),(\d+),(\d+)\)/g).map(t => t.slice(1, -1));
  const mine = rows.filter(r => r.grade === 'C2').map(r => [r.v, r.k, r.lambda, r.mu].join(','));
  if (c2.join(';') !== mine.join(';')) throw new Error('C2 list differs from table_summary.json');
}

const out = {
  source: 'Table 1 of A. Kovaľ, The Bannai–Munemasa–Venkov lattice method for strongly regular graphs: a uniform discriminant-form condition and new nonexistence results, preprint, 10 October 2026, doi:10.5281/zenodo.23275433',
  generated_by: 'tools/bmv_table1.mjs from the LaTeX source of the paper',
  notes: 'One record per open complementary pair; (v,k,lambda,mu) has 2k < v, comp is the complement. Eigenvalues r^f, s^g. V1..V5: [representations without admissible module, representations decided], null = not run; V2 is a cross-check only. P: Corollary 4.1 fails. grade: H = hand proof in the paper, C2 = excluded by at least two of the independent programs V1, V3, V4, V5. reps: (rho,b,c) means G = b(A - rho I) + cJ on the first orientation, of rank d. nl: [m,q] if a side has the parameters of NL_m(q).',
  pairs: rows,
};
writeFileSync('data/bmv_table1.json', JSON.stringify(out, null, 1) + '\n');
const q = x => (/[",]/.test(x) ? '"' + x.replace(/"/g, '""') + '"' : x);
const csv = ['v,k,lambda,mu,r,f,s,g,comp_k,comp_lambda,comp_mu,V1,V2,V3,V4,V5,P,grade,representations,reason,NL'];
for (const R of rows) {
  const c = x => (x ? x.join('/') : '');
  csv.push([R.v, R.k, R.lambda, R.mu, R.r, R.f, R.s, R.g, R.comp.k, R.comp.lambda, R.comp.mu, c(R.V1), c(R.V2), c(R.V3), c(R.V4), c(R.V5),
    R.P ? 'yes' : '', R.grade,
    q(R.reps.map(x => `${x.by} (${x.rep.join(',')})_${x.d}${x.also.length ? ' [' + x.also.join(',') + ']' : ''}`).join('; ')),
    q(R.reason), q((R.nl || []).map(([m, qq]) => `NL_${m}(${qq})`).join('; '))].join(','));
}
writeFileSync('data/bmv_table1.csv', csv.join('\n') + '\n');
const html = readFileSync('bmv.html', 'utf8');
const A = '<!--T1:BEGIN-->', B = '<!--T1:END-->', ia = html.indexOf(A), ib = html.indexOf(B);
if (ia < 0 || ib < 0) throw new Error('markers not found in bmv.html');
const json = JSON.stringify(rows).replace(/</g, '\\u003c');
writeFileSync('bmv.html', html.slice(0, ia + A.length) + '\n<script id="t1data" type="application/json">' + json + '</script>\n' + html.slice(ib));
console.log(`pairs ${rows.length}  H ${nH}  C2 ${nC2}  parity ${rows.filter(r => r.P).length}  NL ${rows.filter(r => r.nl).length}`);
