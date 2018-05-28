#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(here, os.pardir))

from project_name.main import run_server
run_server()
