import logging
from repository.astract import AbstractOrderRepository
from pymongo import MongoClient

from domain import entity
from service.logger import Logger


class OrderMongoRepository(AbstractOrderRepository):
    def __init__(self, logger: Logger, mongo_client: MongoClient):

        self.logger = logger

        self.__mongo_client = mongo_client
        self.__db = self.__mongo_client["demo"]
        self.collection = self.__db["orders"]


    def create_order(self, order) -> entity.Order:

        self.logger.log(level=logging.INFO, user_id=order.user_id, order_id=None, extra={}, message="mongo Create order started")
        try:
            result = self.collection.insert_one(order.model_dump())
        except Exception as e:
            self.logger.log(level=logging.ERROR, user_id=order.user_id, order_id=order.id, extra={}, message=f"mongo create_order insert_one failed: {e}")
            raise e
        
        self.logger.log(level=logging.INFO, user_id=order.user_id, order_id=order.id, extra={}, message="mongo Create order completed")

        return entity.Order(
            id=str(result.inserted_id),
            user_id=order.user_id,
            item=order.item,
            total=order.total
        )
        

    def get_order_by_user_id(self, user_id) -> entity.Order:
        
        self.logger.log(level=logging.INFO, user_id=user_id, order_id=None, extra={}, message="mongo Get order by id started")
        try:
            order = self.collection.find_one({"user_id": user_id})
        except Exception as e:
            self.logger.log(level=logging.ERROR, user_id=user_id, order_id=None, extra={}, message=f"mongo find_one failed: {e}")
            raise e
        
        self.logger.log(level=logging.INFO, user_id=user_id, order_id=str(order["_id"]), extra={}, message="mongo Get order by id completed")
        
        return entity.Order(
            id=str(order["_id"]),
            user_id=order["user_id"],
            item=order["item"],
            total=order["total"]
        )