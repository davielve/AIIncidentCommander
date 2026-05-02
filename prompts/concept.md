Instrukser: Fra næste linje kommer prompten du skal arbejde på, den er på engelsk for at du bedre forstår den. Men vi skal kommunikere på dansk.

You are a senior full-stack, DevOps, and AI automation engineer.

Build a complete local-first project called:

AI Incident Commander

Goal:
Create a fully local, dockerized, open-source AI agent system for incident triage and response orchestration.
The system must use n8n as the orchestration layer and visual workflow canvas, Ollama as the local LLM runtime, and only open-source tools that can run locally in Docker.
The project must look impressive in n8n screenshots and demos.
It must not depend on any paid APIs, cloud AI services, or external SaaS accounts.
It must be safe by design: no real destructive remediation, only simulated remediation actions in a local mock environment.

Core product concept:
An operator triggers an incident analysis.
The system collects local logs, synthetic alerts, service status, and runbook data.
An AI agent analyzes the incident, classifies severity, proposes likely root cause, suggests next actions, and drafts a postmortem.
Any remediation tool that changes state must require explicit human approval before execution.
All outputs stay local.

==================================================
HIGH-LEVEL REQUIREMENTS
==================================================

Build a complete project repository with all source files.

Use:
- n8n for orchestration and AI agent workflow
- Ollama for local LLM inference
- Docker Compose for local deployment
- Only open-source software
- Local-only networking
- No cloud dependencies
- No scraping of external websites
- No personal data required
- Synthetic data and mock systems only

The final project must include:
1. docker-compose.yml
2. .env.example
3. README.md
4. A project folder structure that is clean and production-like
5. One or more n8n workflow JSON exports ready to import
6. A local mock incident simulator service
7. A local synthetic log/alert generator
8. Local runbook documents in markdown
9. A simple storage approach for reports and artifacts on disk
10. Scripts or Make targets for easy startup
11. Clear demo instructions
12. Seed/sample incidents for testing
13. Updated and top notch README.md file

==================================================
ARCHITECTURE
==================================================

Build the system with these services in Docker Compose:

1. n8n
- Main orchestration UI
- Expose on port 5678
- Persist n8n data in a volume
- Basic auth enabled via environment variables
- Use mounted local workflow JSON files and docs

2. Ollama
- Local LLM runtime
- Expose port 11434
- Persistent model storage
- Use a configurable model via env var OLLAMA_MODEL
- Default to a small model that can realistically run locally, e.g. llama3.2 or another lightweight instruct model available in Ollama
- Prefer direct HTTP API integration from n8n rather than any cloud credential flow

3. Mock Incident API service
- Build a small Python FastAPI app
- Expose a local API with endpoints such as:
  - GET /health
  - GET /services
  - GET /alerts
  - GET /incidents
  - GET /logs/{service}
  - POST /simulate/restart-service
  - POST /simulate/clear-queue
  - POST /simulate/rollback-release
  - POST /simulate/toggle-maintenance
- These actions must be simulated and safe
- Keep in-memory or file-based state
- Include seeded incidents and service metadata
- Include realistic fake alerts and logs

4. Synthetic Log Generator
- A lightweight local service or script that continuously writes realistic logs/events for a few fake microservices
- Example services:
  - api-gateway
  - payments-service
  - auth-service
  - notification-service
  - postgres
- Simulate common failures:
  - high error rates
  - timeout spikes
  - DB connection pool exhaustion
  - 502 upstream failures
  - queue backlog
  - memory pressure
  - failed deployment
- The generator must support switching scenarios via env vars or local files

5. Optional observability stack (recommended)
- Add Grafana Loki for local log aggregation if it keeps the project manageable
- If Loki is added, also include Promtail or a simple compatible log shipping path
- If this adds too much complexity, use the mock API and mounted log files as the source of truth instead
- Keep the system simple enough to run reliably 