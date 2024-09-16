
from pymongo import MongoClient
from app.handler.order import OrderHandler
from repository.mongo.order import OrderMongoRepository
from service.config import Configure
from service.logger import Logger
from usecase.order import OrderUsecase


logger = Logger(level="INFO")
configure = Configure()

mongo_client = MongoClient("mongodb://root:example@localhost:27017")
order_repo = OrderMongoRepository(logger=logger, mongo_client=mongo_client)
order_usecase = OrderUsecase(logger=logger, order_repo=order_repo)
order_handler = OrderHandler(logger=logger, order_usecase=order_usecase)
