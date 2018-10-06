import praw
from graphviz import Graph
from requests import Session

def get_date(submission):
        time = submission.created
        return datetime.datetime.fromtimestamp(time)
def main():
     # graph_attri = {'overlap': 'false', 'spines': 'ortho', 'nodesep': '0.5'}
     # node_attri = {'shape': 'circle', 'color': 'green'}
     # dot = Graph('G', filename = 'test.gv', engine = 'fdp', node_attr = node_attri, graph_attr = graph_attri)

    reddit = praw.Reddit(user_agent='HackNCfysix',
            client_secret='Y0aO7fFQsiwDdx7mmQDyTxWwkzk',
            client_id = '7I5stAk1fFpC-Q')

    source = 'AskReddit'
    top_posts = reddit.subreddit(source).top(limit=10)
     # dot.node(source, color='red')
    for submission in top_posts:
        submission.comments.replace_more(limit=0)
        print(get_date(submission))
        for comments in submission.comments:
             # user = post.author
            try:
                print('hi')
            except UnicodeEncodeError:
                continue

if __name__ == '__main__':
    main()
