import tweepy as tw
import matplotlib.pyplot as plt
import pydot
import sys

def main():
    #Twitter API Authentication
    AUTH_TOKEN = "bdyFwvaWIjqTO0tIwIaChRxU3"
    AUTH_SECRET = "2tO3cColKfZRzfz4U6Qp0qynkFt6AjwaRzRT6PLXhUD6csTPlp"

    ACCESS_TOKEN = "1048366404993503232-WHs7tljVcFHudMGPr25LutCVBNdKoG"
    ACCESS_SECRET = "pnh4WjmS8dVEbu1e1gYcHnMfN9beVqb2sReBScXp6GXTv"
    
    auth = tw.OAuthHandler(AUTH_TOKEN, AUTH_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    
    c = tw.Cursor(api.followers_ids, screen_name="miraieu").pages()
    ids = []
    for page in c:
        ids.extend(page)
    g = pydot.Dot(graph_type = 'digraph')
    root = pydot.Node("ROOT", style = 'filled', fillcolor='white')
    g.add_node(Node)
    for edge in ids:
        node = pydot.Node(edge, style="filled", fillcolor="red")
        g.add_node(node)
        g.add_edge(root, node)
    g.write_png('out.png')
    #nx.draw(g)
    #plt.savefig("test.png")





if __name__ == '__main__':
    main()



