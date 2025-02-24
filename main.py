from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from rms_pdf_parser import extract_questions_from_pdf
from llm_api import generate_message

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "RSM-style Markdown Generator"})


@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are allowed!"}

    try:
        pdf_data = await file.read()
        
        questions = extract_questions_from_pdf(pdf_data)

        if not questions:
            return {"error": "No questions found in the PDF."}

        return RedirectResponse(url="/quesbox/", status_code=303)

    except Exception as e:
        return {"error": f"Failed to process PDF: {str(e)}"}

@app.post("/generate/")
async def generate(request: Request):
    data = await request.json()
    questions = data.get("questions", [])
    if not questions:
        return {"error": "No questions provided."}

    # responses = ["# sample response 1", "`test response` \n- 2"]
    responses = [f"{generate_message(q)}" for q in questions]

    return {"response": responses}