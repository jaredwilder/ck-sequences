# The exact sequences

The rows below are exact finite values. The defining relation uses distinct elements and allows **some ordering** of the selected `(k+1)` elements to realize the vanishing `k`-th finite difference. Historical novelty of individual rows is separate from computational exactness.

## C3

**Definition.** `C3(N)` is the maximum size of `S subset {1,...,N}` containing no four distinct elements admitting an ordering `x1,x2,x3,x4` with

`x1 - 3*x2 + 3*x3 - x4 = 0`.

26 values, `N=30..55`. Optimality is proven on **every one**.

| N | C3 |
|---|---:|
| 30 | **9** |
| 31 | **9** |
| 32 | **9** |
| 33 | **10** |
| 34 | **10** |
| 35 | **10** |
| 36 | **10** |
| 37 | **10** |
| 38 | **10** |
| 39 | **10** |
| 40 | **10** |
| 41 | **10** |
| 42 | **10** |
| 43 | **10** |
| 44 | **10** |
| 45 | **11** |
| 46 | **11** |
| 47 | **11** |
| 48 | **11** |
| 49 | **11** |
| 50 | **11** |
| 51 | **12** |
| 52 | **12** |
| 53 | **12** |
| 54 | **12** |
| 55 | **12** |

Within this range:

- `C3=10` on `N=33..44`, length 12;
- `C3=11` on `N=45..50`, length 6;
- the next jump is **`C3(51)=12`**.

## C4

**Definition.** `C4(N)` is the maximum size of a subset of `{1,...,N}` containing no five distinct elements whose ordering has vanishing fourth finite difference.

34 values, `N=1..34`. Optimality is proven on **every one**.

| N | C4 |
|---|---:|
| 1 | **1** |
| 2 | **2** |
| 3 | **3** |
| 4 | **4** |
| 5 | **4** |
| 6 | **5** |
| 7 | **6** |
| 8 | **6** |
| 9 | **6** |
| 10 | **6** |
| 11 | **6** |
| 12 | **6** |
| 13 | **7** |
| 14 | **8** |
| 15 | **8** |
| 16 | **8** |
| 17 | **8** |
| 18 | **8** |
| 19 | **8** |
| 20 | **8** |
| 21 | **8** |
| 22 | **8** |
| 23 | **8** |
| 24 | **9** |
| 25 | **9** |
| 26 | **9** |
| 27 | **10** |
| 28 | **10** |
| 29 | **10** |
| 30 | **10** |
| 31 | **11** |
| 32 | **12** |
| 33 | **12** |
| 34 | **12** |

Notable exact transitions:

- `C4=8` on `N=14..23`, length 10;
- `C4=10` on `N=27..30`;
- **`C4(31)=11` and `C4(32)=12`**, two consecutive jumps.

## C5

**Definition.** `C5(N)` is the maximum size of a subset of `{1,...,N}` containing no six distinct elements whose ordering has vanishing fifth finite difference.

24 values, `N=1..24`. Optimality is proven on **every one**.

| N | C5 |
|---|---:|
| 1 | **1** |
| 2 | **2** |
| 3 | **3** |
| 4 | **4** |
| 5 | **5** |
| 6 | **5** |
| 7 | **5** |
| 8 | **6** |
| 9 | **6** |
| 10 | **6** |
| 11 | **6** |
| 12 | **6** |
| 13 | **6** |
| 14 | **7** |
| 15 | **7** |
| 16 | **7** |
| 17 | **7** |
| 18 | **7** |
| 19 | **7** |
| 20 | **7** |
| 21 | **7** |
| 22 | **7** |
| 23 | **7** |
| 24 | **7** |

Within the computed range, `C5=7` for **at least eleven consecutive values**, `N=14..24`.

## Extension receipt

The September 11 extension first replayed the complete previously published table for each `k` with zero discrepancies, then solved the new rows to CP-SAT status `OPTIMAL`. Exact witnesses, run IDs and artifact digests are recorded in [`evidence/extension-2026-09-11.md`](evidence/extension-2026-09-11.md).
