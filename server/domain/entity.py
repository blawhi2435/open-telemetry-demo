from pydantic import BaseModel


class Order(BaseModel):
    id: str | None = None
    user_id: int
    item: str
    total: float


class User(BaseModel):
    id: int
    name: str