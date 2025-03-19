FROM python:3.12-slim
WORKDIR /src

# install req
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["fastapi", "run", "main.py"]
