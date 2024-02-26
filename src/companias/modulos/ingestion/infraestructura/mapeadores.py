""" Mapeadores para la capa de infraestructura del dominio de ingestion"""

from companias.seedwork.dominio.repositorios import Mapeador
from companias.modulos.ingestion.dominio.objetos_valor import EstadoCompania, Nombre, Email, Identificacion
from companias.modulos.ingestion.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO

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
        breakpoint()
        compania = Compania(id=dto.id, 
                            fecha_creacion=dto.fecha_creacion, 
                            fecha_actualizacion=dto.fecha_actualizacion, 
                            nombre=dto.nombre, 
                            email=dto.email, 
                            identificacion=dto.identificacion)
        
        return compania
        