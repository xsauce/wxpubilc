__author__ = 'samgu'

class AI(object):
    def __init__(self):
        pass

    def get_wx_reuslt(self, msg_dict):
        return getattr(self, msg_dict['msg_type'])(self, msg_dict)

    def text(self, msg_dict):
        return msg_dict['content']


