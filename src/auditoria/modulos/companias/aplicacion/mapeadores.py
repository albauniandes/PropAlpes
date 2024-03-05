from companias.seedwork.aplicacion.dto import Mapeador as AppMap
from companias.seedwork.dominio.repositorios import Mapeador as RepMap
from auditoria.modulos.companias.dominio.entidades import AuditoriaCompania
from auditoria.modulos.companias.dominio.objetos_valor import MotivoAuditoria, Nombre, Email, Identificacion
from .dto import AuditoriaCompaniaDTO

from datetime import datetime


class MapeadorAuditoriaCompaniaDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> AuditoriaCompaniaDTO:
        # breakpoint()

        info_auditoria_compania = externo.get('compania')
        print(info_auditoria_compania)
        auditoria_compania_dto = AuditoriaCompaniaDTO(email=info_auditoria_compania.get('email'),
                                                      nombre=info_auditoria_compania.get('nombre'),
                                                      identificacion=info_auditoria_compania.get('identificacion'),
                                                      motivo_auditoria=info_auditoria_compania.get('motivo_auditoria')
                                                      )

        return auditoria_compania_dto

    def dto_a_externo(self, dto: AuditoriaCompaniaDTO) -> dict:
        return dto.__dict__


class MapeadorAuditoriaCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return AuditoriaCompania.__class__

    def entidad_a_dto(self, entidad: AuditoriaCompania) -> AuditoriaCompaniaDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _nombre = str(entidad.nombre)
        _email = str(entidad.email)
        _identificacion = str(entidad.identificacion)
        _motivo_auditoria = str(entidad.motivo_auditoria)

        return AuditoriaCompaniaDTO(fecha_creacion,
                                    fecha_actualizacion,
                                    _id,
                                    _nombre,
                                    _email,
                                    _identificacion,
                                    _motivo_auditoria)

    def dto_a_entidad(self, dto: AuditoriaCompaniaDTO) -> AuditoriaCompania:
        # breakpoint()
        auditoria_compania = AuditoriaCompania(nombre=dto.nombre,
                                               identificacion=dto.identificacion,
                                               email=dto.email,
                                               motivo_auditoria=dto.motivo_auditoria)

        return auditoria_compania
