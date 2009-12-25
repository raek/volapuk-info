# -*- coding: utf-8 -*-
"""Setup the volapuksite application"""
import logging

from volapuksite.config.environment import load_environment
from volapuksite import model
from volapuksite.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup volapuksite here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    meta.metadata.create_all(bind=meta.engine)
    
