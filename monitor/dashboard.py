from rich.console import Console
from rich.table import Table

def display_dashboard(cpu_usage, gpu_data):
    console = Console()
    table = Table(title="System Performance Dashboard")
    table.add_column("Component", style="cyan")
    table.add_column("Usage", style="green")
    table.add_column("Temperature", style="red")

    table.add_row("CPU", f"{cpu_usage}%", "N/A")
    for gpu in gpu_data:
        table.add_row(f"GPU-{gpu[0]}", f"{gpu[1]}%", f"{gpu[2]}°C")

    console.print(table)
