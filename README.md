# Phase2-FastAPI
Phase 2 — FastAPI backend development with async, Redis caching, Celery task queues, and PostgreSQL integration for AI applications.

# Phase 2 — FastAPI + Redis + Async + Celery

Part of my AI Field Developer Engineer (FDE) learning roadmap.

## What this phase covers
- FastAPI — building production-ready API backends
- Pydantic — request and response validation
- Async/await — non-blocking API endpoints
- Redis — response caching and session management
- Celery — background task queues for long-running AI jobs
- PostgreSQL integration — connecting Phase 1 SQL knowledge to APIs
- Deployment — live URL on Railway

## Projects
- Easy: GitHub Profile API with Redis caching
- Medium: Multi-Source Data Aggregator with async
- Hard: Webhook Receiver + Celery Background Processor

## Stack
Python, FastAPI, Uvicorn, Redis, Celery, PostgreSQL, SQLAlchemy, Pydantic, Railway

## How to run
1. Clone the repo
2. Create .env file with credentials
3. Install dependencies: pip install -r requirements.txt
4. Run: uvicorn main:app --reload