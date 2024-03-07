#!/usr/bin/python3
""" holds class Department"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship


class Department(BaseModel, Base):
    """Representation of a Department """
    __tablename__ = 'departments'
    name = Column(String(128), nullable=False) #exist
    description = Column(String(128)) #exist
    department_head_id = Column(String(60), ForeignKey('doctors.id')) #exist
    appointments = relationship('Appointment', backref='department')
    # doctors = relationship("Doctor", secondary="doctor_department")
    # patients = relationship("Patient", secondary="patient_department")
    # appointments = relationship("Appointment", secondary="appointment_department")
    # specializations = relationship("Specialization", secondary="department_specialization")
    # rooms = relationship("Room", secondary="department_room")
    # beds = relationship("Bed", secondary="department_bed")
    # nurses = relationship("Nurse", secondary="department_nurse")
