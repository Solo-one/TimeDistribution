# -*- coding: UTF-8 -*-
# author fangxiaoming01

class Student(object):
    def __init__(self, name, scores):
        self.name = name
        self.__scores = scores

    def print_score(self):
        print('%s : %s' % (self.name, self.__scores))

    def get_score(self):
        return self.__scores

    def set_score(self, score):
        self.__scores = score


if __name__ == '__main__':
    aa = Student('xiaoming', 23)
    bb = Student('xierui', 23)
    aa.print_score()
    bb.print_score()

    print(aa.name)
    # print(bb.scores)
    bb.set_score(102)
    print(bb.get_score())
