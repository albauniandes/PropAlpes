from pulsar.schema import *
from geograficos.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from geograficos.seedwork.infraestructura.utils import time_millis
import uuid


class DatosGeograficosCreadosPayload(Record):
    id_geograficos = String()
    estado = String()
    fecha_creacion = Long()
    nombre_propiedad = String()
    latitud = String()
    longitud = String()


class EventoDatosGeograficosCreados(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = DatosGeograficosCreadosPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    estado = String()
    fecha_creacion = Long()
    identificacion_catastral = String()
    nit = String()
    nombre = String()
    # fecha_creacion = String()


class EventoPropiedadCreada(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados,
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = PropiedadCreadaPayload()
