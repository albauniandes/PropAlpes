import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import propiedades.modulos.validacion.aplicacion
    import propiedades.modulos.ingestion.aplicacion

def importar_modelos_alchemy():
    import propiedades.modulos.validacion.infraestructura.dto
    import propiedades.modulos.ingestion.infraestructura.dto

def comenzar_consumidor(app):

    import threading
    # import propiedades.modulos.validacion.infraestructura.consumidores as validacion
    import propiedades.modulos.ingestion.infraestructura.consumidores as ingestion

    # Suscripción a eventos
    # threading.Thread(target=validacion.suscribirse_a_eventos).start()
    threading.Thread(target=ingestion.suscribirse_a_eventos, args=[app]).start()

    # Suscripción a comandos
    # threading.Thread(target=validacion.suscribirse_a_comandos).start()
    threading.Thread(target=ingestion.suscribirse_a_comandos, args=[app]).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    # Inicializa la DB
    from propiedades.config.db import init_db, database_connection
    
    # app.config['SQLALCHEMY_DATABASE_URI'] =\
    #         'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_connection(configuracion, basedir=basedir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


     # Inicializa la DB
    from propiedades.config.db import init_db
    init_db(app)

    from propiedades.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor(app)

     # Importa Blueprints
    from . import validacion
    from . import ingestion

    # Registro de Blueprints
    app.register_blueprint(validacion.bp)
    app.register_blueprint(ingestion.bp)

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