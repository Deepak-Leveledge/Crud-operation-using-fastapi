from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email:str
    password: str


class UserOut(BaseModel):
    id:int
    username: str
    email: str
    is_active: bool


    class congfig:
        orm_mode=True