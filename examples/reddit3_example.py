import praw
from graphviz import Graph
from requests import Session
import datetime

def get_date(submission):
        time = submission.created
        return datetime.datetime.fromtimestamp(time)

def main():

    reddit = praw.Reddit(user_agent='HackNCfysix',
            client_secret='Y0aO7fFQsiwDdx7mmQDyTxWwkzk',
            client_id = '7I5stAk1fFpC-Q')

    hits = 0
    tot = 0
    source = 'MemeEconomy'
    top_posts = reddit.subreddit(source).top(limit=100)
      # dot.node(source, color='red')
    for submission in top_posts:
        submission.comments.replace_more(limit=0)
        try:
            check = str(submission.title)
            if 'moth' in check.lower():
                print(check)
                hits += 1
                tot += 1
            else:
                tot += 1
        except UnicodeEncodeError:
            continue

    print(hits/tot)

if __name__ == '__main__':
    main()
