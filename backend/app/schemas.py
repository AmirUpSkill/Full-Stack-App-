from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
class TaskCreate(TaskBase):
    pass
class TaskUpdate(TaskBase):
    is_completed: bool
class Task(TaskBase):
    id: int
    is_completed: bool
    class Config:
        orm_mode = True