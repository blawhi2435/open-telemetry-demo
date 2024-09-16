from fastapi import APIRouter
from app.injection import order_handler
from app.viewModels import CreateOrderRequest


router = APIRouter()

@router.get("/orders/users/{user_id}")
async def get_order_by_user_id(user_id: int):
    return order_handler.get_order_by_id(user_id)

@router.post("/orders")
async def create_order(order: CreateOrderRequest):
    return order_handler.create_order(order)