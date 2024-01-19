from fastapi import APIRouter
from .schemas import CreateUser
from . import crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/users/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)