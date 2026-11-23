FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uv/bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN /uv/bin/uv sync --frozen --no-dev

COPY app/ ./app/

EXPOSE 5000

CMD ["uv", "run", "fastapi", "dev", "--port", "5000"]