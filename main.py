from rich.console import Console

from menu import show_menu
from services.upload import upload_wallpapers

console = Console()


def main():
    while True:
        choice = show_menu()

        match choice:
            case "1":
                console.print("\n[cyan]Starting wallpaper upload...[/cyan]\n")
                upload_wallpapers()
                input("\nPress Enter to continue...")

            case "2":
                console.print("[yellow] Search and Edit Post (Coming Soon)[/yellow]")
                input("\nPress Enter to continue...")

            case "0":
                console.print("[bold red]Goodbye![/bold red]")
                break


if __name__ == "__main__":
    main()
