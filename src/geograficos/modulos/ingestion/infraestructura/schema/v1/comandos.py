from pulsar.schema import *
from dataclasses import dataclass, field
from geograficos.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)


class ComandoCrearDatosGeograficosPayload(ComandoIntegracion):
    nombre_propiedad = String()
    latitud = String()
    longitud = String()
    fecha_creacion = String()
class ComandoCrearDatosGeograficos(ComandoIntegracion):
    data = ComandoCrearDatosGeograficosPayload()


class ComandoRechazarDatosGeograficosPayload(ComandoIntegracion):
    geograficos_id = String()

class ComandoRechazarDatosGeograficos(ComandoIntegracion):
    data = ComandoRechazarDatosGeograficosPayload()