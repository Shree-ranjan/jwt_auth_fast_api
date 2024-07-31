from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from core.database import get_db
from users.schemas import CreateUserRequest
from users.services import create_user_account
from core.security import oauth2_scheme
from users.responses import UserResponse;

router = APIRouter(
    prefix="/api/v1",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.post('/register-user', status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    await create_user_account(data=data, db=db)
    payload = {"message": "User account has been succesfully created."}
    return JSONResponse(content=payload)


@router.get('/me', status_code=status.HTTP_200_OK, response_model=UserResponse, dependencies=[Depends(oauth2_scheme)])
def get_user_detail(request: Request):
    return request.user