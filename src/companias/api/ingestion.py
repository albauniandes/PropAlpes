import companias.seedwork.presentacion.api as api
import json
from companias.modulos.ingestion.aplicacion.servicios import ServicioCompania
from companias.modulos.ingestion.aplicacion.dto import CompaniaDTO
from companias.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from companias.modulos.ingestion.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from companias.modulos.ingestion.aplicacion.comandos.crear_compania import CrearCompania
from companias.modulos.ingestion.aplicacion.queries.obtener_compania import ObtenerCompania
from companias.seedwork.aplicacion.comandos import ejecutar_commando
from companias.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('ingestion', '/ingestion')

@bp.route('/compania', methods=('POST',))
def crear_compania():
    try:
        compania_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)

        sr = ServicioCompania()
        dto_final = sr.crear_compania(compania_dto)

        return map_compania.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/compania-comando', methods=('POST',))
def crear_compania_asincrona():
    try:
        compania_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)

        comando = CrearCompania(compania_dto.fecha_creacion, compania_dto.fecha_actualizacion, compania_dto.id)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/compania', methods=('GET',))
@bp.route('/compania/<id>', methods=('GET',))
def dar_compania(id=None):
    if id:
        sr = ServicioCompania()
        map_compania = MapeadorCompaniaDTOJson()
        
        return map_compania.dto_a_externo(sr.obtener_compania_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/compania-query', methods=('GET',))
@bp.route('/compania-query/<id>', methods=('GET',))
def dar_compania_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCompania(id))
        map_compania = MapeadorCompaniaDTOJson()
        
        return map_compania.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]