from tornado.web import RequestHandler
import settings
from util import log, wx_util
__author__ = 'samgu'


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.logger = log.get_server_logger()



class TestHandler(BaseHandler):
    def get(self):
        self.logger.info('hello world test')
        self.write('hello world')

class WXHandler(BaseHandler):
    def get(self):
        signature = self.get_query_argument('signature', '')
        timestamp = self.get_query_argument('timestamp', '')
        nonce = self.get_query_argument('nonce', '')
        echostr = self.get_query_argument('echostr', '')
        token = settings.WX_CONF['token']
        if wx_util.valid_wx(token, timestamp, nonce, signature):
            self.write(echostr)
        else:
            self.logger.error('valid wx error;')
            self.write('Failed')

    def post(self, *args, **kwargs):
        self.logger.debug('post content: {0}'.format(self.request.body_arguments))


