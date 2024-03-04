from pulsar.schema import *
from dataclasses import dataclass, field
from companias.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)


class ComandoCrearAuditoriaCompaniaPayload(ComandoIntegracion):
    # TODO Cree los records para itinerarios
    nombre = String()
    email = String()
    identificacion = String()
    fecha_creacion = String()
    motivo_auditoria = String()


class ComandoCrearAuditoriaCompania(ComandoIntegracion):
    data = ComandoCrearAuditoriaCompaniaPayload()