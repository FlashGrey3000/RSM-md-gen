from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from llm_api import generate_message

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Groq Markdown Generator"})

@app.get("/generate")
async def generate():
    response = generate_message("quicksort")
    return {"response": response}
