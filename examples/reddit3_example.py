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
    source = 'neoliberal'
    top_posts = reddit.subreddit(source).top(limit=100)
    for submission in top_posts:
        submission.comments.replace_more(limit=0)
        for comments in submission.comments:
            try:
                check = comments.body.lower()
                if 'technocrat' in check:
                    print(f'technocrat time: {comments.created}')
                    hits += 1
                    tot += 1
                elif 'global' in check:
                    print(f'global time: {comments.created}')
                    hits += 1
                    tot += 1
                else:
                    tot += 1
            except UnicodeEncodeError:
                continue

    print(hits)
    print(tot)
    print(hits/tot)

if __name__ == '__main__':
    main()
