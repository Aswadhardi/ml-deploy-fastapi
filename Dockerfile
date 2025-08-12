FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install dependencies
RUN pip install --no-cache-dir uvicorn fastapi pandas scikit-learn

WORKDIR /app


ENV PATH="/app/.venv/bin:$PATH"


COPY ".python-version" "pyproject.toml" "uv.lock" "./"

RUN uv sync --locked


COPY "predict.py" "model.bin" "./"

EXPOSE 8000 

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]
