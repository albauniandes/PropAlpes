import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))
import asyncio
tasks = list()
import threading

def registrar_handlers():
    import auditoria.modulos.propiedades.aplicacion

def importar_modelos_alchemy():
    import auditoria.modulos.propiedades.infraestructura.dto

def comenzar_consumidor(app):

    import threading
    # import propiedades.modulos.validacion.infraestructura.consumidores as validacion
    import auditoria.modulos.propiedades.infraestructura.consumidores as propiedades
    import auditoria.modulos.geograficos.infraestructura.consumidores as geograficos
    import auditoria.modulos.sagas.infraestructura.consumidores as sagas


    # Suscripción a eventos
    threading.Thread(target=sagas.suscribirse_a_topicos()).start()
    # threading.Thread(target=propiedades.suscribirse_a_eventos, args=[app]).start()
    # threading.Thread(target=geograficos.suscribirse_a_eventos, args=[app]).start()
    # threading.Thread(target=sagas.suscribirse_a_eventos_geograficos, args=[app]).start()
    # threading.Thread(target=sagas.suscribirse_a_eventos_propiedades, args=[app]).start()


    # Suscripción a comandos_
    # threading.Thread(target=validacion.suscribirse_a_comandos).start()
    # threading.Thread(target=propiedades.suscribirse_a_comandos, args=[app]).start()
    # threading.Thread(target=geograficos.suscribirse_a_comandos, args=[app]).start()
    # threading.Thread(target=sagas.suscribirse_a_comandos_geograficos, args=[app]).start()
    # threading.Thread(target=sagas.suscribirse_a_comandos_propiedades, args=[app]).start()


def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    # Inicializa la DB
    from auditoria.config.db import init_db, database_connection
    
    # app.config['SQLALCHEMY_DATABASE_URI'] =\
    #         'sqlite:///' + os.path.join(basedir, 'database.db')
    conn = database_connection(configuracion, basedir=basedir)
    print(conn)
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


     # Inicializa la DB
    from companias.config.db import init_db
    init_db(app)

    from companias.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
           comenzar_consumidor(app)

    # Importa Blueprints
    from . import auditoria

    # Registro de Blueprints
    app.register_blueprint(auditoria.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.1"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
