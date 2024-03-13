#!/usr/bin/python3
""" holds the main app """
from flask import Flask, jsonify, request, abort, render_template, redirect, url_for
from flasgger.utils import swag_from
from models import storage
from models.doctor import Doctor
from flaskr.views import app_views


from .auth import login_required

@app_views.route('/doctors', methods=['GET'], strict_slashes=False)
@login_required
def doctor():
    """ doctor route """
    doctors = storage.query(Doctor).all()
    return render_template('doctor/doctorsList.html', doctors=doctors)

@app_views.route('/doctor', methods=['POST', 'GET'], strict_slashes=False)
@swag_from('documentation/doctor/post_doctor.yml', methods=['POST'])
def storeDoctor():
    """ storeDoctor route """ 
    if request.method == 'GET':
        return render_template('doctor/addDoctor.html', flag=0)
    if request.method == 'POST':
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
        return redirect('/doctors')


@app_views.route('/doctors/<doctor_id>/del/', methods=['POST'], strict_slashes=False)
def deleteDoctor(doctor_id):
    """ deleteDoctor route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    doctor.delete()
    storage.save()
    return redirect('/doctors')


@app_views.route('/doctors/<doctor_id>', methods=['POST', 'GET'], strict_slashes=False)
def updateDoctor(doctor_id):
    """ updateDoctor route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    if request.method == 'GET':
        flag = 1
        doctor = storage.get(Doctor, doctor_id)
        return render_template('doctor/updateDoctor.html', doctor=doctor, flag=flag)
    if request.method == 'POST':
        doctor.name = request.form.get("name")
        doctor.salary = request.form.get("salary")
        doctor.email = request.form.get("email")
        doctor.phone = request.form.get("phone")
        doctor.address = request.form.get("address")
        doctor.gender = request.form.get("gender")
        doctor.save()
        return redirect("/doctors")
