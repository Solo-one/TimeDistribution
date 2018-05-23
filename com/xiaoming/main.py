# -*- coding: UTF-8 -*-
# author xiaoming

import codecs
import csv
import datetime


def readCSVFile():
    csvFile = open("../log.csv", "r")
    with codecs.open("../log.csv", "rb", 'gb2312') as csvFile:
        # csvFile = open("D:\workspace\Python\log.csv", "r")
        reader = csv.reader(csvFile)
        # reader = csv.DictReader(csvFile)
        result = {}  # 建立空字典
        for item in reader:
            if reader.line_num == 1:
                continue
            print
            item[1], item[0]
            result[item[0]] = item[1]
        csvFile.close()


mydict = {}


def clc(hour, minute):
    # mydict = {}
    # for item in range(0, 48):
    #     mykey = item;
    #     mydict[mykey] = 0;

    # mydict[key] + 1;

    dict = {'00:00-00:30': 0, '00:30-01:00': 1, '01:00-01:30': 0}
    # print dict['00:30-01:00'] + 1
    # key = hour + minute
    # mydict[key] += 1
    print(str(20) + "1")
    sp = int(minute / 30)
    key1 = str(hour) + "_" + str(sp)
    mydict[key1] += 1
    print(key1)

    return


def test():
    csvFile = open("../log.csv", "r")
    reader = csv.reader(csvFile)

    for item in reader:
        if reader.line_num == 1:
            continue
        str = item[0]
        # str = "2018年05月9日 23:35"
        mydate = datetime.datetime.strptime(str, "%Y年%m月%d日 %H:%M")
        print(mydate.hour, mydate.minute)
        clc(mydate.hour, mydate.minute)
        # print item[0].decode("gbk"), item[8]
    csvFile.close()


if __name__ == "__main__":
    print("hello world! 你好")
    for i in range(0, 24):
        for j in range(0, 2):
            mydict[str(i) + "_" + str(j)] = 0  # 初始化key

    # 简单频次计算
    test()

    for (k, v) in mydict.items():
        print("mydict[%s]=" % k, v)
