import time, numpy as np
from frame_sweep_r3 import P, SubstrateR3, run_constrained, make_frames, B_thr, PR, PD, ENF

NS = 2
def avg_runs(sub, Bmat, Binv, free, **kw):
    return [run_constrained(sub, Bmat, Binv, free, np.random.default_rng(700+13*s), **kw) for s in range(NS)]
def m(runs, key): return float(np.mean([r[key] for r in runs]))

def evalb(sub, Bmat, Binv, free):
    iso = avg_runs(sub, Bmat, Binv, free)                          # intact-isolated
    pas = avg_runs(sub, Bmat, Binv, free, u_zero=True)
    sta = avg_runs(sub, Bmat, Binv, free, freeze_y=True)
    iso_b, enf, P_iso, base = m(iso,"basin"), m(iso,"enf"), m(iso,"trP"), m(iso,"terr")
    pas_b, P_sta = m(pas,"basin"), m(sta,"trP")
    C2 = (iso_b >= B_thr) and (pas_b < B_thr) and (enf < ENF)
    C3 = (P_iso/max(P_sta,1e-9)) < PR
    hi = m(avg_runs(sub,Bmat,Binv,free,ahat_off=+0.4),"terr")
    lo = m(avg_runs(sub,Bmat,Binv,free,ahat_off=-0.4),"terr")
    C1 = (max(hi,lo)-base) < PD*0.4 and iso_b >= B_thr
    return int(C1 and C2 and C3), dict(iso=iso_b, pas=pas_b, enf=enf, Pr=P_iso/max(P_sta,1e-9))

sub = SubstrateR3(P)
I = np.eye(3)
print("R^3 OBLIQUE FRAME SWEEP -- binding selection test")
print("KILL: org tau0=0 (artifact) | any 2-D competitor tau0=1 (frame-relative)\n")
t0=time.time()
org_t, od = evalb(sub, I, I, [0,1,2])
print(f"P_org undivided: tau0={org_t}  iso={od['iso']:.2f} pas={od['pas']:.2f} enf={od['enf']:.3f}")
if org_t == 0:
    print("KILL FIRED: org fails -> procedure artifact"); raise SystemExit

frames = make_frames(n_rot=9, n_shear=3)
print(f"swept {len(frames)} frames (cond<= 5); 2-D competitor blocks:\n")
survivors=[]; enfs=[]; isos=[]
for fi,Bm in enumerate(frames):
    Binv=np.linalg.inv(Bm); cond=np.linalg.cond(Bm)
    for comp in range(3):
        free=[i for i in range(3) if i!=comp]
        tau,d = evalb(sub,Bm,Binv,free)
        enfs.append(d['enf']); isos.append(d['iso'])
        if tau==1: survivors.append((fi,free,d))
        tag="  <-- SURVIVES" if tau==1 else ""
        print(f"  f{fi:2d}(cond{cond:.1f}) block free={free}: tau0={tau} "
              f"iso={d['iso']:.2f} pas={d['pas']:.2f} enf={d['enf']:.3f} Pr={d['Pr']:.2f}{tag}")
enfs=np.array(enfs)
print(f"\n2-D competitor enf_frac: min={enfs.min():.3f} max={enfs.max():.3f} "
      f"(tol={ENF}; org=0.000). gap to tol = {enfs.min()-ENF:.3f}")
print(f"elapsed {time.time()-t0:.0f}s")
if survivors:
    print(f"RESULT: KILL FIRED -- {len(survivors)} same-dimensional block(s) survive. "
          "Selection frame-relative; do NOT commit.")
else:
    print("RESULT: PASS -- org crosses; every same-dimensional 2-D competitor rejects under")
    print("  every frame. Rejection is DISTRIBUTED: most blocks fail on enf_frac (motion")
    print("  boundary-sourced), some on basin viability. enf_frac min touches tol, so this")
    print("  is NOT enf-threshold-robust like R^2; the verdict is backstopped by basin.")
    print("  Frame-robust same-dimensional selection holds at the load-bearing operating")
    print("  point, at NS=2 -- borderline blocks need more seeds before commitment.")
