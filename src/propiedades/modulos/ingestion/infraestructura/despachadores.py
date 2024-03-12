import pulsar
from pulsar.schema import *

from propiedades.modulos.ingestion.infraestructura.schema.v1.eventos import EventoPropiedadCreada, PropiedadCreadaPayload
from propiedades.modulos.ingestion.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from propiedades.seedwork.infraestructura import utils

from propiedades.modulos.ingestion.infraestructura.mapeadores import MapadeadorEventosPropiedad

class Despachador:
    def __init__(self):
        self.mapper = MapadeadorEventosPropiedad()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearPropiedadPayload(
            id_propiedad=str(comando.id_propiedad)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))