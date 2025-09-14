# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copiar dependências e instalar
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o projeto
COPY . /app

# Porta que o Flask vai usar
EXPOSE 5002

# Rodar app.py
CMD ["python", "app.py"]
