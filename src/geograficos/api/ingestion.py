import geograficos.seedwork.presentacion.api as api
import json
# from geograficos.modulos.ingestion.aplicacion.servicios import ServicioCompania
from geograficos.modulos.ingestion.aplicacion.dto import DatosGeograficosDTO
from geograficos.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from geograficos.modulos.ingestion.aplicacion.mapeadores import MapeadorDatosGeograficosDTOJson
from geograficos.modulos.ingestion.aplicacion.comandos.crear_datos_geograficos import CrearDatosGeograficos
from geograficos.modulos.ingestion.aplicacion.queries.obtener_datos_geograficos import ObtenerDatosGeograficos
from geograficos.seedwork.aplicacion.comandos import ejecutar_comando
from geograficos.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('ingestion', '/ingestion')

@bp.route('/datos-geograficos-comando', methods=('POST',))
def crear_datos_geograficos_asincrona():
    try:
        datos_geograficos_dict = request.json

        map_datos_geograficos = MapeadorDatosGeograficosDTOJson()
        datos_geograficos_dto = map_datos_geograficos.externo_a_dto(datos_geograficos_dict)
        print(datos_geograficos_dto)
        comando = CrearDatosGeograficos(datos_geograficos_dto.fecha_creacion, datos_geograficos_dto.fecha_actualizacion,  datos_geograficos_dto.id, datos_geograficos_dto.nombre_propiedad, datos_geograficos_dto.latitud, datos_geograficos_dto.longitud)
        
        ejecutar_comando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

# @bp.route('/datos_geograficos', methods=('GET',))
# @bp.route('/compania/<id>', methods=('GET',))
# def dar_compania(id=None):
#     if id:
#         sr = ServicioCompania()
#         map_compania = MapeadorCompaniaDTOJson()
        
#         return map_compania.dto_a_externo(sr.obtener_compania_por_id(id))
#     else:
#         return [{'message': 'GET!'}]

@bp.route('/datos-geograficos-query', methods=('GET',))
@bp.route('/datos-geograficos-query/<id>', methods=('GET',))
def dar_datos_geograficos_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerDatosGeograficos(id))
        map_datos_geograficos = MapeadorDatosGeograficosDTOJson()
        
        return map_datos_geograficos.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]