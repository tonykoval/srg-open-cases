Ancillary files for: New strongly regular graphs on open parameter sets of Brouwer's table
Author: Anton Kovaľ (AI Lead, VÚB banka, Bratislava, Slovakia; akoval@pobox.sk)
DRAFT (6 October 2026; srg(324,114,36,42) lines 15-22 added 7 October 2026): merged from the ancillary files of three earlier drafts; not submitted.

Graph files (graph6 format, one graph per line, each line ending in a single LF;
line numbers = graph numbers used in the paper; see its Data availability section):

file                       parameters           graphs  SHA-256
srg250_81_24_27.g6         (250,81,24,27)            1  b9a1ab109443afc039170c1c225a9277eb70d130ddce888c7806ce5148cac9a7
srg300_69_18_15.g6         (300,69,18,15)            2  2f345c3f5632b0d4dd56a64edadce70a0ebf8956d24891c0fb48ab1474dcbc9b
srg320_87_22_24.g6         (320,87,22,24)           35  1afbb0435db3f25461461e7fbd60bf78b3ca75eb687c024788a2d70ff47febc9
srg320_88_24_24.g6         (320,88,24,24)           95  6f907d49ff3f4e154394d4eefc6c0dab686e6271cf0515332ec9b306ab680549
srg486_100_22_20.g6        (486,100,22,20)           2  74e21b4648c2274147db40d0eabe6a2d1d1453131e4d62ef286c26af05ca780d
srg486_97_16_20.g6         (486,97,16,20)            2  5b63dd24455c0f22041961b8265279ccac450c0c582a0b7be6b46037069cb592
srg324_136_58_56.g6        (324,136,58,56)          93  da1f703379880c364ab3f956245efe08004b523bc9187dcf9afa008518507568
srg324_114_36_42.g6        (324,114,36,42)          22  a7c88ab25275efee026ae05d86c1db60256563069445430c824f888a1f0cf781
srg324_133_52_56.g6        (324,133,52,56)          10  954fde68fe7bde4f41ddbbc690558eea6e8b5898bfd81d25a850d0125fbf3d5f
sumgraph_D0_88.g6          (320,88,24,24)            1  99fb2750c3a5ecbb90eb62ec9fda0105631dcd8439f4488bbdd8dbbc05609bff
sumgraph_D0_87.g6          (320,87,22,24)            1  1517e007bcc17b3c0362a2c2b697c2929508a6adf4943dddc0570243bf2fca05

srg300_69_18_15.g6: line 1 = Gamma_A, line 2 = Gamma_B (formerly two one-line files).
The 250/300 files use the vertex order of the builders; the sumgraph files (abelian sum graphs,
not vertex-transitive) are not canonical; all other files are in nauty canonical form
(nauty-labelg 2.8.9, dense). Lines appended after the first versions (earlier line numbers kept):
  srg320_87_22_24.g6 18-35, srg320_88_24_24.g6 72-75 and 76-95, srg486_97_16_20.g6 2,
  srg324_136_58_56.g6 28, 29-41, 42-67 and 68-93 (68-93 added 6 October 2026),
  srg324_114_36_42.g6 7-14 (added 6 October 2026) and 15-22 (added 7 October 2026).

Verifier: verify_srg.py (plain Python 3, no packages). It decodes each graph6 line and
checks A^2 = kI + lambda*A + mu*(J-I-A), i.e. every vertex has degree k and every pair of
distinct vertices has lambda (adjacent) or mu (non-adjacent) common neighbours. Usage:

    python3 verify_srg.py FILE v k lambda mu

    python3 verify_srg.py srg250_81_24_27.g6 250 81 24 27
    python3 verify_srg.py srg300_69_18_15.g6 300 69 18 15
    python3 verify_srg.py srg320_87_22_24.g6 320 87 22 24
    python3 verify_srg.py srg320_88_24_24.g6 320 88 24 24
    python3 verify_srg.py srg486_100_22_20.g6 486 100 22 20
    python3 verify_srg.py srg486_97_16_20.g6 486 97 16 20
    python3 verify_srg.py srg324_136_58_56.g6 324 136 58 56
    python3 verify_srg.py srg324_114_36_42.g6 324 114 36 42
    python3 verify_srg.py srg324_133_52_56.g6 324 133 52 56
    python3 verify_srg.py sumgraph_D0_88.g6 320 88 24 24
    python3 verify_srg.py sumgraph_D0_87.g6 320 87 22 24

Programs and data, under their repository paths:
  scripts/new_srgs/          mini_check.py (Appendix A), build_srg250.py, build_srg300.py
                             (output byte-identical to the 250/300 graph6 lines)
  scripts/paper2/            builders for 320 and 486 vertices (Python and GAP), data_*.g,
                             fusion_dfs.c, fusion_run.py, the programs for Theta
  scripts/hits_novelty_324/verify_cyclo.py   check of the cyclotomic srg(324,136,58,56)
  out/hits_novelty_batch2/, out/paper2/, out/novelty_shortcut/   connection sets (320, 486, D0)
  out/l13/srg324_extra.tsv, out/paper324/cyclo_rerun.log,
  out/hits_novelty_324/abelian_pds.log, out/hits_novelty_324/pds_324_163.txt
                             connection sets for srg(324,136,58,56)
  out/hits_novelty_324_114/pds_sol1..6.txt   connection sets of srg(324,114,36,42) lines 1-6
  out/hits_novelty_324_nl/r7_pds_sol1..3.txt connection sets of srg(324,133,52,56) lines 1-3
                             (plain coordinate vectors a0 a1 | y0 y1 y2 y3 in Z_2^2 x Z_3^4;
                             the order of these solution files need not match the line order)
  out/hits_s_2026_10_06/{sA,s2,s3}/HITS/*.src  server provenance of the graphs added 6 October 2026
  out/hits_s_2026_10_07/s1/HITS/*.src         server provenance of the graphs added 7 October 2026
The GAP programs and the Theta programs were run in the author's container with the repository
at /work and read or write files under /work and /scratch; paths in them may need adjusting.
SHA256SUMS lists the SHA-256 of every ancillary file except README.txt and itself.
