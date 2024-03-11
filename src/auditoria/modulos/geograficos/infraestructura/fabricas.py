""" Fábricas para la creación de objetos en la capa de infraestructura del dominio de propiedades"""

from dataclasses import dataclass, field
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.repositorios import Repositorio
from auditoria.modulos.geograficos.dominio.repositorios import RepositorioAuditoriaGeograficos, RepositorioEventosAuditoriaGeograficos
from .repositorios import RepositorioAuditoriaGeograficosSQLAlchemy, RepositorioEventosAuditoriaGeograficosSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAuditoriaGeograficos.__class__:
            return RepositorioAuditoriaGeograficosSQLAlchemy()
        elif obj == RepositorioEventosAuditoriaGeograficos:
            return RepositorioEventosAuditoriaGeograficosSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
