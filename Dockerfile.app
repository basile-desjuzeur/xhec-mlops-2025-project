FROM python:3.11.6-slim

WORKDIR /web_service

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uv

COPY pyproject.toml uv.lock ./

RUN /uv sync --locked

COPY . .

RUN chmod +x /web_service/bin/run_services.sh

EXPOSE 8001
EXPOSE 4201

CMD ["bash", "-c", "source /web_service/.venv/bin/activate && /web_service/bin/run_services.sh"]

