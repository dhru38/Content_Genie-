import praw



CLIENT_ID = ""
CLIENT_SECRET = ""
USERNAME = ""
PASSWORD = ""
USER_AGENT = ""  # MUST be descriptive

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT
)


def get_post() :
    for post in reddit.subreddit("AITAH").new(limit=10):
        if len(post.selftext.split()) < 200 :
            return str(post.selftext)

def get_title () : 
    for post in reddit.subreddit("AITAH").new(limit=10):
        if len(post.selftext.split()) < 200 :
            return str(post.title)

def get_link () : 
    for post in reddit.subreddit("AITAH").new(limit=10):
        if len(post.selftext.split()) < 200 :
            return str(post.shortlink)
