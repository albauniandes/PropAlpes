from geograficos.seedwork.aplicacion.dto import Mapeador as AppMap
from geograficos.seedwork.dominio.repositorios import Mapeador as RepMap
from geograficos.modulos.ingestion.dominio.entidades import DatosGeograficos
from geograficos.modulos.ingestion.dominio.objetos_valor import EstadoDatosGeograficos, NombrePropiedad, Latitud, Longitud
from .dto import DatosGeograficosDTO

from datetime import datetime

class MapeadorDatosGeograficosDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> DatosGeograficosDTO:
        #breakpoint()
        
        info_datos_geograficos = externo.get('datos_geograficos')
        print(info_datos_geograficos)
        datos_geograficos_dto = DatosGeograficosDTO(nombre_propiedad = info_datos_geograficos.get('nombre_propiedad'),
                                   latitud = info_datos_geograficos.get('latitud'),
                                   longitud = info_datos_geograficos.get('longitud'))
        
        return datos_geograficos_dto

    def dto_a_externo(self, dto: DatosGeograficosDTO) -> dict:
        return dto.__dict__

class MapeadorDatosGeograficos(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return DatosGeograficos.__class__
        

    def entidad_a_dto(self, entidad: DatosGeograficos) -> DatosGeograficosDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _nombre_propiedad = str(entidad.nombre_propiedad)
        _latitud = str(entidad.latitud)
        _longitud = str(entidad.longitud)
        
        return DatosGeograficosDTO(fecha_creacion, fecha_actualizacion, _id, _nombre_propiedad, _latitud, _longitud)

    def dto_a_entidad(self, dto: DatosGeograficosDTO) -> DatosGeograficos:
        #breakpoint()
        datos_geograficos = DatosGeograficos(nombre_propiedad=dto.nombre_propiedad,latitud=dto.latitud,longitud=dto.longitud)
        
        return datos_geograficos