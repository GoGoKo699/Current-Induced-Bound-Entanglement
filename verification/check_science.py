"""Independent GKSL, Choi, separable-decomposition, and asymptotic checks.

Run from any directory: python verification/check_science.py
Results are written beside this script. Finite tests do not prove the theorems.
"""
from __future__ import annotations
import json
import platform
from itertools import product
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


def product_twirl(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    """Average all third-root local phases and simultaneous cyclic shifts."""
    average = np.zeros((9, 9), dtype=complex)
    phase_vectors = np.exp(2j*np.pi*np.array(list(product(range(3), repeat=3)))/3)
    for shift in range(3):
        shifted_left = np.roll(left, shift)
        shifted_right = np.roll(right, shift)
        for phases in phase_vectors:
            ket = np.kron(phases*shifted_left, phases.conj()*shifted_right)
            average += np.outer(ket, ket.conj())
    return average/(3*len(phase_vectors))


def bell_line(shift: int, phase: int) -> np.ndarray:
    labels = np.arange(3)
    ket = np.zeros(9, dtype=complex)
    ket[3*((labels+shift) % 3)+labels] = np.exp(2j*np.pi*phase*labels/3)/np.sqrt(3)
    return np.outer(ket, ket.conj())


def bell_mixture(p: np.ndarray, c: float) -> np.ndarray:
    """Build the target from all nine Bell vectors independently of twirling."""
    rho = np.zeros((9, 9), dtype=complex)
    for shift in range(3):
        for phase in range(3):
            weight = p[shift]/3
            if shift == 0:
                weight += (2 if phase == 0 else -1)*c/3
            rho += weight*bell_line(shift, phase)
    return rho


def separable_cycle_state(p: np.ndarray, c: float) -> tuple[np.ndarray, float]:
    """Rebuild a proposed separable state using explicit product averages."""
    uniform_share = max(2*c-p[0], 0)
    pair_share = abs(c)-uniform_share
    residual = p-uniform_share
    result = np.zeros((9, 9), dtype=complex)
    if uniform_share > 0:
        uniform_ket = np.full(3, 1/np.sqrt(3))
        result += 3*uniform_share*product_twirl(uniform_ket, uniform_ket)
    if pair_share > 0:
        # Saturate the larger budget to avoid magnifying cancellation near a zero smaller budget.
        ratio = residual[1]/pair_share if residual[1] >= residual[2] else pair_share/residual[2]
        large = np.sqrt(ratio/(1+ratio))
        small = np.sqrt(1/(1+ratio))
        left = np.array([small, large, 0])
        right = np.array([large, np.sign(c)*small, 0])
        result += pair_share*(2+ratio+1/ratio)*product_twirl(left, right)
        residual -= pair_share*np.array([2, ratio, 1/ratio])
    for shift, weight in enumerate(residual):
        for label in range(3):
            index = 3*((label+shift) % 3)+label
            result[index, index] += weight/3
    return result, float(residual.min())


def check_static_slice() -> dict:
    rng = np.random.default_rng(20261123)
    edge_cases = np.array([
        [0, 0, 1], [0, .5, .5], [1, 0, 0], [1/3, 1/3, 1/3],
        [.2, .2, .6], [.6, .2, .2], [.5, .2, .3], [.4, .3, .3],
    ])
    populations = np.vstack((edge_cases, rng.dirichlet(np.ones(3), size=128)))
    max_error = 0.
    min_residual = 0.
    sign_cases = {'negative': 0, 'zero': 0, 'positive': 0}
    outside = {'ppt': 0, 'realignment_with_ppt': 0}
    for p in populations:
        e = np.hypot((3*p[0]-1)/2, np.sqrt(3)*(p[1]-p[2])/2)
        ppt_ceiling = np.sqrt(p[1]*p[2])
        realignment_ceiling = (1-e)/3
        lower = -min(p[0]/2, ppt_ceiling)
        upper = min(p[0], ppt_ceiling, realignment_ceiling)
        for c in (lower, lower/2, 0., upper/2, upper):
            target = bell_mixture(p, c)
            rebuilt, residual = separable_cycle_state(p, c)
            max_error = max(max_error, float(np.max(np.abs(rebuilt-target))))
            min_residual = min(min_residual, residual)
            require(np.linalg.eigvalsh(target)[0] > -2e-12, 'static positivity')
            require(np.linalg.eigvalsh(partial_transpose(target, 3))[0] > -2e-12, 'static PPT')
            require(np.linalg.svd(realignment(target, 3), compute_uv=False).sum() < 1+2e-12, 'static realignment')
            sign = 'positive' if c > 0 else 'negative' if c < 0 else 'zero'
            sign_cases[sign] += 1
        if ppt_ceiling+1e-8 < p[0]:
            rho = bell_mixture(p, (ppt_ceiling+p[0])/2)
            require(np.linalg.eigvalsh(partial_transpose(rho, 3))[0] < -1e-10, 'static outside PPT')
            outside['ppt'] += 1
        physical_ppt_ceiling = min(p[0], ppt_ceiling)
        if realignment_ceiling+1e-8 < physical_ppt_ceiling:
            rho = bell_mixture(p, (realignment_ceiling+physical_ppt_ceiling)/2)
            require(np.linalg.eigvalsh(partial_transpose(rho, 3))[0] >= -2e-12, 'static PPT-entangled example')
            require(np.linalg.svd(realignment(rho, 3), compute_uv=False).sum() > 1+1e-10, 'static outside realignment')
            outside['realignment_with_ppt'] += 1
    require(max_error < 2e-12 and min_residual >= -2e-12, 'static product decomposition residual')
    return {'cases_by_coherence_sign':sign_cases,'outside_cases':outside,'max_reconstruction_error':max_error,'minimum_diagonal_residual':min_residual}


def crossover_dephasing(eta: float) -> float:
    def crossover(t):
        return 2*np.exp(-1.5*t)*(1+np.cos(np.sqrt(3)*eta*t/2))-1

    time = brentq(crossover, .01, 2., xtol=1e-14)
    return -np.log((1-np.exp(-1.5*time))/3)/time-1


def check_exact_onsets() -> dict:
    regimes = {'bound_interval': 0, 'coincident': 0, 'delayed': 0}
    crossover = []
    examples = []
    max_error = 0.
    min_residual = 0.
    for eta in (-1., -.5, -.1, 0., .1, .5, 1.):
        gammas = [0., .5, 1., 2., 10.]
        critical = crossover_dephasing(eta)
        if eta != 0:
            crossover.append({'eta':eta,'critical_gamma':critical})
            gammas.extend((critical-.05, critical, critical+.05))
        q = cycle_q(eta)
        for gamma in gammas:
            noise = np.sqrt(gamma)*np.eye(3)
            t_ppt = brentq(lambda t: determinant(eta, gamma, t), .001, 4., xtol=1e-14)
            t_star = brentq(lambda t: np.exp(-1.5*t)+3*np.exp(-(1+gamma)*t)-1, .001, 4., xtol=1e-14)
            gap = t_star-t_ppt
            if eta == 0 or abs(gamma-critical) < 1e-12:
                require(abs(gap) < 2e-12, 'onsets coincide at the crossover or zero bias')
                regimes['coincident'] += 1
            elif gamma < critical:
                require(gap > 0, 'bound interval below crossover')
                regimes['bound_interval'] += 1
            else:
                require(gap < 0, 'current delays the coincident thresholds above crossover')
                regimes['delayed'] += 1
            t_eb = max(t_ppt,t_star)
            rho = choi_direct(q, noise, np.zeros(3), t_eb)
            p = expm(q*t_eb)[:, 0]
            rebuilt, residual = separable_cycle_state(p, np.exp(-(1+gamma)*t_eb))
            max_error = max(max_error, float(np.max(np.abs(rebuilt-rho))))
            min_residual = min(min_residual, residual)
            rho_before = choi_direct(q, noise, np.zeros(3), t_eb-1e-6)
            before_pt = np.linalg.eigvalsh(partial_transpose(rho_before, 3))[0]
            before_realignment = np.linalg.svd(realignment(rho_before, 3), compute_uv=False).sum()
            require(before_pt < -1e-10 or before_realignment > 1+1e-10, 'direct witness before EB onset')
            if eta == 1 and gamma in (0., .5, 1.):
                examples.append({'eta':eta,'gamma':gamma,'t_star':t_star,'t_ppt':t_ppt,'t_eb':t_eb})
    require(max_error < 2e-12 and min_residual >= -2e-12, 'dynamical product decomposition residual')
    return {'regime_counts':regimes,'crossover':crossover,'examples':examples,'max_reconstruction_error':max_error,'minimum_diagonal_residual':min_residual}


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
    result={'status':'pass','environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__},'cycle':check_cycles(),'static_bell_slice':check_static_slice(),'exact_cycle_onsets':check_exact_onsets(),'reversible':check_reversible(),'weak_bias':check_weak_bias(),'limits':'Finite decomposition, threshold, and high-precision checks support the analytical proofs in science/.'}
    destination=Path(__file__).with_name('results.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
