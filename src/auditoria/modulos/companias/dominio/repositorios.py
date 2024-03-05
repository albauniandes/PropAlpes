""" Interfaces para los repositorios del dominio de companias"""

from abc import ABC
from companias.seedwork.dominio.repositorios import Repositorio

class RepositorioAuditoriaCompanias(Repositorio, ABC):
    ...

class RepositorioEventosAuditoriaCompanias(Repositorio, ABC):
    ...