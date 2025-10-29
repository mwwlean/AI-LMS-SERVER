from fastapi import APIRouter, Depends
from markdown import markdown
from pydantic import BaseModel

from app.api.dependencies import get_db
from app.schemas.assistant import AssistantRequest, AssistantResponse
from app.services.ai_assistant_service import AIAssistantService

router = APIRouter(prefix="/assistant", tags=["assistant"])


class AssistantResponse(BaseModel):
    response: str
    response_html: str
    matches: list[str]


@router.post("/chat", response_model=AssistantResponse)
async def ask_assistant(payload: AssistantRequest, db=Depends(get_db)):
    service = AIAssistantService(db)
    result = await service.handle_query(payload.query.strip())
    
    # Generate HTML response with book table if books are found
    html_response = service.format_html_response(result["response"], result["books"])
    
    return {
        "response": result["response"],
        "response_html": html_response,
        "matches": result["matches"],
    }