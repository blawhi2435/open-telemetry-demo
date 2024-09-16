import json
import logging
from pydantic import TypeAdapter
import requests
from domain import entity
from repository.astract import AbstractOrderRepository
from service.config import Configure
from service.logger import Logger
from repository.api import model


class OrderRestfulRepository(AbstractOrderRepository):
    def __init__(self, logger: Logger, config: Configure):
        self.logger = logger
        self.config = config

    def create_order(self, order: entity.Order) -> entity.Order:

        request_order = model.CreateOrderRequest(
            user_id=order.user_id,
            item=order.item,
            total=order.total
        )
        try:
            response = requests.post(self.config.order_server_urls.create_order, json=request_order.model_dump())
            response.raise_for_status()
        except Exception as err:
            self.logger.log(level=logging.ERROR, user_id=order.user_id, order_id=order.id, extra={}, message=f"api create_order failed: {err}")
            raise err
        
        self.logger.log(level=logging.INFO, user_id=order.user_id, order_id=order.id, extra={}, message=f"response: {response.json()}")


        import json
        
        order = TypeAdapter(entity.Order).validate_json(json.dumps(response.json()))
        return order

    def get_order_by_user_id(self, user_id: int) -> entity.Order:
        try:
            response = requests.get(f"{self.config.order_server_urls.get_order_by_user_id}{user_id}")
            response.raise_for_status()
        except Exception as e:
            self.logger.log(level=logging.ERROR, user_id=user_id, order_id=None, extra={}, message=f"api get_order_by_user_id failed: {e}")
            raise e
        
        order = TypeAdapter(entity.Order).validate_json(json.dumps(response.json()))
        return order