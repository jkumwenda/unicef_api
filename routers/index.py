from fastapi import APIRouter
from schemas.schemas import WelcomeSchema

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def index():
    return {"welcome": "Hello world, this is API feedback"}
