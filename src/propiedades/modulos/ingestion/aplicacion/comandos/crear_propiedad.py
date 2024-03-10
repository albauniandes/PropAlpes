from propiedades.modulos.ingestion.infraestructura.despachadores import Despachador
from propiedades.seedwork.aplicacion.comandos import Comando
from propiedades.modulos.ingestion.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.comandos import ejecutar_comando as comando

from propiedades.modulos.ingestion.dominio.entidades import Propiedad
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedades.modulos.ingestion.aplicacion.mapeadores import MapeadorPropiedad
from propiedades.modulos.ingestion.infraestructura.repositorios import RepositorioPropiedad, RepositorioEventosPropiedad

from pydispatch import dispatcher

@dataclass
class CrearPropiedad(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    identificacion_catastral: str
    nit: str
    nombre: str


class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   identificacion_catastral=comando.identificacion_catastral
            ,   nit=comando.nit
            ,   nombre=comando.nombre)

        propiedad: Propiedad = self.fabrica_ingestion.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)
        #breakpoint()
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedad.__class__)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosPropiedad)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania, repositorio_eventos_func=repositorio_eventos.agregar)

        repositorio.agregar(propiedad)

        for evento in propiedad.eventos:
            dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
        #UnidadTrabajoPuerto.commit()
            
            despachador = Despachador()
            despachador.publicar_evento(evento, "eventos-propiedad-creada")
        
        from propiedades.config.db import db
        db.session.commit()

@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
    