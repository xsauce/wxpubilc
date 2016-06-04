This is a weixin roboto, provide some abilities to service people

Abilities:
1. simple chat.
2. recognize flower
3. recognize word in photo and translate word to specified language
4. support some commands

Change log:
2016-05-31: change to python 3.5.1

Requirement:

lxml
tornado
https://github.com/huntersan9/Py3kAiml.git
ConcurrentLogHandler
requests
supervisor



Deploy:
# build venv
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install 3.5.1
pyenv virtualenv 3.5.1 wxenv

# config supervisor

# config nginx

# build server environment
python wxpublic/manager.py -build_env=1 -user={username}