# Exact `C_k(N)` sequences for `k=3,4,5`

**Exact optimal values of `C_k(N)` for `k=3,4,5`**, where `C_k(N)` is the largest subset of `{1,…,N}` containing no tuple with vanishing `k`-th finite difference. Every value listed below comes with a solver proof of optimality and a directly checked witness.

Author: Jared Wilder. First public timestamp: 2026-09-11.

For `k=3`, the forbidden relation is

```text
x1 - 3*x2 + 3*x3 - x4 = 0
```

with general coefficients `c_i = (-1)^i binom(k,i)`.

## Exact values

| k | range | values | optimality proven |
|---|---|---|---|
| **C3** | `N=30..45` | 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11 | **16 of 16** |
| **C4** | `N=1..26` | 1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9 | **26 of 26** |
| **C5** | `N=1..17` | 1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7 | **17 of 17** |

Per-value tables, plateau ranges and first-jump points are in `SEQUENCES.md`. Every witness and the raw optimization evidence are in `evidence/`.

## Plateaus

- **C3 = 10 for twelve consecutive values of `N`**, from 33 through 44, then jumps to 11 at 45.
- **C4 = 8 for ten consecutive values of `N`**, from 14 through 23.
- **C5 = 6 for six consecutive values of `N`**, from 8 through 13.

## Computation and verification

The optimization uses Google OR-Tools CP-SAT. A value is included only when the solver returns **`OPTIMAL`**; feasible-but-unproved solutions are not reported as exact sequence values.

Three independent checks accompany the optimization:

1. **Direct witness verification.** Every returned subset is checked against the defining finite-difference relation independently of the solver model.
2. **Published-sequence benchmarks.** The same code reproduces OEIS **A003002** (`r_3`) for 52 exact values and **A143824** (Sidon) for 39 values, with zero mismatches.
3. **Relation sanity check.** The program rejects a specification whose forbidden relation is vacuous, preventing a malformed relation from silently producing `C_k(N)=N`.

The entire C3 range was also recomputed from scratch in a separate process and reproduced the same values.

## Literature status

The exact values above are computationally established for the stated ranges. Historical novelty of the individual entries has not yet been comprehensively adjudicated against the literature; if some values are known, this repository provides an independently reproducible computation of them.

The observed plateau lengths are facts about these finite ranges, not asymptotic theorems about the full sequences.

## License

Apache-2.0.