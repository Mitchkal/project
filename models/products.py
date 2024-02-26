"""
Module products.py
contains functions to interact with firestore dtabase
"""
from google.cloud import firestore
from pydantic import BaseModel

# db = firestore.Client()


class Product(BaseModel):
    """
    class for the product items
    """
    name = name
    description = description
    price = price
    category = category
    image_url = image_url
    stock_quanity = stock_quantity

    def to_dict(self):
        """
        converts model to dictionary for storage in firestore
        """
        return {
                'name': self.name,
                'description': self.description,
                'price': self.price,
                'category': self.category,
                'image_url': self.image_url,
                'stock_quantity': self.stock_quanity,
        }
