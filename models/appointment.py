#!/usr/bin/python3
""" holds class Appointment"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, ForeignKey, Integer, Date, String
from datetime import date

class Appointment(BaseModel, Base):
    """Representation of a Appointment """
    __tablename__ = 'appointments'
    doctor_id = Column(String(60), ForeignKey('doctors.id'))
    patient_id = Column(String(60), ForeignKey('patients.id'))
    patient_name = Column(String(128))
    date = Column(Date, default=date.today())
    department_id = Column(String(60), ForeignKey('departments.id'))