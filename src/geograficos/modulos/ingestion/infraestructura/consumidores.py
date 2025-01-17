import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from geograficos.modulos.ingestion.infraestructura.schema.v1.eventos import EventoDatosGeograficosCreados
from geograficos.modulos.ingestion.infraestructura.schema.v1.comandos import ComandoCrearDatosGeograficos, ComandoRechazarDatosGeograficos
from geograficos.modulos.ingestion.aplicacion.comandos.crear_datos_geograficos import CrearDatosGeograficos
from geograficos.modulos.ingestion.aplicacion.comandos.rechazar_datos_geograficos import RechazarDatosGeograficos
from geograficos.seedwork.aplicacion.comandos import ejecutar_comando

from geograficos.modulos.ingestion.aplicacion.comandos.crear_datos_geograficos import CrearDatosGeograficos
from geograficos.seedwork.aplicacion.comandos import ejecutar_comando

from geograficos.seedwork.infraestructura import utils


"""def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-eventos-datos-geograficos', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(EventoDatosGeograficosCreados))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido: {datos}')

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()"""


def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')

        consumidor = cliente.subscribe('topic-comando-crear-datos-geograficos', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(ComandoCrearDatosGeograficos)
                                       )

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}')

            fecha_creacion = utils.millis_a_datetime(int(datos.fecha_creacion)).strftime('%Y-%m-%dT%H:%M:%SZ')
            id_geograficos = str(uuid.uuid4())
            try:
                with app.app_context():

                    comando = CrearDatosGeograficos(fecha_creacion, fecha_creacion,
                                            id_geograficos, datos.nombre_propiedad, datos.latitud,
                                            datos.longitud)
                    print(f'Ejecutando comando: {comando}')
                    ejecutar_comando(comando)

            except:
                logging.error('ERROR: Procesando eventos!')
                traceback.print_exc()


            consumidor.acknowledge(mensaje)


        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos_rollback(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')

        consumidor = cliente.subscribe('topic-comando-rollback-datos-geograficos', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(ComandoRechazarDatosGeograficos)
                                       )

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}')

            try:
                with app.app_context():
                    print("#####################")
                    print(datos.geograficos_id)
                    ##########
                    comando = RechazarDatosGeograficos()
                    comando.geograficos_id = datos.geograficos_id
                    print(f'Ejecutando comando: {comando}')
                    ejecutar_comando(comando)
                    print("Datos geograficos fueron eliminados")

            except:
                logging.error('ERROR: Procesando eventos!')
                traceback.print_exc()


            consumidor.acknowledge(mensaje)


        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()