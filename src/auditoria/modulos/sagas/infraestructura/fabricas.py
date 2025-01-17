""" Fábricas para la creación de objetos en la capa de infraestructura del dominio de ingestion"""

from dataclasses import dataclass, field
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.repositorios import Repositorio
from geograficos.modulos.ingestion.dominio.repositorios import RepositorioDatosGeograficos, RepositorioEventosDatosGeograficos
from .repositorios import RepositorioDatosGeograficosSQLAlchemy, RepositorioEventosDatosGeograficosSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioDatosGeograficos.__class__:
            return RepositorioDatosGeograficosSQLAlchemy()
        elif obj == RepositorioEventosDatosGeograficos:
            return RepositorioEventosDatosGeograficosSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
