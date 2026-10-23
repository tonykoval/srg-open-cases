SRG(85,42,20,21): Verma descendants

This data package contains the 86 descendants of Harshit Verma's symmetric
conference matrix of order 86, described in “A symmetric conference matrix of
order 86”, arXiv:2610.08893v1 (2026). The construction is Verma's. The
independent verification, graph6 extraction, class mapping, and packaging were
performed separately for this data release. This package does not include or
relicense the paper, its source, or its PDF.

Files
-----
descendants_all86.g6
    All 86 descendants in the original root order, one graph6 record per line.
    This file is copied without sorting or canonical relabelling.
representatives10.g6
    One representative from each of the ten isomorphism classes, in root order
    0, 1, 2, 9, 16, 23, 30, 37, 44, 65.
verma86_srg85_42_20_21_rootNN.g6
    Individual graph6 files for those ten representatives.
roots.csv
    Mapping from each line in descendants_all86.g6 to its root and class
    representative. CSV labels (i,a) are quoted because they contain commas.
SHA256SUMS
    SHA-256 checksums for every other file in this directory.

Root and vertex indexing
------------------------
Line r+1 of descendants_all86.g6 is the descendant at root index r, for
r=0,...,85. Root 0 is ∞ and root 1 is ∞'. The remaining roots are labelled
(i,a), where r=2+7i+a, 0<=i<12 and 0<=a<7.

In each graph the vertices are the original indices 0,...,85 with the root
omitted, kept in increasing order and then numbered 0,...,84. The graph6
records retain this vertex order. No content-based sorting or canonical
relabeling was applied when preparing these files.

Counts and scope
----------------
The 86 descendants form ten isomorphism classes of sizes
1, 1, 7, 7, 7, 7, 7, 7, 21, 21. Thus “86 graphs” means 86 derived records, not
86 nonisomorphic graphs. This package does not contain the ten complementary
classes also mentioned in the paper, and it is not a classification of all
graphs with parameters (85,42,20,21).

Verification
------------
From the root of the srg-open-cases repository, using the existing dependency-
free verifier:

    python3 data/verify_srg.py data/verma85/descendants_all86.g6 85 42 20 21
    python3 data/verify_srg.py data/verma85/representatives10.g6 85 42 20 21

The cited preprint documents the construction and class count. The graph files
were checked against the independent verification record used to prepare this
package. See SHA256SUMS to verify the released bytes.