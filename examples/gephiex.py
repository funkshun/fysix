from gephistreamer import graph
from gephistreamer import streamer


def main():
    streamer.GephiWS(hostname='localhost', port=8080, workspace='workspace0')
    stream = streamer.Streamer(streamer.GephiWS())
    
    node_a = graph.Node("A")
    node_b = graph.Node("B")
    
    stream.add_node(node_a, node_b)
    edge = graph.Edge(node_a, node_b)
    stream.add_edge(edge)

if __name__ == '__main__':
    main()
