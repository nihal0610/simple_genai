# Use official Python image as base
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
		build-essential \
		&& rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Expose ports (FastAPI: 8000, Streamlit: 8501)
EXPOSE 8000 8501

# Set environment variable to choose app ("backend" or "frontend")
ENV APP_MODE=frontend

# Default command: run backend (FastAPI) or frontend (Streamlit) based on APP_MODE
CMD if [ "$APP_MODE" = "frontend" ]; then \
		streamlit run frontend/app.py --server.port=8501; \
	else \
		uvicorn backend.main:app --host 0.0.0.0 --port 8000; \
	fi
