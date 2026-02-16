FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install --no-cache-dir poetry   

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]