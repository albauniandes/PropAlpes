from pulsar.schema import *
from propiedades.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from propiedades.seedwork.infraestructura.utils import time_millis
import uuid


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)