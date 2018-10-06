import pydot
from graphviz import Graph
import networkx

def main():
    graph_attribute = {'overlap': 'false', 'splines': 'true', 'nodesep': '0.5'}
    node_attribute = {'shape': 'point', 'label': "", }
    dot = Graph('G', filename = 'test.gv', engine = 'fdp', node_attr = node_attribute, graph_attr = graph_attribute)
    dot.node('root', color = 'red')
    for i in range(0, 10):
        dot.node('user%d' % i)
        dot.edge('root', 'user%d' % i)
        for j in range(0, 3):
            dot.node('follow' + str(i) + ', ' + str(j))
            dot.edge('follow' + str(i) + ', ' + str(j), 'user%d' % i)
            

    dot.view()
if __name__ == '__main__':
    main()



