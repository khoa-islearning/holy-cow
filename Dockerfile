FROM python:3.12-slim
WORKDIR /src

# Install system dependencies
RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pull the Mistral model
RUN ollama serve & sleep 5 && ollama pull mistral 

# install req
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ollama serve & fastapi run main.py
