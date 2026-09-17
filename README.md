# Exact `C_k(N)` sequences for `k=3,4,5`

Let `C_k(N)` be the maximum size of a subset of `{1,...,N}` containing no `k+1` distinct elements that can be assigned to the coefficients

\[
(-1)^i\binom ki
\]

with total zero.

Every value in this repository was obtained with solver status `OPTIMAL` and an independently checked witness.

## Exact ranges

| relation | exact range | selected boundary values |
|---|---|---|
| `C_3` | `N=30..55` | `C_3(50)=11`, `C_3(51)=12` |
| `C_4` | `N=1..34` | `C_4(31)=11`, `C_4(32)=12` |
| `C_5` | `N=1..24` | `C_5(N)=7` for `14<=N<=24` |

The complete tables are in [`SEQUENCES.md`](SEQUENCES.md).

The current data contain **84 exact values**.

## Finite structure visible in the tables

For `C_3`:

```text
C_3(N)=10  for 33<=N<=44
C_3(N)=11  for 45<=N<=50
C_3(51)=12
```

For `C_4`, the table includes consecutive jumps

```text
10 -> 11 -> 12
```

at `N=30,31,32`.

For `C_5`, the value 7 persists throughout the current range `14<=N<=24`.

These are exact finite statements; the table by itself does not assert an asymptotic law.

## Semantics

The ordering convention matters. The chosen elements may be assigned arbitrarily to the alternating-binomial coefficients; the relation is not tested only on the increasing ordering of the set.

For example, `C_3` forbids distinct values satisfying

\[
x_1-3x_2+3x_3-x_4=0
\]

under some injective assignment to the four coefficient positions.

The semantic distinction is documented more broadly in [`relation-family-atlas`](https://github.com/jaredwilder/relation-family-atlas).

## Computation

The optimizer uses Google OR-Tools CP-SAT. A value is published as exact only when the solver returns `OPTIMAL`.

Before extending a table, the reproducibility script:

1. recomputes all previously published values in that `k`-series;
2. aborts on any mismatch or non-optimal status;
3. solves the new `N` values;
4. verifies every returned witness directly against the generated forbidden-relation hyperedges.

All replay checks for the published extensions passed.

## Related formal work

A larger `C_3` proof/minimum-span package, including LRAT-backed formal material, is preserved in [`additive-combinatorics-campaigns`](https://github.com/jaredwilder/additive-combinatorics-campaigns).

## Files

- [`SEQUENCES.md`](SEQUENCES.md) — complete exact tables;
- `evidence/` — witnesses, solver receipts, and replay records.

Author: Jared Wilder. License: Apache-2.0.
