# -*- coding: UTF-8 -*-
# author fangxiaoming01

import time
import datetime


def in_time_range(ranges):
    now = time.strptime(time.strftime("%H%M%S"), "%H%M%S")
    ranges = ranges.split(",")
    for range in ranges:
        r = range.split("-")
        if time.strptime(r[0], "%H%M%S") <= now <= time.strptime(r[1], "%H%M%S") \
                or time.strptime(r[0], "%H%M%S") >= now >= time.strptime(r[1], "%H%M%S"):
            return True
    return False


def in_time_is(time, key):
    return 0


def time_range_0000_0030(now):
    start = time.strptime("17:30", "%H:%M")
    end = time.strptime("18:00", "%H:%M")
    if start <= now <= end or start >= now >= end:
        return True
    return False


def time_range(now):
    init = datetime.datetime.strptime("00:00", "%H:%M")
    print(init)
    start = init
    end = init + datetime.timedelta(minutes=30)
    print(start, end)
    if start <= now <= end or start >= now >= end:
        return True
    return False


kv = {"00:00-00:30": 0, "00:30-01:00": 0, "17:30-18:00": 0}

if __name__ == "__main__":
    flag = in_time_range("093000-113000,133000-153000")
    print(flag)
    now = time.strptime(time.strftime("%H%M"), "%H%M")
    print(now)
    print(time_range_0000_0030(now))

    test = datetime.datetime.strptime("2018年05月9日 18:07", "%Y年%m月%d日 %H:%M")
    print(time_range(test))
