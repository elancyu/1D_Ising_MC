import random
import numpy as np
import matplotlib.pyplot as plt
N = 1000    # size of the 1D model
J = 1       # constant
Nt = 10000*N   # run for Nt*N steps.
T = 0.5        # the temperature
beta = 1/T    # inverse temperature
S = np.ones(N,int)
E = -J*N
u = 0
Us = []

for i in range(1,Nt+1,1):
    im = random.randint(0, N-1)
    delta = 0
    if im == 0:
        delta += S[N-1]
    else:
        delta += S[im-1]
    if im == N-1:
        delta += S[0]
    else:
        delta += S[im+1]
    delta = 2*J*delta*S[im]
    prob = np.exp(-delta*beta)
    if random.uniform(0,1)<prob:
        S[im] *= -1
        E += delta
    u += (E - u) / i
    Us.append(u)
    
ts = range(0,len(Us),1)
plt.plot(ts,Us)
plt.xlabel('time')
plt.ylabel('Energy')
u = Us[-1]/1000

