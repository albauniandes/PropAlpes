""" Fábricas para la creación de objetos en la capa de infraestructura del dominio de ingestion"""

from dataclasses import dataclass, field
from propiedades.seedwork.dominio.fabricas import Fabrica
from propiedades.seedwork.dominio.repositorios import Repositorio
from propiedades.modulos.ingestion.dominio.repositorios import RepositorioPropiedad, RepositorioEventosPropiedad
from .repositorios import RepositorioPropiedadSQLAlchemy, RepositorioEventosPropiedadSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedad.__class__:
            return RepositorioPropiedadSQLAlchemy()
        elif obj == RepositorioEventosPropiedad:
            return RepositorioEventosPropiedadSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
