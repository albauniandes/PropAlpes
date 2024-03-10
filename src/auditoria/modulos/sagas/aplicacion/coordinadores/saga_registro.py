from auditoria.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from auditoria.seedwork.aplicacion.comandos import Comando
from auditoria.seedwork.dominio.eventos import EventoDominio

from auditoria.modulos.sagas.aplicacion.comandos.companias import RegistrarCompania, AuditarCompania
from auditoria.modulos.sagas.aplicacion.comandos.geograficos import RegistrarUbicacion, AuditarUbicación

from companias.modulos.ingestion.aplicacion.comandos.crear_compania import CrearCompania
from geograficos.modulos.ingestion.aplicacion.comandos.crear_datos_geograficos import CrearDatosGeograficos

from companias.modulos.ingestion.dominio.eventos import CompaniaAprobada, CompaniaCreada, CompaniaRechazada
from geograficos.modulos.ingestion.dominio.eventos import DatosGeograficosAprobados, DatosGeograficosCreados, DatosGeograficosRechazados


class CoordinadorRegistro(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        # self.pasos = [
        #     Inicio(index=0),
        #     Transaccion(index=1, comando=CrearReserva, evento=ReservaCreada, error=CreacionReservaFallida, compensacion=CancelarReserva),
        #     Transaccion(index=2, comando=PagarReserva, evento=ReservaPagada, error=PagoFallido, compensacion=RevertirPago),
        #     Transaccion(index=3, comando=ConfirmarReserva, evento=ReservaGDSConfirmada, error=ConfirmacionFallida, compensacion=ConfirmacionGDSRevertida),
        #     Transaccion(index=4, comando=AprobarReserva, evento=ReservaAprobada, error=AprobacionReservaFallida, compensacion=CancelarReserva),
        #     Fin(index=5)
        # ]
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearCompania, evento=CompaniaCreada, error=CreacionCompaniaFallida, compensacion=CancelarCreacionCompania),
            Transaccion(index=2, comando=CrearDatosGeograficos, evento=DatosGeograficosCreados, error=CreacionDatosGeograficosFallida, compensacion=CancelarCreacionDatosGeograficosPago),
            Transaccion(index=3, comando=AuditarRegistro, evento=AuditoriaConfirmada, error=AuditoriaFallida, compensacion=CancelarAuditoria),
            Fin(index=4)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        print("MÉTODO PERSISTIR EN SAGA LOG")
        print("MENSAJE: ")
        print(mensaje)
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        print("MÉTODO CONSTRUIR COMANDO")
        print("EVENTO Y TIPO DE COMANDO: ")
        print(evento.type())
        print(tipo_comando.type())
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        # comando:tipo_comando = 
        # comando = tipo_comando(evento.id)
        # print(str(comando))
        if tipo_comando == AuditarCompania:
            comando = AuditarCompania()


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    print("MÉTODO OIR MENSAJE")
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
