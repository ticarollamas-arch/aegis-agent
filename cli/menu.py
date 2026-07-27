#!/usr/bin/env python3
import os
from colorama import Fore, Style
from core.logger import AegisLogger
from core.engine import run_audit, check_ollama_health

def show_menu():
    while True:
        print(Fore.CYAN + "\n╔══════════════════════════════════╗")
        print("║         AEGIS FRAMEWORK          ║")
        print("║     Enterprise CLI Platform      ║")
        print("╚══════════════════════════════════╝" + Style.RESET_ALL)
        print(" [1] Recon (Reconhecimento)")
        print(" [2] Enum (Mapeamento)")
        print(" [3] Crawl (Crawler)")
        print(" [4] Analyze (Auditoria 30 Agentes LLM)")
        print(" [5] Report (Exportar)")
        print(" [6] Doctor (Health Check)")
        print(" [7] Sair\n")
        
        choice = input(Fore.YELLOW + "aegis> " + Style.RESET_ALL)
        
        if choice == '4':
            target = input(Fore.YELLOW + "Informe o Target (ex: https://example.com): " + Style.RESET_ALL)
            if target:
                run_audit(target)
            else:
                AegisLogger.warning("Target inválido.")
        elif choice == '6':
            AegisLogger.info("Executando diagnóstico do sistema...")
            models = check_ollama_health()
            if models:
                AegisLogger.success(f"Ollama OK. Modelos disponíveis: {', '.join(models)}")
            else:
                AegisLogger.error("Ollama indisponível. Verifique o serviço.")
        elif choice == '7':
            AegisLogger.info("Encerrando Aegis Framework...")
            break
        else:
            AegisLogger.warning("Módulo em desenvolvimento ou opção inválida.")
