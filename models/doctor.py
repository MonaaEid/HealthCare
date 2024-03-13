#!/usr/bin/python3
""" holds class Doctor"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Enum, Table
from sqlalchemy.orm import relationship


# appointments = Table(
#     'appointments',
#     Base.metadata,
#     Column('doctor_id', String(60), ForeignKey('doctors.id', onupdate='CASCADE',
#                                             ondelete='CASCADE'), primary_key=True),
#     Column('patient_id', String(60), ForeignKey('patients.id', onupdate='CASCADE',
#                                             ondelete='CASCADE'), primary_key=True)
# )

class Doctor(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'doctors'
    name = Column(String(128), nullable=False) #exist
    birth_date = Column(String(128)) #exist
    gender = Column(Enum("M", "F"), nullable=False) #exist
    email = Column(String(128)) #exist
    phone = Column(String(128)) #exist
    address = Column(String(128)) #exist
    salary = Column(Integer, nullable=False) #exist
    appointments = relationship('Appointment', backref='doctor')
    department = relationship('Department', backref='doctor')
