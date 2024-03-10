""" Fábricas para la creación de objetos del dominio de propiedades"""

from .entidades import AuditoriaGeografico
from .excepciones import TipoObjetoNoExisteEnDominioGeograficosExcepcion
from auditoria.seedwork.dominio.repositorios import Mapeador, Repositorio
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.entidades import Entidad
from auditoria.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaAuditoriaGeografico(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            auditoria_geografico: AuditoriaGeografico = mapeador.dto_a_entidad(obj)
            return auditoria_geografico


@dataclass
class FabricaAuditoriaGeografico(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == AuditoriaGeografico.__class__:
            fabrica_geografico = _FabricaAuditoriaGeografico()
            return fabrica_geografico.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioGeograficosExcepcion()