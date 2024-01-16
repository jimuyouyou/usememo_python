# Dockerfile
FROM python:3.8

WORKDIR /app

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg vim
    
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
