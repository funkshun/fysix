import numpy as np
import pickle
import matplotlib.pyplot as plt
import hackncutils as util
import redditutils as red
import pickle

# INITIALIZATION #

T_init = 100 #total number of time steps

N_init = 15 #total number of communities
M_init = 100
h_init = 1
Y_init = np.zeros((T_init, N_init, 3))  #initial data for s, i, r for each community. It's an array of T arrays that have N arrays that each of the 3 values of s, i ,r
for j in range(N_init): #initialize each jth sub with (s,i,r) = (1,0,0)
    Y_init[0][j] = np.array([1.0, 0.0, 0.0])


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
Y_init[0][0] = np.array([0.7, 0.3, 0.0]) # index of Y_init: 0 is the time (so 0 since this is initial), the next index is the index of sub you want to give initial condition
Y_init[0][1] = np.array([0.2, 0.8, 0.0])
Y_init[0][2] = np.array([0.9, 0.1, 0.0])
Y_init[0][3] = np.array([0.8, 0.2, 0.0])
Y_init[0][4] = np.array([1.0, 0.0, 0.0])
Y_init[0][5] = np.array([0.5, 0.5, 0.0])
Y_init[0][6] = np.array([0.3, 0.7, 0.0])
Y_init[0][7] = np.array([0.4, 0.6, 0.0])
Y_init[0][8] = np.array([1.0, 0.0, 0.0])
Y_init[0][9] = np.array([1.0, 0.0, 0.0])
Y_init[0][10] = np.array([0.6, 0.4, 0.0])
Y_init[0][11] = np.array([0.8, 0.2, 0.0])
Y_init[0][12] = np.array([0.7, 0.3, 0.0])
Y_init[0][13] = np.array([0.9, 0.1, 0.0])
Y_init[0][14] = np.array([1.0, 0.0, 0.0])
#initialize b and k:

#the larger it is, the faster that the subreddit gets infected
b_init = np.array([0.8, 1.5, 0.5, 1.3, 0.5, 1.2, 1.6, 1.4, 1.1, 0.5, 0.8, 0.4, 0.9, 1.1, 0.3]) #usualy range from k to 2
#the larger it is, the faster that the subreddit recovers
k_init = np.array([0.1, 0.01, 0.2, 0.4, 0.3, 0.4, 0.05, 0.1, 0.2, 0.2, 0.6, 0.3, 0.4, 0.6, 0.2]) # usually range from 0.01 to 0.5
def main(Y0, T, N, h, M, b, k, subnames):
    Y = Y0
    t = 0 #initial time step
    h #step size

    #creating connectivity matrix
    #L = np.zeros((N, N)) #matrix of L_jc values; the connectedness of each subreddit, rows and columns ordered same as subnames and within Y
    fileObject = open('conn.pk1', 'rb')
    L = pickle.load(fileObject)
    for d in range(N):
        for e in range(N):
            if d > e:
                L[d,e] = L[e,d]
    print(L)
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
                prob_infection = (sm)/ (N - 1) #probability of infection of jth subreddit by the other subs
                u = np.random.rand()
                #print(prob_infection)
                if u < prob_infection:
                    Y[t+1][j][1] = 1 / M #infecting "one of the sampled users"
        t += 1

    final = {}
    for j in range(N):
        final_i = []
        for i in range(T):
            final_i.append(Y[i][j][1])
        final[subnames[j]] = final_i
    return final

x = main(Y_init, T_init, N_init, h_init, M_init, b_init, k_init, subnames_init)
#print(x)


t = np.arange(T_init)

plt.figure(1)

for name in subnames_init:
    x1 = np.array(x[name])
    plt.plot(t, x1, c=np.random.rand(3,), label = name)

plt.grid()
plt.legend()
plt.show()
