# ck-sequences

**Exact values of C_k(N) for k = 3, 4, 5: the largest subset of {1..N} containing no tuple with a
vanishing k-th finite difference. Every value has proven optimality.**

Author: Jared Wilder. First public timestamp: 2026-09-11.

`C_k(N)` is the maximum size of a subset `S` of `{1, ..., N}` containing no tuple satisfying the
alternating binomial relation with vanishing k-th difference. For k = 3 that relation is

```
x1 - 3*x2 + 3*x3 - x4 = 0
```

with the general coefficients `c_i = (-1)^i * binom(k, i)`.

---

## The values

| k | range | values | optimality proven |
|---|---|---|---|
| **C3** | N = 30..45 | 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11 | **16 of 16** |
| **C4** | N = 1..26 | 1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9 | **26 of 26** |
| **C5** | N = 1..17 | 1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7 | **17 of 17** |

Per-value tables, plateau ranges and first-jump points are in `SEQUENCES.md`. The raw solver
evidence, including every witness, is in `evidence/`.

## The plateaus

These sequences are mostly flat, and the flat stretches are long:

- **C3 sits at 10 for twelve consecutive N** (33 through 44), then jumps to 11 at N = 45.
- **C4 sits at 8 for ten consecutive N** (14 through 23).
- **C5 sits at 6 for six consecutive N** (8 through 13).

## How these were computed, and what would have caught an error

Google OR-Tools CP-SAT exact maximisation. **Only `status: OPTIMAL` was accepted** -- a feasible
solution that the solver could not prove optimal was not recorded as a value.

Three controls, all of which had to pass before any value above counts:

1. **Every witness was re-verified directly from the defining relation, not from the solver model.**
   A solver that returned a wrong optimum with a valid-looking model would be caught here.
2. **Negative control against known sequences.** The same engine reproduces OEIS **A003002**
   (`r_3`) with **52 proven values and zero mismatches**, and **A143824** (Sidon) with **39**. An
   engine that could not reproduce a published sequence is not trusted on an unpublished one.
3. **A vacuity guard rejects relations that forbid nothing.** Without it, a mis-specified relation
   would return `C_k(N) = N` and look like a clean result.

C3 was additionally **computed twice, once inside the search loop and once from scratch in a
separate process with no model in the path. Identical values both times.**

## Scope

**The novelty of these specific values has not been adjudicated against the literature.** If they
are known, this is a reproduction carrying receipts. The plateau lengths are measured facts about the
computed range, not proved properties of the sequences.

## License

Apache-2.0.
