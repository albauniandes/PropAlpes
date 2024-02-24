from companias.seedwork.aplicacion.comandos import Comando, ComandoHandler    

class AgregarCompaniaUsuario(Comando):
    id_usuario: uuid.UUID
    id_compania: uuid.UUID

class AgregarCompaniaUsuarioHandler(ComandoHandler):
    ...