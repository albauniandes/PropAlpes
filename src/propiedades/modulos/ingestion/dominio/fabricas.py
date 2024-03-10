""" Fábricas para la creación de objetos del dominio de ingestion"""

from .entidades import Propiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadExcepcion
from propiedades.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedades.seedwork.dominio.fabricas import Fabrica
from propiedades.seedwork.dominio.entidades import Entidad
from propiedades.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)
            return propiedad


@dataclass
class FabricaIngestion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedad = _FabricaPropiedad()
            variable = fabrica_propiedad.crear_objeto(obj, mapeador)
            print("Esta es la variable")
            print(variable)
            print("///////////////////////////////////////////")
            return variable
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadExcepcion()