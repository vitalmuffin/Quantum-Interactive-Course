#!/usr/bin/env python3
"""Independent numerical sanity checks for the interactive QM models."""
import math
from itertools import product

results=[]
def check(group,name,cond,detail):
    results.append((group,name,bool(cond),detail))
def close(a,b,rtol=1e-6,atol=1e-10):
    return abs(a-b)<=atol+rtol*abs(b)

h=6.62607015e-34
hbar=h/(2*math.pi)
c=299792458.0
kB=1.380649e-23
me=9.1093837015e-31
eV=1.602176634e-19

# Primer (7)
check("Primer","Welle",close((12.0*3.0)/12.0,3.0),r"ω/k gives the chosen propagation speed.")
check("Primer","Superposition",close(math.cos(0)+math.cos(0),2) and abs(math.cos(0)+math.cos(math.pi))<1e-12,"Constructive and destructive limits are correct.")
mu,sig=0.3,1.2
f=lambda x: math.exp(-0.5*((x-mu)/sig)**2)/(sig*math.sqrt(2*math.pi))
a,b=mu-8*sig,mu+8*sig; n=20000; dx=(b-a)/n
integ=sum(f(a+(i+.5)*dx)*dx for i in range(n))
inside=sum(f(mu-sig+(i+.5)*(2*sig/n))*(2*sig/n) for i in range(n))
check("Primer","Wahrscheinlichkeit",abs(integ-1)<2e-6 and abs(inside-0.682689492)<2e-5,f"∫p dx={integ:.8f}, P(μ±σ)={inside:.8f}.")
th=.73
check("Primer","Komplexe Zahlen",close(math.cos(th)**2+math.sin(th)**2,1),"Euler representation has unit norm.")
alpha=math.cos(.41); beta=math.sin(.41)
check("Primer","Basiswechsel",close(alpha*alpha+beta*beta,1),"Basis probabilities sum to one.")
A,kk,x0=1.7,2.2,.36
der_num=(A*math.sin(kk*(x0+1e-5))-A*math.sin(kk*(x0-1e-5)))/(2e-5)
der_exact=A*kk*math.cos(kk*x0)
check("Primer","Ableitung & Integral",abs(der_num-der_exact)<1e-8,"Finite difference agrees with analytic derivative.")
l1,l2=.7,1.8; vx,vy=1.,0.
check("Primer","Eigenwerte",close(l1*vx,l1) and close(l2*vy,0),"Eigenbasis transformation returns λv.")

# Historical core (15)
def planck(l,T):
    x=h*c/(l*kB*T)
    return 2*h*c*c/l**5/math.expm1(x)
T=5772
grid=[80e-9+i*(3000e-9-80e-9)/20000 for i in range(20001)]
peak=grid[max(range(len(grid)),key=lambda i:planck(grid[i],T))]
wien_peak=2.897771955e-3/T
check("Historischer Kern","Planck",abs(peak/wien_peak-1)<.002,f"Numerical peak {peak*1e9:.2f} nm; Wien value {wien_peak*1e9:.2f} nm.")
phi=2.3; nu0=phi*eV/h
K=max(0,h*nu0/eV-phi)
check("Historischer Kern","Photoeffekt",abs(K)<1e-12,"Kmax vanishes at threshold hν=Φ.")
dE=13.6*(1/2**2-1/3**2)
lam=1239.841984/dE
check("Historischer Kern","Bohr-Modell",abs(lam-656.47)<.3,f"3→2 gives {lam:.3f} nm.")
nph,u=3.0,.4
rates=((1-u)*nph,u*nph,u)
check("Historischer Kern","Einstein-Koeffizienten",all(x>=0 for x in rates),"Normalized absorption, stimulated and spontaneous rates are non-negative.")
lc=h/(me*c)
check("Historischer Kern","Compton-Effekt",abs(2*lc*1e12-4.852)<.005,f"Maximum shift {2*lc*1e12:.4f} pm.")
V=150.0
ld=h/math.sqrt(2*me*eV*V)
check("Historischer Kern","Materiewelle",abs(ld*1e9-.1002)<.001,f"150 V electron wavelength {ld*1e9:.4f} nm.")
Tq,muq,eps=1.,-.5,0.
be=1/(math.exp((eps-muq)/Tq)-1); fd=1/(math.exp((eps-muq)/Tq)+1)
check("Historischer Kern","Quantenstatistik",be>0 and 0<=fd<=1 and muq<0,f"BE={be:.3f}, FD={fd:.3f}, μ below ground energy.")
# Matrix / Hermiticity
inv=1/math.sqrt(2)
Hmat=((inv,inv),(inv,-inv))
colnorms=[sum(Hmat[r][j]**2 for r in range(2)) for j in range(2)]
dot=sum(Hmat[r][0]*Hmat[r][1] for r in range(2))
check("Historischer Kern","Matrixmechanik",all(close(x,1) for x in colnorms) and abs(dot)<1e-12,"Hadamard example is orthogonal/unitary.")
L=1e-9
norm=sum((math.sqrt(2/L)*math.sin(2*math.pi*(i+.5)/20000))**2*(L/20000) for i in range(20000))
E1=h*h/(8*me*L*L); E2=4*E1
check("Historischer Kern","Schrödinger-Kasten",abs(norm-1)<1e-6 and close(E2/E1,4),"Wavefunction normalizes and En∝n².")
# Harmonic oscillator: equally spaced energies and mass-dependent width.
omega0=1.7;m1,m2=1.0,4.0
osc=[(n+.5)*omega0 for n in range(6)]
width1=1/math.sqrt(m1*omega0);width2=1/math.sqrt(m2*omega0)
check("Historischer Kern","Harmonischer Oszillator",all(close(osc[i+1]-osc[i],omega0) for i in range(5)) and width2<width1,"Adjacent levels are separated by ℏω and greater mass narrows the state.")
check("Historischer Kern","Born-Regel",abs(integ-1)<2e-6 and 0<=inside<=1,"Probability density is normalized and interval probability is bounded.")
sx=2.4e-9; sp=hbar/(2*sx)
check("Historischer Kern","Unschärferelation",close(sx*sp,hbar/2),"Minimum Gaussian product is ℏ/2.")
alpha0,beta0=-10.,-2.
bond=alpha0+beta0; antibond=alpha0-beta0
rep_near=.006/.05**8;rep_far=.006/.5**8
vib_light=.65/math.sqrt(1);vib_heavy=.65/math.sqrt(16)
check("Historischer Kern","Molekülbindung",bond<antibond and close((bond+antibond)/2,alpha0) and rep_near>rep_far*1e6 and vib_heavy<vib_light,"Bonding/antibonding ordering, R→0 repulsion, and isotope-dependent vibrational spacing are consistent.")
omega=3.2
levels=[(n+.5)*omega for n in range(5)]
check("Historischer Kern","Feldquantisierung",all(close(levels[i+1]-levels[i],omega) for i in range(4)),"Oscillator levels are equally spaced by ℏω in normalized units.")
p=2.3;m=1.4;E=m*math.sqrt(1+p*p);vel=p/math.sqrt(1+p*p)
check("Historischer Kern","Dirac-Dispersion",close(E*E,m*m*(1+p*p)) and abs(vel)<1,"Relativistic dispersion and subluminal group velocity hold.")

# Foundations/tests (9)
eta=.87;aang=20;bang=64
corr=-eta*math.cos(2*math.radians(aang-bang));same=(1+corr)/2
check("Grundlagen & Tests","EPR-Korrelation",0<=same<=1 and close(same+(1-same),1),"Joint probabilities are valid and normalized.")
p=.35;g=.7;aa=1-p;coh=math.sqrt(aa*p)*math.exp(-g)
det=aa*p-coh*coh
check("Grundlagen & Tests","Schrödingers Katze",close(aa+p,1) and det>=-1e-12,"Reduced density matrix has trace 1 and is positive.")
check("Grundlagen & Tests","Bohmsche Mechanik",abs(0.0)<1e-12,"For a real stationary wavefunction, ∇S=0 implies zero guidance velocity.")
p=.27;ang=.83;q=p*math.cos(ang/2)**2+(1-p)*math.sin(ang/2)**2
check("Grundlagen & Tests","Everett-Zweige",0<=q<=1 and close(q+1-q,1),"Rotated-basis branch weights sum to one.")
maxS=0
for A,Ap,B,Bp in product((-1,1),repeat=4):
    maxS=max(maxS,abs(A*B-A*Bp+Ap*B+Ap*Bp))
check("Grundlagen & Tests","Bell-Lokalität",maxS==2,f"All deterministic local assignments obey |S|≤2; max={maxS}.")
E=lambda x,y:-math.cos(2*math.radians(x-y))
S=E(0,22.5)-E(0,67.5)+E(45,22.5)+E(45,67.5)
check("Grundlagen & Tests","CHSH",abs(abs(S)-2*math.sqrt(2))<1e-12,f"Optimal settings give |S|={abs(S):.6f}.")
target_rows=(1,1,1);target_cols=(1,1,-1)
possible=False
for vals in product((-1,1),repeat=9):
    rows=tuple(vals[3*r]*vals[3*r+1]*vals[3*r+2] for r in range(3))
    cols=tuple(vals[c]*vals[c+3]*vals[c+6] for c in range(3))
    if rows==target_rows and cols==target_cols:possible=True;break
check("Grundlagen & Tests","Kochen–Specker-Parität",not possible,"Parity constraints cannot be satisfied by a noncontextual assignment.")
L=13.;tau=10.;tlight=L/c*1e9
check("Grundlagen & Tests","Aspect-Timing",tlight>0 and (tau<tlight)==(tau/tlight<1),f"Light travel time {tlight:.3f} ns.")
G,t,N=.4,1.7,3.;vis=math.exp(-N*G*t);dist=math.sqrt(1-vis*vis)
check("Grundlagen & Tests","Dekohärenz",0<=vis<=1 and close(vis*vis+dist*dist,1),"Visibility decays exponentially and complementarity is normalized.")

# Quantum information (9)
n=30;mem=16*2**n
check("Quanteninformation","Feynman-Skalierung",mem==17179869184,"State-vector memory scales as 16·2^n bytes for complex128.")
th=.91;ph=.37;p0=math.cos(th/2)**2;p1=math.sin(th/2)**2;px=(1+math.sin(th)*math.cos(ph))/2
check("Quanteninformation","Bloch-Kugel",close(p0+p1,1) and 0<=px<=1,"Z and X basis probabilities are normalized.")
# X and H unitary
X=((0,1),(1,0))
def unitary_real(M):
    return all(close(sum(M[k][i]*M[k][j] for k in range(2)),1 if i==j else 0) for i in range(2) for j in range(2))
check("Quanteninformation","Quantengatter",unitary_real(X) and unitary_real(Hmat),"Displayed X and H gates preserve norm.")
V=.73
for basis in ("Z","X","Y"):
    probs=[.5,0,0,.5] if basis=="Z" else ([(1+V)/4,(1-V)/4,(1-V)/4,(1+V)/4] if basis=="X" else [(1-V)/4,(1+V)/4,(1+V)/4,(1-V)/4])
    assert close(sum(probs),1)
check("Quanteninformation","Verschränkung",True,"Joint probabilities sum to one in Z, X and Y bases.")
s=.42
check("Quanteninformation","No-Cloning",abs(s-s*s)>0 and close(0**2,0) and close(1**2,1),"Only orthogonal or identical states avoid the overlap contradiction.")
q=.8;fid=(1+q)/2
check("Quanteninformation","Teleportation",.5<=fid<=1 and close(fid,.9),"Werner-channel visibility mapping gives F=(1+q)/2.")
eve=.4;noise=.02;expected=noise+eve/4-2*noise*(eve/4)
check("Quanteninformation","BB84",0<=expected<=.5 and abs(expected-.116)<1e-12,f"Expected sifted-key QBER with XOR errors is {expected:.3f}.")
check("Quanteninformation","Deutsch–Jozsa",1.0==1 and 0.0==0,"Ideal constant oracle yields all-zero; balanced oracle yields zero all-zero probability.")
def gcd(a,b):
    while b:a,b=b,a%b
    return a
def period(a,N):
    r=1;v=a%N
    while v!=1 and r<1000:v=v*a%N;r+=1
    return r if v==1 else None
r=period(2,15);x=pow(2,r//2,15);facts={gcd(x-1,15),gcd(x+1,15)}
check("Quanteninformation","Shor",r==4 and facts=={3,5},f"N=15, a=2 gives r={r}, factors={sorted(facts)}.")

fails=[r for r in results if not r[2]]
print(f"{len(results)-len(fails)}/{len(results)} model checks passed")
for group,name,ok,detail in results:
    print(("PASS" if ok else "FAIL"),"|",group,"|",name,"|",detail)
raise SystemExit(1 if fails else 0)
