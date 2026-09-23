import sys, csv, os, numpy as np
from frame_sweep_r3 import P, SubstrateR3, run_constrained, make_frames, B_thr, PR, PD, ENF

NS = 6
START, END = int(sys.argv[1]), int(sys.argv[2])
OUT = "sweep_ns6.csv"

def runs(sub,Bm,Bi,free,**kw):
    return [run_constrained(sub,Bm,Bi,free,np.random.default_rng(700+13*s),**kw) for s in range(NS)]
def m(rs,k): return float(np.mean([r[k] for r in rs]))

def evalb(sub,Bm,Bi,free):
    iso=runs(sub,Bm,Bi,free); pas=runs(sub,Bm,Bi,free,u_zero=True); sta=runs(sub,Bm,Bi,free,freeze_y=True)
    iso_b,enf,P_iso,base=m(iso,"basin"),m(iso,"enf"),m(iso,"trP"),m(iso,"terr")
    pas_b,P_sta=m(pas,"basin"),m(sta,"trP")
    C2=(iso_b>=B_thr) and (pas_b<B_thr) and (enf<ENF)
    C3=(P_iso/max(P_sta,1e-9))<PR
    hi=m(runs(sub,Bm,Bi,free,ahat_off=+0.4),"terr"); lo=m(runs(sub,Bm,Bi,free,ahat_off=-0.4),"terr")
    C1=(max(hi,lo)-base)<PD*0.4 and iso_b>=B_thr
    return int(C1 and C2 and C3), iso_b, pas_b, enf, P_iso/max(P_sta,1e-9)

sub=SubstrateR3(P); frames=make_frames(n_rot=9,n_shear=3)
new = not os.path.exists(OUT)
f=open(OUT,"a",newline=""); w=csv.writer(f)
if new: w.writerow(["frame","cond","free","tau0","iso","pas","enf","Pr"])
if START==0:
    I=np.eye(3); t,iso,pas,enf,pr=evalb(sub,I,I,[0,1,2]); w.writerow([-1,1.0,"org",t,iso,pas,enf,pr]); f.flush()
    print(f"org tau0={t} iso={iso:.2f} pas={pas:.2f}")
for fi in range(START,END):
    Bm=frames[fi]; Bi=np.linalg.inv(Bm); cond=float(np.linalg.cond(Bm))
    for comp in range(3):
        free=[i for i in range(3) if i!=comp]
        t,iso,pas,enf,pr=evalb(sub,Bm,Bi,free)
        w.writerow([fi,round(cond,1),str(free),t,round(iso,3),round(pas,3),round(enf,3),round(pr,3)]); f.flush()
        print(f"f{fi:2d} free={free}: tau0={t} iso={iso:.2f} pas={pas:.2f} enf={enf:.3f}")
f.close()
