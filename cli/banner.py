from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_banner():
    banner_text = """
   █████╗ ███████╗ ██████╗ ██╗███████╗
  ██╔══██╗██╔════╝██╔════╝ ██║██╔════╝
  ███████║█████╗  ██║  ███╗██║███████╗
  ██╔══██║██╔══╝  ██║   ██║██║╚════██║
  ██║  ██║███████╗╚██████╔╝██║███████║
  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝
    """
    text = Text(banner_text, style="cyan bold", justify="center")
    text.append("\nEnterprise Security AI Agents\n", style="white bold")
    text.append("Version: 1.0.0 | Status: Ready", style="green")
    
    panel = Panel(text, border_style="cyan", padding=(1, 2))
    console.print(panel)
