""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de ingestion"""

from dataclasses import dataclass, field
from companias.seedwork.dominio.fabricas import Fabrica
from companias.seedwork.dominio.repositorios import Repositorio
from companias.modulos.ingestion.dominio.repositorios import RepositorioProveedores, RepositorioCompanias
from .repositorios import RepositorioCompaniasSQLite, RepositorioProveedoresSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias.__class__:
            return RepositorioCompaniasSQLite()
        elif obj == RepositorioProveedores.__class__:
            return RepositorioProveedoresSQLite()
        else:
            raise ExcepcionFabrica()