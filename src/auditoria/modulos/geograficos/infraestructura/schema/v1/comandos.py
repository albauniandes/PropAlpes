from pulsar.schema import *
from dataclasses import dataclass, field
from companias.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)


class ComandoCrearAuditoriaGeograficoPayload(ComandoIntegracion):
    # TODO Cree los records para itinerarios
    latitud = String()
    longitud = String()
    identificacion = String()
    fecha_creacion = String()
    motivo_auditoria = String()


class ComandoCrearAuditoriaGeografico(ComandoIntegracion):
    data = ComandoCrearAuditoriaGeograficoPayload()