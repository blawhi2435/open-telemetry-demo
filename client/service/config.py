
import os
from pydantic import BaseModel


class Configure:
    def __init__(self):
        self.order_server_urls = OrderServerURLs(
            create_order=os.getenv("ORDER_SERVER_CREATE_ORDER"),
            get_order_by_user_id=os.getenv("ORDER_SERVER_GET_ORDER_BY_USER_ID")
        )


class OrderServerURLs(BaseModel):
    create_order: str = "http://localhost:8081/server/orders"
    get_order_by_user_id: str = "http://localhost:8081/server/orders/user/"