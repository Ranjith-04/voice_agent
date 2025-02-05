from fastapi import APIRouter, Body
from app.services.openai_chatgpt import ChatGPTService

router = APIRouter()
chatgpt_service = ChatGPTService(api_key="your-portkey-api-key")

@router.post("/generate-response/")
async def generate_response(prompt: str = Body(..., embed=True)):
    response = chatgpt_service.generate_response(prompt)
    return {"response": response}