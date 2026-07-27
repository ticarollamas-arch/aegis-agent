import os
import time
import json
import requests
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from core.logger import log_info, log_success, log_warning, log_error

NOMES_AGENTES = [
    ("Reconhecimento Web", "Mapeia tecnologias e estrutura"),
    ("Headers de Seguranca", "Analisa headers HTTP"),
    ("OWASP Top 10", "Verifica conformidade OWASP"),
    ("Score Seguranca", "Calcula score 0-100")
]

def check_ollama_health(base_url: str, timeout: float = 5.0) -> bool:
    try:
        response = requests.get(f"{base_url}/api/tags", timeout=timeout)
        response.raise_for_status()
        return True
    except requests.exceptions.Timeout:
        log_error(f"Tempo limite excedido ({timeout}s) ao conectar no Ollama em {base_url}")
    except requests.exceptions.ConnectionError:
        log_error(f"Falha de conexao recusada com Ollama em {base_url}. O servico esta rodando?")
    except requests.exceptions.HTTPError as http_err:
        log_error(f"Erro HTTP retornado pelo Ollama: {http_err}")
    except Exception as e:
        log_error(f"Erro inesperado ao verificar Ollama: {str(e)}")
    return False

def run_audit(target: str, model: str, base_url: str):
    if not check_ollama_health(base_url):
        return
    
    log_info(f"Inicializando LLM ({model})...")
    llm = Ollama(model=model, base_url=base_url, temperature=0.7)
    log_success("LLM configurado com sucesso.")
    
    agents = []
    tasks = []
    
    log_info("Criando esquadrao de agentes...")
    for nome, desc in NOMES_AGENTES:
        agent = Agent(
            role=f"Especialista em {nome}",
            goal=f"Analisar {desc} do target {target}",
            backstory=f"Auditor senior especializado em {nome}",
            llm=llm,
            verbose=False,
            allow_delegation=False
        )
        agents.append(agent)
        
        task = Task(
            description=f"Execute analise de {nome} para {target}",
            expected_output=f"Relatorio detalhado de {nome}",
            agent=agent
        )
        tasks.append(task)
    
    log_success(f"{len(agents)} agentes criados.")
    
    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=False
    )
    
    log_info("Iniciando auditoria sequencial...")
    start_time = time.time()
    
    try:
        result = crew.kickoff()
        elapsed = time.time() - start_time
        
        os.makedirs("reports", exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = f"reports/audit_{timestamp}.json"
        
        report_data = {
            "target": target,
            "model": model,
            "execution_time_seconds": round(elapsed, 2),
            "timestamp": datetime.now().isoformat(),
            "status": "COMPLETED"
        }
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2)
            
        log_success(f"Auditoria concluida em {elapsed:.2f}s")
        log_success(f"Relatorio salvo em: {report_path}")
        
    except Exception as e:
        log_error(f"Falha critica durante a execucao da auditoria: {str(e)}")
