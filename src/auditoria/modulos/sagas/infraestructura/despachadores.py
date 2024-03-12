import uuid
import pulsar
from pulsar.schema import *
import typing
from auditoria.modulos.sagas.infraestructura.schema.v1.eventos import EventoDatosGeograficosCreados, DatosGeograficosCreadosPayload, EventoPropiedadCreada, PropiedadCreadaPayload
from auditoria.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearDatosGeograficos, ComandoRechazarDatosGeograficosPayload, ComandoRechazarDatosGeograficos, ComandoCrearPropiedad, ComandoRechazarPropiedad, ComandoRechazarPropiedadPayload
from auditoria.seedwork.infraestructura import utils

from auditoria.modulos.sagas.infraestructura.mapeadores import MapadeadorEventosDatosGeograficos, MapadeadorEventosPropiedad

class DespachadorGeograficos:
    def __init__(self):
        self.mappergeografico = MapadeadorEventosDatosGeograficos()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_mensaje(self, mensaje, topico, schema):
        json_schema = utils.consultar_schema_registry(schema)  
        avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)
        # breakpoint()
        print(mensaje, topico)
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=avro_schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mappergeografico.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando_rechazar_geograficos(self, geograficos_id):
        payload = dict(
            geograficos_id=str(geograficos_id)
        )
        comando_integracion = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoRechazarDatosGeograficos",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "Auditoria",
            data = payload
        )
        print("????????????????????????????")
        print(comando_integracion["data"])
        print("????????????????????????????")


        self.publicar_mensaje(comando_integracion, "topic-comando-rollback-datos-geograficos", "public/default/topic-comando-rollback-datos-geograficos")


class DespachadorPropiedades:
    def __init__(self):
        self.mapperpropiedad = MapadeadorEventosPropiedad()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_mensaje(self, mensaje, topico, schema):
        json_schema = utils.consultar_schema_registry(schema)  
        avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)
        # breakpoint()
        print(mensaje, topico)
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=avro_schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapperpropiedad.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando_rechazar_propiedad(self, propiedad_id):
        payload = dict(
            propiedad_id_id=str(propiedad_id)
        )
        comando_integracion = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoRechazarPropiedad",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "Auditoria",
            data = payload
        )
        print("????????????????????????????")
        print(comando_integracion["data"])
        print("????????????????????????????")


        self.publicar_mensaje(comando_integracion, "topic-comando-rollback-propiedad", "public/default/topic-comando-rollback-propiedad")
