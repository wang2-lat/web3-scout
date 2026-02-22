import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from analyzer import analyze_project
from publisher import publish_content
from tracker import show_dashboard

app = typer.Typer(help="Web3 project analysis and multi-platform marketing automation")
console = Console()


@app.command()
def analyze(
    project_name: str = typer.Argument(..., help="Project name or GitHub repo"),
    github_repo: Optional[str] = typer.Option(None, help="GitHub repository URL"),
    token_address: Optional[str] = typer.Option(None, help="Token contract address"),
):
    """Analyze Web3 project credibility and generate score"""
    console.print(f"[bold cyan]Analyzing project: {project_name}[/bold cyan]")
    
    result = analyze_project(project_name, github_repo, token_address)
    
    table = Table(title="Project Analysis Report")
    table.add_column("Metric", style="cyan")
    table.add_column("Score", style="magenta")
    table.add_column("Status", style="green")
    
    for metric, data in result.items():
        table.add_row(metric, str(data["score"]), data["status"])
    
    console.print(table)
    console.print(f"\n[bold]Overall Score: {result['overall']['score']}/100[/bold]")


@app.command()
def publish(
    content: str = typer.Argument(..., help="Content to publish"),
    platforms: str = typer.Option("twitter,telegram,discord", help="Comma-separated platforms"),
    template: Optional[str] = typer.Option(None, help="Template name to use"),
):
    """Publish content to multiple Web3 platforms"""
    platform_list = [p.strip() for p in platforms.split(",")]
    
    console.print(f"[bold cyan]Publishing to: {', '.join(platform_list)}[/bold cyan]")
    
    results = publish_content(content, platform_list, template)
    
    table = Table(title="Publishing Results")
    table.add_column("Platform", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Post ID", style="yellow")
    
    for platform, result in results.items():
        status = "✓ Success" if result["success"] else "✗ Failed"
        table.add_row(platform, status, result.get("post_id", "N/A"))
    
    console.print(table)


@app.command()
def dashboard(
    campaign_id: Optional[str] = typer.Option(None, help="Campaign ID to track"),
):
    """Show campaign tracking dashboard with performance metrics"""
    console.print("[bold cyan]Campaign Performance Dashboard[/bold cyan]\n")
    
    metrics = show_dashboard(campaign_id)
    
    table = Table(title="Platform Performance")
    table.add_column("Platform", style="cyan")
    table.add_column("Posts", style="magenta")
    table.add_column("Engagement", style="green")
    table.add_column("Reach", style="yellow")
    
    for platform, data in metrics.items():
        table.add_row(
            platform,
            str(data["posts"]),
            str(data["engagement"]),
            str(data["reach"])
        )
    
    console.print(table)


@app.command()
def init():
    """Initialize configuration and create .env template"""
    from config import create_env_template
    
    create_env_template()
    console.print("[green]✓[/green] Created .env.example template")
    console.print("Please copy .env.example to .env and add your API keys")


if __name__ == "__main__":
    app()
