__author__ = 'samgu'
import os
DEBUG = False

ROOT_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(ROOT_DIR, 'conf')
TMP_DIR = '/tmp/wxpublic'

TURING_API_CONF = {
    'api': 'http://www.tuling123.com/openapi/api',
    'key': '0a027fafe5460cd71c5239f64eb319e0'
}

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


