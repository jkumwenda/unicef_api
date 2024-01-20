from pydantic import BaseModel


class WelcomeSchema(BaseModel):
    welcome: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {"welcome": "Hello world, this is API feedback"}}
