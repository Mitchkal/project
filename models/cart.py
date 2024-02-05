"""
module cart.py
contains The cart model and methods
"""

from pydantic import BaseModel
from typing import List
from datetime import datetime


class CartItem(BaseModel):
    """
    the cartitem model 
    """
    product_id: str
    quantity: int


class Cart(BaseModel):
    """The cart model"""
    cart_id: str
    user_id: str #obtained from firebase authentication

    products: List[CartItem] = []
    total_price: float = 0.0
    date_created: datetime = datetime.now()


    def display_cart_items(self):
        """displays the cart items"""
        return [item.product_id for item in self.products]

    def add_item_to_cart(self, product_is: str, quantity: int):
        """adds items to the cart"""
        #check if item in cart
        for item in self.products:
            if item.product_id == product_id:
                item.quanity += quantity
                break
            else:
                self.products.append(CartItem(product_id=product_id,
                                     quantity=quantity))
        self.calculate_total_price()

    def remove_item_from_cart(self, product_id: str, quantity: int):
        """checks if items is in cart and removes it"""

        for item in self.products:
            if item.product_id == product_id:
                if item.quanity <= quantity:
                    self.products.remove(item)
                else:
                    item.quantity -= quantity
                self.calculate_total_price()
                break

    def calculate_total_price(self):
        """calculates total price based on items in cart"""
        self.total_price = sum(item.quantity * get_product_price(
                               item.product_id) for item in self.products)

def get_product_price(product_id: str) -> float:
        """logic to fetch product price
        currently returnng static value
        """
        return 10.0
