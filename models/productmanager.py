""""
module products manager
encapsulates logic for interacting with firestore
"""

from google.cloud import firestore


class ProductManager:
    """
    logic for firestore interaction
    """
    def __init__(self):
        """initialize firestore client"""
        self.db = firestore.Client()

    def add_product(self, product):
        """
        Adds product to database and returns id
        """
        products_ref = db.collection('products')

        product_data = product.to_dict()

        doc_ref = products_ref.add(product_data)

        return doc_ref.id

    def get_all_products(self):
        """Retrieves all products from store"""

        products_ref = self.db.collection('products')
        products = products_ref.stream()
        product_list = [Product.from_dict(doc.to_dict()) for doc in products]
        return product_list

    @staticmethod
    def from_dict(data):
        """
        create product object from dictionary
        """
        return Product(
                name=data['name'],
                description=data['description'],
                price=data['price'],
                category=data['category'],
                image_url=data['image_url'],
                stock_quantity=data['stock_quantity'],
                )
