# -*- coding: utf-8 -*-
import hashlib
from flask import request
import earning.settings
from earning.exceptions import WrongParameterError

class wechat_Handler(object):
    def __init__(self):
        pass

    def check_access_action(self):
        if self.is_valid_msg():
            return request.args.get('echostr')
        else:
            raise WrongParameterError('invalid wechat message')

    def is_valid_msg(self):
        sign = request.args.get('signature')
        token = earning.settings.WECHAT_SETTINGS['token']
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        sha = hashlib.sha1()
        sha.update(''.join(sorted([token, timestamp, nonce])))
        return sha.hexdigest() == sign

    def receive_msg_action(self):
        pass