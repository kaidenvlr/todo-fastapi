from sqlalchemy import Integer, String
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import mapped_column, Mapped

from app.core.exceptions import NotFoundException
from app.models.base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = ({"schema": "app"},)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    @classmethod
    async def get(cls, user_id: int, db_session: AsyncSession):
        stmt = select(cls).where(cls.id == user_id)
        result = await db_session.execute(stmt)
        instance = result.scalars().first()
        if instance is None:
            raise NotFoundException(msg="There is no user with this ID")
        else:
            return instance

    @classmethod
    async def get_by_email(cls, email: str, db_session: AsyncSession):
        stmt = select(cls).where(cls.email == email)
        result = await db_session.execute(stmt)
        instance = result.scalars().first()
        if instance is None:
            raise NotFoundException(msg="There is no user with this Email")
        else:
            return instance

    @classmethod
    async def list(cls, db_session: AsyncSession):
        stmt = select(cls)
        result = await db_session.execute(stmt)
        queryset = result.scalars().all()
        return queryset
