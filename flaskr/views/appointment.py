#!/usr/bin/python3
""" Appointment views"""
from flask import Flask, jsonify, request, abort, render_template, flash, redirect
from models import storage
from models.doctor import Doctor
from models.appointment import Appointment
from flaskr.views import app_views
from .auth import login_required

@app_views.route('/doctors/<doctor_id>/appointments', methods=['GET'], strict_slashes=False)
@login_required
def doctorAppointments(doctor_id):
    """ doctorAppointments route """
    doctor = storage.get(Doctor, doctor_id)
    if doctor is None:
        abort(404)
    appointments = storage.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()
    if appointments is None:
        flash("No appointments found")
    return render_template('appointment/appointmentsList.html', appointments=appointments)


@app_views.route('/appointments', methods=['GET'], strict_slashes=False)
@login_required
def appointments():
    """ appointments route """
    appointments = storage.query(Appointment).all()
    return render_template('appointment/appointmentsList.html', appointments=appointments)

@app_views.route('/doctors/appointments', methods=['GET', 'POST'], strict_slashes=False)
def storeAppointment():
    """ storeAppointment route """
    if request.method == 'POST':
        doctor_id = request.form.get("doctor_id")
        # patient_id = request.form.get("patient_id")
        patient_name = request.form.get("patient_name")
        department_id = request.form.get("department_id")
        date = request.form.get("date")
        data = {"doctor_id": doctor_id, "date": date, "patient_name": patient_name, "department_id": department_id}
        instance = Appointment(**data)
        instance.save()
        return jsonify(data), 201
    doctors = [doctor.to_dict() for doctor in storage.all("Doctor").values()]
    departments = [department.to_dict() for department in storage.all("Department").values()]
    patients = [patient.to_dict() for patient in storage.all("Patient").values()]
    return render_template('appointment/appointment.html', doctors=doctors, departments=departments, patients=patients)

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



@app_views.route('/appointment/<appointment_id>/del', methods=['POST'], strict_slashes=False)
def deleteAppointment(appointment_id):
    """ deleteAppointment route """
    appointment = storage.get(Appointment, appointment_id)
    if appointment is None:
        abort(404)
    appointment.delete()
    storage.save()
    return redirect('/appointments')


@app_views.route('appointment/<appointment_id>', methods=['POST', 'GET'], strict_slashes=False)
def updateAppointment(appointment_id):
    """ updateAppointment route """
    appointment = storage.query(Appointment).filter(Appointment.id == appointment_id).first()

    if appointment is None:
        abort(404)
    if request.method == 'GET':
        return render_template('appointment/updateAppointment.html', appointment=appointment)
    if request.method == 'POST':
        appointment = storage.get(Appointment, appointment_id)
        appointment.doctor_id = request.form.get("doctor_id")
        appointment.date = request.form.get("date")
        appointment.patient_name = request.form.get("patient_name")
        appointment.department_id = request.form.get("department_id")
        appointment.save()
        return redirect('/appointments')
