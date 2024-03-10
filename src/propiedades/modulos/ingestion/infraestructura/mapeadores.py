""" Mapeadores para la capa de infraestructura del dominio de ingestion"""

from propiedades.seedwork.dominio.repositorios import Mapeador
from propiedades.seedwork.infraestructura.utils import unix_time_millis
from propiedades.modulos.ingestion.dominio.objetos_valor import EstadoPropiedad, IdentificacionCatastral, Nit, Nombre
from propiedades.modulos.ingestion.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO

from propiedades.modulos.ingestion.dominio.eventos import PropiedadAprobada, PropiedadRechazada, PropiedadCreada, EventoPropiedad
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapadeadorEventosPropiedad(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            PropiedadCreada: self._entidad_a_propiedad_creada,
            PropiedadAprobada: self._entidad_a_propiedad_aprobada,
            PropiedadRechazada: self._entidad_a_propiedad_rechazada,
        }

    def obtener_tipo(self) -> type:
        return EventoPropiedad.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_propiedad_creada(self, entidad: PropiedadCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import PropiedadCreadaPayload, EventoPropiedadCreada

            payload = PropiedadCreadaPayload(
                id_propiedad=str(evento.id_propiedad),
                estado=str(evento.estado),
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion)),
                identificacion_catastral = str(evento.identificacion_catastral),
                nit = str(evento.nit),
                nombre = str(evento.nombre)
            )
            evento_integracion = EventoPropiedadCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'PropiedadCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'propiedades'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def _entidad_a_propiedad_aprobada(self, entidad: PropiedadAprobada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def _entidad_a_propiedad_rechazada(self, entidad: PropiedadRechazada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError


    def entidad_a_dto(self, entidad: EventoPropiedad, version=LATEST_VERSION) -> PropiedadDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: PropiedadDTO, version=LATEST_VERSION) -> Propiedad:
        raise NotImplementedError

class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        propiedad_dto = PropiedadDTO()
        propiedad_dto.fecha_creacion = entidad.fecha_creacion
        propiedad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        propiedad_dto.id = str(entidad.id)
        propiedad_dto.identificacion_catastral = str(entidad.identificacion_catastral)
        propiedad_dto.nit = str(entidad.nit)
        propiedad_dto.nombre = str(entidad.nombre)

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        # breakpoint()
        propiedad = Propiedad(id=dto.id, 
                            fecha_creacion=dto.fecha_creacion, 
                            fecha_actualizacion=dto.fecha_actualizacion, 
                            identificacion_catastral=dto.identificacion_catastral, 
                            nit=dto.nit, 
                            nombre=dto.nombre)
        
        return propiedad
        