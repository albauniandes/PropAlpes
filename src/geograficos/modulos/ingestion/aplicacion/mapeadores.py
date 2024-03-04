from geograficos.seedwork.aplicacion.dto import Mapeador as AppMap
from geograficos.seedwork.dominio.repositorios import Mapeador as RepMap
from geograficos.modulos.ingestion.dominio.entidades import DatosGeograficos
from geograficos.modulos.ingestion.dominio.objetos_valor import NombrePropiedad, Latitud, Longitud
from .dto import DatosGeograficosDTO

from datetime import datetime

class MapeadorDatosGeograficosDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> DatosGeograficosDTO:
        #breakpoint()
        
        info_datos_geograficos = externo.get('datos_geograficos')
        print(info_datos_geograficos)
        datos_geograficos_dto = DatosGeograficosDTO(nombre_propiedad= info_datos_geograficos.get('nombre'),
                                   latitud = info_datos_geograficos.get('latitud'),
                                   longitud = info_datos_geograficos.get('longitud'))
        
        return datos_geograficos_dto

    def dto_a_externo(self, dto: DatosGeograficosDTO) -> dict:
        return dto.__dict__

class MapeadorDatosGeograficos(RepMap):
    def obtener_tipo(self) -> type:
        return DatosGeograficos.__class__


    def entidad_a_dto(self, entidad: DatosGeograficos) -> DatosGeograficosDTO:
        
        _id = str(entidad.id)
        _nombre_propiedad = str(entidad.nombre)
        _latitud = str(entidad.latitud)
        _longitud = str(entidad.longitud)
        
        return DatosGeograficosDTO(_id, _nombre_propiedad, _latitud, _longitud)

    def dto_a_entidad(self, dto: DatosGeograficosDTO) -> DatosGeograficos:
        #breakpoint()
        datos_geograficos = DatosGeograficos(nombre=dto.nombre,Latitud=dto.latitud,Longitud=dto.longitud)
        
        return datos_geograficos