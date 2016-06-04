# coding: utf-8
import logging
import time
from lib.ai import AI
import hashlib
from lxml import etree

__author__ = 'samgu'

NO_SUPPORT = 'no_support'

def valid_wx(token, timestamp, nonce, signature):
    valid_str = ''.join(sorted([token, timestamp, nonce]))
    valid_str = hashlib.sha1(valid_str).hexdigest()
    if valid_str.lower() == signature.lower():
        return 1
    else:
        return 0


def handle_wx_message(xml_str):
    logger = logging.getLogger(__name__)
    try:
        if xml_str:
            parser = WXMessageParser(xml_str)
            msg_dict = parser.parse()
            reply_dict = AI().get_wx_reuslt(msg_dict)
            reply = WXMessageReply(msg_dict['to_user_name'], msg_dict['from_user_name'], reply_dict)
            reply_xml = reply.reply_xml()
            logger.debug('succss to reply xml:{0}'.format(reply_xml))
            return reply_xml
        else:
            raise Exception('message xml is null')

    except:
        logger.error('fail to reply wx message', exc_info=True)
        return 'failed'


class WXMessageParser(object):
    def __init__(self, xml_str):
        self.xml_str = xml_str
        self.logger = logging.getLogger(__name__)

    def parse(self):
        msg_dict = {}
        try:
            if self.xml_str:
                self.xml_obj = etree.fromstring(self.xml_str)
                msg_dict['to_user_name'] = self.xml_obj.xpath('ToUserName')[0].text
                msg_dict['from_user_name'] = self.xml_obj.xpath('FromUserName')[0].text
                msg_dict['create_time'] = self.xml_obj.xpath('CreateTime')[0].text
                msg_dict['msg_type'] = self.xml_obj.xpath('MsgType')[0].text
                msg_dict['content_obj'] = getattr(self, msg_dict['msg_type'] + '_parse')()
                return msg_dict
        except Exception as e:
            self.logger.error('fail to parse wx message', exc_info=True)
            raise e

    def text_parse(self):
        return self.xml_obj.xpath('Content')[0].text

    def image_parse(self):
        return NO_SUPPORT

    def voice_parse(self):
        return NO_SUPPORT

    def video_parse(self):
        return NO_SUPPORT

    def music_parse(self):
        return NO_SUPPORT

    def news_parse(self):
        return NO_SUPPORT



class WXMessageReply(object):
    def __init__(self, from_user_name, to_user_name, reply_dict):
        self.from_user_name = from_user_name
        self.to_user_name = to_user_name
        self.reply_dict = reply_dict

    def reply_xml(self):
        return getattr(self, self.reply_dict['msg_type'] + '_reply')()

    def text_reply(self):
        return '''
        <xml>
        <ToUserName><![CDATA[{0}]]></ToUserName>
        <FromUserName><![CDATA[{1}]]></FromUserName>
        <CreateTime>{2}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{3}]]></Content>
        </xml>
        '''.format(self.to_user_name, self.from_user_name, int(time.time()), self.reply_dict['content'])





