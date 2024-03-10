""" Interfaces para los repositorios del dominio de propiedades"""

from abc import ABC
from companias.seedwork.dominio.repositorios import Repositorio

class RepositorioAuditoriaGeograficos(Repositorio, ABC):
    ...

class RepositorioEventosAuditoriaGeograficos(Repositorio, ABC):
    ...