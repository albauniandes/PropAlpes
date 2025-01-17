""" Interfaces para los repositorios del dominio de propiedades"""

from abc import ABC
from companias.seedwork.dominio.repositorios import Repositorio

class RepositorioAuditoriaPropiedads(Repositorio, ABC):
    ...

class RepositorioEventosAuditoriaPropiedads(Repositorio, ABC):
    ...