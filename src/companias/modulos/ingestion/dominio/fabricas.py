""" Fábricas para la creación de objetos del dominio de ingestion"""

from .entidades import Compania
# from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioCompaniasExcepcion
from companias.seedwork.dominio.repositorios import Mapeador, Repositorio
from companias.seedwork.dominio.fabricas import Fabrica
from companias.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            compania: Compania = mapeador.dto_a_entidad(obj)

            # self.validar_regla(MinimoUnItinerario(compania.itinerarios))
            # [self.validar_regla(RutaValida(ruta)) for itin in compania.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return compania

# @dataclass
# class FabricaVuelos(Fabrica):
#     def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
#         if mapeador.obtener_tipo() == Compania.__class__:
#             fabrica_compania = _FabricaCompania()
#             return fabrica_compania.crear_objeto(obj, mapeador)
#         else:
#             raise TipoObjetoNoExisteEnDominioCompaniasExcepcion()

