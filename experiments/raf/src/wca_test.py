"""W_CA positive-selection test on RAF substrates. Pre-registered harness.
Run: python3 wca_test.py run   (test seeds >= 1000; do NOT run before deposit)"""
import sys, json, numpy as np, scipy.sparse as sp
from scipy.integrate import solve_ivp
from raf import build, max_raf, produced, closure
from kin import Kinetics

N_LEN, F_CAT = 6, 3.0
PAR = dict(k0=0.0, kc=1e3, phi=0.1, kcl=0.1, food_in=1.0)
T_BURN, W_AVG, T_REC = 1000.0, 200.0, 500.0
EPS = 0.5
TH_SPECIES = 1e-4
RHO_ACT, RHO_CLOSED, R_COMP = 0.01, 0.5, 0.9
PHI_SERIES = [0.10, 0.12, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]
SEED_START, SEED_CAP, N_TEST = 1000, 1000, 5

def setup(seed):
    net = build(n=N_LEN, f=F_CAT, seed=seed)
    net['cat'] = [c - net['F'] for c in net['cat']]      # food non-catalytic
    return net

def integ(K, x0, T, dense=False):
    return solve_ivp(K.rhs, (0, T), x0, method='LSODA', rtol=1e-6, atol=1e-12, dense_output=dense)

def tavg(sol, t0, t1, n=201):
    ts = np.linspace(t0, t1, n); return np.clip(sol.sol(ts), 0, None).mean(axis=1)

def intact(net, par=PAR, cat_override=None):
    Ms = max_raf(net)
    if len(Ms) < 5: return None
    SR = produced(net, Ms); idxR = np.array([m in SR for m in net['X']])
    K = Kinetics(net, **par)
    if cat_override is not None: K.Cm = cat_override
    sol = integ(K, K.x_food_only() + 0.01*idxR, T_BURN, dense=True)
    return K, sol, tavg(sol, T_BURN - W_AVG, T_BURN), np.clip(sol.y[:, -1], 0, None)

def admissible(net):
    r = intact(net)
    if r is None: return False, None
    K, sol, xbar, xend = r
    real = (xbar > TH_SPECIES) & ~K.food
    ts = np.linspace(T_BURN/2, T_BURN, 201); m = np.clip(sol.sol(ts), 0, None)[~K.food].sum(0)
    ok = real.sum() >= 20 and xbar[~K.food].sum()/xbar[K.food].sum() >= 0.1 and m.min() >= 0.5*m.mean()
    return ok, r

def carves(net, K, xbar):
    X, F = net['X'], net['F']
    real = {m for m in X if m not in F and xbar[K.ix[m]] > TH_SPECIES}
    idx = [i for i, r in enumerate(net['R']) if all(y in real|F for y in r[1]) and all(z in real|F for z in r[0])]
    Mr = max_raf(net, idx); S_raf = produced(net, Mr)
    used = set()
    for i in Mr:
        used |= set(net['R'][i][0]); used |= {c for c in net['cat'][i] if c in real}
    C = {'S_RAF': S_raf,
         'S_LEN': {m for m in S_raf if len(m) <= N_LEN - 2},
         'S_LONG': {m for m in S_raf if len(m) >= N_LEN - 1}}
    per = S_raf - used
    if per: C['S_PER'] = per; C['S_CORE'] = S_raf & used
    return C, Mr, idx

def severed_kinetics(net, K, S, par=PAR):
    """Disable material and catalytic input from outside S (food excepted) into reactions producing S species."""
    F = net['F']; nR = len(net['R'])
    mask = np.ones(nR); rows = []; cols = []
    Sidx = {K.ix[m] for m in S}
    for i, (re, pr, kd) in enumerate(net['R']):
        if any(y in S for y in pr):
            if any(z not in S and z not in F for z in re): mask[i] = 0.0
            for c in net['cat'][i]:
                if c not in S: rows.append(i); cols.append(K.ix[c])
    Cm = K.Cm.tolil()
    for i, j in zip(rows, cols): Cm[i, j] = 0.0
    K2 = Kinetics(net, **par); K2.Cm = Cm.tocsr(); K2.rx_mask = mask
    return K2

def verdict(net, K, xbar, xstart, S, par=PAR, eps=EPS, t_rec=T_REC):
    Si = np.array([K.ix[m] for m in sorted(S)])
    x0 = xstart.copy(); x0[Si] *= eps
    K2 = severed_kinetics(net, K, S, par)
    sol = integ(K2, x0, t_rec, dense=True)
    xr = tavg(sol, t_rec - W_AVG, t_rec)
    rho = xr[Si].sum() / xbar[Si].sum()
    a, b = np.log10(xr[Si] + 1e-12), np.log10(xbar[Si] + 1e-12)
    r = float(np.corrcoef(a, b)[0, 1]) if len(Si) > 1 and a.std() > 0 else float('nan')
    tau0 = int(rho >= RHO_ACT)
    kappa = 'subthreshold' if not tau0 else ('closed' if (rho >= RHO_CLOSED and r >= R_COMP) else 'closure-competent')
    return dict(rho=float(rho), r=r, tau0=tau0, kappa=kappa)

def keystone_links(net, Mr, idx, real):
    F = net['F']; C = closure(F, net['R'], Mr)
    links = sorted((i, c) for i in Mr for c in net['cat'][i] if c in C and c in real)
    ks, ctrl = [], []
    for (i, c) in links:
        net['cat'][i].discard(c); m = len(max_raf(net, set(idx))); net['cat'][i].add(c)
        if m == 0: ks.append((i, c))
        elif len(Mr) - m <= 1: ctrl.append((i, c))
    return ks, ctrl

def cat_without(K, link):
    i, c = link; Cm = K.Cm.tolil(); Cm[i, K.ix[c]] = 0.0; return Cm.tocsr()

def run_network(seed, net, r):
    K, sol, xbar, xend = r
    C, Mr, idx = carves(net, K, xbar)
    out = {'seed': seed, 'sizes': {k: len(v) for k, v in C.items()}, 'verdicts': {}}
    for name, S in C.items():
        if S: out['verdicts'][name] = verdict(net, K, xbar, xend, S)
    # T* series on S_RAF (descriptive)
    out['Tstar'] = {}
    for phi in PHI_SERIES:
        p = dict(PAR, phi=phi); rr = intact(net, p)
        Kp, solp, xbp, xep = rr
        if xbp[[Kp.ix[m] for m in C['S_RAF']]].sum() < 1e-6: out['Tstar'][phi] = 'collapsed-intact'; continue
        out['Tstar'][phi] = verdict(net, Kp, xbp, xep, C['S_RAF'], par=p)
    # cut-the-loop
    real = C['S_RAF']; ks, ctrl = keystone_links(net, Mr, idx, real)
    rng = np.random.default_rng(seed)
    for label, pool in [('keystone', ks), ('control', ctrl)]:
        if not pool: out[label] = 'none-available'; continue
        link = pool[0] if label == 'keystone' else pool[rng.integers(len(pool))]
        net['cat'][link[0]].discard(link[1])
        rr = intact(net, PAR)
        net['cat'][link[0]].add(link[1])
        if rr is None: out[label] = {'link': [int(link[0]), link[1]], 'kappa': 'subthreshold', 'note': 'no RAF'}; continue
        Kc, solc, xbc, xec = rr
        Sidx = [Kc.ix[m] for m in real]
        if xbc[Sidx].sum() < 1e-6*xbar[[K.ix[m] for m in real]].sum():
            out[label] = {'link': [int(link[0]), link[1]], 'kappa': 'subthreshold', 'note': 'intact collapse'}; continue
        v = verdict(net, Kc, xbar, xec, real); v['link'] = [int(link[0]), link[1]]; out[label] = v
    # robustness (descriptive)
    out['robust'] = {f'eps={e}': {n: verdict(net, K, xbar, xend, S, eps=e)['kappa'] for n, S in C.items() if S} for e in (0.2, 0.8)}
    return out

def network_pass(o):
    v = o['verdicts']; ok = []
    ok.append(v['S_RAF']['kappa'] == 'closed')
    ok.append(v['S_LEN']['kappa'] == 'subthreshold' if 'S_LEN' in v else True)
    ok.append(v['S_LONG']['kappa'] == 'subthreshold' if 'S_LONG' in v else True)
    if 'S_PER' in v: ok.append(v['S_PER']['kappa'] == 'subthreshold')
    ok.append(isinstance(o['keystone'], dict) and o['keystone']['kappa'] == 'subthreshold')
    ok.append(isinstance(o['control'], dict) and o['control']['tau0'] == 1)
    return all(ok), ok

if __name__ == '__main__' and sys.argv[1:] == ['run']:
    results = []; seed = SEED_START
    while len(results) < N_TEST and seed < SEED_START + SEED_CAP:
        net = setup(seed); ok, r = admissible(net)
        if ok:
            o = run_network(seed, net, r); o['pass'], o['checks'] = network_pass(o); results.append(o)
            print(json.dumps(o, default=str), flush=True)
        seed += 1
    if len(results) < N_TEST: print('VOID: fewer than', N_TEST, 'admissible networks')
    else:
        n = sum(o['pass'] for o in results); print('OVERALL', 'PASS' if n >= 4 else 'FAIL', f'({n}/{N_TEST} networks)')
    json.dump(results, open('results.json', 'w'), default=str, indent=1)
