# Reddit Bot

A simple Reddit bot using PRAW (Python Reddit API Wrapper).

## Setup

1. Install dependencies:
   ```bash
   pip install praw
   ```

2. Copy `config.example.py` to `config.py`:
   ```bash
   copy config.example.py config.py
   ```

3. Fill in your own Reddit credentials in `config.py`:
   - Get your `CLIENT_ID` and `CLIENT_SECRET` from [Reddit App Preferences](https://www.reddit.com/prefs/apps)
   - Get your `REFRESH_TOKEN` using OAuth2 authentication
   - Update `USER_AGENT` with your bot's information

4. Run the bot:
   ```bash
   python redditBot.py
   ```

## Notes

- `config.py` is in `.gitignore` and will not be in this repository

