import praw
from graphviz import Graph
from requests import Session

def main():
    graph_attri = {'overlap': 'false', 'spines': 'true', 'nodesep': '0.5'}
    node_attri = {'shape': 'circle', 'color': 'green'}
    dot = Graph('G', filename = 'test.gv', engine = 'neato', node_attr = node_attri, graph_attr = graph_attri)

    reddit = praw.Reddit(user_agent='HackNCfysix',
             client_secret='Y0aO7fFQsiwDdx7mmQDyTxWwkzk',
             client_id = '7I5stAk1fFpC-Q')

    top_posts = reddit.subreddit('askreddit').top(limit=10)
    dot.node('askreddit', color='red')
    for post in top_posts:
        user = post.author
        dot.node(user.name, color ='green')
        dot.edge('askreddit', user.name, color = 'blue')
        for comment in user.comments.new(limit=100):
            y = comment.subreddit.display_name
            dot.node(y, color = 'red')
            dot.edge(user.name, y, color = 'orange')


    dot.view()

if __name__ == '__main__':
    main()

