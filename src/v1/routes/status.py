from fastapi import APIRouter
from pydantic import BaseModel

from src.v1.selectors import get_current_status

router = APIRouter()


class Status(BaseModel):
    app: str
    db: str
    auth: str


@router.get('/v1/status', tags=['status'], response_model=Status)
async def read_status():
    return get_current_status()
