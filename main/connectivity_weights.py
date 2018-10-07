from graphviz import Graph
from redditutils import connectivity, group_connectivity
import time

def main():
    start_time = time.time()
    graph_attri = {'overlap': 'false', 'spines': 'ortho', 'nodesep': '0.5'}
    node_attri = {'shape': 'circle', 'color': 'green'}
    dot = Graph('G', filename = 'test.gv', engine = 'neato', node_attr = node_attri, graph_attr = graph_attri)

    subreddits = ['liberal', 'democrats', 'politics', 'democraticparty', 'BlueMidterm2018']

    conns = group_connectivity(subreddits, 100)

    for i in range(0, 5):
        dot.node(subreddits[i])
    for j in range(0, 5):
        for k in range(j, 5):
            if k == j:
                pass
            else:
                dot.edge(subreddits[j], subreddits[k], label = str(connectivity(subreddits[j], subreddits[k], conns)))

    print("---- %s seconds ----" % (time.time() - start_time))
    dot.view()

if __name__ == '__main__':
    main()

