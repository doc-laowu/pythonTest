#-*- coding: UTF-8 -*-
# ==================================================================================================
# desc          : 处理考勤原始数据的脚本,需要把存放在excel中的数据粘贴到文本文件中进行处理
# created info  : system 2020-10-09 21:57:15
# note          : yisheng.wu
# ==================================================================================================
import datetime


# 进行考勤数据的清晰操作
def dealKaoQinTime(date_first, date_last, month, jstr, lastDate, dateArr):

    # 当用户的首次打卡记录为（0-7）并且前一天有打卡记录则设置前一天末次打卡记录为23:59:00。
    if (bool(lastDate) and int(date_first[0:2]) >= 0 and int(date_first[0:2]) <= 7):
        tmp_end_time = "2020-%s-%s %s:00" % (month, jstr, "23:59")
        tmp_end_time=(datetime.datetime.strptime(tmp_end_time, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(-1)).strftime("%Y-%m-%d %H:%M:%S")
        lastDate['end_time'] = tmp_end_time

    start_time = None
    end_time = None

    # 当用户首次和末次打卡记录都为上午（0-12），则补晚上19点下班打卡记录。
    if (int(date_first[0:2]) >= 0 and int(date_last[0:2]) < 12):
        start_time = "2020-%s-%s %s:00" % (month, jstr, date_first)
        end_time = "2020-%s-%s %s:00" % (month, jstr, "19:00")

    # 当用户首次和末次打卡记录都为下午（12-23），则补早上10点上班打卡记录。
    elif (int(date_first[0:2]) >= 12 and int(date_last[0:2]) <= 23):
        start_time = "2020-%s-%s %s:00" % (month, jstr, "10:00")
        end_time = "2020-%s-%s %s:00" % (month, jstr, date_last)

    # 打卡时间正常
    else:
        start_time = "2020-%s-%s %s:00" % (month, jstr, date_first)
        end_time = "2020-%s-%s %s:00" % (month, jstr, date_last)

    # 返回当天的数据
    record_str = ','.join(dateArr)
    record_str = "2020-%s-%s %s" % (month, jstr, record_str)
    ret = {
        "name":name,
        "start_time":start_time,
        "end_time":end_time,
        "record":record_str
    }
    return ret


if __name__ == "__main__":

    readFilepath = 'C:\\Users\\gaosen\\Desktop\\month_9.txt'
    writeFilepath = 'C:\\Users\\gaosen\\Desktop\\month_9_dealed.txt'
    month = "09"

    readfd = open(file=readFilepath, mode='r', encoding='UTF-8')
    writefd = open(file=writeFilepath, mode='w+', encoding='UTF-8')
    lines = readfd.readlines()
    for line in lines:
        arr = line.split("\t")
        # 姓名
        name = arr[2].rstrip(' ').lstrip(' ')
        j = 0
        jstr = None
        start_time = None
        end_time = None
        # 用来存储上一个
        lastDate = {}

        for i in range(3, len(arr)):

            dateArr = arr[i].lstrip(" ").split(" ")

            j = j+1
            if (j < 10):
                jstr = "0%d" % j
            else:
                jstr = "%d" % j


            if(len(dateArr) >= 1 and len(dateArr[len(dateArr)-1]) >= 5):
                date_first = dateArr[0].rstrip("\r\n")
                date_last = dateArr[len(dateArr)-1].rstrip("\r\n")
                ret = dealKaoQinTime(date_first, date_last, month, jstr, lastDate, dateArr)
                # 先取出老的数据
                if(bool(lastDate)):
                    name = lastDate["name"]
                    start_time = lastDate["start_time"]
                    end_time = lastDate["end_time"]
                    record = lastDate["record"]
                    lastDate.clear()
                    content = "%s\t%s\t%s\t%s\n" % (name, start_time, end_time, record)
                    print(content)
                    writefd.write(content)
                # 再设置新数据
                lastDate = ret

            else:
                # 先取出老的数据
                if (bool(lastDate)):
                    name = lastDate["name"]
                    start_time = lastDate["start_time"]
                    end_time = lastDate["end_time"]
                    record = lastDate["record"]
                    lastDate.clear()
                    content = "%s\t%s\t%s\t%s\n" % (name, start_time, end_time, record)
                    print(content)
                    writefd.write(content)


    writefd.flush()
    writefd.close()
    readfd.close()
