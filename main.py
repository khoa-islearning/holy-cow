from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fortune import get_random_fortune
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from cowsay import cowsay, read_dot_cow
import ollama
from pydantic import BaseModel
from io import StringIO
import unicodedata

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates (used for HTML rendering)
templates = Jinja2Templates(directory="templates")


# Root endpoint that serves the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/fortune")
async def random():
    fortune = get_random_fortune("./fortunes")
    msg = cowsay(fortune)
    return {"fortune": msg, "raw": fortune}


class ConvoRequest(BaseModel):
    msg: str


class ConvoResponse(BaseModel):
    response: str


@app.post("/response", response_model=ConvoResponse)
async def response(request: ConvoRequest):
    msg = (
        "response to this message, be short (less than 15 words), witty and serious, dont use icon and use full-width character: "
        + request.msg
    )
    # print(msg)

    cow = read_dot_cow(
        StringIO(
            """
$the_cow = <<"EOC";
                    ^__^    /
            _______/($eyes)   /
        /\\/(       /(__)
           ||w----[|
           ||     ||
EOC
"""
        )
    )

    response = ollama.chat(
        model="llama3.2:1b", messages=[{"role": "user", "content": msg}]
    )
    clean_msg = unicodedata.normalize(
        "NFKC", response["message"]["content"].replace('"', "")
    )
    # print(repr(clean_msg))
    response = cowsay(clean_msg, cowfile=cow)
    return {"response": response}
