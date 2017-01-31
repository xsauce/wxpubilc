# coding:utf-8
import logging

import requests

from speak import settings

__author__ = 'samgu'
# import aiml


# class SimpleChat(object):
#     def __init__(self):
#         self._logger = logging.getLogger(__name__)
#         self._startup_xml = os.path.join(settings.TMP_DIR, 'aiml', 'std-startup.xml')
#         self._chat_brain_file = os.path.join(settings.CONF_DIR, 'aiml', 'chat_brain.brn')
#         if os.path.exists(self._chat_brain_file):
#             self._brain = aiml.Kernel()
#             self._brain.bootstrap(brainFile=self._chat_brain_file)
#         else:
#             self.boot()
#             self._brain = None
#
#     def boot(self):
#         self._brain = aiml.Kernel()
#         self._brain.bootstrap(learnFiles=self._startup_xml, commands='chat')
#         self._brain.saveBrain(self._chat_brain_file)
#
#     def reply(self, input):
#         if self._brain:
#             return self._brain.respond(input)
#         else:
#             self._logger.error('no brain')
#             return ''


class Turing123Robot(object):
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def reply(self, userid, text):
        request_body = {
            'key': settings.TURING_API_CONF['key'],
            'userid': userid,
            'info': text
        }
        response = requests.post(
            settings.TURING_API_CONF['api'],
            data=request_body
        )
        turing_resp = response.json()
        if turing_resp['code'] == 40007:
            self._logger.error('turing error:%s', str(turing_resp))
            return '系统异常, %s' % str(turing_resp)
        else:
            return turing_resp.get('text')


class AI(object):
    def __init__(self):
        self._chat_power = Turing123Robot()

    def get_wx_reuslt(self, msg_dict):
        return getattr(self, msg_dict['msg_type'])(msg_dict)

    def chat(self, text, to_user_name):
        return self._chat_power.reply(text, to_user_name)

    def text(self, msg_dict):
        try:
            input = str(msg_dict['content_obj']).strip()
        except:
            input = ''
        return {'msg_type': 'text', 'content': self.chat(msg_dict['to_user_name'], input)}

    def voice(self, msg_dict):
        return {'msg_type': 'text', 'content': '暂时不能语音对话哦！'}

    def image(self, msg_dict):
        return {'msg_type': 'text', 'content': '暂时看不懂图片！'}

    def video(self, msg_dict):
        return {'msg_type': 'text', 'content': '暂时看不懂视频哦'}

    def music(self, msg_dict):
        return {'msg_type': 'text', 'content': '暂时听不懂音乐'}

    def news(self, msg_dict):
        return {'msg_type': 'text', 'content': '不懂你发的啥'}





