Enterprise RAG Assistant
=======================

Enterprise-grade RAG-based assistant template using Python + FastAPI.

Description
- Developed enterprise-grade RAG-based assistant using vector search and hybrid retrieval pipelines.
- Built scalable backend services for LLM-powered applications using Python and FastAPI.
- Containerized AI services and deployed using Kubernetes and automated CI/CD pipelines.
- Optimized retrieval and inference pipelines to improve performance and reduce operational costs.
- Collaborated with cross-functional teams to deploy and monitor AI systems in production.

Repository name recommendation
- Primary (recommended): enterprise-rag-assistant
- Alternatives: rag-assistant-template, rag-backend-template

Quickstart
- Build and run locally:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- Health check: GET /health
- Query endpoint: POST /query {"question": "..."}

Notes
- The `app` contains a minimal FastAPI stub. Implement vector DB, retriever, and LLM inference in `app/services/`.
- CI/workflow and Kubernetes manifests are included as starting points.
