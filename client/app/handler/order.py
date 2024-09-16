import logging
from domain import entity
from service.logger import Logger
from usecase.abstract import AbstractOrderUsecase
from app.viewModels import CreateOrderRequest
from fastapi.responses import JSONResponse


class OrderHandler:
    def __init__(self, logger: Logger, order_usecase: AbstractOrderUsecase):
        self.logger = logger
        self.order_usecase = order_usecase

    def get_order_by_id(self, user_id: int) -> entity.Order:
        self.logger.log(level=logging.INFO, user_id=user_id, order_id=None, extra={}, message="Get order by id started")

        try:
            order = self.order_usecase.get_order_by_user_id(user_id)
        except Exception as e:
            self.logger.log(level=logging.ERROR, user_id=user_id, order_id=None, extra={}, message=f"handler get_order_by_user_id failed: {e}")
            return JSONResponse({"error": f"handler get_order_by_user_id: {e}"}, status_code=500)
        
        self.logger.log(level=logging.INFO, user_id=user_id, order_id=order.id, extra={}, message="handler Get order by id completed")
        
        return JSONResponse(order.model_dump())
    
    def create_order(self, request: CreateOrderRequest):
            
            self.logger.log(level=logging.INFO, user_id=request.user_id, order_id=None, extra={}, message="handler Create order started")
            order = entity.Order(
                user_id=request.user_id,
                item=request.item,
                total=request.total
            )
    
            try:
                order = self.order_usecase.create_order(order)
            except Exception as e:
                self.logger.log(level=logging.ERROR, user_id=request.user_id, order_id=None, extra={}, message=f"handler create_order failed: {e}")
                return JSONResponse({"error": f"An error occurred: {e}"}, status_code=500)
            
            self.logger.log(level=logging.INFO, user_id=request.user_id, order_id=order.id, extra={}, message="handle Create order completed")
            
            return JSONResponse(order.model_dump())

