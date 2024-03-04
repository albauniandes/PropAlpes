import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from companias.modulos.ingestion.infraestructura.schema.v1.eventos import EventoCompaniaCreada
from companias.modulos.ingestion.infraestructura.schema.v1.comandos import ComandoCrearCompania
from companias.modulos.ingestion.aplicacion.comandos.crear_compania import CrearCompania

from companias.seedwork.aplicacion.comandos import ejecutar_comando

#from companias.modulos.ingestion.infraestructura.proyecciones import ProyeccionReservasLista, ProyeccionReservasTotales
#from companias.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from companias.seedwork.infraestructura import utils


def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='compania-sub-eventos',
                                       schema=AvroSchema(EventoCompaniaCreada))

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
        consumidor = cliente.subscribe('comando-crear-compania', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='creacion-compania-sub-comandos',
                                       schema=AvroSchema(ComandoCrearCompania))

        while True:
            mensaje = consumidor.receive()
            valor = mensaje.value()
            print(f'Comando recibido: {mensaje.value().data}')

            fecha_creacion = utils.millis_a_datetime(valor.data.fecha_creacion).strftime('%Y-%m-%dT%H:%M:%SZ')
            id_compania = str(uuid.uuid4())

            try:
                with app.app_context():
                    comando = CrearCompania(fecha_creacion, fecha_creacion, id_compania, valor.data.nombre, valor.data.email, valor.data.identificacion)
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