from tornado.web import RequestHandler
import settings
from util import log, wx_util
__author__ = 'samgu'


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.logger = log.create_logger('server')



class TestHandler(BaseHandler):
    def get(self):
        self.logger.info('hello world test')
        self.write('hello world')

class WXValidHandler(BaseHandler):
    def get(self):
        signature = self.get_query_argument('signature', '')
        timestamp = self.get_query_argument('timestamp', '')
        nonce = self.get_query_argument('nonce', '')
        echostr = self.get_query_argument('echostr', '')
        token = settings.WX_CONF['token']
        if wx_util.valid_wx(token, timestamp, nonce, signature):
            self.write('Success')
        else:
            self.write('Failed')
