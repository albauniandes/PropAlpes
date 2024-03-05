import companias.seedwork.presentacion.api as api
import json
# from companias.modulos.companias.aplicacion.servicios import ServicioCompania
from auditoria.modulos.companias.aplicacion.dto import AuditoriaCompaniaDTO
from auditoria.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from auditoria.modulos.companias.aplicacion.mapeadores import MapeadorAuditoriaCompaniaDTOJson
from auditoria.modulos.companias.aplicacion.comandos.auditar_compania import CrearAuditoriaCompania
from auditoria.modulos.companias.aplicacion.queries.obtener_compania import ObtenerAuditoriaCompania
from auditoria.seedwork.aplicacion.comandos import ejecutar_comando
from auditoria.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('auditoria', '/auditoria')

@bp.route('/auditoria-compania-comando', methods=('POST',))
def crear_auditoria_compania_asincrona():
    try:
        auditoria_compania_dict = request.json

        map_auditoria_compania = MapeadorAuditoriaCompaniaDTOJson()
        auditoria_compania_dto = map_auditoria_compania.externo_a_dto(auditoria_compania_dict)

        comando = CrearAuditoriaCompania(auditoria_compania_dto.fecha_creacion,
                                auditoria_compania_dto.fecha_actualizacion,
                                auditoria_compania_dto.id,
                                auditoria_compania_dto.nombre,
                                auditoria_compania_dto.email,
                                auditoria_compania_dto.identificacion,
                                auditoria_compania_dto.motivo_auditoria)
        
        ejecutar_comando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

# @bp.route('/compania', methods=('GET',))
# @bp.route('/compania/<id>', methods=('GET',))
# def dar_compania(id=None):
#     if id:
#         sr = ServicioCompania()
#         map_compania = MapeadorCompaniaDTOJson()
        
#         return map_compania.dto_a_externo(sr.obtener_compania_por_id(id))
#     else:
#         return [{'message': 'GET!'}]

@bp.route('/auditoria-compania-query', methods=('GET',))
@bp.route('/auditoria-compania-query/<id>', methods=('GET',))
def dar_auditoria_compania_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerAuditoriaCompania(id))
        map_auditoria_compania = MapeadorAuditoriaCompaniaDTOJson()
        
        return map_auditoria_compania.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]