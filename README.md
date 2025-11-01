# RedditRalph

A simple bot I made to fetch and print the latest posts from r/mechmarket using PRAW.

I spend a lot of time the subreddit to see what keyboards people are selling. (Topre/HHKBs are my favorite)

## How to use

1. Install PRAW:
   ```bash
   pip install praw
   ```
   Or use the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

2. Get your Reddit API credentials:
   - Go to https://www.reddit.com/prefs/apps
   - Click "create app" or "create another app"
   - Choose "script" as the type
   - Fill in name, description (optional)
   - Set redirect URI to `http://localhost:8080`
   - Your `CLIENT_ID` is the string under the app name
   - Your `CLIENT_SECRET` is the "secret" field

3. Get a refresh token:
   - You'll need to do OAuth2 authentication to get a refresh token
   - Check out the PRAW docs: https://praw.readthedocs.io/en/stable/getting_started/authentication.html
   - Or look for Reddit OAuth2 tutorials online - there are a few ways to do it
   - The refresh token is what lets your bot stay authenticated

4. Set up your config:
   - Copy `config.example.py` to `config.py`:
   ```bash
   copy config.example.py config.py
   ```
   - Open `config.py` and fill in:
     - `CLIENT_ID` - from step 2
     - `CLIENT_SECRET` - from step 2
     - `REFRESH_TOKEN` - from step 3
     - `USER_AGENT` - format like `BotName by /u/YourUsername`

5. Run the bot:
   ```bash
   python redditBot.py
   ```


