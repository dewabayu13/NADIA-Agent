import typer
from rich.console import Console

app = typer.Typer(
    help="NADIA Agent Command Line Interface"
)

console = Console()


@app.callback()
def main():
    """NADIA CLI."""
    pass


@app.command()
def version():
    """Show NADIA Agent version."""
    console.print("[bold green]NADIA Agent[/bold green]")
    console.print("Version : 0.1.0")
    console.print("Runtime : Initialized")


if __name__ == "__main__":
    app()
