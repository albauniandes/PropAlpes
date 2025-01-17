from auditoria.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from auditoria.seedwork.aplicacion.comandos import Comando
from auditoria.seedwork.dominio.eventos import EventoDominio


from auditoria.modulos.sagas.dominio.eventos.geograficos import GeograficoCreado, GeograficoEliminado, CreacionGeograficoFallida
from auditoria.modulos.sagas.dominio.eventos.propiedades import PropiedadCreada, PropiedadEliminada, CreacionPropiedadFallida
from auditoria.modulos.propiedades.dominio.eventos import AuditoriaPropiedadCreada, CreacionAuditoriaPropiedadFallida
from auditoria.modulos.geograficos.dominio.eventos import AuditoriaGeograficoCreada, CreacionAuditoriaGeograficoFallida

from auditoria.modulos.propiedades.aplicacion.comandos.auditar_propiedad import CrearAuditoriaPropiedad
from auditoria.modulos.propiedades.aplicacion.comandos.eliminar_auditoria_propiedad import EliminarAuditoriaPropiedad
from auditoria.modulos.geograficos.aplicacion.comandos.auditar_geografico import CrearAuditoriaGeografico
from auditoria.modulos.geograficos.aplicacion.comandos.eliminar_auditoria_geografico import EliminarAuditoriaGeografico

from auditoria.modulos.sagas.aplicacion.comandos.propiedades import CrearPropiedad, EliminarPropiedad, RechazarPropiedad, EliminarPropiedad
from auditoria.modulos.sagas.aplicacion.comandos.geograficos import CrearGeografico, EliminarGeografico, RechazarDatosGeograficos, EliminarGeografico


class CoordinadorAuditoria(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearPropiedad, evento=PropiedadCreada, error=CreacionPropiedadFallida, compensacion=EliminarPropiedad),
            Transaccion(index=2, comando=CrearGeografico, evento=GeograficoCreado, error=CreacionGeograficoFallida, compensacion=EliminarGeografico),
            Transaccion(index=3, comando=CrearAuditoriaPropiedad, evento=AuditoriaPropiedadCreada, error=CreacionAuditoriaPropiedadFallida, compensacion=EliminarAuditoriaPropiedad),
            Transaccion(index=4, comando=CrearAuditoriaGeografico, evento=AuditoriaGeograficoCreada, error=CreacionAuditoriaGeograficoFallida, compensacion=EliminarAuditoriaGeografico),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje, schema):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        from auditoria.config.db import db
        from auditoria.modulos.sagas.infraestructura.dto import Sagalog
        import json
        contenido_json = json.dumps(mensaje)
        id_entidad = mensaje.get('id_geograficos') or mensaje.get('id_propiedad') or None
        mensaje_log = Sagalog(id_entidad=id_entidad, tipo_accion=schema.__name__, contenido=contenido_json)
        db.session.add(mensaje_log)
        db.session.commit()

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        comando = tipo_comando(evento.id)

    def procesar_evento(self, evento: EventoDominio):
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def almacenar_mensaje(mensaje, schema):
    coordinador = CoordinadorAuditoria()
    coordinador.persistir_en_saga_log(mensaje, schema)

def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorAuditoria()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
