#!/usr/bin/python3
""" holds the main app """
from flask import Flask, jsonify, request, abort, render_template, make_response, session
from flaskr.views import app_views


@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index route """
    return render_template('index.html')
