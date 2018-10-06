import praw
from graphviz import Graph
from requests import Session

def main():
    graph_attri = {'overlap': 'false', 'spines': 'ortho', 'nodesep': '0.5'}
    node_attri = {'shape': 'circle', 'color': 'green'}
    dot = Graph('G', filename = 'test.gv', engine = 'fdp', node_attr = node_attri, graph_attr = graph_attri)

    reddit = praw.Reddit(user_agent='HackNCfysix',
             client_secret='Y0aO7fFQsiwDdx7mmQDyTxWwkzk',
             client_id = '7I5stAk1fFpC-Q')
    
    source = 'AskReddit'
    top_posts = reddit.subreddit(source).top(limit=100)
    dot.node(source, color='red')
    for post in top_posts:
        user = post.author
        for comment in user.comments.new(limit=10):
            if comment.score < 5:
                pass
            else:
                y = comment.subreddit.display_name
                if y != source:
                    dot.node(y, color = 'blue')
                    dot.edge(source, y, color = 'orange')


    dot.view()

if __name__ == '__main__':
    main()

