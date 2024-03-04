from pulsar.schema import *
from dataclasses import dataclass, field
from geograficos.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)


class ComandoCrearDatosGeograficosPayload(ComandoIntegracion):
    id_datos_geograficos = String()
    # TODO Cree los records para itinerarios


class ComandoCrearDatosGeograficos(ComandoIntegracion):
    data = ComandoCrearDatosGeograficosPayload()