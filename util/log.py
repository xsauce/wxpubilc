__author__ = 'samgu'
import os
import logging
import settings

_server_logger = None

def create_logger(logger_name):
    logger = logging.getLogger(logger_name)
    log_level_dict = {
        'NOTSET': logging.NOTSET,
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    logger.setLevel(log_level_dict[settings.LOGGING['level']])
    formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
    # console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    #

    # file handler
    fh = logging.FileHandler(os.path.join(settings.LOGGING['dirname'], logger_name) + '.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    #
    return logger


def get_server_logger():
    global _server_logger
    if _server_logger is None:
        _server_logger = create_logger('server')
    return _server_logger






