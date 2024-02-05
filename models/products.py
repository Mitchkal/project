"""
Module products.py
contains functions to interact with firestore dtabase
"""
from google.cloud import firestore

db = firestore.Client()


class Product:
    """
    class for the product items
    """
    def __init__(self, name, description, price,
                 category, image_url, stock_quanity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image_url = image_url
        self.stock_quanity = stock_quantity

    def to_dict(self):
        """
        converts object to dictionary for storage in firestore
        """
        return {
                'name': self.name,
                'description': self.description,
                'price': self.price,
                'category': self.category,
                'image_url': self.image_url,
                'stock_quantity': self.stock_quanity,
        }
