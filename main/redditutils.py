import praw

#reddit authentication (Boo's Account "Deklyned")
reddit = praw.Reddit(user_agent='HackNCfysix',
         client_secret='Y0aO7fFQsiwDdx7mmQDyTxWwkzk',
         client_id = '7I5stAk1fFpC-Q')

#Accepts Two Subreddit names and a number of random draws
#Returns a connectivity index by evaluating the number of
#posters randomly selected who post in both subs over number selected

def connectivity(sub1, sub2, draws):
    
    sum_connected = 0
    authors = []
    
    #get sum posts
    init_posts = reddit.subreddit(sub1).top(limit=draws)
    authors_checked = 0
    for post in init_posts:
        try:
            #if we have enough unique authors, finish
            if len(authors) == draws:
                break
            #if we have already seen this one, next
            elif post.author.name in authors:
                pass
            #else, add to authors
            else:
                authors.append(post.author.name)
                if len(authors) % 20 == 0:
                    print(len(authors))
        except:
            pass
    for author in authors:
        user = reddit.redditor(author)
        authors_checked += 1
        if authors_checked % 20 == 0:
            print("Author " + str(authors_checked))
        try:
            for submission in user.submissions.new(limit=10):
                y = submission.subreddit.display_name
                if y == sub2:
                    sum_connected += 1
                    break
        except:
            pass
    return (sum_connected / draws)
    
    

def del_dups(seq):
    seen = {}
    pos = 0
    for item in seq:
        if item not in seen:
            seen[item] = True
            seq[pos] = item
            pos += 1
    del seq[pos:]

def main():
    print(connectivity('AskReddit', 'explainlikeimfive', 1000))

if __name__ == '__main__':
    main()
