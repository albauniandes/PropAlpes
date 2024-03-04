""" Interfaces para los repositorios del dominio de ingestion"""

from abc import ABC
from geograficos.seedwork.dominio.repositorios import Repositorio

class RepositorioDatosGeograficos(Repositorio, ABC):
    ...

class RepositorioEventosDatosGeograficos(Repositorio, ABC):
    ...