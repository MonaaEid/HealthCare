#!/usr/bin/python3
""" holds class Employee"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship


class Employee(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'employees'
    name = Column(String(128), nullable=False) #exist
    birth_date = Column(String(128)) #exist
    gender = Column(Enum("M", "F"), nullable=False) #exist
    email = Column(String(128)) #exist
    phone = Column(String(128), nullable=False) #exist
    address = Column(String(128)) #exist
    salary = Column(Integer) #exist
