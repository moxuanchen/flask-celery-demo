# -*- coding: utf-8 -*-

import os
import yaml


class Config(object):

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    def __init__(self):
        APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
        config_file = os.path.join(APP_DIR, "settings" + '.yaml')
        if os.path.isfile(config_file):
            conf = yaml.load(open(config_file), Loader=yaml.SafeLoader) or {}
            for k, v in conf.items():
                setattr(self, k, v)


class LocalConfig(Config):
    """Production configuration."""
    pass


def get_config_env():
    envs = {
        "local": LocalConfig()
    }
    return envs[os.getenv("FLASK_ENV", "local")]
