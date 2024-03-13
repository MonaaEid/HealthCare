#!/usr/bin/python3
""" Department views"""
from flask import Flask, jsonify, request, abort, render_template, flash, redirect
from flasgger.utils import swag_from
from models import storage
from models.department import Department
from flaskr.views import app_views
from .auth import login_required

@app_views.route('/departments', methods=['GET'], strict_slashes=False)
@login_required
def departments():
    """ departments route """
    departments = storage.query(Department).all()
    return render_template('department/departmentList.html', departments=departments)


@app_views.route('/department', methods=['POST', 'GET'], strict_slashes=False)
def storeDepartment():
    """ storeDepartment route """
    if request.method == 'POST':
        name = request.form.get("name")
        description = request.form.get("description")
        department_head_id = request.form.get("doctor_id")
        data = {"name": name, "description": description, "department_head_id": department_head_id }
        instance = Department(**data)
        instance.save()
        return jsonify(data), 201
    doctors = [doctor.to_dict() for doctor in storage.all("Doctor").values()]
    return render_template('department/addDepartment.html', doctors=doctors)


@app_views.route('/departments/<department_id>/del', methods=['POST'], strict_slashes=False)
def deleteDepartment(department_id):
    """ deleteDepartment route """
    department = storage.get(Department, department_id)
    if department is None:
        abort(404)
    storage.delete(department)
    storage.save()
    return redirect('/departments')