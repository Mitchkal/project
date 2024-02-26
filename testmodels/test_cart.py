"""test module for cart_items"""

from datetime import datetime
from models.cart_model import Cart, CartItem


def test_display_cart_items():
    """
    test module for the cart model
    """

    cart = Cart(
            cart_id='123',
            user_id='user123',
            products=[CartItem(product_id='p1', quantity=2),
                      CartItem(product_id='p2', quantity=1)],
            total_price=30.0,
            date_created=datetime.now()
            )
    assert cart.display_cart_items() == ['p1', 'p2']


def test_add_item_to_cart():
    """tests add item to cart"""
    cart = Cart(
            cart_id='123',
            user_id='user123',
            products=[CartItem(product_id='p1', quantity=2)],
            total_price=20.0,
            date_created=datetime.now()
            )
    cart.add_item_to_cart(product_id='p2', quantity=3)
    assert cart.display_cart_items() == ['p1', 'p2']
    assert cart.total_price == 50.0


def test_remove_item_from_cart():
    """test removal from cart"""

    cart = Cart(
            cart_id='123',
            user_id='user123',
            products=[CartItem(product_id='p1', quantity=2),
                      CartItem(product_id='p2', quantity=3)],
            total_price=50.0,
            date_created=datetime.now()
            )
    cart.remove_item_from_cart(product_id='p1', quantity=1)
    assert cart.display_cart_items() == ['p1', 'p2']
    assert cart.total_price == 40.0


def test_calculate_total_prices():
    """tests total price calculation"""
    cart = Cart(
            cart_id='123',
            user_id='user123',
            products=[CartItem(product_id='p1', quantity=2),
                      CartItem(product_id='p2', quantity=3)],
            total_price=0.0,
            date_created=datetime.now()
            )
    assert cart.total_price == 70.0
