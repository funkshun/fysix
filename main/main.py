import numpy as np
import hackncutils.py as util

# INITIALIZATION #
T_init = 1000 #total number of time steps
N_init = 3 #total number of communities
Y_init = np.zeros((T, N, 3))  #initial data for s, i, r for each community. It's an array of T arrays that have N arrays that each of the 3 values of s, i ,r
subnames_init = ["AskReddit", "explainlikeimfive", "offmychest"] #a dict of size N of subreddit names (strings) ORDERED THE SAME as the 3-arrays in Y_init
M_init = 10000
#example for how to initalize the values for the subreddit indexed 2 (from 0,1,2.... N-1):
#if I want to initialize explainlikeimfive as being infected with some i, while the other communities as non-infected (so s,i,r = 0):
Y_init[0][1] = np.array([0.9, 0.1, 0.0]) # index of Y_init: 0 is the time (so 0 since this is initial), the next index is the index of sub you want to give initial condition

def main(Y0, T, N, subnames, M):
    Y = Y0
    t = 0 #initial time step

    #creating connectivity matrix
    L = np.zeros((N, N)) #matrix of L_jk values; the connectedness of each subreddit, rows and columns ordered same as subnames and within Y
    for j in range(N):
        for k in range(N):
            L[j,k] = util.connectivity(subnames[j], subnames[k], M)
    #while loop
    while t < T:


        t += 1
