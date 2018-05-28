#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging

from flask import render_template, Blueprint

from project_name.config import config

blueprint = Blueprint('templated', __name__, template_folder='templates')

log = logging.getLogger('<project_name>')


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template('index.html',
                           page_name='Main',
                           project_name="<project_name>")
