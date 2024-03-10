""" Mapeadores para la capa de infraestructura del dominio de propiedades"""

from auditoria.seedwork.dominio.repositorios import Mapeador
from auditoria.seedwork.infraestructura.utils import unix_time_millis
from auditoria.modulos.propiedades.dominio.objetos_valor import Nombre, Email, Identificacion
from auditoria.modulos.propiedades.dominio.entidades import AuditoriaPropiedad
from .dto import AuditoriaPropiedad as AuditoriaPropiedadDTO

from auditoria.modulos.propiedades.dominio.eventos import AuditoriaPropiedadCreada, EventoAuditoriaPropiedad
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapadeadorEventosAuditoriaPropiedad(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            AuditoriaPropiedadCreada: self._entidad_a_auditoria_compania_creada,
        }

    def obtener_tipo(self) -> type:
        return EventoAuditoriaPropiedad.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_auditoria_compania_creada(self, entidad: AuditoriaPropiedadCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import AuditoriaPropiedadCreadaPayload, EventoAuditoriaPropiedadCreada

            payload = AuditoriaPropiedadCreadaPayload(
                id_compania=str(evento.id_compania),
                estado=str(evento.estado),
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoAuditoriaPropiedadCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'CompaniaCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'propiedades'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def entidad_a_dto(self, entidad: EventoAuditoriaPropiedad, version=LATEST_VERSION) -> AuditoriaPropiedadDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: AuditoriaPropiedadDTO, version=LATEST_VERSION) -> AuditoriaPropiedad:
        raise NotImplementedError


class MapeadorAuditoriaPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return AuditoriaPropiedad.__class__

    def entidad_a_dto(self, entidad: AuditoriaPropiedad) -> AuditoriaPropiedadDTO:
        auditoria_compania_dto = AuditoriaPropiedadDTO()
        auditoria_compania_dto.fecha_creacion = entidad.fecha_creacion
        auditoria_compania_dto.fecha_actualizacion = entidad.fecha_actualizacion
        auditoria_compania_dto.id = str(entidad.id)
        auditoria_compania_dto.nombre = str(entidad.nombre)
        auditoria_compania_dto.email = str(entidad.email)
        auditoria_compania_dto.identificacion = str(entidad.identificacion)
        auditoria_compania_dto.motivo_auditoria = str(entidad.motivo_auditoria)

        return auditoria_compania_dto

    def dto_a_entidad(self, dto: AuditoriaPropiedadDTO) -> AuditoriaPropiedad:
        # breakpoint()
        auditoria_compania = AuditoriaPropiedad(id=dto.id,
                            fecha_creacion=dto.fecha_creacion,
                            fecha_actualizacion=dto.fecha_actualizacion,
                            nombre=dto.nombre,
                            email=dto.email,
                            identificacion=dto.identificacion,
                            motivo_auditoria=dto.motivo_auditoria)

        return auditoria_compania
