import praw
from graphviz import Graph
from requests import Session
import datetime
import csv

def get_date(submission):
        time = submission.created
        return datetime.datetime.fromtimestamp(time)

def main():

    reddit = praw.Reddit(user_agent='HackNCfysix',
            client_secret='Y0aO7fFQsiwDdx7mmQDyTxWwkzk',
            client_id = '7I5stAk1fFpC-Q')

    hits = 0
    tot = 0
    source = 'memes'
    time_hits = []
    top_posts = reddit.subreddit(source).top(limit=100)
    for submission in top_posts:
        if 'moth' in submission.title:
            print(f'moth title time: {submission.created}')
            hits += 1
            tot += 1
            time_hits.append(submission.created)
        if 'lamp' in submission.title:
            print(f'lamp title time: {submission.created}')
            hits += 1
            tot += 1
            time_hits.append(submission.created)
        submission.comments.replace_more(limit=0)
        for comments in submission.comments:
            try:
                check = comments.body.lower()
                if 'moth' in check:
                    print(f'moth comment time: {comments.created}')
                    hits += 1
                    tot += 1
                    time_hits.append(submission.created)
                elif 'lamp' in check:
                    print(f'lamp comment time: {comments.created}')
                    hits += 1
                    tot += 1
                    time_hits.append(submission.created)
                else:
                    tot += 1
            except UnicodeEncodeError:
                continue

    print(hits)
    print(tot)
    print(hits/tot)
    print(time_hits)

    csvfile = "/Users/davisbrown/hackNC2018/fysix/examples/moth_meme.csv"
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in time_hits:
            writer.writerow([val])

if __name__ == '__main__':
    main()
