from typing import Optional, Dict


def show_dashboard(campaign_id: Optional[str] = None) -> Dict:
    """Show campaign tracking dashboard"""
    
    # Simulate tracking data (in real implementation, fetch from database/API)
    platforms = [
        "twitter", "telegram", "discord", "reddit", "medium",
        "lens", "farcaster", "mastodon", "bluesky"
    ]
    
    metrics = {}
    
    for platform in platforms:
        metrics[platform] = {
            "posts": _get_post_count(platform, campaign_id),
            "engagement": _get_engagement(platform, campaign_id),
            "reach": _get_reach(platform, campaign_id)
        }
    
    return metrics


def _get_post_count(platform: str, campaign_id: Optional[str]) -> int:
    """Get post count for platform"""
    return hash(platform) % 50 + 10


def _get_engagement(platform: str, campaign_id: Optional[str]) -> str:
    """Get engagement metrics"""
    engagement = hash(platform) % 1000 + 100
    return f"{engagement} interactions"


def _get_reach(platform: str, campaign_id: Optional[str]) -> str:
    """Get reach metrics"""
    reach = hash(platform) % 10000 + 1000
    return f"{reach} users"
