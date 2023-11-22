from datetime import timedelta, datetime
from typing import Annotated

from fastapi import Depends
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import pwd_context, settings, oauth2_scheme
from app.core.db import get_db
from app.core.exceptions import UnauthorizedException, BadRequestException
from app.models.user import User
from app.schemas.user import TokenDataSchema


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate(db: AsyncSession, username, password) -> User | bool:
    user = await User.get_by_email(username, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(db: Annotated[AsyncSession, Depends(get_db)], token: Annotated[User, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise UnauthorizedException(msg="Could not validate credentials")
        token_data = TokenDataSchema(username=username)
    except JWTError:
        raise UnauthorizedException(msg="Could not validate credentials")
    user = await User.get_by_email(token_data.username, db)
    if user is None:
        raise UnauthorizedException(msg="Could not validate credentials")
    return user
