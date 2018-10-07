# USEFUL FUNCTIONS #

import numpy as np
from itertools import combinations

#So these are the ODEs set up for a single community
#Here the quanity y is the following vector:
#x = [s,i,r]
#t is time
#really just setting up the 'virial spread' ODEs for each individual
#community here
def get_dydt(y,b,k):
    #print(b)
    s = y[0]
    i = y[1]
    dydt = np.zeros(3)
    dydt[0] = -1*b*s*i
    dydt[1] = b*s*i - k*i
    dydt[2] = k*i
    return dydt

def rk4(y,h,b,k):
    #print(b)
    k1 = h*get_dydt(y,b,k)
    k2 = h*get_dydt(y+0.5*k1,b,k)
    k3 = h*get_dydt(y+0.5*k2,b,k)
    k4 = h*get_dydt(y+k3, b, k)

    return y+(1/6)*k1+(1/3)*k2+(1/3)*k3+(1/6)*k4


#This function corresponds to the probability correction since the connectedness of the
#communities corresponds to their intersection, while the union should correspond to the probability
#that an uninfected community gets infected
#Inputs:
#    L: Connectedness Matrix
#    Y: Big ol' matrix object
#    t: current times step in simulation function
#    j: current index in simulation function
def probSum(Y,L,t,j):
    #here o is a dummy variable
    T,N,o = np.shape(Y)

    terms = []
    for c in range(N-1):
        terms.append(Y[t][c][1]*L[j,c])

    result = []

    for i in range(2,N):
        r = list(combinations(range(1,N),i))
        for m in r:
            term = 1
            for t in range(len(m)):
                term *= terms[m[t]]
            result.append(term)

    if N % 2 == 0:
        return -1*sum(result)
    else:
        return -1*sum(result)+sum(terms)






#Now we added a stepper through time given initial conditions
#t0: starting time
#t1: end time
#nstep: number of steps
#x0: initial 'position'
#as aove the varaiables
"""
def stepper(t0,t1,x0,nstep,h,b,k):

    #time values to use
    times = np.linspace(t0,t1,nstep)

    #resulting x vector of s i and r
    x = np.zeros(3,nstep)

    for i in range(nstep):
        x[:,i] = rk4(times[k],x[:,k],h,b,k)
    return times,x
"""
