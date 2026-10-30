"""Independent small-dimension check of the cyclic Lindblad formulas.

Usage: python -m pip install numpy scipy; python verification/check_cycle.py
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

def generator(eta, gamma):
    d=3
    S=np.roll(np.eye(d),1,axis=0)
    a=(1+eta)/2
    b=(1-eta)/2
    Q=a*S+b*S@S-np.eye(d)
    L=np.zeros((d*d,d*d),dtype=complex)
    basis=lambda i,j: np.outer(np.eye(d)[i],np.eye(d)[j])
    def lindblad(X):
        y=np.zeros_like(X,dtype=complex)
        for i in range(d):
            for j in range(d):
                if i==j: continue
                r=Q[i,j]
                J=basis(i,j)
                proj=J.conj().T@J
                y+=r*(J@X@J.conj().T-.5*(proj@X+X@proj))
        y+=gamma*(np.diag(np.diag(X))-X)
        return y
    for i in range(d):
        for j in range(d):
            col=i+d*j
            L[:,col]=lindblad(basis(i,j)).reshape(-1,order='F')
    return L,Q

def partial_transpose(rho,d=3):
    return rho.reshape(d,d,d,d).transpose(0,3,2,1).reshape(d*d,d*d)

def realignment(rho,d=3):
    return rho.reshape(d,d,d,d).transpose(0,2,1,3).reshape(d*d,d*d)

def check(eta,gamma,t):
    L,Q=generator(eta,gamma)
    superop=expm(L*t)
    d=3
    J=np.zeros((d*d,d*d),complex)
    for i in range(d):
        for j in range(d):
            E=np.zeros((d,d),complex);E[i,j]=1
            out=(superop@E.reshape(-1,order='F')).reshape(d,d,order='F')
            J+=np.kron(out,E)
    rho=J/d
    P=expm(Q*t)
    E=np.exp(-1.5*t)
    theta=np.sqrt(3)*eta*t/2
    c=np.exp(-(1+gamma)*t)
    p=[(1+2*E*np.cos(theta-2*np.pi*m/3))/3 for m in range(3)]
    assert np.allclose(np.sort(P[0]),np.sort(p),atol=1e-12)
    ppt=min(np.linalg.eigvalsh(partial_transpose(rho)))
    predicted=min([P[i,j]*P[j,i]-c*c for i in range(d) for j in range(i)],default=0)
    r=np.linalg.svd(realignment(rho),compute_uv=False).sum()
    expected=(1+2*E)/3+2*c
    assert abs(r-expected)<1e-10,(r,expected)
    assert (ppt>=-1e-10)==(predicted>=-1e-10),(ppt,predicted)
    return ppt,r

def main():
    tstar=brentq(lambda t:(1+2*np.exp(-1.5*t))/3+2*np.exp(-t)-1,.1,5)
    assert abs(tstar-1.26188944840409)<1e-10
    for eta in (0.,.1,.5,1.):
        for gamma in (0.,.25,.5):
            for t in (.1,1.25,tstar,2.):
                check(eta,gamma,t)
    ppt,r=check(1.,0.,1.25)
    assert ppt>0 and r>1
    print('PASS: 48 exact-superoperator comparisons; t* =',tstar)
    print('eta=1,gamma=0,t=1.25: min(PPT eigenvalue) =',ppt,'realignment =',r)

if __name__=='__main__':
    main()
