from tornado.web import RequestHandler
from util import log
__author__ = 'samgu'


class TestHandler(RequestHandler):
    def get(self):
        logger = log.create_logger('test_handler')
        logger.info('hello world test')
        self.write('hello world')