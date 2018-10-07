import numpy as np
import matplotlib.pyplot as plt
import hackncutils as util
import redditutils as red
import pickle
import os

# INITIALIZATION #
def initialize(simName): #returns a dict specifying prechosen initial quantities. takes in simulation name out of smallpolitical, political
    #format: 'pickle name' : [picklefilename (str), T, N, M, subnames (list of str), b array, k array, initialization array(N, 3)]
    masterlist = []
    if simName == 'smallpolitical':
        T_init = 200 #total number of time steps
        N_init = 5 #total number of communities
        M_init = 100
        h_init = 1
        y_init = np.zeros((N_init,3))  #initial data for s, i, r for each community. It's an array of T arrays that have N arrays that each of the 3 values of s, i ,r
        for j in range(N_init): #initialize each jth sub with (s,i,r) = (1,0,0)
            y_init[j] = np.array([1.0, 0.0, 0.0])

        subnames_init = ["esist",
        "The_Mueller",
        "liberal",
        "politics",
        "neoliberal"] #a list of size N of subreddit names (strings) ORDERED THE SAME as the 3-arrays in Y_init

        simulatingstring = "Trump"

        #if I want to initialize explainlikeimfive as being infected with some i, while the other communities as non-infected (so s,i,r = 0):
        y_init[0] = np.array([1.0, 0.0, 0.0]) # index of Y_init: 0 is the time (so 0 since this is initial), the next index is the index of sub you want to give initial condition
        y_init[1] = np.array([0.9999, 0.0001, 0.0])
        y_init[2] = np.array([1.0, 0.0, 0.0])
        y_init[3] = np.array([0.7, 0.3, 0.0])
        y_init[4] = np.array([1.0, 0.0, 0.0])
        #initialize b and k:

        #the larger it is, the faster that the subreddit gets infected
        b_init = np.array([1.1, 1.5, 0.4, 1.0, 0.6]) #usualy range from k to 2
        #the larger it is, the faster that the subreddit recovers
        k_init = np.array([0.02, 0.01, 0.2, 0.25, 0.3]) # usually range from 0.01 to 0.5

        masterlist = ['smallpolitical.pk1', T_init, N_init, M_init, subnames_init, b_init, k_init, y_init]

        return masterlist


    # political #
    if simName == 'political':
        T_init = 200 #total number of time steps
        N_init = 15 #total number of communities
        M_init = 100
        h_init = 1
        y_init = np.zeros(( N_init, 3))  #initial data for s, i, r for each community. It's an array of T arrays that have N arrays that each of the 3 values of s, i ,r
        for j in range(N_init): #initialize each jth sub with (s,i,r) = (1,0,0)
            y_init[j] = np.array([1.0, 0.0, 0.0])


        subnames_init = ["esist",
        "The_Mueller",
        "liberal",
        "politics",
        "neoliberal",
        "TrumpCriticizesTrump",
        "EnoughTrumpSpam",
        "Impeach_Trump",
        "PoliticalHumor",
        "funny",
        "news",
        "socialism",
        "LateStageCapitalism",
        "dankmemes",
        "pics"] #a list of size N of subreddit names (strings) ORDERED THE SAME as the 3-arrays in Y_init

        simulatingstring = "Trump"

        #if I want to initialize explainlikeimfive as being infected with some i, while the other communities as non-infected (so s,i,r = 0):
        y_init[0] = np.array([1.0, 0.0, 0.0]) # index of Y_init: 0 is the time (so 0 since this is initial), the next index is the index of sub you want to give initial condition
        y_init[1] = np.array([0.9, 0.1, 0.0])
        y_init[2] = np.array([1.0, 0.0, 0.0])
        y_init[3] = np.array([1.0, 0.0, 0.0])
        y_init[4] = np.array([1.0, 0.0, 0.0])
        y_init[5] = np.array([1.0, 0.0, 0.0])
        y_init[6] = np.array([1.0, 0.0, 0.0])
        y_init[7] = np.array([1.0, 0.0, 0.0])
        y_init[8] = np.array([1.0, 0.0, 0.0])
        y_init[9] = np.array([1.0, 0.0, 0.0])
        y_init[10] = np.array([0.6, 0.4, 0.0])
        y_init[11] = np.array([1.0, 0.0, 0.0])
        y_init[12] = np.array([1.0, 0.0, 0.0])
        y_init[13] = np.array([1.0, 0.0, 0.0])
        y_init[14] = np.array([1.0, 0.0, 0.0])
        #initialize b and k:

        #the larger it is, the faster that the subreddit gets infected
        b_init = np.array([0.8, 1.5, 0.2, 0.4, 0.3, 0.7, 0.8, 1.4, 0.3, 0.1, 0.5, 0.3, 0.6, 0.9, 0.2]) #usualy range from 0 to 2
        #the larger it is, the faster that the subreddit recovers
        k_init = np.array([0.05, 0.01, 0.1, 0.1, 0.09, 0.08, 0.09, 0.08, 0.03, 0.07, 0.1, 0.07, 0.05, 0.04, 0.1]) # usually range from 0.01 to 0.1

        masterlist = ['political.pk1', T_init, N_init, M_init, subnames_init, b_init, k_init, y_init]

        return masterlist
#format: 'pickle name' : [picklefilename (str), T, N, M, subnames (list of str), b array, k array, initialization array(N, 3)]

# SIMULATOR #
def simulate(simName): # Y0, T, N, h, M, b, k, subnames
    masterlist = initialize(simName)

    picklefilename = masterlist[0]
    T = masterlist[1]
    N = masterlist[2]
    M = masterlist[3]
    subnames = masterlist[4]
    b = masterlist[5]
    k = masterlist[6]

    Y0 = np.zeros((T,N,3))  #initial data for s, i, r for each community. It's an array of T arrays that have N arrays that each of the 3 values of s, i ,r
    Y0[0] = masterlist[7]
    Y = Y0

    t = 0 #initial time step
    h = 1 #stepsize

    #creating connectivity matrix
    #L = np.zeros((N, N)) #matrix of L_jc values; the connectedness of each subreddit, rows and columns ordered same as subnames and within Y
    #os.chdir(r'C:\Users\tumuz\git\fysix\main')
    fileObject = open(picklefilename, 'rb')
    L = pickle.load(fileObject)
    #print(L)
    for d in range(N):
        for e in range(N):
            if d > e:
                L[d,e] = L[e,d]
    #print(L)
    #TEST:
    #L = np.random.uniform(0.2, 0.7, (N,N))
    #print(L)
    #while loop
    while t < (T-1): #begins at t =0
        #print(t)
        #print(Y)
        y_t = Y[t] #most recent array y, of dimensions (N, 3) of the most recent solutions to s, i, r
        #print(y_t)
        y_new = np.zeros((N, 3)) #next iteration

        #progress stepper:
        for j in range(N): #steps forward the x = (s, i, r) of each subreddit
            #print(b[j])
            y_new[j] = util.rk4(y_t[j],h,b[j],k[j]) #progressing

        #after running rk4 on each sub, put the y vector of the N new (s,i,r) vectors into big Y:
        Y[t+1] = y_new

        #next, determines if new uninfected subs should be infected:
        for j in range(N):
            if Y[t+1][j][1] == 0.0 and Y[t+1][j][2] == 0.0: #if non infected (and non recovered)
                sm = 0
                for c in range(N):
                    if c != j:
                        i_c = Y[t+1][c][1] #current infection percentage of the kth subreddit
                        #print((j,c))
                        #print(i_c)
                        sm += L[j,c]*i_c
                prob_infection = (sm)+ util.probSum(Y,L,t,j) #probability of infection of jth subreddit by the other subs
                u = np.random.rand()
                #print(prob_infection)
                if u < prob_infection:
                    Y[t+1][j][1] = 1 / M #infecting "one of the sampled users"
        #next, can randomly make some "recovered subreddit re-infected by switching recovered to susceptible":
        """
        for j in range(N):
            if Y[t+1][j][2] > 0.5: #if more than 50% recovered
                test = 1 / (T)
                u = np.random.rand()
                if u < test: #if subreddit is randomly
                    #print('Idea reappeared!')
                    #print('at iteration ' + str(t))
                    suscepthold = Y[t+1][j][0]
                    #print(suscepthold)
                    Y[t+1][j][1] += 0.1 * Y[t+1][j][2]
                    Y[t+1][j][2] -= 0.1 * Y[t+1][j][2] #infecting "one of the sampled users"
                    break #so that only one random re-start thing can happen per iteration
        """

        t += 1

    final = {}
    for j in range(N):
        final_i = []
        for i in range(T):
            final_i.append(Y[i][j][1])
        final[subnames[j]] = final_i
    return final
