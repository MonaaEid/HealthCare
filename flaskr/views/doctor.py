#!/usr/bin/python3
""" holds the main app """
from flask import Flask, jsonify, request, abort, render_template, make_response
from flasgger.utils import swag_from
from models import storage
from models.doctor import Doctor
from flaskr.views import app_views

@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index route """
    # name = request.args.get("name", "world")
    return render_template('doctor/index.html')


@app_views.route('/doctors', methods=['GET'], strict_slashes=False)
def doctor():
    """ doctor route """
    doctors =  [doctor.to_dict() for doctor in storage.all("Doctor").values()]
    return render_template('doctor/doctorsList.html', doctors=doctors)


@app_views.route('/doctors/<doctor_id>', methods=['GET'], strict_slashes=False)
def doctorById(doctor_id):
    """ doctorById route """
    doctor = storage.get("Doctor", doctor_id)
    if doctor is None:
        abort(404)
    return jsonify(doctor.to_dict())


@app_views.route('/doctors', methods=['POST'], strict_slashes=False)
@swag_from('documentation/doctor/post_doctor.yml', methods=['POST'])
def storeDoctor():
    """ storeDoctor route """
    name = request.form.get("name")
    salary = request.form.get("salary")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    gender = request.form.get("gender")
    data = {"name": name, "salary": salary, "email": email,
                    "phone": phone, "address": address, "gender":gender}
    instance = Doctor(**data)
    instance.save()
    return jsonify(data), 201


@app_views.route('/doctors/<doctor_id>', methods=['DELETE'], strict_slashes=False)
def deleteDoctor(doctor_id):
    """ deleteDoctor route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    doctor.delete()
    storage.save()
    return render_template('doctor/index.html')


@app_views.route('/doctors/<doctor_id>', methods=['PUT'], strict_slashes=False)
def updateDoctor(doctor_id):
    """ updateDoctor route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    doctor.name = request.form.get("name")
    doctor.salary = request.form.get("salary")
    doctor.email = request.form.get("email")
    doctor.phone = request.form.get("phone")
    doctor.address = request.form.get("address")
    doctor.gender = request.form.get("gender")
    doctor.save()
    return jsonify(doctor.to_dict()), 200


# @app_views.route('/doctors/<doctor_id>/appointments', methods=['GET'], strict_slashes=False)
# def doctorAppointments(doctor_id):
#     """ doctorAppointments route """
#     doctor = storage.get("Doctor", doctor_id)
#     if doctor is None:
#         abort(404)
#     return jsonify([appointment.to_dict() for appointment in doctor.appointments])

