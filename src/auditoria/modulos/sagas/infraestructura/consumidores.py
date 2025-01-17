import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime
from auditoria.modulos.sagas.aplicacion.comandos.geograficos import RechazarDatosGeograficos
from auditoria.modulos.sagas.aplicacion.comandos.propiedades import RechazarPropiedad

from auditoria.modulos.sagas.infraestructura.schema.v1.eventos import EventoDatosGeograficosCreados, \
    EventoPropiedadCreada
from auditoria.modulos.sagas.infraestructura.schema.v1.comandos import (ComandoCrearDatosGeograficos,
                                                                        ComandoCrearPropiedad,
                                                                        ComandoRechazarPropiedad,
                                                                        ComandoRechazarDatosGeograficos,
                                                                        )

from auditoria.modulos.sagas.aplicacion.coordinadores.saga_auditorias import oir_mensaje, almacenar_mensaje
from auditoria.seedwork.aplicacion.comandos import ejecutar_comando

from auditoria.seedwork.infraestructura import utils


def suscribirse_a_topicos(app=None):
    import re
    cliente = None
    try:
        # breakpoint()
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        topic_pattern = re.compile('persistent://public/default/topic-.*')
        consumer = cliente.subscribe(topic_pattern, 'sub-auditoria')
        while True:
            msg = consumer.receive()
            try:
                topic_schema_dict = {
                    'topic-comando-crear-datos-geograficos': ComandoCrearDatosGeograficos,
                    'topic-eventos-datos-geograficos': EventoDatosGeograficosCreados,
                    'topic-comando-crear-propiedad': ComandoCrearPropiedad,
                    'topic-eventos-propiedad-creada': EventoPropiedadCreada,
                    'topic-comando-rollback-propiedad' : ComandoRechazarPropiedad,
                    'topic-comando-rollback-datos-geograficos' : ComandoRechazarDatosGeograficos
                }
                print(f'!!!!!!!!!!!!TOPICO: {msg.topic_name()}')

                schema_list = [ComandoCrearPropiedad,
                               ComandoCrearDatosGeograficos,
                               EventoPropiedadCreada,
                               EventoDatosGeograficosCreados,
                               ComandoRechazarPropiedad,
                               ComandoRechazarDatosGeograficos]

                decoded_schema = None

                topic_without_prefix = msg.topic_name().replace("persistent://public/default/", "")
                print(topic_without_prefix)
                schema = topic_schema_dict[topic_without_prefix]

                data_decoded = AvroSchema(schema).decode(msg.data())

                # for schema in schema_list:
                #     print(schema.__name__)
                #     try:
                #         data_decoded = AvroSchema(schema).decode(msg.data())
                #         print("Original message", msg.data())
                #         print("Decoded message:", data_decoded.data.__dict__)
                #         decoded_schema = schema
                #         break
                #     except Exception as e:
                #         print("Error decoding message:", e)
                #
                # print(f"RECEIVED MESSAGE / SCHEMA {data_decoded.data.__dict__}/{decoded_schema.__name__}")
                # almacenar_mensaje(data_decoded.data.__dict__, decoded_schema)
                almacenar_mensaje(data_decoded.data.__dict__, schema)
                # Acknowledge successful processing of the message
                consumer.acknowledge(msg)
                print("##########################################")
                print(schema.__name__)
                print("##########################################")
                if schema.__name__ == "EventoPropiedadCreada":

                    print("-----------------------")
                    print(data_decoded.data.__dict__)
                    propiedad = data_decoded.data.__dict__
                    print(propiedad["nombre"])
                    print("-----------------------")
                    if propiedad["nombre"] == "invalid_name":
                        time.sleep(15)
                        comando = RechazarPropiedad()
                        comando.propiedad_id = propiedad['id_propiedad']
                        ejecutar_comando(comando)

                if schema.__name__ == "EventoDatosGeograficosCreados":

                    print("-----------------------")
                    print(schema.data.__dict__)
                    geograficos = data_decoded.data.__dict__
                    print(geograficos["nombre_propiedad"])
                    print("-----------------------")
                    if geograficos["nombre_propiedad"] == "invalid_name":
                        time.sleep(15)
                        comando = RechazarDatosGeograficos()
                        comando.geograficos_id = geograficos['id_geograficos']
                        ejecutar_comando(comando)

            except Exception:
                # Message failed to be processed
                consumer.negative_acknowledge(msg)
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose a topicos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_eventos_geograficos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-eventos-datos-geograficos', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(EventoDatosGeograficosCreados))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento Geograficos recibido: {datos}')

            # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
            # ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
            # ejecutar_proyeccion(
            #     ProyeccionReservasLista(datos.id_reserva, datos.id_cliente, datos.estado, datos.fecha_creacion,
            #                             datos.fecha_creacion), app=app)

            consumidor.acknowledge(mensaje)
            print("##################")
            print(datos.nombre_propiedad)
            if datos.nombre_propiedad == "invalid_name":
                time.sleep(15)
                comando = RechazarDatosGeograficos()
                comando.geograficos_id = datos.id_geograficos
                ejecutar_comando(comando)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos_geograficos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')

        consumidor = cliente.subscribe('topic-comando-crear-datos-geograficos',
                                       consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(ComandoCrearDatosGeograficos)
                                       )

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando Geografico recibido: {mensaje.value().data}')

            fecha_creacion = utils.millis_a_datetime(int(datos.fecha_creacion)).strftime('%Y-%m-%dT%H:%M:%SZ')
            id_geograficos = str(uuid.uuid4())
            # try:
            #     with app.app_context():
            #
            #         comando = CrearDatosGeograficos(fecha_creacion, fecha_creacion,
            #                                 id_geograficos, datos.nombre_propiedad, datos.latitud,
            #                                 datos.longitud)
            #         print(f'Ejecutando comando: {comando}')
            #         ejecutar_comando(comando)
            #
            # except:
            #     logging.error('ERROR: Procesando eventos!')
            #     traceback.print_exc()

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_eventos_propiedades(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-eventos-propiedad', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(EventoPropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento Propiedades recibido: {datos}')

            # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
            # ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
            # ejecutar_proyeccion(
            #     ProyeccionReservasLista(datos.id_reserva, datos.id_cliente, datos.estado, datos.fecha_creacion,
            #                             datos.fecha_creacion), app=app)

            consumidor.acknowledge(mensaje)
            print(datos.nombre)
            if datos.nombre == "invalid_name":
                time.sleep(15)
                comando = RechazarPropiedad()
                comando.propiedad_id = datos.id_propiedad
                print("$$$$$$$$$$$$$$$$$$$$$444")
                print(comando)
                ejecutar_comando(comando)

        cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos_propiedades(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')

        consumidor = cliente.subscribe('topic-comando-crear-propiedad', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(ComandoCrearPropiedad)
                                       )

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando Propiedades recibido: {mensaje.value().data}')

            fecha_creacion = utils.millis_a_datetime(int(datos.fecha_creacion)).strftime('%Y-%m-%dT%H:%M:%SZ')
            id_propiedad = str(uuid.uuid4())
            # try:
            #     with app.app_context():
            #
            #         comando = CrearPropiedad(fecha_creacion, fecha_creacion,
            #                                 id_propiedad, datos.identificacion_catastral, datos.nit,
            #                                 datos.nombre)
            #
            #         ejecutar_comando(comando)
            #
            #         # if len(datos.nombre) == 0 or len(datos.email) or len(datos.identificacion):
            #         #     despachador = Despachador()
            #         #     despachador.publicar_comando(evento, 'topic-eventos-compania')
            #
            #
            # except:
            #     logging.error('ERROR: Procesando eventos!')
            #     traceback.print_exc()

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
