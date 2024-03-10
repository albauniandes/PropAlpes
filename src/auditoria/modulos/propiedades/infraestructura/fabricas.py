""" Fábricas para la creación de objetos en la capa de infraestructura del dominio de propiedades"""

from dataclasses import dataclass, field
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.repositorios import Repositorio
from auditoria.modulos.propiedades.dominio.repositorios import RepositorioAuditoriaPropiedads, RepositorioEventosAuditoriaPropiedads
from .repositorios import RepositorioAuditoriaPropiedadsSQLAlchemy, RepositorioEventosAuditoriaPropiedadsSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAuditoriaPropiedads.__class__:
            return RepositorioAuditoriaPropiedadsSQLAlchemy()
        elif obj == RepositorioEventosAuditoriaPropiedads:
            return RepositorioEventosAuditoriaPropiedadsSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
