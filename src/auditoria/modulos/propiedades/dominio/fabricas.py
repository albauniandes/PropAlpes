""" Fábricas para la creación de objetos del dominio de propiedades"""

from .entidades import AuditoriaPropiedad
from .excepciones import TipoObjetoNoExisteEnDominioCompaniasExcepcion
from auditoria.seedwork.dominio.repositorios import Mapeador, Repositorio
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.entidades import Entidad
from auditoria.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaAuditoriaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            auditoria_compania: AuditoriaPropiedad = mapeador.dto_a_entidad(obj)
            return auditoria_compania


@dataclass
class FabricaAuditoriaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == AuditoriaPropiedad.__class__:
            fabrica_compania = _FabricaAuditoriaPropiedad()
            return fabrica_compania.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()