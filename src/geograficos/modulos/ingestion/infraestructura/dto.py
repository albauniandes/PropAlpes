"""DTOs para la capa de infraestructura del dominio de ingestion"""

from geograficos.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

import uuid

Base = db.declarative_base()

class DatosGeograficos(db.Model):
    __tablename__ = "geograficos"
    id = db.Column(db.String(40), primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    nombre_propiedad = db.Column(db.String(40))
    latitud = db.Column(db.String(40))
    longitud = db.Column(db.String(40))

class EventosDatosGeograficos(db.Model):
    __tablename__ = "eventos_datos_geograficos"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)