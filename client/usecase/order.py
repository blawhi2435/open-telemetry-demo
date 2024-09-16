import logging
from domain import entity
from repository.astract import AbstractOrderRepository
from service.logger import Logger
from usecase.abstract import AbstractOrderUsecase


class OrderUsecase(AbstractOrderUsecase):
    def __init__(self, logger: Logger, order_repo: AbstractOrderRepository):
        self.logger = logger
        self.order_repo = order_repo

    def get_order_by_user_id(self, user_id: int) -> entity.Order:

        self.logger.log(level=logging.INFO, user_id=user_id, order_id=None, extra={}, message="usecase Get order by id started")

        try:
            order = self.order_repo.get_order_by_user_id(user_id)
        except Exception as e:
            self.logger.log(level=logging.ERROR, user_id=user_id, order_id=None, extra={}, message=f"usecase get_order_by_user_id failed: {e}")
            raise e
        
        self.logger.log(level=logging.INFO, user_id=order.user_id, order_id=order.id, extra={}, message="usecase Get order by id completed")
        
        return order

    def create_order(self, order: entity.Order) -> entity.Order:
        
        self.logger.log(level=logging.INFO, user_id=order.user_id, order_id=None, extra={}, message="usecase Create order started")

        try:
            order = self.order_repo.create_order(order)
        except Exception as e:
            self.logger.log(level=logging.ERROR, user_id=order.user_id, order_id=None, extra={}, message=f"usecase create_order failed: {e}")
            raise e
        
        self.logger.log(level=logging.INFO, user_id=order.user_id, order_id=order.id, extra={}, message="usecase Create order completed")
        
        return order