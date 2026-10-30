"""Independent GKSL, Choi, reversible-decomposition, and asymptotic checks.

Run from any directory: python verification/check_science.py
Results are written beside this script. Finite tests do not prove the theorems.
"""
from __future__ import annotations
import json
import platform
from pathlib import Path
import numpy as np
import scipy
import mpmath as mp
from scipy.linalg import expm
from scipy.optimize import brentq
from scipy.special import roots_hermite


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def matrix_unit(d: int, i: int, j: int) -> np.ndarray:
    out = np.zeros((d, d), complex)
    out[i, j] = 1
    return out


def liouvillian(q: np.ndarray, noise: np.ndarray, energies: np.ndarray) -> np.ndarray:
    """Column vectorization; assemble jump terms without using the Choi formula."""
    d = len(q)
    require(q.shape == (d, d), 'Q must be square')
    require(np.max(np.abs(q.sum(axis=0))) < 1e-12, 'Q columns must sum to zero')
    eye = np.eye(d)
    h = np.diag(energies)
    out = -1j * (np.kron(eye, h) - np.kron(h.T, eye))
    jumps = []
    for i in range(d):
        for j in range(d):
            if i != j:
                require(q[i, j] >= 0, 'negative rate')
                jumps.append(np.sqrt(q[i, j]) * matrix_unit(d, i, j))
    jumps.extend(np.diag(noise[:, alpha]) for alpha in range(noise.shape[1]))
    for jump in jumps:
        product = jump.conj().T @ jump
        out += np.kron(jump.conj(), jump)
        out -= .5 * (np.kron(eye, product) + np.kron(product.T, eye))
    return out


def choi_direct(q: np.ndarray, noise: np.ndarray, energies: np.ndarray, time: float) -> np.ndarray:
    d = len(q)
    channel = expm(time * liouvillian(q, noise, energies))
    result = np.zeros((d*d, d*d), complex)
    for i in range(d):
        for j in range(d):
            e = matrix_unit(d, i, j)
            image = (channel @ e.reshape(-1, order='F')).reshape(d, d, order='F')
            result += np.kron(image, e) / d
    return result


def closed_choi(q: np.ndarray, noise: np.ndarray, energies: np.ndarray, time: float):
    d = len(q)
    p = expm(time*q)
    rates = -np.diag(q)
    distance = ((noise[:, None, :] - noise[None, :, :])**2).sum(axis=2)
    c = np.exp(-time*(rates[:, None]+rates[None, :]+distance)/2)
    result = np.diag(p.reshape(-1)).astype(complex)
    for i in range(d):
        for j in range(d):
            if i != j:
                result[i*d+i, j*d+j] = c[i, j]*np.exp(-1j*time*(energies[i]-energies[j]))
    return result/d, p, c


def partial_transpose(rho: np.ndarray, d: int) -> np.ndarray:
    return rho.reshape(d, d, d, d).transpose(0, 3, 2, 1).reshape(d*d, d*d)


def realignment(rho: np.ndarray, d: int) -> np.ndarray:
    return rho.reshape(d, d, d, d).transpose(0, 2, 1, 3).reshape(d*d, d*d)


def cycle_q(eta: float) -> np.ndarray:
    s = np.roll(np.eye(3), 1, axis=0)
    return (1+eta)*s/2 + (1-eta)*(s@s)/2 - np.eye(3)


def determinant(eta: float, gamma: float, t: float) -> float:
    p = expm(cycle_q(eta)*t)
    return float(p[0, 1]*p[1, 0] - np.exp(-2*(1+gamma)*t))


def check_cycles() -> dict:
    max_choi = max_realign = max_ppt = max_singular = 0.0
    count = 0
    example = None
    for eta in (-1., -.3, 0., .02, .1, .5, 1.):
        for gamma in (0., .25, .5):
            for t in (0., .1, .924196240746594, 1.25, 1.261889448404092, 2.):
                q = cycle_q(eta)
                noise = np.sqrt(gamma)*np.eye(3)
                rho = choi_direct(q, noise, np.zeros(3), t)
                expected, p, cmat = closed_choi(q, noise, np.zeros(3), t)
                max_choi = max(max_choi, float(np.max(np.abs(rho-expected))))
                e = np.exp(-1.5*t)
                c = np.exp(-(1+gamma)*t)
                theta = np.sqrt(3)*eta*t/2
                offsets = np.array([(1+2*e*np.cos(theta-2*np.pi*k/3))/3 for k in range(3)])
                s = np.roll(np.eye(3), 1, axis=0)
                require(np.max(np.abs(p-(offsets[0]*np.eye(3)+offsets[1]*s+offsets[2]*(s@s)))) < 2e-12, 'offset orientation')
                sv = np.linalg.svd(p, compute_uv=False)
                max_singular = max(max_singular, float(np.max(np.abs(sv-np.array([1,e,e])))))
                real = float(np.linalg.svd(realignment(rho, 3), compute_uv=False).sum())
                max_realign = max(max_realign, abs(real-((1+2*e)/3+2*c)))
                block_min = min(float(np.linalg.eigvalsh([[p[i,j], c],[c,p[j,i]]])[0]/3) for i in range(3) for j in range(i))
                pt_min = float(np.linalg.eigvalsh(partial_transpose(rho,3))[0])
                predicted = min(block_min, float(np.diag(p).min()/3))
                max_ppt = max(max_ppt, abs(pt_min-predicted))
                require(np.linalg.eigvalsh(rho)[0] > -2e-12, 'Choi positivity')
                require(abs(np.trace(rho)-1) < 2e-12, 'trace normalization')
                count += 1
                if eta == 1 and gamma == 0 and t == 1.25:
                    example = {'eta':eta,'gamma':gamma,'time':t,'ppt_min_eigenvalue':pt_min,'ppt_determinant':determinant(eta,gamma,t),'realignment':real}
    require(max(max_choi,max_realign,max_ppt,max_singular) < 2e-11, 'cycle residual')
    require(example['ppt_min_eigenvalue'] > 0 and example['realignment'] > 1, 'bound-entangled example')
    roots = [{'eta':eta,'t_ppt':brentq(lambda t: determinant(eta,0.,t), .01, 4.,xtol=1e-14)} for eta in (0., .1, .5, 1.)]
    return {'cases':count,'max_choi_error':max_choi,'max_realignment_error':max_realign,'max_ppt_eigenvalue_error':max_ppt,'max_population_singular_value_error':max_singular,'example':example,'zero_dephasing_roots':roots}


def check_reversible() -> dict:
    rng = np.random.default_rng(20261030)
    residual = balance_residual = kernel_residual = 0.0
    cases = 0
    # Gauss-Hermite nodes independently approximate nonnegative Gaussian Gram factors.
    x, weight = roots_hermite(80)
    for d in (2,3,4,5):
        for sample in range(3):
            pi = rng.uniform(.4,1.,d); pi /= pi.sum()
            conductance = rng.uniform(.03,.2,(d,d)); conductance = (conductance+conductance.T)/2
            np.fill_diagonal(conductance,0)
            q = conductance/pi[None,:]; np.fill_diagonal(q,-q.sum(axis=0))
            noise = rng.uniform(-.3,.3,(d,1))
            energies = rng.normal(size=d)
            for t in (.15,1.,4.):
                rho = choi_direct(q,noise,energies,t)
                expected,p,c = closed_choi(q,noise,energies,t)
                residual = max(residual,float(np.max(np.abs(rho-expected))))
                balance_residual = max(balance_residual,float(np.max(np.abs(p*pi[None,:]-(p*pi[None,:]).T))))
                v = noise[:,0]
                gram_factors = np.exp(-t*((-np.diag(q))/2 + v*v))[:,None]*np.exp(np.sqrt(2*t)*v[:,None]*x[None,:])*np.sqrt(weight/np.sqrt(np.pi))[None,:]
                gram = gram_factors @ gram_factors.T
                kernel_residual = max(kernel_residual,float(np.max(np.abs(gram-c))))
                # Test the theorem's residual population coefficients, with no diagonal-H phases.
                pair_ppt = all(p[i,j]*p[j,i] >= c[i,j]**2-1e-12 for i in range(d) for j in range(i))
                residual_weights = p-c*np.sqrt(pi[:,None]/pi[None,:])
                if pair_ppt:
                    require(residual_weights.min() >= -2e-12,'reversible decomposition residual')
                # Each failed pair produces a two-qubit NPT projection with positive probability.
                for i in range(d):
                    for j in range(i):
                        if p[i,j]*p[j,i] < c[i,j]**2-1e-10:
                            indices = [i*d+i,i*d+j,j*d+i,j*d+j]
                            projection = rho[np.ix_(indices,indices)]
                            success = float(np.trace(projection).real)
                            require(success>0,'projection probability')
                            require(np.linalg.eigvalsh(partial_transpose(projection/success,2))[0]<0,'two-qubit projection')
                cases += 1
    require(max(residual,balance_residual,kernel_residual)<2e-11,'reversible residual')
    # Disconnected components: positive no-jump coherence but zero transfer between components.
    q=np.array([[-1.,1.,0.,0.],[1.,-1.,0.,0.],[0.,0.,-2.,2.],[0.,0.,2.,-2.]])
    rho,p,c=closed_choi(q,np.zeros((4,0)),np.zeros(4),2.)
    require(p[0,2]==0 and p[2,0]==0 and c[0,2]>0,'reducible example')
    require(np.linalg.eigvalsh(partial_transpose(rho,4))[0]<0,'reducible NPT')
    return {'cases':cases,'max_choi_error':residual,'max_detailed_balance_error':balance_residual,'max_nonnegative_gram_quadrature_error':kernel_residual,'disconnected_example':'NPT at tested finite time; infinite-time claim is analytical'}


def check_weak_bias() -> dict:
    mp.mp.dps=70
    def root(gamma,eta):
        def fun(t):
            e=mp.exp(-3*t/2); u=mp.cos(mp.sqrt(3)*eta*t/2)
            return (1-2*e*u+e*e*(4*u*u-3))/9-mp.exp(-2*(1+gamma)*t)
        return mp.findroot(fun,(mp.mpf('.8'),mp.mpf('1.5')))
    tstar=root(0,0); e=mp.exp(-3*tstar/2)
    k=3*e*(1-4*e)*tstar*tstar/(4*(1-e)*(e+2))
    eta=mp.mpf('0.00001')
    ratio=(tstar-root(0,eta))/(eta*eta)
    require(abs(ratio-k)<mp.mpf('1e-10'),'quadratic coefficient')
    endpoint=2*mp.log(4)/3
    quartic=(endpoint-root(mp.mpf('.5'),eta))/(eta**4)
    expected4=endpoint**4/64
    require(abs(quartic-expected4)<mp.mpf('1e-10'),'quartic endpoint')
    return {'precision_decimal_digits':70,'eta':str(eta),'t_star':str(tstar),'quadratic_coefficient':str(k),'measured_gap_over_eta_squared':str(ratio),'endpoint_quartic_coefficient':str(expected4),'measured_endpoint_gap_over_eta_fourth':str(quartic)}


def main() -> None:
    result={'status':'pass','environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__},'cycle':check_cycles(),'reversible':check_reversible(),'weak_bias':check_weak_bias(),'limits':'Finite-dimensional numerical checks and high-precision expansions; not a universal proof or separability decision algorithm.'}
    destination=Path(__file__).with_name('results.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
