""" Mapeadores para la capa de infraestructura del dominio de companias"""

from companias.seedwork.dominio.repositorios import Mapeador
from companias.seedwork.infraestructura.utils import unix_time_millis
from companias.modulos.ingestion.dominio.objetos_valor import EstadoCompania, Nombre, Email, Identificacion
from companias.modulos.ingestion.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO

from companias.modulos.ingestion.dominio.eventos import CompaniaAprobada, CompaniaRechazada, CompaniaCreada, EventoCompania
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapadeadorEventosCompania(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            CompaniaCreada: self._entidad_a_compania_creada,
            CompaniaAprobada: self._entidad_a_compania_aprobada,
            CompaniaRechazada: self._entidad_a_compania_rechazada,
        }

    def obtener_tipo(self) -> type:
        return EventoCompania.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_compania_creada(self, entidad: CompaniaCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import CompaniaCreadaPayload, EventoCompaniaCreada

            payload = CompaniaCreadaPayload(
                id_compania=str(evento.id_compania),
                estado=str(evento.estado),
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoCompaniaCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'CompaniaCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'companias'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def _entidad_a_compania_aprobada(self, entidad: CompaniaAprobada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def _entidad_a_compania_rechazada(self, entidad: CompaniaRechazada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError


    def entidad_a_dto(self, entidad: EventoCompania, version=LATEST_VERSION) -> CompaniaDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: CompaniaDTO, version=LATEST_VERSION) -> Compania:
        raise NotImplementedError

class MapeadorCompania(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        
        compania_dto = CompaniaDTO()
        compania_dto.fecha_creacion = entidad.fecha_creacion
        compania_dto.fecha_actualizacion = entidad.fecha_actualizacion
        compania_dto.id = str(entidad.id)
        compania_dto.nombre = str(entidad.nombre)
        compania_dto.email = str(entidad.email)
        compania_dto.identificacion = str(entidad.identificacion)

        return compania_dto

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        # breakpoint()
        compania = Compania(id=dto.id, 
                            fecha_creacion=dto.fecha_creacion, 
                            fecha_actualizacion=dto.fecha_actualizacion, 
                            nombre=dto.nombre, 
                            email=dto.email, 
                            identificacion=dto.identificacion)
        
        return compania
        