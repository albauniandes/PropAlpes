""" Excepciones del dominio de geograficos"""

from companias.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioGeograficosExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de geograficos'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)