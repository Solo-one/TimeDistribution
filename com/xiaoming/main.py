# -*- coding: UTF-8 -*-
# author xiaoming

import csv
import codecs
import sys
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
            print item[1], item[0]
            result[item[0]] = item[1]
        csvFile.close()


mydict = {}


def clc(hour, minute):
    # mydict = {}
    # for item in range(0, 48):
    #     mykey = item;
    #     mydict[mykey] = 0;

    # mydict[key] + 1;

    dict = {'00:00-00:30': 0, '00:30-01:00': 1, '01:00-01:30': 0};
    # print dict['00:30-01:00'] + 1
    return


def test():
    csvFile = open("../log.csv", "r")
    reader = csv.reader(csvFile)

    for item in reader:
        if reader.line_num == 1:
            continue
        str = item[0]
        # str = "2018年05月9日 23:35"
        mydate = datetime.datetime.strptime(str, "%Y\xc4\xea%m\xd4\xc2%d\xc8\xd5 %H:%M")
        print mydate.hour, mydate.minute
        clc(mydate.hour, mydate.minute)
        # print item[0].decode("gbk"), item[8]
    csvFile.close()


if __name__ == "__main__":
    print "hello world! 你好"
    for item in range(0, 48):
        mykey = item;
        mydict[mykey] = 0;
    # readCSVFile()
    str = "2018年05月9日 00:15"
    data_str = '2016-05-01 12:01:01'
    print datetime.datetime.strptime(str, "%Y年%m月%d日 %H:%M")
    test()

    for (k, v) in mydict.items():
        print "mydict[%s]=" % k, v
