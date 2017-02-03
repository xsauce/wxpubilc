# -*- coding: utf-8 -*-
class NormalError(Exception):
    def __init__(self, *args, **kwargs):
        super(NormalError, self).__init__(*args, **kwargs)


class WrongParameterError(Exception):
    def __init__(self, *args, **kwargs):
        super(WrongParameterError, self).__init__(*args, **kwargs)

