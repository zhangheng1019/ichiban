# -*- coding: utf-8-*-
# import os
# import datetime
# from io import BytesIO, StringIO
# from Order.query_API import *
# from Finance.query_API import *
# from Basic_info.models import *
# from Order.models import *
# from Finance.models import *
# from apple.views import *
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import *
# from django.contrib.auth import *
# from django.contrib.auth.decorators import login_required
# import json
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib import messages
# from django.core.serializers import serialize
# from django.forms.models import model_to_dict
# from django.contrib.auth.models import User
#
# import xlwt
# import time
# from pandas import DataFrame


# while i < 20:
#     # ========为样式创建字体
#     font = xlwt.Font()
#
#     # 字体类型
#     font.name = 'name Times New Roman'
#     # 字体颜色
#     font.colour_index = i
#     # 字体大小，11为字号，20为衡量单位
#     font.height = 20 * 11
#     # 字体加粗
#     font.bold = False
#     # 下划线
#     font.underline = True
#     # 斜体字
#     font.italic = True
#
#     # ========设置单元格对齐方式
#     alignment = xlwt.Alignment()
#     # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
#     alignment.horz = 0x02
#     # 0x00(上端对齐)、0x01(垂直方向上居中对齐)、0x02(底端对齐)
#     alignment.vert = 0x01
#
#     # 设置自动换行
#     alignment.wrap = 1
#
#     # ========设置边框
#     borders = xlwt.Borders()
#     # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
#     # 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
#     borders.left = 1
#     borders.right = 2
#     borders.top = 3
#     borders.bottom = 4
#     borders.left_colour = i
#     borders.right_colour = i
#     borders.top_colour = i
#     borders.bottom_colour = i
#
#     # 设置列宽，一个中文等于两个英文等于两个字符，11为字符数，256为衡量单位
#     sheet.col(1).width = 50 * 256
#
#     # ========设置背景颜色
#     pattern = xlwt.Pattern()
#     # 设置背景颜色的模式
#     pattern.pattern = xlwt.Pattern.SOLID_PATTERN
#     # 背景颜色
#     pattern.pattern_fore_colour = i
#
#     # 初始化样式
#     style0 = xlwt.XFStyle()
#     style0.font = font
#
#     style1 = xlwt.XFStyle()
#     style1.pattern = pattern
#
#     style2 = xlwt.XFStyle()
#     style2.alignment = alignment
#
#     style3 = xlwt.XFStyle()
#     style3.borders = borders
#
#     # ========设置文字模式
#     font.num_format_str = '#,##0.00'
#
#     # 数据写入
#     sheet.write(i, 0, u'字体', style0)
#     sheet.write(i, 1, u'背景', style1)
#     sheet.write(i, 2, u'对齐方式', style2)
#     sheet.write(i, 3, u'边框', style3)
#
#     # ========合并单元格，合并第2行到第4行的第4列到第5列
#     # sheet.write_merge(2, 4, 4, 5, u'合并')
#     i += 1
#
# book.save(time.strftime("%Y%m%d%H%M%S") + '.xlsx')

# pandas
# data = {
#     'name': [u'张三', u'李四', u'王五'],
#     'age': [21, 22, 23],
#     'sex': [u'男', u'女', u'男']
# }
# df = DataFrame(data)
# df.to_excel('test.xlsx')


# 定时任务
from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
#
#
#     # 1）date触发器，特定的时间点触发，作业任务只会执行一次。
#     '''
#     date：一次性任务，即只执行一次任务。
#     参数如下：
#     next_run_time (datetime|str) – 下一次任务执行时间
#     timezone (datetime.tzinfo|str) – 时区
#     '''
#     # 在 2019-03-29 14:00:00 时刻运行一次 job_func 方法
#     # scheduler.add_job(job_func, 'date', run_date=datetime(2019, 3, 29, 14, 0, 0), args=['text'])
#
#     # 2）interval 触发器，固定时间间隔触发。
#     '''
#     interval：循环任务，即按照时间间隔执行任务。
#     参数如下：
#     seconds (int) – 秒
#     minutes (int) – 分钟
#     hours (int) – 小时
#     days (int) – 日
#     weeks (int) – 周
#     start_date (datetime|str) – 启动开始时间
#     end_date (datetime|str) – 最后结束时间
#     timezone (datetime.tzinfo|str) – 时区
#     '''
#     # 在 2019-03-29 14:00:01 ~ 2019-03-29 14:00:10 之间, 每隔两分钟执行一次job_func方法。
#     # scheduler.add_job(job_func, 'interval', minutes=2, start_date='2019-03-29 14:00:01', end_date='2019-03-29 14:00:10')
#
#     # 3）cron 触发器，在特定时间周期性地触发，和Linux crontab格式兼容。
#     '''
#     cron：定时任务，即在每个时间段执行任务。
#     参数如下：
#     second (int|str) – 秒 (0-59)
#     minute (int|str) – 分钟 (0-59)
#     hour (int|str) – 小时 (0-23)
#     day_of_week (int|str) – 一周中的第几天 (0-6 or mon,tue,wed,thu,fri,sat,sun)
#     day (int|str) – 日 (1-31)
#     week (int|str) – 一年中的第几周 (1-53)
#     month (int|str) – 月 (1-12)
#     year (int|str) – 年(四位数)
#     start_date (datetime|str) – 最早开始时间
#     end_date (datetime|str) – 最晚结束时间
#     timezone (datetime.tzinfo|str) – 时区
#     '''
#     # 在2019-03-30 00:00:00之前，每周一到周五的5:30(am)触发
#     # sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2019-03-30')
