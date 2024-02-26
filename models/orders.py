#!/usr/bin/python3
"""
The order model
"""

from pydantic import BaseModel
from typing import List
from datetime import datetime


class OrderItem(BaseModel):
    """Class for each item in order
    """
    product_id: str
    quantity: int


class Order(BaseModel):
    """ The order model """
    order_id: str
    user_id: str
    products: List[OrderItem] = []
    total_price: float = 0.0
    order_status: str
    date_ordered: datetime = datetime.now()

    def display_order_items(self):
        """displays items in order"""
        return [item.product_id for item in self.products]

    def add_item_to_order(self, product_id: str, quantity: int):
        """adds items to the order"""
        self.products.append(OrderItem(product_id=product_id,
                             quantity=quantity))
        self.calculate_total_price()

    def remove_item_from_order(self, product_id: str, quantity: int):
        """removes items from the order"""
        item_to_remove = next((item for item in self.products
                              if item.product_id == product_id), None)
        if item_to_remove:
            item_to_remove.quantity -= quantity
            if item_to_remove.quantity <= 0:
                self.products.remove(item_to_remove)
                self.calculate_total_price()

    def calculate_total_price(self):
        """calculates total price in checkout"""
        self.total_price = sum(item.quantity * get_product_price(
                               item.product_id)for item in self.products)

    def get_product_price(product_id: str) -> float:
        """place holder for getting product prices"""
        return 10.0
