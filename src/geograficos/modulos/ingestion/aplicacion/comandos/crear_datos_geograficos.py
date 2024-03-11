from geograficos.modulos.ingestion.infraestructura.despachadores import Despachador
from geograficos.seedwork.aplicacion.comandos import Comando
from geograficos.modulos.ingestion.aplicacion.dto import DatosGeograficosDTO
from .base import CrearDatosGeograficosBaseHandler
from dataclasses import dataclass, field
from geograficos.seedwork.aplicacion.comandos import ejecutar_comando as comando

from geograficos.modulos.ingestion.dominio.entidades import DatosGeograficos
from geograficos.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from geograficos.modulos.ingestion.aplicacion.mapeadores import MapeadorDatosGeograficos
from geograficos.modulos.ingestion.infraestructura.repositorios import RepositorioDatosGeograficos, RepositorioEventosDatosGeograficos

from pydispatch import dispatcher

@dataclass
class CrearDatosGeograficos(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre_propiedad: str
    latitud: str
    longitud: str


class CrearDatosGeograficosHandler(CrearDatosGeograficosBaseHandler):
    
    def handle(self, comando: CrearDatosGeograficos):
        datos_geograficos_dto = DatosGeograficosDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   nombre_propiedad=comando.nombre_propiedad
            ,   latitud=comando.latitud
            ,   longitud=comando.longitud)
        #breakpoint()
        datos_geograficos: DatosGeograficos = self.fabrica_ingestion.crear_objeto(datos_geograficos_dto, MapeadorDatosGeograficos())
        datos_geograficos.crear_datos_geograficos(datos_geograficos)
        #breakpoint()
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioDatosGeograficos.__class__)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosDatosGeograficos)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania, repositorio_eventos_func=repositorio_eventos.agregar)

        repositorio.agregar(datos_geograficos)

        for evento in datos_geograficos.eventos:
            print("-------------------------------------------------------------------")
            print(evento)
            print("-------------------------------------------------------------------")
            dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
        #UnidadTrabajoPuerto.commit()
            
            despachador = Despachador()
            despachador.publicar_evento(evento, "topic-eventos-datos-geograficos-creados")

        from geograficos.config.db import db
        db.session.commit()

@comando.register(CrearDatosGeograficos)
def ejecutar_comando_crear_datos_geograficos(comando: CrearDatosGeograficos):
    handler = CrearDatosGeograficosHandler()
    handler.handle(comando)
    