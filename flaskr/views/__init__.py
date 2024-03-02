#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/')

from flaskr.views.index import *
from flaskr.views.doctor import *
from flaskr.views.auth import *