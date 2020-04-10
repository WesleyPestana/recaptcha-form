from importlib import import_module
from dynaconf import FlaskDynaconf


def load_extensions(app):
    for extention in app.config.get('EXTENSIONS'):
        module = import_module(extention)
        module.init_app(app)


def init_app(app):
    FlaskDynaconf(app)
