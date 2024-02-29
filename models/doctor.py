#!/usr/bin/python3
""" holds class Doctor"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship


class Doctor(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'doctors'
    name = Column(String(128), nullable=False)
    birth_date = Column(String(128))
    gender = Column(Enum("M", "F"), nullable=False)
    email = Column(String(128))
    phone = Column(String(128))
    address = Column(String(128))
    # specializations = relationship("Specialization", secondary="doctor_specialization")
    # appointments = relationship("Appointment", back_populates="doctor")
    # patients = relationship("Patient", secondary="appointments")
    salary = Column(Integer, nullable=False)
    # department_id = Column(String(60), ForeignKey('departments.id'), nullable=False)
