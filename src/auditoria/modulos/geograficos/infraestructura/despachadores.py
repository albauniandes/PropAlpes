import pulsar
from pulsar.schema import *

from auditoria.modulos.geograficos.infraestructura.schema.v1.eventos import EventoAuditoriaGeograficoCreada, AuditoriaGeograficoCreadaPayload
from auditoria.modulos.geograficos.infraestructura.schema.v1.comandos import ComandoCrearAuditoriaGeografico, ComandoCrearAuditoriaGeograficoPayload
from companias.seedwork.infraestructura import utils

from auditoria.modulos.propiedades.infraestructura.mapeadores import MapadeadorEventosAuditoriaPropiedad

class Despachador:
    def __init__(self):
        self.mapper = MapadeadorEventosAuditoriaPropiedad()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoAuditoriaGeograficoCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearAuditoriaGeograficoPayload(
            id_compania=str(comando.id_compania)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearAuditoriaGeografico(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearAuditoriaGeografico))
