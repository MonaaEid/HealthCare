#!/usr/bin/python3
""" holds class Doctor"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Enum, Table
from sqlalchemy.orm import relationship

class Doctor(BaseModel, Base):
    """Representation of a Doctor"""
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
