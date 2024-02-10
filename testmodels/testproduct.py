from models import Product
from models import ProductManager


product_manager = ProductManager()


new_product = Product(
        name='Example Product',
        description='A description of the product',
        price=19.99,
        category='Example Categpry'
        image_url='https://example.com/product_image.jpg'
        stock_quantity=50,
        )
new_product_id = product_manager.add_product(new_product)

all_products = product_manager.get_all_products()

for product in all_products:
    print(product.name, product.price)
