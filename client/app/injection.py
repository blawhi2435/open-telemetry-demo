
from app.handler.order import OrderHandler
from repository.api.order import OrderRestfulRepository
from service.config import Configure
from service.logger import Logger
from usecase.order import OrderUsecase

logger = Logger(level="INFO")
configure = Configure()

order_repo = OrderRestfulRepository(logger=logger, config=configure)
order_usecase = OrderUsecase(logger=logger, order_repo=order_repo)
order_handler = OrderHandler(logger=logger, order_usecase=order_usecase)
