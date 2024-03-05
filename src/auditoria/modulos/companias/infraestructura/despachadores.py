import pulsar
from pulsar.schema import *

from auditoria.modulos.companias.infraestructura.schema.v1.eventos import EventoAuditoriaCompaniaCreada, AuditoriaCompaniaCreadaPayload
from auditoria.modulos.companias.infraestructura.schema.v1.comandos import ComandoCrearAuditoriaCompania, ComandoCrearAuditoriaCompaniaPayload
from companias.seedwork.infraestructura import utils

from auditoria.modulos.companias.infraestructura.mapeadores import MapadeadorEventosAuditoriaCompania

class Despachador:
    def __init__(self):
        self.mapper = MapadeadorEventosAuditoriaCompania()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoAuditoriaCompaniaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearAuditoriaCompaniaPayload(
            id_compania=str(comando.id_compania)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearAuditoriaCompania(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearAuditoriaCompania))
