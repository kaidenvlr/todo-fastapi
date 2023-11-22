from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.db import get_db
from app.core.exceptions import UnauthorizedException
from app.core.utils import authenticate, create_access_token
from app.schemas.user import TokenResponse

router = APIRouter()


@router.post('/token', response_model=TokenResponse)
async def login_for_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Annotated[AsyncSession, Depends(get_db)]
):
    user = await authenticate(db, form_data.username, form_data.password)
    if not user:
        raise UnauthorizedException(msg="Incorrect username or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "Bearer"}
