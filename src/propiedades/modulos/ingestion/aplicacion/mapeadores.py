from propiedades.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedades.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedades.modulos.ingestion.dominio.entidades import Propiedad
from propiedades.modulos.ingestion.dominio.objetos_valor import EstadoPropiedad, IdentificacionCatastral, Nit, Nombre
from .dto import PropiedadDTO

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        #breakpoint()
        
        info_propiedad = externo.get('propiedad')
        print(info_propiedad)
        propiedad_dto = PropiedadDTO(identificacion_catastral = info_propiedad.get('identificacion_catastral'),
                                   nit = info_propiedad.get('nit'),
                                   nombre = info_propiedad.get('nombre'))
        
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__

class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__
        

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _identificacion_catastral = str(entidad.identificacion_catastral)
        _nit = str(entidad.nit)
        _nombre = str(entidad.nombre)
        
        return PropiedadDTO(fecha_creacion, fecha_actualizacion, _id, _identificacion_catastral, _nit, _nombre)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        #breakpoint()
        propiedad = Propiedad(identificacion_catastral=dto.identificacion_catastral,nit=dto.nit,nombre=dto.nombre)
        
        return propiedad