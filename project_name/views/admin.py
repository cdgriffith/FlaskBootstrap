#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging

from flask import render_template, Blueprint

from project_name.config import config

# We are adding the prefix to the blueprint itself, then will add
# BasicAuth via Nginx to project all these endpoints

blueprint = Blueprint('admin', __name__,
                      url_prefix="/admin",
                      template_folder='templates')

log = logging.getLogger('<project_name>')


@blueprint.route('/')
def index():
    return render_template('admin.html',
                           page_name='Admin Area',
                           project_name="<project_name>")
