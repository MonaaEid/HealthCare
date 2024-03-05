#!/usr/bin/python3
""" Patient views """
from flask import Flask, jsonify, request, abort, render_template, make_response, redirect, url_for
from flasgger.utils import swag_from
from models import storage
from models.patient import Patient
from flaskr.views import app_views
from models.engine.db_storage import DBStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


@app_views.route('/patients', methods=['GET'], strict_slashes=False)
def patient():
    """ patient route """
    # patients =  [patient.to_dict() for patient in storage.all("Patient").values()]
    patients = storage.all(Patient).values()
    return render_template('patient/patientsList.html', patients=patients)


@app_views.route('/patients/<patient_id>', methods=['GET'], strict_slashes=False)
def patientById(patient_id):
    """ patientById route """
    patient = storage.get("Patient", patient_id)
    if patient is None:
        abort(404)
    return jsonify(patient.to_dict())


@app_views.route('/patient', methods=['POST', 'GET'], strict_slashes=False)
@swag_from('documentation/patient/post_patient.yml', methods=['POST'])
def storePatient():
    """ storePatient route """
    if request.method == 'GET':
        flag = 0
        return render_template('patient/addPatient.html', flag=flag)
    elif request.method == 'POST':
        name = request.form.get("name")
        birth_date = request.form.get("birthdate")
        phone = request.form.get("phone")
        gender = request.form.get("gender")
        data = {"name": name, "birth_date": birth_date, "phone": phone, "gender": gender}
        instance = Patient(**data)
        instance.save()
        return jsonify(data), 201


@app_views.route('/patients/<patient_id>/del/', methods=['POST'], strict_slashes=False)
def deletePatient(patient_id):
    """ deletePatient route """
    patient = storage.get(Patient, patient_id)
    if patient is None:
        abort(404)
    patient.delete()
    storage.save()
    return redirect(url_for('patients'))


@app_views.route('/patients/<patient_id>', methods=['POST', 'GET'], strict_slashes=False)
def updatePatient(patient_id):
    """ updatePatient route """
    patient = storage.get(Patient, patient_id)
    if patient is None:
        abort(404)
    if request.method == 'GET':
        flag = 1
        patient = storage.get(Patient, patient_id)
        return render_template('patient/updatePatient.html', patient=patient, flag=flag)
    elif request.method == 'POST':
        patient.name = request.form.get("name")
        patient.birth_date = request.form.get("birthdate")
        patient.phone = request.form.get("phone")
        patient.gender = request.form.get("gender")
        patient.save()
        return jsonify(patient.to_dict())