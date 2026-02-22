import os


def create_env_template():
    """Create .env.example template file"""
    
    template = """# Web3 Scout Configuration

# Platform API Keys
TWITTER_API_KEY=your_twitter_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
DISCORD_BOT_TOKEN=your_discord_bot_token
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret

# Additional Platforms
MEDIUM_API_KEY=your_medium_api_key
LENS_API_KEY=your_lens_api_key
FARCASTER_API_KEY=your_farcaster_api_key
MASTODON_ACCESS_TOKEN=your_mastodon_token
BLUESKY_API_KEY=your_bluesky_api_key

# Analytics
GITHUB_TOKEN=your_github_token
ETHERSCAN_API_KEY=your_etherscan_api_key
"""
    
    with open(".env.example", "w") as f:
        f.write(template)
