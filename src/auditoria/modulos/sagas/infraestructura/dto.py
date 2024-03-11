"""DTOs para la capa de infraestructura del dominio de ingestion"""

from geograficos.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint
import datetime
import uuid

Base = db.declarative_base()


class Sagalog(db.Model):
    __tablename__ = "sagalog"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    tipo_accion = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contenido = db.Column(db.Text, nullable=False)