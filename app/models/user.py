from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = ({"schema": "app"}, )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
