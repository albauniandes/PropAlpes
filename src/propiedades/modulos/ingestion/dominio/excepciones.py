""" Excepciones del dominio de ingestion"""

from propiedades.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioPropiedadExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de ingestion'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)