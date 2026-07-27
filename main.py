#!/usr/bin/env python3
import argparse
from cli.menu import show_menu
from core.engine import run_audit
from core.logger import AegisLogger

def main():
    parser = argparse.ArgumentParser(description="Aegis-Audit: Enterprise Security CLI")
    parser.add_argument("--target", "-t", help="URL alvo para execução direta")
    parser.add_argument("--verbose", "-v", action="store_true", help="Modo verboso")
    args = parser.parse_args()

    try:
        if args.target:
            AegisLogger.info(f"Iniciando execução direta para o alvo: {args.target}")
            run_audit(args.target, args.verbose)
        else:
            show_menu()
    except KeyboardInterrupt:
        print("\n")
        AegisLogger.warning("Processo interrompido pelo usuário.")
    except Exception as e:
        AegisLogger.error(f"Falha fatal: {str(e)}")

if __name__ == "__main__":
    main()
