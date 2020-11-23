from flask import Flask
from demo.view import xxx_blueprint
from demo.extensions import db, migrate
from demo.settings import get_config_env
from demo.extensions import login_manager


def create_app(config_object=get_config_env()):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    init_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


def init_blueprints(app):
    app.register_blueprint(xxx_blueprint)

