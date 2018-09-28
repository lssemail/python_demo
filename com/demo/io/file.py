#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
input / output
"""

from io import StringIO


file = 'G:\liusir\PycharmProject\python_demo\com\logs\\201809261055.log'
with open(file, 'r') as f:
    print(f.read())

f = StringIO()
f.write('hello')
f.write('world')

print(f.getvalue())