# -*- coding: UTF-8 -*-
# author fangxiaoming01

class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0--100')
        self.__score = value


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


if __name__ == '__main__':
    s = Student()
    s.score = 60  # s.set_score(60)
    print(s.score)

    f = now
    f()
