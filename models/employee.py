#!/usr/bin/python3
""" holds class Employee"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship


class Employee(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'employees'
    name = Column(String(128), nullable=False)
    birth_date = Column(String(128))
    gender = Column(Enum, nullable=False)
    email = Column(String(128))
    phone = Column(String(128), nullable=False)
    address = Column(String(128))
    salary = Column(Integer)
