"""Mass-action flow-reactor kinetics for the binary polymer network."""
import numpy as np, scipy.sparse as sp
from scipy.integrate import solve_ivp

class Kinetics:
    def __init__(self, net, k0=1e-4, kc=10.0, phi=0.1, food_in=1.0, rx_mask=None, cat_mask=None, kcl=1.0):
        X=net['X']; self.X=X; self.ix={m:i for i,m in enumerate(X)}; N=len(X); R=net['R']
        self.N=N; self.phi=phi; self.k0=k0; self.kc=kc
        self.food=np.array([m in net['F'] for m in X]); self.food_in=food_in
        A=[];B=[];P=[]; kind=[]
        for (re,pr,kd) in R:
            A.append(self.ix[re[0]]); B.append(self.ix[re[1]] if len(re)>1 else -1)
            P.append([self.ix[y] for y in pr]); kind.append(kd)
        self.A=np.array(A); self.B=np.array(B); self.lig=np.array([k=='lig' for k in kind]); self.kfac=np.where(self.lig,1.0,kcl)
        nR=len(R)
        # stoichiometry
        rows=[];cols=[];vals=[]
        for r in range(nR):
            rows.append(A[r]);cols.append(r);vals.append(-1)
            if B[r]>=0: rows.append(B[r]);cols.append(r);vals.append(-1)
            for p in P[r]: rows.append(p);cols.append(r);vals.append(1)
        self.S=sp.csr_matrix((vals,(rows,cols)),shape=(N,nR))
        # catalysis matrix (nR x N)
        cr=[];cc=[]
        for r,cs in enumerate(net['cat']):
            for c in cs: cr.append(r); cc.append(self.ix[c])
        self.Cm=sp.csr_matrix((np.ones(len(cr)),(cr,cc)),shape=(nR,N))
        self.rx_mask=np.ones(nR) if rx_mask is None else rx_mask
        self.cat_mask=cat_mask  # optional (nR x N) 0/1 sparse multiplier on catalysis
    def rates(self,x):
        Cm=self.Cm if self.cat_mask is None else self.Cm.multiply(self.cat_mask).tocsr()
        m=self.k0+self.kc*(Cm@x)
        xb=np.where(self.B>=0, x[np.maximum(self.B,0)], 1.0)
        return self.kfac*m*x[self.A]*xb*self.rx_mask
    def rhs(self,t,x):
        x=np.maximum(x,0)
        dx=self.S@self.rates(x) - self.phi*x
        dx[self.food]+=self.phi*self.food_in
        return dx
    def run(self,x0,T=2000.0):
        sol=solve_ivp(self.rhs,(0,T),x0,method='LSODA',rtol=1e-6,atol=1e-10)
        return sol
    def x_food_only(self):
        x=np.zeros(self.N); x[self.food]=self.food_in; return x
