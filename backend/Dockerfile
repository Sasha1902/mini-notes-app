FROM python:3.12-slim

WORKDIR /app

# Damit Python Module in app gefunden werden
ENV PYTHONPATH=/app

# Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY app ./app

# Kommando zum Starten des Backends
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
