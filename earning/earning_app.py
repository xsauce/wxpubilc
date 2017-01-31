# -*- coding: utf-8 -*-
import sys
sys.path.append('/usr/local/wxpublic/earning/')
import importlib
from flask import Flask

app = Flask(__name__)

@app.route('/<path:relative_path>', methods=['GET', 'POST'])
def app_main(relative_path):
    paths = relative_path.split('/')
    handler_name = paths[0]
    action_name = paths[1]
    handler_module = importlib.import_module('handler.{0}_handler'.format(handler_name))
    handler_obj = getattr(handler_module, '{0}_Handler'.format(handler_name))()
    return getattr(handler_obj, '{0}_action'.format(action_name))()