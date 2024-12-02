import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    password = Column(String(30), nullable=False)
    subscripcionDate = (Column(DateTime))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Caract(Base):
    _tablename_ = 'caract'
    id = Column(Integer, primary_key=True)
    gender = Column(String(100))
    hair_color = Column(String(100))
    name = Column (String(100), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Planets(Base):
    _tablename_ = 'planets'
    id = Column(Integer, primary_key=True)
    climate= Column (String(100))
    name= Column (String(100), nullable=False)
    population = (Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
