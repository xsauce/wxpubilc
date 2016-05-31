import os
import settings

__author__ = 'samgu'
import aiml


class SimpleChat(object):
    def __init__(self, startupxml, speech_mode):
        self.startupxml = startupxml
        self._brain = aiml.Kernel()
        self._brain.learn(startupxml)
        self._brain.respond(speech_mode)

    def reply(self, input):
        return self._brain.respond(input)



class AI(object):

    AIML_XML = os.path.join(settings.CONF_DIR, 'aiml', 'std-startup.xml')

    def __init__(self):
        self._chat_power = SimpleChat(self.AIML_XML, 'basic')

    def get_wx_reuslt(self, msg_dict):
        return getattr(self, msg_dict['msg_type'])(msg_dict)

    def chat(self, text):
        return self._chat_power.reply(text)

    def text(self, msg_dict):
        try:
            input = str(msg_dict['content_obj']).strip()
        except:
            input = ''
        return {'msg_type': 'text', 'content': self.chat(input)}





