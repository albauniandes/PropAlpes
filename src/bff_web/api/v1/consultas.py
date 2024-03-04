
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    companias: typing.List[Compania] = strawberry.field(resolver=obtener_companias)

@strawberry.type
class Query:
    geograficos: typing.List[DatosGeograficos] = strawberry.field(resolver=obtener_datos_geograficos)