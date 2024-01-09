from fastapi import APIRouter
from src.models.user import User


router = APIRouter(prefix="/user", tags=["User"])

@router.get("/", response_model=User)
def add_user():
    return "All the user are: John, Jane, James"

