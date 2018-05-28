#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

import flask
from flask_session import Session

from project_name.config import config


here = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask('<project_name>',
                  static_folder=os.path.join(here, 'static'),
                  static_url_path='/static',
                  template_folder=os.path.join(here, 'templates'))


app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = config.session_cache_dir
app.secret_key = config.session_secret

Session(app)

# Here is where you could add stuff like DB initialization
# or wrap the app with other things


@app.teardown_appcontext
def shutdown_session(exception=None):
    """This is where you would end connections to the database"""


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return flask.render_template('404.html', error=e), 404


def register_blueprints():
    """This is functionalized so that a view could
    potentially import this app file if necessary"""
    from project_name.views import templated, admin
    app.register_blueprint(templated.blueprint)
    app.register_blueprint(admin.blueprint)
