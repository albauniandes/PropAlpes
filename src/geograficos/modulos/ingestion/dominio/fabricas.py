""" Fábricas para la creación de objetos del dominio de ingestion"""

from .entidades import DatosGeograficos
from .excepciones import TipoObjetoNoExisteEnDominioDatosGeograficosExcepcion
from geograficos.seedwork.dominio.repositorios import Mapeador, Repositorio
from geograficos.seedwork.dominio.fabricas import Fabrica
from geograficos.seedwork.dominio.entidades import Entidad
from geograficos.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaDatosGeograficos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            datos_geograficos: DatosGeograficos = mapeador.dto_a_entidad(obj)
            return datos_geograficos


@dataclass
class FabricaIngestion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == DatosGeograficos.__class__:
            fabrica_datos_geograficos = _FabricaDatosGeograficos()
            return fabrica_datos_geograficos.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioDatosGeograficosExcepcion()