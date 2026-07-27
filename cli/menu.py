from rich.prompt import Prompt
from rich.console import Console
from cli.banner import show_banner
from cli.commands import analyze, doctor
from core.logger import log_info, log_warning
import sys

console = Console()

def interactive_menu():
    show_banner()
    while True:
        console.print("\n[bold cyan]TOOLBOX MENU[/bold cyan]")
        console.print("  [1] Recon (Reconhecimento de hosts)")
        console.print("  [2] Enum (Mapeamento de servicos)")
        console.print("  [3] Crawl (Crawler assincrono)")
        console.print("  [4] Analyze (Auditoria LLM Completa)")
        console.print("  [5] Report (Exportar relatorios)")
        console.print("  [6] Doctor (Health Check)")
        console.print("  [7] Sair")
        
        choice = Prompt.ask("\n[bold white]Selecione uma opcao[/bold white]", choices=["1", "2", "3", "4", "5", "6", "7"])
        
        if choice == "1":
            log_warning("Modulo Recon em desenvolvimento (Plugin Architecture).")
        elif choice == "2":
            log_warning("Modulo Enum em desenvolvimento (Plugin Architecture).")
        elif choice == "3":
            log_warning("Modulo Crawl em desenvolvimento (Plugin Architecture).")
        elif choice == "4":
            target = Prompt.ask("[bold white]Digite o Target (ex: https://example.com)[/bold white]")
            analyze(target=target)
        elif choice == "5":
            log_info("Verifique a pasta 'reports/' para os JSONs gerados.")
        elif choice == "6":
            doctor()
        elif choice == "7":
            log_info("Encerrando Aegis CLI. Ate logo!")
            sys.exit(0)
