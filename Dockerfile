FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /uvx /bin/

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Compile bytecode
ENV UV_COMPILE_BYTECODE=1

# uv Cache
ENV UV_LINK_MODE=copy

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

ENV PYTHONPATH=/app

COPY ./scripts /app/scripts
COPY ./pyproject.toml ./uv.lock ./alembic.ini /app/
COPY ./app /app/app
COPY ./tests /app/tests

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync

# --- FIX IS HERE ---
# 1. Added --host 0.0.0.0 (Crucial for Cloud Run ingress)
# 2. Removed --workers 4 (Prevents memory/startup crashes on default Cloud Run instances)
# 3. Kept port logic to listen on GCP's injected PORT (usually 8080)
CMD ["sh", "-c", "fastapi run app/main.py --host 0.0.0.0 --port ${PORT:-8080}"]