#!/usr/bin/env python3
import sys
from colorama import Fore, Style, init

init(autoreset=True)

class AegisLogger:
    @staticmethod
    def info(msg):
        print(f"{Fore.CYAN}[+] {Style.RESET_ALL}{msg}")

    @staticmethod
    def success(msg):
        print(f"{Fore.GREEN}[✓] {Style.RESET_ALL}{msg}")

    @staticmethod
    def warning(msg):
        print(f"{Fore.YELLOW}[!] {Style.RESET_ALL}{msg}")

    @staticmethod
    def error(msg):
        print(f"{Fore.RED}[-] {Style.RESET_ALL}{msg}")
