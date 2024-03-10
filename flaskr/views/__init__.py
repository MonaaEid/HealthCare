#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/')

from flaskr.views.index import *
from flaskr.views.doctor import *
from flaskr.views.auth import *
from flaskr.views.patient import *
from flaskr.views.appointment import *
from . import auth

app_views.register_blueprint(auth.bp)
# from flaskr.views.department import *