# Exact `C_k(N)` sequences for `k=3,4,5`

**Exact optimal values of `C_k(N)` for `k=3,4,5`**, where `C_k(N)` is the largest subset of `{1,…,N}` containing no `(k+1)` distinct elements that admit an ordering with vanishing `k`-th finite difference. Every listed value has solver status **OPTIMAL** and an explicitly checked witness.

Author: Jared Wilder. First public timestamp: 2026-09-11.

For `k=3`, the forbidden relation is

```text
x1 - 3*x2 + 3*x3 - x4 = 0
```

with general coefficients `c_i = (-1)^i binom(k,i)`. The ordering clause is load-bearing: the finite relation is tested over coefficient assignments to the chosen distinct elements, not only their increasing order.

## Exact values

| k | exact range | newly extended through | optimality proven |
|---|---|---|---|
| **C3** | `N=30..55` | `C3(51)=12`, values exact through 55 | **26 of 26** |
| **C4** | `N=1..34` | `C4(31)=11`, `C4(32)=12` | **34 of 34** |
| **C5** | `N=1..24` | value 7 persists through 24 | **24 of 24** |

The complete per-value tables are in [`SEQUENCES.md`](SEQUENCES.md). The release-day extension receipts, witnesses, workflow run and artifact SHA-256 digests are in [`evidence/extension-2026-09-11.md`](evidence/extension-2026-09-11.md).

## Newly established finite structure

The September 11 extension adds **25 new exact values** beyond the original 59-row release:

- `C3(46..50)=11` and `C3(51..55)=12`;
- `C4(27..30)=10`, `C4(31)=11`, and `C4(32..34)=12`;
- `C5(18..24)=7`.

So the current exact tables contain **84 values** in total.

Notable observed plateaus/jumps:

- `C3=10` for `N=33..44`, then `C3=11` for `N=45..50`, with the next jump at **`N=51`**;
- `C4=8` for `N=14..23`, followed later by consecutive jumps **10 → 11 → 12** at `N=30,31,32`;
- `C5=7` for at least `N=14..24`, an 11-value plateau in the current exact range.

These are exact finite statements, not asymptotic claims.

## Related C3 proof and minimum-span package

The substantial [C3 campaign source](https://github.com/jaredwilder/additive-combinatorics-campaigns/tree/b8d712e9bdc05388ac841fd52791ea61f4ed0289/apex-c3-campaign)
was previously discoverable only inside the mixed additive-combinatorics
archive. It contains 821 files, including formal proof material, minimum-span
work, search runs and explicitly labeled research targets.

Start with the [mathematical overview](https://github.com/jaredwilder/additive-combinatorics-campaigns#c3-free-sets),
then the [Lean closure report](https://github.com/jaredwilder/additive-combinatorics-campaigns/blob/b8d712e9bdc05388ac841fd52791ea61f4ed0289/apex-c3-campaign/runs/APX-031/LEAN-CLOSURE.md)
and its [chunked LRAT proof](https://github.com/jaredwilder/additive-combinatorics-campaigns/tree/b8d712e9bdc05388ac841fd52791ea61f4ed0289/apex-c3-campaign/runs/APX-031/chunked-lrat).
The source files remain in that archive; these direct links connect them to
their mathematical subject home. This routing adds no values to the 84-row
table above and makes no new proof-replay claim.

## Computation and verification

The optimization uses Google OR-Tools CP-SAT. A value is included only when the solver returns **`OPTIMAL`**; feasible-but-unproved solutions are not reported as exact values.

The extension engine adds a fail-closed reproducibility gate:

1. before extending a chosen `k`, it recomputes **every previously published value** for that `k`;
2. any mismatch or non-`OPTIMAL` replay aborts the extension;
3. only after the full replay passes are new `N` values solved;
4. every returned witness is checked directly against the generated forbidden-relation hyperedges independently of the CP-SAT model objective.

All three replay gates passed with zero discrepancies in Actions run `34612101228`.

The original release also benchmarked the machinery against OEIS **A003002** (`r_3`) and **A143824** (Sidon) and included a relation-vacuity negative control.

## Literature status

The exact values are computationally established for the stated ranges. Targeted release-day searches did not surface a prior table for this exact extremal function and these extension rows, but absence from a targeted search is not proof of priority. **Historical novelty remains unresolved.**

## License

Apache-2.0.
