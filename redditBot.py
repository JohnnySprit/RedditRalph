import praw
from config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, USER_AGENT



# Initializes Reddit instanc
# Credentials from the config.py file that is in .gitignore
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    refresh_token=REFRESH_TOKEN,
    user_agent=USER_AGENT
)

print(f"Authenticated as: {reddit.user.me()}")

# Fetches and prints the top 10 posts from the subreddit r/mechmarket
for post in reddit.subreddit("mechmarket").top(limit=10):
    print(post.title)
    print(post.url)
    print(post.score)
    print(post.num_comments)
    print(post.author)
