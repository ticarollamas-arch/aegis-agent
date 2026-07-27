# 🚀 Guia Rápido: Ativando CrewAI + Ollama no Termux

Guia completo para reativar sua ferramenta de auditoria com 30 agentes CrewAI + Ollama no Termux.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- ✅ Termux instalado
- ✅ Python 3.10+ instalado
- ✅ CrewAI instalado no ambiente virtual
- ✅ Ollama instalado

---

## 🔧 PASSO 1: ATIVAR O AMBIENTE VIRTUAL

```bash
# Ativar o ambiente virtual
source ~/crewai-env/bin/activate

# Verificar se está ativado (deve mostrar (crewai-env) no prompt)
which python

# Verificar versão do Python
python --version
```

---

## 🔧 PASSO 2: VERIFICAR OLLAMA

```bash
# Verificar se Ollama está rodando
curl http://localhost:11434/api/tags

# Se não estiver rodando, iniciar em background
ollama serve > /dev/null 2>&1 &

# Aguardar iniciar
sleep 3

# Verificar novamente
curl http://localhost:11434/api/tags

# Listar modelos disponíveis
ollama list
```

---

## 🔧 PASSO 3: VERIFICAR ARQUIVOS DO PROJETO

```bash
# Entrar no diretório do projeto
cd ~/30agents-crewai

# Verificar se o script principal existe
ls -la main_olluna.py

# Se não existir, criar o arquivo (ver seção "Criando o Script")
```

---

## 🚀 PASSO 4: EXECUTAR A FERRAMENTA

```bash
# Executar com target específico
python main_olluna.py --target https://ifood.com.br --model llama3.2:latest --verbose

# Ou com target de exemplo
python main_olluna.py --target https://example.com --model llama3.2:latest --verbose
```

---

## 🔧 COMANDO COMPLETO EM UMA LINHA

```bash
source ~/crewai-env/bin/activate && ollama serve > /dev/null 2>&1 & && sleep 3 && cd ~/30agents-crewai && python main_olluna.py --target https://ifood.com.br --model llama3.2:latest --verbose
```

---

## ✅ VERIFICAÇÃO RÁPIDA (TUDO DE UMA VEZ)

```bash
# Verificar tudo de uma vez
source ~/crewai-env/bin/activate
pip list | grep crewai
ollama list
python main_olluna.py --target https://example.com --verbose
```

---

## 📁 CRIANDO O SCRIPT PRINCIPAL

Se o arquivo `main_olluna.py` não existir, crie-o com o comando abaixo:

```bash
cat > main_olluna.py << 'EOF'
# Conteúdo completo do script aqui
EOF
```

---

## 🎯 EXEMPLO DE SAÍDA ESPERADA

```
╔══════════════════════════════════════════════════════════════════╗
║  ██████╗ ██╗     ██╗   ██╗███╗   ██╗                          ║
║  ██╔══██╗██║     ██║   ██║████╗  ██║                          ║
║  ██████╔╝██║     ██║   ██║██╔██╗ ██║                          ║
║  ██╔═══╝ ██║     ██║   ██║██║╚██╗██║                          ║
║  ██║     ███████╗╚██████╔╝██║ ╚████║                          ║
║  ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝                          ║
╠══════════════════════════════════════════════════════════════════╣
║                   v3.0 - 30 SECURITY AGENTS                    ║
║                                                                  ║
║  TARGET  https://ifood.com.br                                    ║
║  MODEL   llama3.2:latest                                         ║
║  AGENTS  30 SPECIALISTS                                          ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🐛 SOLUÇÃO DE PROBLEMAS

### Erro: "ModuleNotFoundError: No module named 'crewai'"

```bash
# Instalar CrewAI novamente
source ~/crewai-env/bin/activate
pip install crewai crewai-tools
```

### Erro: "Ollama não está rodando"

```bash
# Iniciar Ollama
ollama serve > /dev/null 2>&1 &

# Verificar
curl http://localhost:11434/api/tags
```

### Erro: "Modelo não encontrado"

```bash
# Baixar modelo
ollama pull llama3.2
ollama pull mistral
```

---

## 📊 ESTRUTURA DO PROJETO

```
~/30agents-crewai/
├── main_olluna.py          # Script principal
├── reports/                # Relatórios gerados
│   └── report_*.json
├── crewai-env/             # Ambiente virtual
└── README.md               # Documentação
```

---

## 📝 NOTAS IMPORTANTES

- ⚠️ A auditoria é **apenas para fins educacionais e autorizados**
- ✅ Use apenas em domínios que você tem permissão para testar
- 🔒 Respeite as políticas de bug bounty e termos de serviço

---

**Pronto! Sua ferramenta está ativa novamente!** 🚀

---

## 🔗 LINKS ÚTEIS

- [Documentação CrewAI](https://docs.crewai.com/)
- [Documentação Ollama](https://ollama.com/)
- [Google VRP](https://bugbounty.google.com/)
