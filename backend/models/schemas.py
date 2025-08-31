from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, example="Купить молоко")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=100)
    completed: bool | None = None

class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True
