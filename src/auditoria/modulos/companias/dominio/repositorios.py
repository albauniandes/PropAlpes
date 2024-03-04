""" Interfaces para los repositorios del dominio de companias"""

from abc import ABC
from companias.seedwork.dominio.repositorios import Repositorio

class RepositorioCompanias(Repositorio, ABC):
    ...

class RepositorioEventosCompanias(Repositorio, ABC):
    ...