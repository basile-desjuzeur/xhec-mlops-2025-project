
## Prerequisites
- Docker, git, Python, uv and pip available on the machine.

To install uv, run:
```
   pip install uv

## Start Prefect (orchestration)
1. Set API URL:
   uv run prefect config set PREFECT_API_URL=http://0.0.0.0:4200/api
2. Start server:
   uv run prefect server start --host 0.0.0.0
3. (Optional) Reset DB:
   uv run prefect server database reset
4. Open dashboard:
   $BROWSER http://0.0.0.0:4200/dashboard

## Start API (FastAPI)
1. Install deps:
   pip install -r requirements.txt
2. Run locally:
   uv run uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
3. API docs:
   $BROWSER http://0.0.0.0:8000/docs

## Docker (containerized deployment)
1. Build:
   docker build -t abalone-api -f docker/Dockerfile .
2. Run:
   docker run --rm -p 8000:8000 abalone-api

## Ports
- Prefect dashboard: 4200
- FastAPI: 8000
