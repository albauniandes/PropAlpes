import auditoria.seedwork.presentacion.api as api
import json
# from propiedades.modulos.propiedades.aplicacion.servicios import Serviciopropiedadad
from auditoria.modulos.propiedades.aplicacion.dto import AuditoriaPropiedadDTO
from auditoria.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from auditoria.modulos.propiedades.aplicacion.mapeadores import MapeadorAuditoriaPropiedadDTOJson
from auditoria.modulos.propiedades.aplicacion.comandos.auditar_propiedad import CrearAuditoriaPropiedad
from auditoria.modulos.propiedades.aplicacion.queries.obtener_propiedad import ObtenerAuditoriaPropiedad
from auditoria.seedwork.aplicacion.comandos import ejecutar_comando
from auditoria.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('auditoria', '/auditoria')


@bp.route('/auditoria-propiedad-comando', methods=('POST',))
def crear_auditoria_propiedad_asincrona():
    try:
        auditoria_propiedad_dict = request.json

        map_auditoria_propiedad = MapeadorAuditoriaPropiedadDTOJson()
        auditoria_propiedad_dto = map_auditoria_propiedad.externo_a_dto(auditoria_propiedad_dict)

        comando = CrearAuditoriaPropiedad(auditoria_propiedad_dto.fecha_creacion,
                                          auditoria_propiedad_dto.fecha_actualizacion,
                                          auditoria_propiedad_dto.id,
                                          auditoria_propiedad_dto.nombre,
                                          auditoria_propiedad_dto.email,
                                          auditoria_propiedad_dto.identificacion,
                                          auditoria_propiedad_dto.motivo_auditoria)

        ejecutar_comando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/auditoria-propiedad-query', methods=('GET',))
@bp.route('/auditoria-propiedad-query/<id>', methods=('GET',))
def dar_auditoria_propiedad_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerAuditoriaPropiedad(id))
        map_auditoria_propiedad = MapeadorAuditoriaPropiedadDTOJson()

        return map_auditoria_propiedad.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
