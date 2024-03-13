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


@app_views.route('/department', methods=['POST'], strict_slashes=False)
def storeDepartment():
    """ storeDepartment route """
    if request.method == 'POST':
        name = request.form.get("name")
        data = {"name": name}
        instance = Department(**data)
        instance.save()
        return jsonify(data), 201
    return render_template('department/department.html')


@app_views.route('/departments/<department_id>', methods=['POST'], strict_slashes=False)
def deleteDepartment(department_id):
    """ deleteDepartment route """
    department = storage.get(Department, department_id)
    if department is None:
        abort(404)
    storage.delete(department)
    storage.save()
    return jsonify({}), 200