import praw
from graphviz import Graph
from requests import Session
import datetime
import csv
import re

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
    time_hits = []
    top_posts = reddit.subreddit(source).top(limit=1000000)

    #define REGEXs
    lampreg = re.compile('^lamp$')
    mothreg = re.compile('^moth$')
    for submission in top_posts:
        try:
            lex = submission.title.split(" ")
            for token in lex:
                if mothreg.search(token):
                    print(f'moth title time: {submission.created}')
                    print(f'moth title: {submission.title}')
                    hits += 1
                    tot += 1
                    time_hits.append(submission.created)
            for token in lex:
                if lampreg.search(token):
                    print(f'lamp title time: {submission.created}')
                    print(f'lamp title: {submission.title}')
                    hits += 1
                    tot += 1
                    time_hits.append(submission.created)
        except UnicodeEncodeError:
            continue

        submission.comments.replace_more(limit=0)

        for comments in submission.comments:
            try:
                check = comments.body.lower().split(" ")
                for token in check:
                    if mothreg.search(token):
                        print(f'moth comment time: {comments.created}')
                        print(f'moth comment: {comments.body}')
                        hits += 1
                        tot += 1
                        time_hits.append(comments.created)
                    elif lampreg.search(token):
                        print(f'lamp comment time: {comments.created}')
                        print(f'lamp comment: {comments.body}')
                        hits += 1
                        tot += 1
                        time_hits.append(comments.created)
                    else:
                        tot += 1
            except UnicodeEncodeError:
                continue

    print(hits)
    print(tot)
    print(hits/tot)
    print(time_hits)

    csvfile = 'memeeconomy_moth.csv'
    with open(csvfile, 'w+') as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in time_hits:
            writer.writerow([val])

if __name__ == '__main__':
    main()
