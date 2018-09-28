#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
this is a test module
"""

__author__ = 'oop'

import types


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.__age = 18

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def set_score(self, score):
        self.__score = score

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('age must between 0 ~ 100!')
        self.__age = value


def myFunction():
    pass

if __name__ == '__main__':

    student = Student('Jack', 89)
    student.print_score()
    print(student.get_grade())
    print(student.get_name())
    print(type(myFunction))
    print(types.FunctionType)
    print(type(myFunction) == types.FunctionType)
    print(dir(student))