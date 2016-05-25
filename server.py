import handler
from util import log

__author__ = 'samgu'
import tornado.ioloop
import tornado.web
import settings
import argparse


URL_ROUTES = [(r'/test', handler.TestHandler)]

def make_server():
    return tornado.web.Application(URL_ROUTES, **settings.SERVER_SETTINGS)

if __name__ == '__main__':
    logger = log.create_logger('server')
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-debug', type=int, default=0)
        parser.add_argument('-port', type=int, default=80)

        args = parser.parse_args()
        if args.debug == 1:
            settings.DEBUG = True
            settings.LOGGING['level'] = 'DEBUG'

        server = make_server()
        logger.info('start server on port {0}'.format(args.port))
        server.listen(args.port)
        tornado.ioloop.IOLoop.current().start()
    except:
        logger.error('fail to start server', exc_info=True)


