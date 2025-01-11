#!/usr/bin/env python3

# imports
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create a Base class for the ORM
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

# Create the SQLite engine and initialize the database schema
engine = create_engine('sqlite:///students.db', future=True)
Base.metadata.create_all(engine)
