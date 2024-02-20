#!/usr/bin/python3
"""
The Flask App
"""

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, jsonify, render_template, make_response
from flask_cors import CORS
from flassger import Swagger
from flassger.utils import swag_from


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blue_print(app_views)


@app.errorhandler(404)
def not_found(error):
    """
    handles 404 error
    """
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
        'title': 'HairHaven Rest API',
        'uiversion': 3
}

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
    app.run(host=host, port=port, threaded=True)
