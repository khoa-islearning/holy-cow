# Holy Cow
A cow fortune-teller app, build to learn abit about fastapi

![screenshot](./screenshot.png)

## Using Docker
```sh
docker compose build
docker compose run
```

## Normal
```
python -m venv venv
source venv/bin/activate
pip install -r requirements
fastapi run main.py 
```

Also checkout the `responsive` version for AI response with ollama (not dockerized).

```
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
fastapi run main.py

```
![screenshot](./responsive.png)
