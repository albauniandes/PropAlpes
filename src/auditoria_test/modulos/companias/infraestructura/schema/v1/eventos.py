from pulsar.schema import *
from companias.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from companias.seedwork.infraestructura.utils import time_millis
import uuid


class AuditoriaCompaniaCreadaPayload(Record):
    id_compania = String()
    estado = String()
    fecha_creacion = Long()


class EventoAuditoriaCompaniaCreada(EventoIntegracion):
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
    data = AuditoriaCompaniaCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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