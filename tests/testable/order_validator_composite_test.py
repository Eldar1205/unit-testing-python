import pytest
from onlineshop.order import Order
from onlineshop.testable.iorder_validator import IOrderValidator
from onlineshop.testable.order_validator_composite import OrderValidatorComposite

# Purposefully showing manually written mock, in real cases unittest.mock module is usually the way to go
class OrderValidatorMock(IOrderValidator):
    def __init__(self, is_valid: bool) -> None:
        self.is_valid = is_valid

    def validate(self, order: Order) -> bool:
        return self.is_valid

def test_empty_validators_composite(test_order: Order) -> None:
    order_validator = OrderValidatorComposite([])

    is_valid = order_validator.validate(test_order)

    assert is_valid == True

@pytest.mark.parametrize(
    "is_valid, expected",
    [(True, True), (False, False)],
    ids=["Valid", "Invalid"])
def test_single_validator_composite(test_order: Order, is_valid: bool, expected: bool) -> None:
    mock_validator = OrderValidatorMock(is_valid)
    order_validator = OrderValidatorComposite([mock_validator])

    is_valid = order_validator.validate(test_order)

    assert is_valid == expected

@pytest.mark.parametrize(
    "is_valid_1, is_valid_2, expected",
    [(True, True, True), (True, False, False), (False, True, False), (False, False, False)],
    ids=["Both Valid", "Only First Valid", "Only Second Valid", "Both Invalid"])
def test_multiple_validator_composite(test_order: Order, is_valid_1: bool, is_valid_2: bool, expected: bool) -> None:
    mock_validator_1 = OrderValidatorMock(is_valid_1)
    mock_validator_2 = OrderValidatorMock(is_valid_2)
    order_validator = OrderValidatorComposite([mock_validator_1, mock_validator_2])

    is_valid = order_validator.validate(test_order)

    assert is_valid == expected