""" Interfaces para los repositorios del dominio de ingestion"""

from abc import ABC
from auditoria.seedwork.dominio.repositorios import Repositorio

class RepositorioDatosAuditoria(Repositorio, ABC):
    ...

class RepositorioSagalog(Repositorio, ABC):
    ...

class RepositorioEventosDatosGeograficos(Repositorio, ABC):
    ...