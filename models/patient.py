#!/usr/bin/python3
""" holds class Patient"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship


class Patient(BaseModel, Base):
    """Representation of a Patient """
    __tablename__ = 'patients'
    name = Column(String(128), nullable=False)
    birth_date = Column(String(128))
    gender = Column(Enum("M", "F"), nullable=False)
    phone = Column(String(128), nullable=False)
