from companias.seedwork.aplicacion.dto import Mapeador as AppMap
from companias.seedwork.dominio.repositorios import Mapeador as RepMap
from companias.modulos.ingestion.dominio.entidades import Compania
from companias.modulos.ingestion.dominio.objetos_valor import EstadoCompania, Nombre, Email, Identificacion
from .dto import CompaniaDTO

from datetime import datetime

class MapeadorCompaniaDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        #breakpoint()
        
        info_compania = externo.get('compania')
        print(info_compania)
        compania_dto = CompaniaDTO(email = info_compania.get('email'),
                                   nombre = info_compania.get('nombre'),
                                   identificacion = info_compania.get('identificacion'))
        
        return compania_dto

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__

class MapeadorCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__
        

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _nombre = str(entidad.nombre)
        _email = str(entidad.email)
        _identificacion = str(entidad.identificacion)
        
        return CompaniaDTO(fecha_creacion, fecha_actualizacion, _id, _nombre, _email, _identificacion)

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        #breakpoint()
        compania = Compania(nombre=dto.nombre,identificacion=dto.identificacion,email=dto.email)
        
        return compania