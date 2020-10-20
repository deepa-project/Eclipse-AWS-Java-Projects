# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 03:29:41 2020

@author: deepa
Ref:https://stackoverflow.com/questions/7870869/python-main-call-within-class
"""


class Example(object):
    def run(self):
        print("Hello, world!")

if __name__ == '__main__':
    Example().run()