from pydantic import BaseModel


class AssistantRequest(BaseModel):
    query: str


class AssistantResponse(BaseModel):
    response: str
    matches: list[str]