"""DTOs para la capa de infrastructura del dominio de ingestion"""

from companias.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla companias e itinerarios
companias_itinerarios = db.Table(
    "companias_itinerarios",
    db.Model.metadata,
    db.Column("compania_id", db.String, db.ForeignKey("companias.id")),
    db.Column("odo_orden", db.Integer),
    db.Column("segmento_orden", db.Integer),
    db.Column("leg_orden", db.Integer),
    db.Column("fecha_salida", db.DateTime),
    db.Column("fecha_llegada", db.DateTime),
    db.Column("origen_codigo", db.String),
    db.Column("destino_codigo", db.String),
    db.ForeignKeyConstraint(
        ["odo_orden", "segmento_orden", "leg_orden", "fecha_salida", "fecha_llegada", "origen_codigo", "destino_codigo"],
        ["itinerarios.odo_orden", "itinerarios.segmento_orden", "itinerarios.leg_orden", "itinerarios.fecha_salida", "itinerarios.fecha_llegada", "itinerarios.origen_codigo", "itinerarios.destino_codigo"]
    )
)

class Itinerario(db.Model):
    __tablename__ = "itinerarios"
    odo_orden = db.Column(db.Integer, primary_key=True, nullable=False)
    segmento_orden = db.Column(db.Integer, primary_key=True, nullable=False)
    leg_orden = db.Column(db.Integer, primary_key=True, nullable=False)
    fecha_salida = db.Column(db.DateTime, nullable=False, primary_key=True)
    fecha_llegada = db.Column(db.DateTime, nullable=False, primary_key=True)
    origen_codigo = db.Column(db.String, nullable=False, primary_key=True)
    destino_codigo= db.Column(db.String, nullable=False, primary_key=True)


class Compania(db.Model):
    __tablename__ = "companias"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    itinerarios = db.relationship('Itinerario', secondary=companias_itinerarios, backref='companias')
