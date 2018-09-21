#!/usr/bin/env python3
# -*- coding: utf-8 -*-

myBook = list()
myBook.append('java')
myBook.append('python')
myBook.append('js')

for i in myBook:
    print(i)

myBook.insert(1, 'linux')
myBook.pop(len(myBook) - 1)

for i in myBook:
    print(i)

myTuple = (1, )
print(myTuple[0])

myInput = input('please input your number:')
print('my input number is:', myInput)