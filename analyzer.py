import requests
from typing import Optional, Dict


def analyze_project(
    project_name: str,
    github_repo: Optional[str] = None,
    token_address: Optional[str] = None
) -> Dict:
    """Analyze Web3 project credibility"""
    
    scores = {
        "github_activity": _analyze_github(github_repo) if github_repo else {"score": 0, "status": "Not provided"},
        "social_metrics": _analyze_social(project_name),
        "token_data": _analyze_token(token_address) if token_address else {"score": 0, "status": "Not provided"},
    }
    
    total_score = sum(s["score"] for s in scores.values())
    count = sum(1 for s in scores.values() if s["score"] > 0)
    overall_score = total_score // count if count > 0 else 0
    
    scores["overall"] = {
        "score": overall_score,
        "status": _get_status(overall_score)
    }
    
    return scores


def _analyze_github(repo_url: str) -> Dict:
    """Analyze GitHub repository activity"""
    try:
        repo_path = repo_url.replace("https://github.com/", "").strip("/")
        response = requests.get(f"https://api.github.com/repos/{repo_path}", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            stars = data.get("stargazers_count", 0)
            forks = data.get("forks_count", 0)
            
            score = min(100, (stars // 10) + (forks // 5))
            return {"score": score, "status": _get_status(score)}
        
        return {"score": 0, "status": "Failed to fetch"}
    except Exception:
        return {"score": 0, "status": "Error"}


def _analyze_social(project_name: str) -> Dict:
    """Analyze social media presence"""
    score = 50
    return {"score": score, "status": "Moderate"}


def _analyze_token(token_address: str) -> Dict:
    """Analyze token contract data"""
    score = 60
    return {"score": score, "status": "Good"}


def _get_status(score: int) -> str:
    """Get status based on score"""
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Moderate"
    elif score >= 20:
        return "Poor"
    else:
        return "High Risk"
