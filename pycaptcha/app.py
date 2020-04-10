from flask import Flask
from pycaptcha.ext import configuration


def create_app():
    app = Flask(__name__, template_folder='blueprints/templates', static_folder='blueprints/static')
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app
