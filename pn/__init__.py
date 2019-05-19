from flask import Flask

from config import config

from . import extensions, modules


app = Flask(__name__, static_url_path='/static')
def create_app(config_name):
    config_obj = config[config_name]()
    #app = Flask(__name__, static_url_path='/static')

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
    print ("returing app")
    return app
'''
#app = create_app(os.getenv('FLASK_CONFIG', 'default'))
if __name__ == "__main__":
    app = create_app(os.getenv('FLASK_CONFIG', 'default'))
    #app.run(ssl_context=('/etc/certificates/www.phaninuthaky.com.140F4232D3B6D267534FC8B5A5A13964B8889B73.cert.pem', '/etc/certificates/www.phaninuthaky.com.140F4232D3B6D267534FC8B5A5A13964B8889B73.key.pem'))
    app.run(ssl_context=('fullchain.pem', 'privkey.pem'))
    #app.run()
'''
