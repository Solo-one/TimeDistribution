# -*- coding: UTF-8 -*-
# author fangxiaoming01

from types import MethodType


class Student(object):
    pass


def set_score(self, score):
    self.score = score


if __name__ == '__main__':
    s = Student()
    s.name = 'xiaoming'
    s.score = 100
    # s.set_score = MethodType(set_score, s)
    Student.set_score = set_score
    s.set_score(102)
    print(s.name, s.score)
    print(s)

    b = Student()
    b.set_score(11)
    print(b.score)
