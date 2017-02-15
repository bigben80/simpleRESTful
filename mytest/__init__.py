from flask import Blueprint, Flask
from .config import DebugConfig as debug_config
from .config import config
from .api_1_0 import api_bp
from gevent.wsgi import WSGIServer

import logging
import os
import socket

strformat = ('[%(asctime)s] %(name)-10s %(filename)s:%(lineno)d ' +
             '%(levelname)s %(message)s')
logging.basicConfig(
    filename='./test.log',
    level=logging.DEBUG,
    format=strformat,
    datefmt='%m/%d/%y %H:%M:%S')

logging.getLogger(__name__).setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)

def create_app():
    template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'template')
    app = Flask(__name__, template_folder=template_folder)
    app.config.from_object(debug_config)

    try:
        app.register_blueprint(api_bp, url_prefix=app.config["URL_PREFIX"])
        
    except:
        logger.error("Can not register Blueprint API")
    
    return app

def run():
    logger.info(">>>> starting app now >>>>")

    logger.info(">>>> configuration items loaded: >>>>")

    app = create_app()
    
    for k, v in app.config.items():
        logger.info("\t\t\t %s: %s" % (k, v))

    try:
        port = int(app.config["PORT"])
        http_server = WSGIServer(('', port), app)
        http_server.serve_forever()
    except socket.error:
        logger.error("Socket error! can not start app at port {}".format(port))

def version():
    import pkg_resources
    return pkg_resources.require("mytest")[0].version
