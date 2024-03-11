import pulsar
from pulsar.schema import *

from auditoria.modulos.sagas.infraestructura.schema.v1.eventos import EventoDatosGeograficosCreada, DatosGeograficosCreadaPayload
from auditoria.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearDatosGeograficos, ComandoCrearDatosGeograficosPayload
from auditoria.seedwork.infraestructura import utils

from auditoria.modulos.sagas.infraestructura.mapeadores import MapadeadorEventosDatosGeograficos

class Despachador:
    def __init__(self):
        self.mapper = MapadeadorEventosDatosGeograficos()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoDatosGeograficosCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearDatosGeograficosPayload(
            id_geograficos=str(comando.id_geograficos)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearDatosGeograficos(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearDatosGeograficos))