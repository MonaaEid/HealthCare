#!/usr/bin/python3
""" holds the main app """
from flask import Flask, jsonify, request, abort, render_template, make_response
from flasgger.utils import swag_from


app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index route """
    # name = request.args.get("name", "world")
    return render_template('index.html')


@app.route('/storeDoctor', methods=['POST'], strict_slashes=False)
@swag_from('documentation/doctor/post_doctor.yml', methods=['POST'])
def storeDoctor():
    """ storeDoctor route """
    name = request.form.get("name")
    salary = request.form.get("salary")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    gender = request.form.get("gender")
    return jsonify({"name": name, "salary": salary, "email": email,
                    "phone": phone, "address": address, "gender":gender})

    return doctor
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)