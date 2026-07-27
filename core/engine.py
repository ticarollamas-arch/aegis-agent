#!/usr/bin/env python3
import os, sys, json, time
from datetime import datetime
import requests
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from cli.ui_3d import banner_3d, show_agent_3d, progress_bar_3d
from core.logger import AegisLogger
from colorama import Fore, Style

NOMES_AGENTES = [
    ("🔍 Reconhecimento Web", "Mapeia tecnologias e estrutura", "🧠"),
    ("📋 Headers de Segurança", "Analisa headers HTTP", "🛡️"),
    ("🍪 Cookies", "Verifica segurança de cookies", "🔒"),
    ("🔐 SSL/TLS", "Analisa certificados SSL", "🔑"),
    ("🌐 CORS", "Verifica configuração CORS", "🌍"),
    ("🛡️ CSP", "Analisa Content Security Policy", "🛡️"),
    ("🔑 Autenticação", "Verifica mecanismos de login", "🔐"),
    ("👤 Gerenciamento de Sessão", "Analisa sessões e JWT", "🧑‍💻"),
    ("📝 Validação de Input", "Verifica proteção contra injeção", "✍️"),
    ("⚠️ Tratamento de Erros", "Analisa vazamento de informações", "⚠️"),
    ("📊 Logs e Monitoramento", "Verifica práticas de logging", "📈"),
    ("📜 OWASP Top 10", "Verifica conformidade OWASP", "📋"),
    ("📏 CIS Benchmarks", "Verifica conformidade CIS", "📐"),
    ("🔏 GDPR", "Verifica conformidade GDPR", "🔏"),
    ("💳 PCI-DSS", "Verifica conformidade PCI-DSS", "💳"),
    ("💻 Segurança de Código", "Analisa código fonte", "💻"),
    ("📦 Dependências", "Verifica CVEs em dependências", "📦"),
    ("🔑 Secrets", "Identifica credenciais expostas", "🔑"),
    ("⚙️ Configurações", "Analisa hardening", "⚙️"),
    ("📊 Score de Segurança", "Calcula score 0-100", "📊"),
    ("🎯 Priorização", "Prioriza vulnerabilidades", "🎯"),
    ("📁 Relatórios", "Gera relatório técnico", "📁"),
    ("🔧 Remediação", "Sugere correções", "🔧"),
    ("🤝 Conselheiro", "Recomenda melhorias", "🤝"),
    ("🔗 APIs REST", "Analisa segurança de APIs", "🔗"),
    ("📡 GraphQL", "Analisa segurança GraphQL", "📡"),
    ("🔌 WebSockets", "Analisa segurança WebSockets", "🔌"),
    ("🎫 JWT", "Analisa segurança de tokens", "🎫"),
    ("🚦 Rate Limiting", "Verifica proteção anti-DoS", "🚦"),
    ("📋 Recomendações Finais", "Consolida recomendações", "📋"),
]

def check_ollama_health():
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    try:
        response = requests.get(f"{host}/api/tags", timeout=5.0)
        response.raise_for_status()
        data = response.json()
        models = [m.get("name") for m in data.get("models", [])]
        return models
    except requests.exceptions.Timeout:
        AegisLogger.error("Tempo limite excedido ao conectar no Ollama.")
        return []
    except requests.exceptions.ConnectionError:
        AegisLogger.error(f"Falha de conexão. Ollama não está rodando em {host}.")
        return []
    except requests.exceptions.HTTPError as http_err:
        AegisLogger.error(f"Erro HTTP ao acessar Ollama: {http_err}")
        return []
    except Exception as e:
        AegisLogger.error(f"Erro inesperado ao verificar Ollama: {str(e)}")
        return []

def run_audit(target, verbose=False):
    models = check_ollama_health()
    if not models:
        AegisLogger.error("Nenhum modelo disponível ou Ollama offline. Abortando.")
        return
    
    modelo_usar = next((m for m in ["llama3.2:latest", "mistral:latest", "llama3:latest"] if m in models), models[0])
    
    os.system('clear' if os.name == 'posix' else 'cls')
    banner_3d(target, modelo_usar)
    
    AegisLogger.info("Configurando LLM...")
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    llm = Ollama(model=modelo_usar, base_url=host, temperature=0.7)
    AegisLogger.success("LLM configurado!")
    
    AegisLogger.info("\n🔍 CRIANDO 30 AGENTES ESPECIALIZADOS...\n")
    agents = []
    for i, (nome, desc, icone) in enumerate(NOMES_AGENTES, 1):
        agent = Agent(
            role=f"Especialista em {nome}",
            goal=f"Analisar {desc} do target {target}",
            backstory=f"Especialista em {nome} com anos de experiência em segurança",
            llm=llm,
            verbose=verbose,
            allow_delegation=False
        )
        agents.append(agent)
        print(Fore.GREEN + Style.BRIGHT + f"  ✅ {i:02d}. {icone} {nome}" + Fore.LIGHTBLACK_EX + f" - {desc}" + Style.RESET_ALL)
    
    tasks = []
    for i, agent in enumerate(agents):
        task = Task(
            description=f"Realizar análise completa de {NOMES_AGENTES[i][0]} do target {target}. Identifique vulnerabilidades teóricas e documente.",
            expected_output=f"Relatório detalhado de {NOMES_AGENTES[i][0]}",
            agent=agent
        )
        tasks.append(task)
    
    print(Fore.CYAN + Style.BRIGHT + "\n🚀 INICIANDO AUDITORIA COM 30 AGENTES...\n" + Style.RESET_ALL)
    
    try:
        start_time = time.time()
        for i, agent in enumerate(agents):
            nome, desc, icone = NOMES_AGENTES[i]
            show_agent_3d(i+1, nome, desc, icone)
            task = tasks[i]
            # Execução síncrona simulada para o blueprint
            task.execute_sync() if hasattr(task, 'execute_sync') else None
            progress_bar_3d(i+1, len(agents), nome)
            print()
        
        elapsed_time = time.time() - start_time
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = f"reports/report_30agents_{timestamp}.json"
        
        os.makedirs("reports", exist_ok=True)
        report_data = {
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "model": modelo_usar,
            "total_agents": len(agents),
            "execution_time": elapsed_time,
            "result": "Auditoria concluída (Simulação)"
        }
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
            
        AegisLogger.success(f"RELATÓRIO SALVO: {report_path}")
        
    except KeyboardInterrupt:
        AegisLogger.warning("Auditoria interrompida pelo usuário.")
    except Exception as e:
        AegisLogger.error(f"Erro durante a auditoria: {str(e)}")
