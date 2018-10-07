import numpy as np
import hackncutils as util
import redditutils as red

# INITIALIZATION #
T_init = 1000 #total number of time steps
N_init = 3 #total number of communities
M_init = 10000
b_init = 1/3
k_init = 1/2
h_init = 1
subnames_init = ["AskReddit", "explainlikeimfive", "offmychest"] #a list of size N of subreddit names (strings) ORDERED THE SAME as the 3-arrays in Y_init
#example for how to initalize the values for the subreddit indexed 2 (from 0,1,2.... N-1):

Y_init = np.zeros((T_init, N_init, 3))  #initial data for s, i, r for each community. It's an array of T arrays that have N arrays that each of the 3 values of s, i ,r
for j in range(N_init): #initialize each jth sub with (s,i,r) = (1,0,0)
    Y_init[0][j] = np.array([1.0, 0.0, 0.0])

#if I want to initialize explainlikeimfive as being infected with some i, while the other communities as non-infected (so s,i,r = 0):
Y_init[0][1] = np.array([0.9, 0.1, 0.0]) # index of Y_init: 0 is the time (so 0 since this is initial), the next index is the index of sub you want to give initial condition

def main(Y0, T, N, h, M, b, k, subnames):
    Y = Y0
    t = 0 #initial time step
    h #step size

    #creating connectivity matrix
    L = np.zeros((N, N)) #matrix of L_jk values; the connectedness of each subreddit, rows and columns ordered same as subnames and within Y
    for j in range(N):
        for k in range(N):
            L[j,k] = red.connectivity(subnames[j], subnames[k], M)
    #while loop
    while t < T: #begins at t =0
        y_t = Y[t] #most recent array y, of dimensions (N, 3) of the most recent solutions to s, i, r
        y_new = np.zeros((N, 3)) #next iteration

        #progress stepper:
        for j in N: #steps forward the x = (s, i, r) of each subreddit
            y_new[j] = util.rk4(y_t[j],h,b,k) #progressing

        #after running rk4 on each sub, put the y vector of the N new (s,i,r) vectors into big Y:
        Y[t+1] = y_new

        #next, determines if new uninfected subs should be infected:
        for j in range(N):
            sm = 0
            for k in range(N):
                i_k = Y[t+1][k][1] #current infection percentage of the kth subreddit
                if j != k:
                    sm += L[j,k]*i_k
            prob_infection = sm / (N - 1) #probability of infection of jth subreddit by the other subs
            u = np.random.rand()
            if u < prob_infection:
                Y[t+1][k][1] = 1 / M #infecting "one of the sampled users"
        t += 1

    final = {}
    for j in range(N):
        final_i = []
        for i in range(T):
            final_i.append(Y[i][j][1])
        final[subnames[j]] = final_i
    return final
