from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    email: str = Field(title="", description="")
    password: str = Field(title="", description="")


class LoginResponse(BaseModel):
    access_token: str = Field(title="", description="")


class TokenDataSchema(BaseModel):
    username: str | None = Field(title="", description="")


class UserResponse(BaseModel):
    id: int = Field(title="", description="")
    email: int = Field(title="", description="")
