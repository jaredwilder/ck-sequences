# Exact `C_k(N)` extension tranche — 2026-09-11

Author: Jared Wilder  
Status: exact finite computation; historical novelty unresolved

This tranche extends the independently reproduced `C_k(N)` tables for `k=3,4,5`.

A `(k+1)`-element subset is forbidden when **some ordering** `x_0,...,x_k` of its elements satisfies

`sum_i (-1)^i binom(k,i) x_i = 0`.

The extension engine refuses to emit new exact values until it has first recomputed the complete previously published table for the chosen `k` with solver status `OPTIMAL`. All three replay gates passed with zero discrepancies. Every new row below also returned `OPTIMAL`, and every witness was directly checked against the forbidden-relation hyperedges after optimization.

## New exact values

### `C_3`

| N | exact value | checked witness |
|---:|---:|---|
| 46 | 11 | `{1,3,5,21,23,25,28,38,41,43,45}` |
| 47 | 11 | `{2,6,7,11,16,25,27,36,45,46,47}` |
| 48 | 11 | `{3,5,7,10,20,23,25,27,43,45,47}` |
| 49 | 11 | `{5,7,9,25,27,29,32,42,45,47,49}` |
| 50 | 11 | `{2,6,10,20,24,28,42,46,47,49,50}` |
| 51 | 12 | `{1,4,6,8,11,24,28,41,44,46,48,51}` |
| 52 | 12 | `{1,4,6,8,11,24,28,41,44,46,48,51}` |
| 53 | 12 | `{1,3,6,19,23,26,30,43,46,48,50,53}` |
| 54 | 12 | `{2,5,7,9,12,25,29,36,47,49,52,54}` |
| 55 | 12 | `{3,5,8,10,21,28,32,45,48,50,52,55}` |

Thus the value-11 plateau is exactly `N=45..50` within the computed range, and the next jump is

`C_3(51)=12`.

### `C_4`

| N | exact value | checked witness |
|---:|---:|---|
| 27 | 10 | `{1,2,11,12,16,17,21,22,26,27}` |
| 28 | 10 | `{1,2,7,11,12,16,21,22,26,27}` |
| 29 | 10 | `{1,2,3,4,9,21,26,27,28,29}` |
| 30 | 10 | `{2,4,9,12,14,17,22,24,27,29}` |
| 31 | 11 | `{1,2,6,11,12,17,21,22,26,27,31}` |
| 32 | 12 | `{1,2,6,7,11,12,21,22,26,27,31,32}` |
| 33 | 12 | `{1,3,6,8,11,13,21,23,26,28,31,33}` |
| 34 | 12 | `{1,4,6,9,11,14,21,24,26,29,31,34}` |

This gives consecutive jumps

`C_4(30)=10`, `C_4(31)=11`, `C_4(32)=12`.

### `C_5`

| N | exact value | checked witness |
|---:|---:|---|
| 18 | 7 | `{1,4,8,14,16,17,18}` |
| 19 | 7 | `{1,5,13,16,17,18,19}` |
| 20 | 7 | `{1,7,15,17,18,19,20}` |
| 21 | 7 | `{1,3,7,18,19,20,21}` |
| 22 | 7 | `{2,5,7,11,18,19,21}` |
| 23 | 7 | `{4,11,12,13,17,20,22}` |
| 24 | 7 | `{2,5,7,11,20,21,23}` |

Hence the value-7 plateau, which began at `N=14`, continues through at least `N=24`.

## Reproducibility receipt

GitHub Actions run: `34612101228`  
Source head: `02b25a1042e59aa8e251c2f857e80107931f53c9`

Artifacts:

- `ck-k3-extension`, artifact `10269390223`, ZIP digest `sha256:adf81aff8d335099232188abe223c3dcfd8c3d8622f4f53a284e1fd9cf4c27f1`;
- `ck-k4-extension`, artifact `10269087380`, ZIP digest `sha256:9934d14df49a5af5784793c4112318701efcff43e9f8f503922df05bb0cd9a1e`;
- `ck-k5-extension`, artifact `10268279645`, ZIP digest `sha256:99154f55d22d0b0c445a17ef09d5247e4cf3de95a74d6beefaa1f350572b24d0`.

The executable source is `extend_ck_sequences.py`.

## Literature boundary

Targeted release-day web searches did not surface a published table for this exact extremal function and these new rows. That is not a proof of historical novelty. These values are therefore released as exact, independently reproducible finite mathematics with **historical novelty unresolved**.
