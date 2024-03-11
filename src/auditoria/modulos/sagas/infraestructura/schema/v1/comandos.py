from pulsar.schema import *
from dataclasses import dataclass, field
from geograficos.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)


class ComandoCrearDatosGeograficosPayload(ComandoIntegracion):
    #id_compania = String()
    nombre_propiedad = String()
    latitud = String()
    longitud = String()
    fecha_creacion = String()

class ComandoCrearDatosGeograficos(ComandoIntegracion):
    data = ComandoCrearDatosGeograficosPayload()

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()
    identificacion_catastral = String()
    nit = String()
    nombre = String()
    fecha_creacion = String()
class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()

class ComandoRechazarDatosGeograficosPayload(ComandoIntegracion):
    geograficos_id = String()

class ComandoRechazarDatosGeograficos(ComandoIntegracion):
    data = ComandoRechazarDatosGeograficosPayload()

class ComandoRechazarPropiedadPayload(ComandoIntegracion):
    propiedad_id = String()
class ComandoRechazarPropiedad(ComandoIntegracion):
    data = ComandoRechazarPropiedadPayload()