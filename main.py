#!/usr/bin/env python3
import sys
from cli.menu import interactive_menu
from cli.commands import app

if __name__ == "__main__":
    try:
        # Se argumentos foram passados, usa o Typer CLI
        if len(sys.argv) > 1:
            app()
        # Sendo executado sem argumentos, abre o menu interativo
        else:
            interactive_menu()
    except KeyboardInterrupt:
        print("\n[-] Interrompido pelo usuario. Saindo...")
        sys.exit(1)
    except Exception as e:
        print(f"\n[-] Erro fatal: {str(e)}")
        sys.exit(1)
