# -*- coding: utf-8 -*-
import argparse
import sys
sys.path.append('/usr/local/wxpublic/earning/')
from earning_app import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help='port num', default=9990, type=int)
    parser.add_argument('--debug', help='debug', default=True, type=bool)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=args.debug)