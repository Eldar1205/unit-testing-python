from onlineshop.order import Order
from onlineshop.testable.iorder_validator import IOrderValidator


class OrderValidatorComposite(IOrderValidator):
    def __init__(self, validators: list[IOrderValidator]) -> None:
        self.__validators = validators

    def validate(self, order: Order) -> bool:
        return all(validator.validate(order) for validator in self.__validators)
