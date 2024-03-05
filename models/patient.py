#!/usr/bin/python3
""" holds class Patient"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship


class Patient(BaseModel, Base):
    """Representation of a Patient """
    __tablename__ = 'patients'
    name = Column(String(128), nullable=False) #exist
    birth_date = Column(String(128)) #exist
    gender = Column(Enum("M", "F"), nullable=False) #exist
    phone = Column(String(128), nullable=False) #exist
    address = Column(String(128))
    appointments = relationship('Appointment', backref='patient')
