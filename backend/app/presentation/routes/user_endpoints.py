from fastapi import APIRouter, Depends, HTTPException, status

from app.application.use_cases.user_register import RegisterUserCase
from app.application.use_cases.user_login import TokenGenCase
from app.application.use_cases.user_get import GetUserCase

from app.infrastucture.repositories_impl import UserRepositoryImpl
from app.infrastucture.security import (
    PasswordHasher,
    TokenProvider,
)

from app.presentation.schemas.user_schemas import (
    UserRegisterRequest,
    UserLoginRequest,
    TokenResponse,
)
from app.presentation.dependencies.user_depends import (
    get_password_hasher,
    get_token_provider,
    get_user_repo,
)

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
def register_user(
    data: UserRegisterRequest,
    repo: UserRepositoryImpl = Depends(get_user_repo),
    hasher: PasswordHasher = Depends(get_password_hasher),
    token_provider: TokenProvider = Depends(get_token_provider),
):
    registrate_case = RegisterUserCase(repo, hasher)
    token_case = TokenGenCase(
        user_repo=repo,
        hasher=hasher,
        token_provider=token_provider,
    )
    try:
        user = registrate_case.execute(data.email, data.password)
        access, refresh = token_case.execute(user.email, data.password)
        return TokenResponse(
            access=access,
            refresh=refresh,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/login")
def login_user(
    data: UserLoginRequest,
    repo=Depends(get_user_repo),
    hasher=Depends(get_password_hasher),
    token_provider=Depends(get_token_provider),
):
    token_case = TokenGenCase(repo, hasher, token_provider)
    try:
        access, refresh = token_case.execute(data.email, data.password)
        return TokenResponse(
            access=access,
            refresh=refresh,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/{uid}", response_model=TokenResponse)
def get_user(uid: int, repo=Depends(get_user_repo)):
    use_case = GetUserCase(repo)
    user = use_case.execute(uid)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )
    return TokenResponse(
        id=user.id,
        email=user.email,
        is_active=user.is_active,
        role=user.role,
    )
