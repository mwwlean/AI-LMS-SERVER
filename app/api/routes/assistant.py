from fastapi import APIRouter, Depends

from app.api.dependencies import get_db
from app.schemas.assistant import AssistantRequest, AssistantResponse
from app.services.ai_assistant_service import AIAssistantService

router = APIRouter(prefix="/assistant", tags=["assistant"])


@router.post("/chat", response_model=AssistantResponse)
async def ask_assistant(payload: AssistantRequest, db=Depends(get_db)):
    service = AIAssistantService(db)
    return await service.handle_query(payload.query.strip())