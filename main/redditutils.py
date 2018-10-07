import praw

#reddit authentication (Boo's Account "Deklyned")
reddit = praw.Reddit(user_agent='HackNCfysix',
         client_secret='Y0aO7fFQsiwDdx7mmQDyTxWwkzk',
         client_id = '7I5stAk1fFpC-Q')

#Accepts Two Subreddit names and a number of random draws
#Returns a connectivity index by evaluating the number of
#posters randomly selected who post in both subs over number selected

def _connectivity(sub1, sub2, draws):
    
    sum_connected = 0
    authors = []
    if reddit.subreddit(sub1).subscribers > reddit.subreddit(sub2).subscribers:
        big = sub1
        small = sub2
    else:
        big = sub2
        small = sub1

    #get sum posts
    init_posts = reddit.subreddit(small).top(limit=draws)
    
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
        except:
            pass
    for author in authors:
        user = reddit.redditor(author)
        try:
            for submission in user.submissions.new(limit=draws):
                y = submission.subreddit.display_name
                if y == big:
                    sum_connected += 1
                    break
        except:
            pass
<<<<<<< HEAD
    return 2 * (sum_connected / draws)

def group_connectivity(communities, draws):
    ret = {}
    max_conn = 0
    for i in range(0, len(communities)):
        for j in range(i, len(communities)):
            if i == j:
                pass
            else:
                first = communities[i]
                sec = communities[j]
                ret[first + ", " + sec] = _connectivity(first, sec, draws)
                #ret[sec + ", " + sec] = _connectivity(first, sec, draws)

    for k in range(0, len(communities)):
        for l in range(i, len(communities)):
            if k == l:
                pass
            else:
                first = communities[k]
                sec = communities[l]
                max_conn = max(ret[first + ", " + sec], max_conn)
                #ret[sec + ", " + sec] = _connectivity(first, sec, draws)
    
    for l in range(0, len(communities)):
        for m in range(i, len(communities)):
            if l == m:
                pass
            else:
                first = communities[l]
                sec = communities[m]
                ret[first + ", " + sec] = ret[first + ", " + sec] / max_conn
                #ret[sec + ", " + sec] = _connectivity(first, sec, draws)
    return ret

def connectivity(sub1, sub2, conns):
    return conns[sub1 + ", " + sub2]


        
=======
    return (sum_connected / draws)


>>>>>>> 945aa1e66f7123543b3b3eedb6366c974ce5fcf4

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
