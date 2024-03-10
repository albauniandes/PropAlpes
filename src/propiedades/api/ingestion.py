import propiedades.seedwork.presentacion.api as api
import json
# from propiedades.modulos.ingestion.aplicacion.servicios import ServicioPropiedad
from propiedades.modulos.ingestion.aplicacion.dto import PropiedadDTO
from propiedades.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from propiedades.modulos.ingestion.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedades.modulos.ingestion.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedades.modulos.ingestion.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
from propiedades.seedwork.aplicacion.comandos import ejecutar_comando
from propiedades.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('ingestion', '/ingestion')

# @bp.route('/compania', methods=('POST',))
# def crear_compania():
#     try:
#         compania_dict = request.json

#         map_compania = MapeadorCompaniaDTOJson()
#         compania_dto = map_compania.externo_a_dto(compania_dict)

#         sr = ServicioCompania()
#         dto_final = sr.crear_compania(compania_dto)

#         return map_compania.dto_a_externo(dto_final)
#     except ExcepcionDominio as e:
#         return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/propiedad-comando', methods=('POST',))
def crear_propiedad_asincrona():
    try:
        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(propiedad_dto.fecha_creacion, propiedad_dto.fecha_actualizacion, propiedad_dto.id, propiedad_dto.identificacion_catastral, propiedad_dto.nit, propiedad_dto.nombre)
        
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

@bp.route('/propiedad-query', methods=('GET',))
@bp.route('/propiedad-query/<id>', methods=('GET',))
def dar_propiedad_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedad(id))
        map_propiedad = MapeadorPropiedadDTOJson()
        
        return map_propiedad.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]