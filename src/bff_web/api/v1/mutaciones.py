import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_compania(self, nombre: str, email: str, identificacion: str, info: Info) -> CreacionCompaniaRespuesa:
        print(f"Nombre: {nombre}, email: {email}, identificacion: {identificacion}")
        payload = dict(
            nombre = nombre,
            email = email,
            identificacion = identificacion,
            fecha_creacion = str(utils.time_millis())
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoCreacionCompania",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-compania", "public/default/comando-crear-compania")
        
        return CreacionCompaniaRespuesa(mensaje="Procesando Mensaje", codigo=203)