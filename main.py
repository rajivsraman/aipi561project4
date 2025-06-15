from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bedrock_client import generate_text
from filter import is_safe
from monitor import log_usage

app = FastAPI(title="AWS Text Generation API")

class PromptRequest(BaseModel):
    prompt: str
    user: str = "anonymous"

@app.post("/generate")
def generate(request: PromptRequest):
    if not is_safe(request.prompt):
        raise HTTPException(status_code=400, detail="Inappropriate content detected.")
    try:
        response = generate_text(request.prompt)
        log_usage(request.prompt, request.user, response)
        return {"output": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation error: {e}")
