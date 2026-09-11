#!/usr/bin/env python3
"""Exact extension engine for C_k(N), k=3,4,5.

A (k+1)-subset E of [N] is forbidden iff some ordering x_0,...,x_k
of E satisfies

    sum_i (-1)^i binom(k,i) x_i = 0.

C_k(N) is the maximum size of a subset of [N] containing no forbidden E.

The script first replays the published exact table for the chosen k.  It
refuses to emit extension claims if any historical value fails to reproduce.
Only CP-SAT status OPTIMAL is accepted as an exact value.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import time
from pathlib import Path

from ortools.sat.python import cp_model

PUBLISHED = {
    3: {n: v for n, v in zip(range(30, 46), [9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,11])},
    4: {n: v for n, v in zip(range(1, 27), [1,2,3,4,4,5,6,6,6,6,6,6,7,8,8,8,8,8,8,8,8,8,8,9,9,9])},
    5: {n: v for n, v in zip(range(1, 18), [1,2,3,4,5,5,5,6,6,6,6,6,6,7,7,7,7])},
}


def coefficient_assignments(k: int):
    coeff = [(-1) ** i * math.comb(k, i) for i in range(k + 1)]
    # Global sign does not change the equation.  Deduplicate repeated
    # coefficients and p <-> -p pairs to reduce the finite check.
    out = set()
    for p in set(itertools.permutations(coeff)):
        neg = tuple(-x for x in p)
        out.add(min(tuple(p), neg))
    return tuple(sorted(out))


def forbidden_edges(k: int, n: int):
    assignments = coefficient_assignments(k)
    edges = []
    for comb in itertools.combinations(range(1, n + 1), k + 1):
        if any(sum(c * x for c, x in zip(a, comb)) == 0 for a in assignments):
            edges.append(comb)
    return edges


def verify_witness(k: int, witness, edges):
    s = set(witness)
    bad = [e for e in edges if set(e) <= s]
    if bad:
        raise AssertionError(f"witness contains forbidden edge {bad[0]}")


def solve_one(k: int, n: int, seconds: float):
    t0 = time.time()
    edges = forbidden_edges(k, n)
    t_edges = time.time() - t0

    model = cp_model.CpModel()
    x = [model.new_bool_var(f"x_{i}") for i in range(1, n + 1)]
    for e in edges:
        model.add(sum(x[i - 1] for i in e) <= k)
    model.maximize(sum(x))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = max(1, min(8, os.cpu_count() or 1))
    solver.parameters.random_seed = 1
    status = solver.solve(model)
    status_name = solver.status_name(status)

    witness = [i + 1 for i, var in enumerate(x) if solver.boolean_value(var)] if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) else []
    value = len(witness) if witness else None
    if witness:
        verify_witness(k, witness, edges)

    payload = {
        "k": k,
        "N": n,
        "status": status_name,
        "exact": status == cp_model.OPTIMAL,
        "value": value,
        "witness": witness,
        "forbidden_edges": len(edges),
        "coefficient_assignments": len(coefficient_assignments(k)),
        "edge_generation_seconds": round(t_edges, 6),
        "solver_wall_seconds": round(solver.wall_time, 6),
        "best_objective_bound": solver.best_objective_bound,
    }
    return payload


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, choices=(3,4,5), required=True)
    ap.add_argument("--extend-through", type=int, required=True)
    ap.add_argument("--seconds-per-N", type=float, default=180.0)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    known = PUBLISHED[args.k]
    receipts = []

    print(f"REPLAY_GATE k={args.k} values={len(known)}")
    for n, expected in known.items():
        r = solve_one(args.k, n, args.seconds_per_N)
        receipts.append({"phase": "replay", "expected": expected, **r})
        print("REPLAY", json.dumps(receipts[-1], sort_keys=True))
        if not r["exact"] or r["value"] != expected:
            raise SystemExit(f"FAIL-CLOSED: replay mismatch at k={args.k}, N={n}: expected {expected}, got {r}")

    start = max(known) + 1
    print(f"REPLAY_PASS k={args.k}; EXTEND {start}..{args.extend_through}")
    for n in range(start, args.extend_through + 1):
        r = solve_one(args.k, n, args.seconds_per_N)
        receipts.append({"phase": "extension", **r})
        print("EXTEND", json.dumps(receipts[-1], sort_keys=True))
        # Unknown/feasible values are retained as computation records, never exact claims.

    output = {
        "definition": "maximum subset of [N] containing no (k+1)-subset admitting an ordering with vanishing k-th finite difference",
        "replay_passed": True,
        "k": args.k,
        "published_values_replayed": len(known),
        "extension_start": start,
        "extension_end": args.extend_through,
        "results": receipts,
    }
    raw = json.dumps(output, indent=2, sort_keys=True) + "\n"
    output["receipt_sha256_without_digest_field"] = hashlib.sha256(raw.encode()).hexdigest()
    raw = json.dumps(output, indent=2, sort_keys=True) + "\n"
    out = Path(args.out or f"ck_k{args.k}_extension.json")
    out.write_text(raw)
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
