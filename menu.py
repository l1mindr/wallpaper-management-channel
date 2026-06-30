from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_menu() -> str:
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Wallpaper Automation[/bold cyan]",
            subtitle="v1.0",
            border_style="cyan",
        )
    )

    table = Table(show_header=True, header_style="bold cyan", expand=False)
    table.add_column("Option", justify="center", width=10)
    table.add_column("Action", width=30)

    table.add_row("1", "Auto Upload Wallpapers")
    table.add_row("2", "Search and Edit Post")
    table.add_row("0", "Exit")

    console.print(table)

    while True:
        choice = console.input(
            "\n[bold green]❯ Select an option:[/bold green] "
        ).strip()

        # Default option
        if choice == "":
            return "1"

        if choice in {"0", "1", "2"}:
            return choice

        console.print("[bold red]✗ Invalid option. Please try again.[/bold red]")
