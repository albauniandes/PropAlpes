""" Excepciones del dominio de propiedades"""

from companias.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioCompaniasExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de propiedades'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)