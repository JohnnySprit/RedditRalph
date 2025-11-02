import praw
import time
from config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, USER_AGENT

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    refresh_token=REFRESH_TOKEN,
    user_agent=USER_AGENT
)

print(f"Authenticated as: {reddit.user.me()}")

# Target subreddit
subreddit = reddit.subreddit("mechmarket")

print(f"Listening for new posts on r/{subreddit}...\n")

# Using streams to listen for new submissions in real time
for submission in subreddit.stream.submissions(skip_existing=True):
    print("="*80)
    print(f"Title: {submission.title}")
    print(f"Author: {submission.author}")
    print(f"URL: {submission.url}")
    print(f"Upvotes: {submission.ups}")
    print(f"Score: {submission.score}")
    print(f"Created at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created_utc))}")
    print("="*80)
