""" Mapeadores para la capa de infraestructura del dominio de ingestion"""

from geograficos.seedwork.dominio.repositorios import Mapeador
from geograficos.seedwork.infraestructura.utils import unix_time_millis
from geograficos.modulos.ingestion.dominio.objetos_valor import EstadoDatosGeograficos, NombrePropiedad, Latitud, Longitud
from geograficos.modulos.ingestion.dominio.entidades import DatosGeograficos
from .dto import DatosGeograficos as DatosGeograficosDTO

from geograficos.modulos.ingestion.dominio.eventos import DatosGeograficosAprobados, DatosGeograficosRechazados, DatosGeograficosCreados, EventoDatosGeograficos
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapadeadorEventosDatosGeograficos(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            DatosGeograficosCreados: self._entidad_a_datos_geograficos_creados,
            DatosGeograficosAprobados: self._entidad_a_datos_geograficos_aprobados,
            DatosGeograficosRechazados: self._entidad_a_datos_geograficos_rechazados,
        }

    def obtener_tipo(self) -> type:
        return EventoDatosGeograficos.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_datos_geograficos_creada(self, entidad: DatosGeograficosCreados, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import DatosGeograficosCreadaPayload, EventoDatosGeograficosCreada

            payload = DatosGeograficosCreadaPayload(
                id_geograficos=str(evento.id_geograficos),
                estado=str(evento.estado),
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoDatosGeograficosCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'DatosGeograficosCreados'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'geograficos'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def _entidad_a_datos_geograficos_aprobada(self, entidad: DatosGeograficosAprobados, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def _entidad_a_datos_geograficos_rechazada(self, entidad: DatosGeograficosRechazados, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError


    def entidad_a_dto(self, entidad: EventoDatosGeograficos, version=LATEST_VERSION) -> DatosGeograficosDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: DatosGeograficosDTO, version=LATEST_VERSION) -> DatosGeograficos:
        raise NotImplementedError

class MapeadorDatosGeograficos(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return DatosGeograficos.__class__

    def entidad_a_dto(self, entidad: DatosGeograficos) -> DatosGeograficosDTO:
        
        datos_geograficos_dto = DatosGeograficosDTO()
        datos_geograficos_dto.fecha_creacion = entidad.fecha_creacion
        datos_geograficos_dto.fecha_actualizacion = entidad.fecha_actualizacion
        datos_geograficos_dto.id = str(entidad.id)
        datos_geograficos_dto.nombre_propiedad = str(entidad.nombre_propiedad)
        datos_geograficos_dto.latitud = str(entidad.latitud)
        datos_geograficos_dto.longitud = str(entidad.longitud)

        return datos_geograficos_dto

    def dto_a_entidad(self, dto: DatosGeograficosDTO) -> DatosGeograficos:
        # breakpoint()
        datos_geograficos = DatosGeograficos(id=dto.id, 
                            fecha_creacion=dto.fecha_creacion, 
                            fecha_actualizacion=dto.fecha_actualizacion, 
                            nombre_propiedad=dto.nombre_propiedad, 
                            latitud=dto.latitud, 
                            longitud=dto.longitud)
        
        return datos_geograficos
        