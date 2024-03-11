""" Mapeadores para la capa de infraestructura del dominio de propiedades"""

from auditoria.seedwork.dominio.repositorios import Mapeador
from auditoria.seedwork.infraestructura.utils import unix_time_millis
from auditoria.modulos.geograficos.dominio.objetos_valor import Latitud, Longitud, Identificacion, MotivoAuditoria
from auditoria.modulos.geograficos.dominio.entidades import AuditoriaGeografico
from .dto import AuditoriaGeografico as AuditoriaGeograficoDTO

from auditoria.modulos.geograficos.dominio.eventos import AuditoriaGeograficoCreada, EventoAuditoriaGeografico
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapadeadorEventosAuditoriaGeografico(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            AuditoriaGeograficoCreada: self._entidad_a_auditoria_geografico_creada,
        }

    def obtener_tipo(self) -> type:
        return EventoAuditoriaGeografico.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_auditoria_geografico_creada(self, entidad: AuditoriaGeograficoCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import AuditoriaGeograficoCreadaPayload, EventoAuditoriaGeograficoCreada

            payload = AuditoriaGeograficoCreadaPayload(
                id_geografico=str(evento.id_geografico),
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoAuditoriaGeograficoCreada(id=str(evento.id))
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

    def entidad_a_dto(self, entidad: EventoAuditoriaGeografico, version=LATEST_VERSION) -> AuditoriaGeograficoDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: AuditoriaGeograficoDTO, version=LATEST_VERSION) -> AuditoriaGeografico:
        raise NotImplementedError


class MapeadorAuditoriaGeografico(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return AuditoriaGeografico.__class__

    def entidad_a_dto(self, entidad: AuditoriaGeografico) -> AuditoriaGeograficoDTO:
        auditoria_geografico_dto = AuditoriaGeograficoDTO()
        auditoria_geografico_dto.fecha_creacion = entidad.fecha_creacion
        auditoria_geografico_dto.fecha_actualizacion = entidad.fecha_actualizacion
        auditoria_geografico_dto.id = str(entidad.id)
        auditoria_geografico_dto.latitud = str(entidad.latitud)
        auditoria_geografico_dto.longitud = str(entidad.longitud)
        auditoria_geografico_dto.identificacion = str(entidad.identificacion)
        auditoria_geografico_dto.motivo_auditoria = str(entidad.motivo_auditoria)

        return auditoria_geografico_dto

    def dto_a_entidad(self, dto: AuditoriaGeograficoDTO) -> AuditoriaGeografico:
        # breakpoint()
        auditoria_geografico = AuditoriaGeografico(id=dto.id,
                            fecha_creacion=dto.fecha_creacion,
                            fecha_actualizacion=dto.fecha_actualizacion,
                            latitud=dto.latitud,
                            longitud=dto.longitud,
                            identificacion=dto.identificacion,
                            motivo_auditoria=dto.motivo_auditoria)

        return auditoria_geografico
