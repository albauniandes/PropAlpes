""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestion"""

from companias.config.db import db
from companias.modulos.ingestion.dominio.repositorios import RepositorioCompanias, RepositorioProveedores
from companias.modulos.ingestion.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from companias.modulos.ingestion.dominio.entidades import Proveedor, Aeropuerto, Compania
from companias.modulos.ingestion.dominio.fabricas import FabricaVuelos
from .dto import Compania as CompaniaDTO
from .mapeadores import MapeadorCompania
from uuid import UUID

class RepositorioProveedoresSQLite(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Compania:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Compania]:
        origen=Aeropuerto(codigo="CPT", nombre="Cape Town International")
        destino=Aeropuerto(codigo="JFK", nombre="JFK International Airport")
        legs=[Leg(origen=origen, destino=destino)]
        segmentos = [Segmento(legs)]
        odos=[Odo(segmentos=segmentos)]

        proveedor = Proveedor(codigo=CodigoIATA(codigo="AV"), nombre=NombreAero(nombre= "Avianca"))
        proveedor.itinerarios = [Itinerario(odos=odos, proveedor=proveedor)]
        return [proveedor]

    def agregar(self, entity: Compania):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioCompaniasSQLite(RepositorioCompanias):

    def __init__(self):
        self._fabrica_ingestion: FabricaVuelos = FabricaVuelos()

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