#!/usr/bin/python3
"""
The Flask App
"""
from flask_cors import CORS
import stripe
import config
from models.storage.firestorage import StorageModel
# from apiews import app_views
from os import environ
from flask import Flask, jsonify, render_template,
make_response, request, redirect, url_for
# from flassger import Swagger
# from flassger.utils import swag_from


model = StorageModel()
app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.register_blue_print(app_views)

stripe.api_key = config.STRIPE_PRIVATE_KEY
public_key = config.STRIPE_PUBLIC_KEY


@app.route('/', strict_slashes=False)
def index():
    """renders the index page"""
    return render_template('index.html')


@app.route('/template', strict_slashes=False)
def template():
    """renders the cart template"""
    return render_template('template.html')


@app.route('/detail', methods=['GET'], strict_slashes=False)
def detail():
    """renders the product detail page"""
    product_id = request.args.get('id')
    return render_template('details.html', product_id=product_id)


"""@app.route('./thankyou')
def thankyou():returns the payment thankyou
    return render_template('thankyou.html')"""


@app.errorhandler(404)
def not_found(error):
    """
    handles 404 error
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.route('/products', methods=['GET'])
def retrive_products_from_store():
    """retrieves objects from firestore"""

    products = model.query_collection("hair-products")
    return jsonify(products)


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """stripe checkout"""
    if request.method == 'POST':
        try:
            cart_items = request.get_json()
            products = products
            line_items = validate_cart_items(products, cart_items)

            session = stripe.checkout.Session.create(**params)
            params = {
                    "submit_type": "pay",
                    "payment_method_types": ['card'],
                    "mode": "payment",
                    "billing_address_collection": "auto",
                    "shipping_address_collection": {
                        "allowed_countries": ["US", "CA"]
                        },
                    "line_items": line_items,
                    "success_url": f"{request.host_url}result?session_id={{
                                      CHECKOUT_SESSION_ID}}",
                    "cancel_url": 'http://localhost:5000/cancel'
                    }
            session = stripe.checkout.Session.create(**params)
            return jsonify(checkout_session), 200
        except Exception as e:
            return jsonify({"statusCode": 500, "message": str(e)}), 500
    else:
        return 'Method not allowed', 405


"""app.config['SWAGGER'] = {
        'title': 'HairHaven Rest API',
        'uiversion': 3
}"""
# Swagger(app)


if __name__ == "__main__":
    """
    The main function
    """
    host = environ.get('HAVEN_HOST')
    port = environ.get('HAVEN_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port)
