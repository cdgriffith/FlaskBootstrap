#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import logging
import logging.config

from box import Box
import yaml

here = os.path.abspath(os.path.dirname(__file__))
log = logging.getLogger('<project_name>')

# Box just makes the config dictionary dot.accessible
# i.e. config.env == "development"

config = Box({
    "env": "development",
    "host": "127.0.0.1",
    "port": 8080,
    "session_cache_dir": os.path.join(here, "cache", "session"),
    "session_secret": 'bad_secret',  # make real one with os.urandom(32).hex()
    "data_dir": os.path.join(here, "data"),
    "ssl": False
})

# TODO add find functions for configs

# Sets up custom logging
try:
    with open(os.path.join(here, os.pardir, "project_name.logging.yaml")) as f:
        logging.config.dictConfig(yaml.load(f, yaml.SafeLoader))
except Exception as err:
    print(f"Could not load logging config: {err}")
else:
    log.info("Log configuration applied")

# Overwrites config with custom values,
# allowing for better dev vs prod management
try:
    with open(os.path.join(here, os.pardir, "project_name.config.yaml")) as cf:
        config.update(yaml.load(cf, yaml.SafeLoader))
except OSError as err:
    log.error("Could not load custom config file")
except Exception as err:
    log.exception("Error while loading custom config file")
else:
    log.info("Custom configuration applied")

os.makedirs(config.session_cache_dir, exist_ok=True)
os.makedirs(config.data_dir, exist_ok=True)
