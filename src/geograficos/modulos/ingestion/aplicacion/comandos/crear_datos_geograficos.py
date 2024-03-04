from geograficos.seedwork.aplicacion.comandos import Comando
from geograficos.modulos.ingestion.aplicacion.dto import DatosGeograficosDTO
from .base import CrearDatosGeograficosBaseHandler
from dataclasses import dataclass, field
from geograficos.seedwork.aplicacion.comandos import ejecutar_comando as comando

from geograficos.modulos.ingestion.dominio.entidades import DatosGeograficos
from geograficos.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from geograficos.modulos.ingestion.aplicacion.mapeadores import MapeadorDatosGeograficos
from geograficos.modulos.ingestion.infraestructura.repositorios import RepositorioDatosGeograficos, RepositorioEventosDatosGeograficos

@dataclass
class CrearDatosGeograficos(Comando):
    nombre_propiedad: str
    latitud: float
    longitud: float
    id: str

class CrearDatosGeograficosHandler(CrearDatosGeograficosBaseHandler):
    
    def handle(self, comando: CrearDatosGeograficos):
        datos_geograficos_dto = DatosGeograficosDTO(
                nombre_propiedad=comando.nombre_propiedad
            ,   latitud=comando.latitud
            ,   longitud=comando.longitud
            ,   id=comando.id)
        #breakpoint()
        datos_geograficos: DatosGeograficos = self.fabrica_ingestion.crear_objeto(datos_geograficos_dto, MapeadorDatosGeograficos())
        datos_geograficos.crear_datos_geograficos(datos_geograficos)
        #breakpoint()
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioDatosGeograficos.__class__)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosDatosGeograficos)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, datos_geograficos)
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, datos_geograficos, repositorio_eventos_func=repositorio_eventos.agregar)

        UnidadTrabajoPuerto.commit()


@comando.register(CrearDatosGeograficos)
def ejecutar_comando_crear_datos_geograficos(comando: CrearDatosGeograficos):
    handler = CrearDatosGeograficosHandler()
    handler.handle(comando)
    