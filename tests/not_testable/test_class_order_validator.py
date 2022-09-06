import pytest
from onlineshop.item import Item
from onlineshop.order import Order

from onlineshop.not_testable.order_validator import OrderValidator

# Demonstration of using a test class to reuse code and setup between tests

# We include only few examples for valid order scenarios,
# to test all possible scenarios with all combinations of validations checks
# performed inside OrderValidator will lead to dozens of tests so they are not implemented.

class TestOrderValidator:
    @pytest.fixture(autouse=True) #autouse=True ensures the fixture runs before every test
    def _setup(self, test_order: Order) -> None:
        self.order_validator = OrderValidator()

        # Some valid order
        self.order = test_order
        self.order.items = [Item(item_id=2, price=100)]
        self.order.purchase_cost = 100

    def test_valid_order_single_item(self) -> None:
        # Arrange
        self.order.items = [Item(item_id=2, price=100)]

        # Act
        is_valid = self.order_validator.validate(self.order)

        # Assert (with optional message)
        assert is_valid, "Expected order to be valid because ids are positive, purchase date is in the past, single item price equals purchase cost"

    def test_valid_order_multiple_items(self) -> None:
        # Arrange
        self.order.items = [Item(item_id=2, price=40), Item(item_id=3, price=60)]

        # Act
        is_valid = self.order_validator.validate(self.order)

        # Assert (with optional message)
        assert is_valid, "Expected order to be valid because ids are positive, purchase date is in the past, multiple items prices sum up to purchase cost"



