#!/usr/bin/python3
"""
The Flask App
"""

from models.storage.firestorage import StorageModel
from api.v1.views import app_views
from os import environ
from flask import Flask, jsonify, render_template, make_response, request, redirect, url_for
from flask_cors import CORS
from flassger import Swagger
from flassger.utils import swag_from
import stripe


model = StorageModel()
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.register_blue_print(app_views)

stripe.api_key = ""
# publiv_key = ""

@app.route('/')
def index():
    """renders the index page"""
    return render_template('index.html')

@app.route('./thankyou')
def thankyou():
    """returns the payment thankyou"""
    return render_template('thankyou.html')




@app.errorhandler(404)
def not_found(error):
    """
    handles 404 error
    """
    return make_response(jsonify({'error': "Not found"}), 404)

@app.route('/payment', methods=['POST'])
def create_checkout_session():
    """stripe checkout"""
    # customer information

    customer  = stripe.Customer.create(email=request.form('stripeEmail']),
                                        source=request.form('stripeToken']))
    # payment information

    charge = stripe.Charge.create(
            customer=customer.id
            amount=1999
            currency='usd'
            description='Payment'
        )
    return redirect(url_for('thankyou'))
    # data = request.get_json()

    """session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=data['items'],
            mode='payment',
            success_url='',
            cancel_url='',
    )"""
    # return jsonify({'id': session.id})



app.config['SWAGGER'] = {
        'title': 'HairHaven Rest API',
        'uiversion': 3
}
# example new_document_id = model.add_document("users", {"name": "John Doe", "email": "johndoe@example.com"})
# model.query_collection("products", {"category": "River Island cinched waist blazer in purple"})

Swagger(app)


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
