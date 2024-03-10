from pulsar.schema import *
from dataclasses import dataclass, field
from propiedades.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)


class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()
    # TODO Cree los records para itinerarios
    identificacion_catastral = String()
    nit = String()
    nombre = String()
    fecha_creacion = String()
class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()