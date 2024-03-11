from auditoria.seedwork.aplicacion.comandos import Comando
from auditoria.modulos.propiedades.aplicacion.dto import AuditoriaPropiedadDTO
from .base import CrearAuditoriaPropiedadBaseHandler, EliminarAuditoriaPropiedadBaseHandler
from dataclasses import dataclass, field
from auditoria.seedwork.aplicacion.comandos import ejecutar_comando as comando

from auditoria.modulos.propiedades.dominio.entidades import AuditoriaPropiedad
from auditoria.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from auditoria.modulos.propiedades.aplicacion.mapeadores import MapeadorAuditoriaPropiedad
from auditoria.modulos.propiedades.infraestructura.repositorios import RepositorioAuditoriaPropiedads, RepositorioEventosAuditoriaPropiedads

from pydispatch import dispatcher

@dataclass
class EliminarAuditoriaPropiedad(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre: str
    email: str
    identificacion: str
    motivo_auditoria: str


class EliminarAuditoriaPropiedadHandler(EliminarAuditoriaPropiedadBaseHandler):
    ...
    
#     def handle(self, comando: CrearAuditoriaPropiedad):
#         auditoria_propiedad_dto = AuditoriaPropiedadDTO(
#                 fecha_actualizacion=comando.fecha_actualizacion
#             ,   fecha_creacion=comando.fecha_creacion
#             ,   id=comando.id
#             ,   nombre=comando.nombre
#             ,   email=comando.email
#             ,   identificacion=comando.identificacion
#             ,   motivo_auditoria=comando.motivo_auditoria)
#         #breakpoint()
#         auditoria_propiedad: AuditoriaPropiedad = self.fabrica_ingestion.crear_objeto(auditoria_propiedad_dto, MapeadorAuditoriaPropiedad())
#         auditoria_propiedad.crear_auditoria_propiedad(auditoria_propiedad)
#         #breakpoint()
#         repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditoriaPropiedads.__class__)
#         repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosAuditoriaPropiedads)
#
#         #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, auditoria)
#         #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, auditoria, repositorio_eventos_func=repositorio_eventos.agregar)
#
#         repositorio.agregar(auditoria_propiedad)
#
#         for evento in auditoria_propiedad.eventos:
#             dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
#         #UnidadTrabajoPuerto.commit()
#         from auditoria.config.db import db
#         db.session.commit()
#
@comando.register(EliminarAuditoriaPropiedad)
def ejecutar_comando_eliminar_auditoria_propiedad(comando: EliminarAuditoriaPropiedad):
    handler = EliminarAuditoriaPropiedadHandler()
    handler.handle(comando)
