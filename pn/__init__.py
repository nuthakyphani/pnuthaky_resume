from flask import Flask

from config import config

from . import extensions, modules


app = Flask(__name__, static_url_path='/static')
def create_app(config_name):
    config_obj = config[config_name]()

    # Initializes configuration values.
    app.config.from_object(config_obj)

    # Configure SSL if the current platform supports it.
    if not app.debug and not app.testing and not app.config.get('SSL_DISABLE'):
        from flask_sslify import SSLify
        print ("SSLifying App")
        SSLify(app)

    # Initializes Flask extensions.
    extensions.init_app(app)

    # Initializes modules.
    modules.init_app(app)
    return app
