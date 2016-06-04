# coding:utf-8
__author__ = 'samgu'
from tornado.web import RequestHandler
import settings
from util import wx_util
from util.wx_util import handle_wx_message
import logging


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)


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
        self.logger.info('post content: {0}'.format(self.request.body))
        return_text = handle_wx_message(self.request.body)
        self.logger.info(('return text:%s' % return_text))
        self.write(return_text)

class AsyncWXHandler(BaseHandler):
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
        # valid whether request is from wx
        # signature = self.get_query_argument('signature', '')
        # timestamp = self.get_query_argument('timestamp', '')
        # nonce = self.get_query_argument('nonce', '')
        # token = settings.WX_CONF['token']
        # if wx_util.valid_wx(token, timestamp, nonce, signature):
        #     self.logger.error('invalid wx request')
        #     self.write('invalid request')

        self.logger.info('post content: {0}'.format(self.request.body))
        if self.request.body:
            return_text = handle_wx_message(self.request.body)
            self.logger.info(('return text:%s' % return_text))
            self.write(return_text)
        else:
            self.logger.info('no request message')
            self.write('1')


