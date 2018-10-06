import numpy as np



def prob_infect(): #probability for some subreddit indexed by j to be infected by the other k (N-1) subreddits
    sum = 0

T = 1000 #total number of time steps
N = 10 #total number of communities

Y0 = np.zeros((T, N, 3))  #initial data for s, i, r for each community. It's an array of T arrays that have N arrays that each of the 3 values of s, i ,r

def main(Y0):
    while True:
