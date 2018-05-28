#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cherrypy

from project_name.config import config
from project_name.app import app, register_blueprints


def run_server():
    register_blueprints()
    if config.env == "production":
        cherrypi_server()
    else:
        flask_server()


def flask_server():
    app.run(host=config.host, port=config.port, debug=True)


def cherrypi_server():
    cherrypy.tree.graft(app, '/')

    cherrypy.config.update({
        'engine.autoreload_on': False,
        'log.screen': False,
        'server.socket_port': config.port,
        'server.socket_host': config.host
    })

    if config.get('ssl'):
        cherrypy.config.update({
            'server.ssl_certificate': config.ssl_cert,
            'server.ssl_private_key': config.ssl_key
        })
        if config.get('ssl_chain'):
            cherrypy.config.update({
                'server.ssl_certificate_chain': config.ssl_chain
            })

    cherrypy.engine.start()
    try:
        cherrypy.engine.block()
    finally:
        cherrypy.engine.stop()


if __name__ == '__main__':
    run_server()
