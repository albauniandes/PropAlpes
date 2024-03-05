""" Fábricas para la creación de objetos en la capa de infraestructura del dominio de companias"""

from dataclasses import dataclass, field
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.repositorios import Repositorio
from auditoria.modulos.companias.dominio.repositorios import RepositorioAuditoriaCompanias, RepositorioEventosAuditoriaCompanias
from .repositorios import RepositorioAuditoriaCompaniasSQLAlchemy, RepositorioEventosAuditoriaCompaniasSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAuditoriaCompanias.__class__:
            return RepositorioAuditoriaCompaniasSQLAlchemy()
        elif obj == RepositorioEventosAuditoriaCompanias:
            return RepositorioEventosAuditoriaCompaniasSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
