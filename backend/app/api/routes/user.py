import os
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models.user import User, NewUser
from app.errors.db import Missing, Duplicate

if os.getenv("UNIT_TEST"):
    from app.fake import user as service
else:
    from app.service import user as service


ACCESS_TOKEN_EXPIRE_MINUTES = 30
router = APIRouter(prefix="/user")

oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")


def unauthed():
    raise HTTPException(
        status_code=401,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.post("/token")
async def create_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> dict:
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthed()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user.username}, expires=expires
    )
    response = {"access_token": access_token, "token_type": "Bearer"}
    return response


@router.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    response = {"access_token": token}
    return response


@router.get("/")
def get_all() -> list[User]:
    return service.get_all()


@router.get("/{id}")
def get_one(id: int) -> User:
    try:
        return service.get_one(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("/", status_code=201)
def create(user: NewUser) -> User:
    try:
        return service.create(user)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)


@router.patch("/")
def modify(id: int, user: NewUser) -> User:
    try:
        return service.modify(id, user)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.delete("/{id}")
def delete(id: int) -> None:
    try:
        return service.delete(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
