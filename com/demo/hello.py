#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
this is a test module
"""

__author__ = 'Test module'

import sys


def test():
    args = sys.argv
    length = len(args)
    if length == 1:
        print("hello world!")
    elif length == 2:
        print("hello, %s!" % args[1])
    else:
        print('Nice to meet you!')


if __name__ == '__main__':
    test()


