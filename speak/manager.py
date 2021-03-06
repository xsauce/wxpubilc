from lib.ai import SimpleChat

__author__ = 'samgu'
import os
import settings
import argparse
import subprocess

class Manager:
    def build_server_running_env(self, args):
        try:
            if not args.user:
                print('incorrect user name')
                return
            user = args.user
            log_dir = settings.LOGGING['dirname']
            if not os.path.exists(log_dir):
                subprocess.call('sudo mkdir %s && sudo chown %s %s' % (log_dir, user, log_dir), shell=True)
                print('mkdir log')
            # generate chat.brain
            tmp_aiml_dir = os.path.join(settings.TMP_DIR, 'aiml')
            subprocess.call('mkdir -p %s' % tmp_aiml_dir, shell=True)
            subprocess.call('cp %s/* %s/' % (os.path.join(settings.CONF_DIR, 'aiml'), tmp_aiml_dir), shell=True)
            SimpleChat()
            print('boot chat brain successfully')
        except Exception as e:
            print('build server running env happened errors', e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-build_env', type=int, default=0)
    parser.add_argument('-user', type=str, default='')

    args = parser.parse_args()

    manager = Manager()

    if args.build_env:
        manager.build_server_running_env(args)

