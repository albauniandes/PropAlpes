""" Fábricas para la creación de objetos del dominio de companias"""

from .entidades import AuditoriaCompania
from .excepciones import TipoObjetoNoExisteEnDominioCompaniasExcepcion
from auditoria_test.seedwork.dominio.repositorios import Mapeador, Repositorio
from auditoria_test.seedwork.dominio.fabricas import Fabrica
from auditoria_test.seedwork.dominio.entidades import Entidad
from auditoria_test.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaAuditoriaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            auditoria_compania: AuditoriaCompania = mapeador.dto_a_entidad(obj)
            return auditoria_compania


@dataclass
class FabricaAuditoriaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == AuditoriaCompania.__class__:
            fabrica_compania = _FabricaAuditoriaCompania()
            return fabrica_compania.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()