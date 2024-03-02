#!/usr/bin/python3
""" holds the main app """
from flask import Flask, jsonify, request, abort, render_template, make_response
from models import storage
from flaskr.views import app_views
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = "super secret key"
app.register_blueprint(app_views)
# cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
# cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


# @app.errorhandler(404)
# def not_found(error):
#     """ 404 Error
#     ---
#     responses:
#       404:
#         description: a resource was not found
#     """
#     return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)
