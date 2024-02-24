""" Interfaces para los repositorios del dominio de ingestion

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de ingestion

"""

from abc import ABC
from companias.seedwork.dominio.repositorios import Repositorio

class RepositorioCompanias(Repositorio, ABC):
    ...

class RepositorioProveedores(Repositorio, ABC):
    ...