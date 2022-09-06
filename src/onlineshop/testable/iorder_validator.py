from abc import ABC, abstractmethod

from onlineshop.order import Order


class IOrderValidator(ABC):
    @abstractmethod
    def validate(self, order: Order) -> bool:
        ...