from abc import ABC, abstractmethod

from domain import entity


class AbstractOrderRepository(ABC):
    @abstractmethod
    def create_order(self, order: entity.Order) -> entity.Order:
        pass

    @abstractmethod
    def get_order_by_user_id(self, user_id: int) -> entity.Order:
        pass
