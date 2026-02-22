import os
from typing import List, Dict, Optional
from dotenv import load_dotenv

load_dotenv()


SUPPORTED_PLATFORMS = [
    "twitter", "telegram", "discord", "reddit", "medium", "mirror",
    "lens", "farcaster", "mastodon", "bluesky", "threads", "linkedin",
    "facebook", "instagram", "youtube", "tiktok", "snapchat", "pinterest",
    "tumblr", "wechat", "weibo", "line", "kakao", "vk", "ok",
    "whatsapp", "signal", "element", "slack", "matrix", "nostr"
]


def publish_content(
    content: str,
    platforms: List[str],
    template: Optional[str] = None
) -> Dict:
    """Publish content to multiple platforms"""
    
    if template:
        content = _apply_template(content, template)
    
    results = {}
    
    for platform in platforms:
        if platform.lower() not in SUPPORTED_PLATFORMS:
            results[platform] = {
                "success": False,
                "error": "Platform not supported"
            }
            continue
        
        result = _publish_to_platform(platform.lower(), content)
        results[platform] = result
    
    return results


def _apply_template(content: str, template: str) -> str:
    """Apply template to content"""
    templates = {
        "announcement": f"📢 Announcement\n\n{content}\n\n#Web3 #Crypto",
        "update": f"🔄 Update\n\n{content}\n\n#Development #Progress",
        "launch": f"🚀 Launch Alert\n\n{content}\n\n#NewProject #Launch",
    }
    
    return templates.get(template, content)


def _publish_to_platform(platform: str, content: str) -> Dict:
    """Publish to specific platform"""
    
    api_key = os.getenv(f"{platform.upper()}_API_KEY")
    
    if not api_key:
        return {
            "success": False,
            "error": f"API key not configured for {platform}"
        }
    
    # Simulate publishing (in real implementation, call actual APIs)
    post_id = f"{platform}_{hash(content) % 100000}"
    
    return {
        "success": True,
        "post_id": post_id,
        "platform": platform
    }
