from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    user_id: int = Field(title="", description="")
    title: str = Field(title="", description="")


class TaskDoneSchema(BaseModel):
    task_id: int = Field(title="", description="")


class TaskResponse(BaseModel):
    id: int = Field(title="", description="")
    user_id: int = Field(title="", description="")
    title: int = Field(title="", description="")
