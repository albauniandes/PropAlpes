import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from companias.modulos.ingestion.infraestructura.schema.v1.eventos import EventoCompaniaCreada
from companias.modulos.ingestion.infraestructura.schema.v1.comandos import ComandoCrearCompania

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
        consumidor = cliente.subscribe('comandos-compania', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='compania-sub-comandos',
                                       schema=AvroSchema(ComandoCrearCompania)
                                       )

        while True:
            mensaje = consumidor.receive()
            breakpoint()
            datos = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()