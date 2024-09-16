from pydantic import BaseModel


class CreateOrderRequest(BaseModel):
    user_id: int
    item: str
    total: float
