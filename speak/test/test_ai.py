# coding:utf-8
from speak.lib import AI

__author__ = 'sam'

def test_ai_chat():
    robot = AI()
    while 1:
        t = input("Enter your message >> ")
        print(robot.chat(t))

if __name__ == '__main__':
    test_ai_chat()
