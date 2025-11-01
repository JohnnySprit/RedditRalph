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

subreddit_mechmarket = reddit.subreddit("mechmarket")
# Fetches and prints the latest 25 posts from r/mechmarket
for num, post in enumerate(subreddit_mechmarket.new(limit=25)):
    print(f"{num+1}. {post.title}")
    print(f"Author: {post.author}")
    print(f"URL: {post.url}")
    print(f"Upvotes: {post.ups}")
    print(f"Downvotes: {post.downs}")
    print(f"Total Votes: {post.score}")



