#!/usr/bin/env python3
from colorama import Fore, Style

def banner_3d(target, model):
    print(Fore.CYAN + Style.BRIGHT + """
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║     """ + Fore.YELLOW + Style.BRIGHT + "██████╗ ███████╗ ██████╗ ██╗███████╗" + Fore.CYAN + Style.BRIGHT + """       ║
    ║     """ + Fore.YELLOW + Style.BRIGHT + "██╔══██╗██╔════╝██╔════╝ ██║██╔════╝" + Fore.CYAN + Style.BRIGHT + """       ║
    ║     """ + Fore.YELLOW + Style.BRIGHT + "██████╔╝█████╗  ██║  ███╗██║███████╗" + Fore.CYAN + Style.BRIGHT + """       ║
    ║     """ + Fore.YELLOW + Style.BRIGHT + "██╔══██╗██╔══╝  ██║   ██║██║╚════██║" + Fore.CYAN + Style.BRIGHT + """       ║
    ║     """ + Fore.YELLOW + Style.BRIGHT + "██████╔╝███████╗╚██████╔╝██║███████║" + Fore.CYAN + Style.BRIGHT + """       ║
    ║     """ + Fore.YELLOW + Style.BRIGHT + "╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚══════╝" + Fore.CYAN + Style.BRIGHT + """       ║
    ║                                                                      ║
    ║     """ + Fore.MAGENTA + Style.BRIGHT + "   🛡️  AUDITORIA DE SEGURANÇA - 30 AGENTES  🛡️" + Fore.CYAN + Style.BRIGHT + """      ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """ + Style.RESET_ALL)
    
    if target:
        print(Fore.GREEN + Style.BRIGHT + "    🎯 Target:" + Fore.WHITE + f" {target}")
        print(Fore.GREEN + Style.BRIGHT + "    🧠 Model:" + Fore.WHITE + f" {model}")
        print(Fore.GREEN + Style.BRIGHT + "    🤖 Agents:" + Fore.WHITE + " 30 ESPECIALISTAS")
        print(Fore.CYAN + "═" * 70 + Style.RESET_ALL)

def show_agent_3d(agent_num, nome, descricao, icone):
    cores = [Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.BLUE]
    cor = cores[agent_num % len(cores)]
    print(Fore.YELLOW + Style.BRIGHT + "╔" + "═" * 68 + "╗" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "║" + Fore.WHITE + Style.BRIGHT + f"  AGENTE #{agent_num:02d} ".ljust(68) + Fore.YELLOW + Style.BRIGHT + "║")
    print(Fore.YELLOW + Style.BRIGHT + "╠" + "═" * 68 + "╣" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "║" + cor + Style.BRIGHT + f"  {icone} {nome}".ljust(68) + Fore.YELLOW + Style.BRIGHT + "║")
    print(Fore.YELLOW + Style.BRIGHT + "║" + Fore.LIGHTBLACK_EX + f"  📝 {descricao}".ljust(68) + Fore.YELLOW + Style.BRIGHT + "║")
    print(Fore.YELLOW + Style.BRIGHT + "║" + Fore.GREEN + Style.BRIGHT + "  ⏳ PROCESSANDO...".ljust(68) + Fore.YELLOW + Style.BRIGHT + "║")
    print(Fore.YELLOW + Style.BRIGHT + "╚" + "═" * 68 + "╝" + Style.RESET_ALL)
    print()

def progress_bar_3d(current, total, agent_name):
    percent = (current / total) * 100
    bar_width = 40
    filled = int(percent / 100 * bar_width)
    empty = bar_width - filled
    bar = Fore.GREEN + "█" * filled + Fore.LIGHTBLACK_EX + "░" * empty
    print(Fore.CYAN + Style.BRIGHT + "\n" + "═" * 70)
    print(Fore.YELLOW + Style.BRIGHT + f"  📊 PROGRESSO: {current}/{total} AGENTES".ljust(70))
    print(Fore.CYAN + "═" * 70)
    print(Fore.WHITE + f"  {bar}  {percent:.1f}%")
    print(Fore.LIGHTBLACK_EX + f"  🎯 Atual: {agent_name[:40]}")
    print(Fore.CYAN + "═" * 70 + Style.RESET_ALL)
