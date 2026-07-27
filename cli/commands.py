import typer
import os
from core.logger import log_info, log_success, log_error, log_warning
from core.engine import run_audit, check_ollama_health

app = typer.Typer(help="Aegis Audit CLI")

@app.command("analyze")
def analyze(target: str = typer.Option(..., "--target", "-t", help="Alvo da auditoria"),
            model: str = typer.Option("llama3:latest", "--model", "-m", help="Modelo Ollama")):
    """Inicia a auditoria completa com agentes LLM"""
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    log_info(f"Iniciando analise no alvo: {target}")
    run_audit(target, model, base_url)

@app.command("doctor")
def doctor():
    """Verifica a saude do sistema e dependencias"""
    log_info("Executando diagnostico do sistema...")
    
    # Check Python
    import sys
    log_success(f"Python Version: {sys.version.split()[0]}")
    
    # Check Ollama
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    log_info(f"Verificando Ollama em {base_url}...")
    if check_ollama_health(base_url):
        log_success("Ollama esta online e respondendo.")
    else:
        log_warning("Ollama nao detectado. Verifique se o servico esta rodando.")
        
    # Check Dirs
    if os.path.exists("reports"):
        log_success("Diretorio 'reports' verificado.")
    else:
        log_warning("Diretorio 'reports' ausente. Sera criado em tempo de execucao.")
        
    log_success("Diagnostico concluido.")
