__author__ = 'samgu'
import os
try:
    from cloghandler import ConcurrentRotatingFileHandler as RFHandler
except ImportError:
    # Next 2 lines are optional:  issue a warning to the user
    from warnings import warn
    warn("ConcurrentLogHandler package not installed.  Using builtin log handler")
    from logging.handlers import RotatingFileHandler as RFHandler
from speak import settings
import logging

def setup_logger(log_filename):
    logger = logging.getLogger()
    numeric_level = getattr(logging, settings.LOGGING['level'].upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('incorrect log level %s in settings' % settings.LOGGING['level'])

    logger.setLevel(numeric_level)
    formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
    # console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    #

    # file handler
    log_filepath = os.path.join(settings.LOGGING['dirname'], log_filename)
    rotate_handler = RFHandler(log_filepath, "a", settings.LOGGING['max_size'] * 1024 * 1024, settings.LOGGING['backup_num'])
    rotate_handler.setFormatter(formatter)
    logger.addHandler(rotate_handler)
    #






