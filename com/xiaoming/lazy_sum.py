# -*- coding: UTF-8 -*-
# author fangxiaoming01

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


def test_try():
    try:
        print('try...')
        r = 10 / 1
        assert r != 0, 'sss'
        print('result', r)
    except ZeroDivisionError as e:
        print('except', e)
    finally:
        print('finally...')
    print('END')


if __name__ == '__main__':
    f = lazy_sum(1, 2, 3, 4)
    print(f())
    test_try()
