""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestión"""

from companias.config.db import db
from companias.modulos.ingestion.dominio.repositorios import RepositorioCompanias
from companias.modulos.ingestion.dominio.objetos_valor import EstadoCompania, Nombre, Email, Identificacion
from companias.modulos.ingestion.dominio.entidades import Compania
from companias.modulos.ingestion.dominio.fabricas import FabricaIngestion
from .dto import Compania as CompaniaDTO
from .mapeadores import MapeadorCompania
from uuid import UUID

class RepositorioCompaniasSQLite(RepositorioCompanias):

    def __init__(self):
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> Compania:
        compania_dto = db.session.query(CompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(compania_dto, MapeadorCompania())

    def obtener_todos(self) -> list[Compania]:
        # TODO
        raise NotImplementedError

    def agregar(self, compania: Compania):
        compania_dto = self.fabrica_ingestion.crear_objeto(compania, MapeadorCompania())
        db.session.add(compania_dto)

    def actualizar(self, compania: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, compania_id: UUID):
        # TODO
        raise NotImplementedError