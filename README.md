# AI Incident Commander 🤖🚨

A local-first, AI-powered incident response orchestration system.

<img width="1533" height="361" alt="aicommander" src="https://github.com/user-attachments/assets/6cc64c2e-6d61-4203-a988-1fc6ff65c1c2" />


## Features
- **Local LLM**: Powered by Ollama (llama3.2).
- **Orchestration**: n8n visual workflows.
- **Mock Environment**: Simulated microservices and alerts via FastAPI.
- **Log Analysis**: Synthetic log generation for realistic triage scenarios.
- **Privacy First**: Everything runs in Docker on your local machine. No cloud APIs.

## Architecture
1. **n8n**: The brain. Orchestrates the workflow.
2. **Ollama**: The intelligence. Analyzes logs and runbooks.
3. **Mock API**: The target. Simulates a production environment.
4. **Log Generator**: The noise. Creates synthetic logs for services.

## Quick Start
1. **Setup**:
   ```bash
   cp .env.example .env
   # Update N8N_BASIC_AUTH_USER to your email in .env
   ```
2. **Launch**:
   ```bash
   docker compose up -d
   ```
3. **Import Workflow**:
   - Open `http://localhost:5678`
   - Import `n8n/workflows/incident_commander_workflow.json`
4. **Run Analysis**:
   - Execute the workflow in n8n.
   - It will fetch alerts from `http://localhost:8000/alerts`, read local logs, and ask Ollama for a diagnosis.

## Project Structure
- `services/`: Source code for mock infrastructure.
- `data/runbooks/`: AI instructions for handling incidents.
- `data/logs/`: Live generated logs (mounted into containers).
- `n8n/workflows/`: Exported workflow files.

## Safety Note
This system only performs actions against the internal **Mock API**. It will never affect your real infrastructure.
