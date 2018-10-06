import numpy as np



#So these are the ODEs set up for a single community
#Here the quanity y is the following vector: 
#x = [s,i,r]
#t is time 
#really just setting up the 'virial spread' ODEs for each individual 
#community here 
def dxdt(t,x,b,k):
    dxdt = np.zeros(3)
    dxdt[0] = -1*b*x[0]*x[1]
    dxdt[1] = b*x[0]*x[1]-k*x[1]
    dxdt[2] = k*x[1]
    return dxdt 
    
# here h is the step size of the integrator   
# just a vanilla RK4 integation method
    
def rk4(t,x,h,b,k):
    k1 = h*dxdt(t,x,b,k)
    k2 = h*dxdt(t+0.5*h,x+0.5*k1)
    k3 = h*dxdt(t+0.5*h,x+0.5*k2)
    k4 = h*dxdt(t+h,x+k3)
    
    return x+(1/6)*k1+(1/3)*k2+(1/3)*k3+(1/6)*k4

#Now we added a stepper through time given initial conditions
#t0: starting time 
#t1: end time 
#nstep: number of steps 
#x0: initial 'position'
#as aove the varaiables
def stepper(t0,t1,x0,nstep,h,b,k):
    
    #time values to use 
    times = np.linspace(t0,t1,nstep)
    
    #resulting x vector of s i and r
    x = np.zeros(3,nstep)
    
    for i in range(nstep):
        x[:,i] = rk4(times[k],x[:,k],h,b,k)
    return times,x


def prob_infect(): #probability for some subreddit indexed by j to be infected by the other k (N-1) subreddits
    sum = 0

T = 1000 #total number of time steps
N = 10 #total number of communities

Y0 = np.zeros((T, N, 3))  #initial data for s, i, r for each community. It's an array of T arrays that have N arrays that each of the 3 values of s, i ,r

def main(Y0):
    while True:
