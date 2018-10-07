from graphviz import Graph
import imageio
import os
import numpy as np

import simulator

#pickles = ["smallpolitical", "political", "entertainment"]
pickles = ['smallpolitical']

## Bokeh initialization code


# Code to launch on startup
def startup():
    infected = []
    sub_reference = []
    connections = []
    subreddits = []
    for pickle in pickles:
        sim_tuple = simulator.simulate(pickle)
        connections.append(sim_tuple[0])
        subreddits.append(sim_tuple[1])
        sub_reference.append(sim_tuple[2])

    launch(subreddits, connections, sub_reference)


def launch(all_subreddits, all_connections, sub_reference):
    # Matrices containing constants for each pickles

    numPickles = len(pickles)

    # Store the position, number of subreddits, a
    X = []
    Y = []
    R = []

    for i in range(numPickles):
        X.append([])
        Y.append([])
        R.append([])

    N = []

    infected = all_subreddits

 ## Unload parameters #######################################################
    for l in range(len(all_subreddits)):
        subreddits = all_subreddits[l]
        connections = all_connections[l]
        total = len(connections) # Number of SubReddits Investigated
        timeSteps = len(subreddits[0]) # Length of the arrays (number of time steps)
        x = np.zeros(total) # x Position
        y = np.zeros(total) # y position
        r = np.zeros(total) # radius of node

        for i in range(total): # For each sub reddit
            x[i] = np.random.randint(10) # point's x value
            y[i] = np.random.randint(10) # point's y value
            r[i] = np.random.randint(40, 60) # radius
            #subs[i] = np.random.randint(40, 60) # radius

        #Add the current subreddit data to the Matrices
        X[l] = x
        Y[l] = y
        R[l] = r
        N.append(total)
    graph_attri = {'overlap': 'false', 'spines': 'true', 'nodesep': '0.5'}
    node_attri = {'shape': 'circle'}
    for i in range(numPickles):
        for t in range(timeSteps):
            dot = Graph('G', filename = 'epoch' + str(i) + 'time' + str(t), engine = 'neato', node_attr = node_attri, graph_attr = graph_attri, format = 'png')
            for k in range(len(sub_reference[i])):
                print(sub_reference[i][k])
                dot.node(sub_reference[i][k], color = '#%02x%02x%02x' % get_color(k, t, infected, i))
            for j in range(len(sub_reference[i])):
                for k in range(len(sub_reference[i])):
                    if connections[j][k] > 0:
                        if infected[i][j][t] > 0 and infected[i][k][t] > 0:
                            dot.edge(sub_reference[i][j], sub_reference[i][k], color = '#ff00000')
                        else:
                            dot.edge(sub_reference[i][j], sub_reference[i][k], color = '#0000000')
            dot.render()
        images = []
        for t in range(timeSteps):
            images.append(imageio.imread('epoch'+str(i)+'time'+str(t)+'.png'))
        imageio.mimsave(pickles[i] + '.gif', images)
        for t in range(timeSteps):
            os.remove('epoch'+str(i)+'time'+str(t)+'.png')


def get_color(name_index, time, infected, epoch):
    infection = infected[epoch][name_index][time]
    return (int(255*infection), 20, int(180*(1-infection)))


startup()
