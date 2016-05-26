__author__ = 'samgu'
DEBUG = False

WX_CONF = {
    'token': 'smalllobster'
}

LOGGING = {
    'dirname': '/var/log/wxpublic',
    'level': 'INFO'
}

SERVER_SETTINGS = {
    'autoreload': DEBUG,
    'serve_traceback': DEBUG,
    'debug': DEBUG
}
