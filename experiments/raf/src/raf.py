"""Binary polymer model (Kauffman) + RAF detection (Hordijk & Steel).
Reactions: ligation a+b->ab and cleavage ab->a+b, max length n.
Each molecule catalyzes each reaction independently with prob p."""
import numpy as np, itertools, random

def molecules(n):
    return [''.join(s) for L in range(1, n+1) for s in itertools.product('01', repeat=L)]

def reactions(n):
    R = []  # (reactants tuple, products tuple, kind)
    for L in range(2, n+1):
        for s in itertools.product('01', repeat=L):
            ab = ''.join(s)
            for i in range(1, L):
                a, b = ab[:i], ab[i:]
                R.append(((a, b), (ab,), 'lig'))
                R.append(((ab,), (a, b), 'clv'))
    return R

def build(n=8, t=2, f=1.5, seed=0):
    rng = np.random.default_rng(seed)
    X = molecules(n); R = reactions(n)
    F = set(m for m in X if len(m) <= t)
    p = f / len(R)
    # catalysts: for each molecule, number of reactions catalyzed ~ Binomial(|R|, p)
    cat = [set() for _ in R]
    for m in X:
        k = rng.binomial(len(R), p)
        for r in rng.choice(len(R), size=k, replace=False):
            cat[r].add(m)
    return dict(n=n, t=t, f=f, seed=seed, X=X, R=R, F=F, cat=cat)

def closure(F, R, idx):
    C = set(F); changed = True
    idx = list(idx)
    while changed:
        changed = False
        for i in idx:
            re, pr, _ = R[i]
            if all(x in C for x in re) and not all(y in C for y in pr):
                C.update(pr); changed = True
    return C

def max_raf(net, idx=None):
    R, F, cat = net['R'], net['F'], net['cat']
    cur = set(range(len(R))) if idx is None else set(idx)
    while True:
        C = closure(F, R, cur)
        keep = {i for i in cur if all(x in C for x in R[i][0]) and (cat[i] & C)}
        if keep == cur: return cur
        cur = keep

def irr_raf(net, M, rng):
    cur = set(M)
    order = list(cur); rng.shuffle(order)
    for i in order:
        if i not in cur: continue
        trial = max_raf(net, cur - {i})
        if trial: cur = trial
    return frozenset(cur)

def is_raf(net, idx):
    R, F, cat = net['R'], net['F'], net['cat']
    C = closure(F, R, idx)
    return bool(idx) and all(all(x in C for x in R[i][0]) and (cat[i] & C) for i in idx)

def produced(net, idx):
    return set(y for i in idx for y in net['R'][i][1]) - net['F']

def max_raf_strict(net, idx=None, allowed=None):
    """maxRAF where catalysts must be non-food (and in `allowed` species set if given);
    reactions restricted to idx."""
    R, F, cat = net['R'], net['F'], net['cat']
    cur = set(range(len(R))) if idx is None else set(idx)
    while True:
        C = closure(F, R, cur)
        Cc = C - F if allowed is None else (C - F) & allowed
        keep = {i for i in cur if all(x in C for x in R[i][0]) and (cat[i] & Cc)}
        if keep == cur: return cur
        cur = keep
