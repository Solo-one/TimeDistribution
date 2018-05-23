# -*- coding: UTF-8 -*-
# author fangxiaoming01

import csv
import datetime
import time

'''
调参变量
time_section：时间片段参数，1:60分钟分割 2:30分钟 3:20分钟 4:15分钟 
flag_time：停留时间阀值（单位秒）
'''
time_section = 2  # 30分钟为一个区间段
flag_time = 60  # 建议设置60秒

mydict = {}  # 全局字典
userid = "0"
pre_mydate = ""
tmp_key = ""
all_student = set()


def clc(item, mydate):
    global userid
    global pre_mydate
    global tmp_key

    if item[0] == userid:
        # print(mydate, pre_mydate)
        residence_time = (pre_mydate - mydate).seconds
        if residence_time < flag_time:  # 停留时间阀值
            return

        section = int(mydate.minute / (60 / time_section))
        mykey = str(mydate.hour) + "_" + str(section)
        if tmp_key == mykey:
            return
        else:
            mydict[mykey] += 1
            tmp_key = mykey
            return
    else:
        userid = item[0]
        pre_mydate = mydate
        # section = int(mydate.minute / 30)
        # mykey = str(mydate.hour) + "_" + str(section)
        # mydict[mykey] += 1
    return


'''
def clc(mydate, hour, minute):
    global share
    global premydate
    global tmpKey

    # print(mydate)

    section = int(minute / 30)
    mykey = str(hour) + "_" + str(section)
    mydict[mykey] += 1
    return
'''


def test():
    csvFile = open("../id_time_log.csv", "r")
    reader = csv.reader(csvFile)
    for item in reader:
        if reader.line_num == 1:
            continue
        # str = "2018年05月9日 23:35"
        mydate = datetime.datetime.strptime(item[1], "%d/%m/%y, %H:%M")
        all_student.add(item[0])
        clc(item, mydate)
    csvFile.close()
    return


if __name__ == "__main__":
    print("start calculating ...")
    start = time.time()
    for i in range(0, 24):
        for j in range(0, time_section):
            mydict[str(i) + "_" + str(j)] = 0  # 初始化key

    # 简单频次计算
    test()

    '''遍历输出统计结果'''
    for (k, v) in mydict.items():
        # arr = k.split("_")
        # i = arr[0] + "时" + ("00" if arr[1] == "0" else "30") + "分"
        # j = "--"
        # m = (arr[0] if arr[1] == "0" else str((int(arr[0]) + 1))) + "时" + ("30" if arr[1] == "0" else "00") + "分"
        print("mydict[%s]=" % k, v)

    end = time.time()
    print("耗时：%.3f 秒" % (end - start))
    print("\n参与统计的学生人数：%d" % len(all_student))
