import pulsar
from pulsar.schema import *

from auditoria_test.modulos.companias.infraestructura.schema.v1.eventos import EventoAuditoriaCompaniaCreada, AuditoriaCompaniaCreadaPayload
from auditoria_test.modulos.companias.infraestructura.schema.v1.comandos import ComandoCrearAuditoriaCompania, ComandoCrearAuditoriaCompaniaPayload, ComandoRechazarDatosGeograficos
from companias.seedwork.infraestructura import utils
from companias.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from auditoria_test.modulos.companias.infraestructura.mapeadores import MapadeadorEventosAuditoriaCompania

class Despachador:
    def __init__(self):
        self.mapper = MapadeadorEventosAuditoriaCompania()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoRechazarDatosGeograficos))
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

    def rechazar_datos_geograficos(self, id_geograficos):
        payload = dict(
            id_geograficos = id_geograficos,
        )
        comando = dict(
            id = str(id_geograficos+"1"),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoRechazoGeograficos",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        self._publicar_mensaje(comando, "comando-rollback-datos-geograficos", AvroSchema(ComandoRechazarDatosGeograficos))
