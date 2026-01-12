FROM python:3.12-alpine

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything
COPY . .

# PYTHONPATH auf /app setzen, damit 'app' gefunden wird
ENV PYTHONPATH=/app

# Expose backend port
EXPOSE 8000

# Start FastAPI über uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
