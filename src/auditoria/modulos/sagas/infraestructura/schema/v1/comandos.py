from pulsar.schema import *
from dataclasses import dataclass, field
from geograficos.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)


class ComandoCrearDatosGeograficosPayload(ComandoIntegracion):
    #id_compania = String()
    # TODO Cree los records para itinerarios
    nombre_propiedad = String()
    latitud = String()
    longitud = String()
    fecha_creacion = String()

class ComandoCrearDatosGeograficos(ComandoIntegracion):
    data = ComandoCrearDatosGeograficosPayload()