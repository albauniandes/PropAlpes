""" Interfaces para los repositorios del dominio de ingestion"""

from abc import ABC
from propiedades.seedwork.dominio.repositorios import Repositorio

class RepositorioPropiedad(Repositorio, ABC):
    ...

class RepositorioEventosPropiedad(Repositorio, ABC):
    ...