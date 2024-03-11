import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime
from propiedades.modulos.ingestion.aplicacion.comandos.rechazar_propiedad import RechazarPropiedad

from propiedades.modulos.ingestion.infraestructura.schema.v1.eventos import EventoPropiedadCreada
from propiedades.modulos.ingestion.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoRechazarPropiedad
from propiedades.modulos.ingestion.aplicacion.comandos.crear_propiedad import CrearPropiedad

from propiedades.seedwork.aplicacion.comandos import ejecutar_comando

from propiedades.modulos.ingestion.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedades.seedwork.aplicacion.comandos import ejecutar_comando

from propiedades.seedwork.infraestructura import utils


def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-eventos-propiedad', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(EventoPropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido: {datos}')


            # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
            # ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
            # ejecutar_proyeccion(
            #     ProyeccionReservasLista(datos.id_reserva, datos.id_cliente, datos.estado, datos.fecha_creacion,
            #                             datos.fecha_creacion), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos(app=None):
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
            print(f'Comando recibido: {mensaje.value().data}')

            fecha_creacion = utils.millis_a_datetime(int(datos.fecha_creacion)).strftime('%Y-%m-%dT%H:%M:%SZ')
            id_propiedad = str(uuid.uuid4())
            try:
                with app.app_context():

                    comando = CrearPropiedad(fecha_creacion, fecha_creacion,
                                            id_propiedad, datos.identificacion_catastral, datos.nit,
                                            datos.nombre)
                    ejecutar_comando(comando)

                    # if len(datos.nombre) == 0 or len(datos.email) or len(datos.identificacion):
                    #     despachador = Despachador()
                    #     despachador.publicar_comando(evento, 'topic-eventos-compania')


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

        consumidor = cliente.subscribe('topic-comando-rollback-propiedad', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='sub-propalpes',
                                       schema=AvroSchema(ComandoRechazarPropiedad)
                                       )

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}')

            try:
                with app.app_context():
                    print("#####################")
                    print(datos.propiedad_id)
                    ##########
                    comando = RechazarPropiedad()
                    comando.propiedad_id = datos.propiedad_id
                    print(f'Ejecutando comando: {comando}')
                    ejecutar_comando(comando)
                    print("Datos propiedad fueron eliminados")

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