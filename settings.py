__author__ = 'samgu'
import os
DEBUG = False

ROOT_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(ROOT_DIR, 'conf')

WX_CONF = {
    'token': 'smalllobster'
}

LOGGING = {
    'dirname': '/var/log/wxpublic',
    'level': 'INFO',
    'max_size': 100, # unit is MB
    'backup_num': 5
}

SERVER_SETTINGS = {
    'autoreload': DEBUG,
    'serve_traceback': DEBUG,
    'debug': DEBUG
}
