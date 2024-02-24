"""Mixins del dominio de ingestion"""

from .entidades import Itinerario

class FiltradoItinerariosMixin:

    def filtrar_mejores_itinerarios(self, itinerarios: list[Itinerario]) -> list[Itinerario]:
        # Logica compleja para filtrar itinerarios
        # TODO
        return itinerarios