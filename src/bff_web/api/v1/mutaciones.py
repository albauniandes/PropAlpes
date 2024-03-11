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
    
    @strawberry.mutation
    async def crear_propiedad(self, nombre_propiedad: str, identificacion_catastral: str, nit: str, latitud: str, longitud: str, info: Info) -> CreacionDatosPropiedadRespuesta:
        print(f"Nombre Propiedad: {nombre_propiedad}, latitud: {latitud}, longitud: {longitud}, nit: {nit}, identificacion_catastral: {identificacion_catastral}")
        payload_geograficos = dict(
            nombre_propiedad = nombre_propiedad,
            latitud = latitud,
            longitud = longitud,
            fecha_creacion = str(utils.time_millis())
        )
        payload_propiedad = dict(
            nombre = nombre_propiedad,
            nit = nit,
            identificacion_catastral = identificacion_catastral,
            fecha_creacion = str(utils.time_millis())
        )
        print(payload_geograficos)
        print(payload_propiedad)
        comando_geograficos = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoCreacionDatosGeograficos",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload_geograficos
        )
        comando_propiedad = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoCreacionPropiedad",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload_propiedad
        )
        print(comando_geograficos)
        print(comando_propiedad)
        despachador = Despachador()
        ### Envio del comando para registrar los datos geograficos
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando_geograficos, "topic-comando-crear-datos-geograficos", "public/default/topic-comando-crear-datos-geograficos")
        ### Envio del comando para registrar los datos de la propiedad
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando_propiedad, "topic-comando-crear-propiedad", "public/default/topic-comando-crear-propiedad")
        
        return CreacionDatosPropiedadRespuesta(mensaje="Procesando Mensaje", codigo=203)