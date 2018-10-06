import praw
from graphviz import Graph
from requests import Session

def main():
    graph_attri = {'overlap': 'false', 'spines': 'true', 'nodesep': '0.5'}
    node_attri = {'shape': 'circle'}
    dot = Graph('G', filename = 'test.gv', engine = 'neato', node_attr = node_attri, graph_attr = graph_attri)

    reddit = praw.Reddit(user_agent='HackNCfysix',
             client_secret='Y0aO7fFQsiwDdx7mmQDyTxWwkzk',
             client_id = '7I5stAk1fFpC-Q')

    #redditor = reddit.redditor('Deklyned')
    #dot.node('Deklyned')
    #for comment in redditor.comments.new(limit=100):
    #    y = comment.subreddit.display_name
    #    dot.node(y)
    #    dot.edge('Deklyned', y)
    
    dot.view()
    
if __name__ == '__main__':
    main()

