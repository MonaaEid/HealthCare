#!/usr/bin/python3
""" holds the main app """
from flask import Flask, jsonify, request, abort, render_template, make_response
from flasgger.utils import swag_from
from models import storage
from models.doctor import Doctor
from models.appointment import Appointment
from models.department import Department
from flaskr.views import app_views


@app_views.route('/doctors/<doctor_id>/appointments', methods=['GET'], strict_slashes=False)
def doctorAppointments(doctor_id):
    """ doctorAppointments route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    appointments = [appointment.to_dict() for appointment in doctor.appointments]
    return jsonify(appointments)


@app_views.route('/doctors/appointments', methods=('GET', 'POST'), strict_slashes=False)
def storeAppointment():
    """ storeAppointment route """
    if request.method == 'POST':
        # doctor = storage.get(Doctor, doctor_id)
        # if doctor is None:
        #     abort(404)
        doctor_id = request.form.get("doctor_id")
        # patient_id = request.form.get("patient_id")
        date = request.form.get("date")
        time = request.form.get("time")
        data = {"doctor_id": doctor_id, "date": date}
        instance = Appointment(**data)
        instance.save()
        return jsonify(data), 201
    doctors = [doctor.to_dict() for doctor in storage.all("Doctor").values()]
    departments = [department.to_dict() for department in storage.all("Department").values()]
    return render_template('appointment/appointment.html', doctors=doctors, departments=departments)

@app_views.route('/doctors/<doctor_id>/appointments/<appointment_id>', methods=['GET'], strict_slashes=False)
def appointmentById(doctor_id, appointment_id):
    """ appointmentById route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    appointment = storage.get(Appointment, appointment_id)
    if appointment is None:
        abort(404)
    return jsonify(appointment.to_dict())



@app_views.route('/doctors/<doctor_id>/appointments/<appointment_id>', methods=['DELETE'], strict_slashes=False)
def deleteAppointment(doctor_id, appointment_id):
    """ deleteAppointment route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    appointment = storage.get(Appointment, appointment_id)
    if appointment is None:
        abort(404)
    appointment.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/doctors/<doctor_id>/appointments/<appointment_id>', methods=['PUT'], strict_slashes=False)
def updateAppointment(doctor_id, appointment_id):
    """ updateAppointment route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    appointment = storage.get(Appointment, appointment_id)
    if appointment is None:
        abort(404)
    appointment.date = request.form.get("date")
    appointment.time = request.form.get("time")
    appointment.save()
    return jsonify(appointment.to_dict()), 200
