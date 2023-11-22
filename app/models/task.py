from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = ({"schema": "app"},)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("app.users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    user = relationship("User", back_populates="tasks", lazy="selectin")
