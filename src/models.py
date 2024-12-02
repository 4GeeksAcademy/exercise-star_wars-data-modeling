import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#class Person(Base):
   # __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #name = Column(String(250), nullable=False)


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
    
class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name= Column (String(100), nullable=False)
    climate = Column (String(100))
    cleated= Column (String(100))


class Caract(Base):
    __tablename__ = 'caract'
    id = Column(Integer, primary_key=True)
    gender = Column(String(100))
    hair_color = Column(String(100))
    name = Column (String(100), nullable=False)
    

class Nave(Base):
    __tablename__ = 'nave'
    id = Column(Integer, primary_key=True)
    name= Column (String(100), nullable=False)
    model = Column (String(100))
    consumables= Column (String(100))

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Usuario_id =Column (Integer, ForeignKey('usuario.id'))
    usuario = relationship (Usuario)
    Planetas_id = Column (Integer, ForeignKey('planetas.id'))
    planetas = relationship (Planetas)
    Caract_id = Column(Integer, ForeignKey('caract.id'))
    caract = relationship(Caract)
    Nave_id = Column (Integer, ForeignKey('nave.id'))
    nave = relationship (Nave)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
 