import os
import time
import uuid
import hashlib
import random
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.shortcuts import render, redirect
from apple import settings
from Basic_info.models import *
from Order.models import *
from Finance.models import *
from POM.models import *
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from apple.views import *
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import logging
from send_email import send_mail


# 日志基础配置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='./POM/logs/pom_logs.txt',  # 相对于项目的路径
                    filemode='a')


# 任务出错通知 -- 测试
def my_listener(event):
    if event.exception:
        print('任务出错了！！！！！！')
    else:
        print('任务照常运行...')


# 定时从Po、Po_detail、Contract、Product_send、OMR、OMR_po_detail表中同步数据到POM数据库表Po_point中去
def po_data_check():
    """
    设置定时器，每天定时将Po所有信息转储到po_point表中
    """
    # 删除原有Po_point表中所有数据
    po_point = PoPoint.objects.all()
    po_point.delete()
    # 获取所有item条目数据信息
    po_detail = Po_detail.objects.all()
    if not po_detail:
        return JsonResponse({'status': 'fail', 'msg': 'Po_detail无数据。'})
    # 取出每一条po_detail数据
    for i in po_detail:
        # po信息
        try:
            po = Po.objects.get(order_number=i.po)
        except:
            return JsonResponse({'status': 'fail', 'msg': 'Po无数据。'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=i.po, item_no=i.item_no)
            factory = contract.factory
            fac_currency = contract.fac_currency
            fac_cost = contract.fac_cost
            fac_total = contract.fac_total
            cancle_date = contract.cancle_date
        except:
            factory = ''
            fac_currency = ''
            fac_cost = ''
            fac_total = ''
            cancle_date = ''
            # return JsonResponse({'status': 'fail', 'msg': 'Contract(合同)无数据。'})
            # print('Contract(合同)无数据。')
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=i.po, item_no=i.item_no)
            qc1 = product_send.qc1
            qc2 = product_send.qc2
            qc3 = product_send.qc3
            rqc1 = product_send.rqc1
            rqc2 = product_send.rqc2
            no_pass = product_send.no_pass
            send_person = product_send.send_person
        except:
            qc1 = ''
            qc2 = ''
            qc3 = ''
            rqc1 = ''
            rqc2 = ''
            no_pass = ''
            send_person = ''
            # return JsonResponse({'status': 'fail', 'msg': 'Product_send(消出货)无数据。'})
            # print('Product_send(消出货)无数据。')
        # omr信息
        try:
            omr = OMR.objects.get(po=i.po, item_no=i.item_no)
            special_remark = omr.special_remark
        except:
            special_remark = ''
        # omr详情信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=i.po, item_no=i.item_no)
            process = omr_po_detail.process
            produce_record = omr_po_detail.produce_record
            mark_notice_date = omr_po_detail.mark_notice_date
            label_sure_date = omr_po_detail.label_sure_date
            label_send_date = omr_po_detail.label_send_date
            sample_send_date = omr_po_detail.sample_send_date
            sample_pass_date = omr_po_detail.sample_pass_date
            product_send_date = omr_po_detail.product_send_date
            product_sure_date = omr_po_detail.product_sure_date
            midterm_inspect = omr_po_detail.midterm_inspect
            booking_so = omr_po_detail.booking_so
            ichiban_inspect = omr_po_detail.ichiban_inspect
            customer_inspect = omr_po_detail.customer_inspect
            pl_come_date = omr_po_detail.pl_come_date
            box_sure_date = omr_po_detail.box_sure_date
            box_send_date = omr_po_detail.box_send_date
            shipping_data = omr_po_detail.shipping_data
        except:
            process = ''
            produce_record = ''
            mark_notice_date = ''
            label_sure_date = ''
            label_send_date = ''
            sample_send_date = ''
            sample_pass_date = ''
            product_send_date = ''
            product_sure_date = ''
            midterm_inspect = ''
            booking_so = ''
            ichiban_inspect = ''
            customer_inspect = ''
            pl_come_date = ''
            box_sure_date = ''
            box_send_date = ''
            shipping_data = ''
            # return JsonResponse({'status': 'fail', 'msg': 'omr_po_detail(OMR详情)无数据。'})
            # print('omr_po_detail(OMR详情)无数据。')

        dict_info = {
            # po
            'customer': po.customer,
            'customer_pono': po.customer_pono,
            'cus_receive_date': po.cus_receive_date,
            'fina_date': po.fina_date,
            'receive_date': po.receive_date,
            'order_number': po.order_number,
            'fac_send_date': po.fac_send_date,
            'produce_native_date': po.produce_native_date,
            'delivery_condition': po.delivery_condition,
            'port': po.port,
            'omr': po.omr,
            'pay_type': po.pay_type,
            # po_detail
            'item_no': i.item_no,
            'customer_item': i.customer_item,
            'desc': i.desc,
            'edesc': i.edesc,
            'fac_no': i.fac_no,
            'texture': i.texture,
            'amount': i.amount,
            'unit': i.unit,
            'costrate': i.costrate,
            'currency': i.currency,
            'each_box': i.each_box,
            'outside_box': i.outside_box,
            'middle_box': i.middle_box,
            'inner_box': i.inner_box,
            'box_unit': i.box_unit,
            'for_profit_report': i.for_profit_report,
            'fac_delivery': i.fac_delivery,
            'fac_delivery_port': i.fac_delivery_port,
            'fmr': i.fmr,
            'fqc': i.fqc,
            'sale_date': i.sale_date,
            # contract
            'factory': factory,
            'fac_currency': fac_currency,
            'fac_cost': fac_cost,
            'fac_total': fac_total,
            'cancle_date': cancle_date,
            # product_send
            'qc1': qc1,
            'qc2': qc2,
            'qc3': qc3,
            'rqc1': rqc1,
            'rqc2': rqc2,
            'no_pass': no_pass,
            'send_person': send_person,
            # omr
            'special_remark': special_remark,
            # omr_po_detail
            'process': process,
            'produce_record': produce_record,
            'mark_notice_date': mark_notice_date,
            'label_sure_date': label_sure_date,
            'label_send_date': label_send_date,
            'sample_send_date': sample_send_date,
            'sample_pass_date': sample_pass_date,
            'product_send_date': product_send_date,
            'product_sure_date': product_sure_date,
            'midterm_inspect': midterm_inspect,
            'booking_so': booking_so,
            'ichiban_inspect': ichiban_inspect,
            'customer_inspect': customer_inspect,
            'pl_come_date': pl_come_date,
            'box_sure_date': box_sure_date,
            'box_send_date': box_send_date,
            'shipping_data': shipping_data,
        }
        obj = PoPoint(**dict_info)
        obj.save()


# 每天定时修改更新订单相关事项，加了数据库事务装饰器
@transaction.atomic
def refresh_remind():
    # 删除状态为未完成的订单事项，并重新更新它们
    reminds = Remind.objects.filter(is_order='True', status='False')
    reminds.delete()
    for po in PoPoint.objects.all():
        for point in Point.objects.all():
            if eval(point.code):
                # 根据触发点筛选事件
                point_event = PointEvent.objects.filter(order_point_id=point.id)
                # 循环触发点对应的每一个事件，依次写入到数据库
                for k in point_event:
                    event_id = k.event_id
                    # 确定提醒事件，计划时间等等...
                    try:
                        string = 'po.' + eval(point.date_info)['date_field']
                        n = int(eval(point.date_info)['rule'])
                    except:
                        return JsonResponse({'status': 'fail', 'msg': '日期信息不存在。'})
                    begin_time = getAfterDate(eval(string), n)  # 这个n不是确定的，是根据指定，可以是负数、正数、整数、小数
                    end_time = getAfterDate(eval(string), n)
                    plan_date = getAfterDate(eval(string), n)
                    try:
                        pomm = Staff.objects.filter(name=po.omr)[0].charge
                    except:
                        pomm = ''
                    try:
                        pomc = Staff.objects.filter(name=pomm)[0].charge
                    except:
                        pomc = ''
                    dict_info = {
                        'is_order': 'True',
                        'po': po.order_number,
                        'item_no': po.item_no,
                        'event_id': event_id,
                        'person': po.omr,
                        'begin_time': begin_time,  # 逻辑未知
                        'end_time': end_time,  # 逻辑未知
                        'rate': 3,  # 逻辑未知
                        'plan_date': plan_date,  # 逻辑未知
                        'actual_date': '',  # 逻辑未知
                        'status': 'False',
                        'pomm': pomm,  # 逻辑未知 - 取员工直系领导
                        'pomc': pomc,  # 逻辑未知
                        'is_upload_file': point.is_file,  # 逻辑未知
                        'file_path': '',  # 逻辑未知
                        'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
                    }
                    obj = Remind(**dict_info)
                    obj.save()


# 工厂产能预测提醒
def factory_ability():
    po_point = PoPoint.objects.all()
    times = 0
    for i in po_point:
        try:
            item_id = Po_detail.objects.get(po=i.order_number, item_no=i.item_no).id
            # print('=======================item_id', item_id)
        except:
            return JsonResponse({'status': 'fail', 'msg': '该订单在detail表中不存在'})
        # 字符串转datetime时间类型
        receive_date = datetime.datetime.strptime(i.receive_date, '%Y-%m-%d').date()    # 接单日期
        fac_send_date = datetime.datetime.strptime(i.fac_send_date, '%Y-%m-%d').date()  # 出货日期
        now = datetime.datetime.now().date()  # 当前日期
        # 只有在今天的日期包含在接单日期和出货日期之间时，并且未消出货，才运行邮件提醒程序，否则验证下一个订单
        if receive_date < now < fac_send_date and not i.sale_date:
            # 计算下单时间与今天的时间间隔
            after_order_days = (now - receive_date).days            # 下单后多少天
            producted_days = (fac_send_date - receive_date).days    # 生产周期
            now_to_send_days = (fac_send_date - now).days           # 今日距离出货日期还有多少天
            # 获取对应工厂的产能基础信息
            try:
                fac_ability = FactoryAbility.objects.filter(item_id=item_id)[0]
            except:  # 因为没有找到该工厂，此处应当提醒工作人员录入工厂信息
                print('没有录入该订单的工厂产能信息')
                return JsonResponse({'status': 'fail', 'msg': '没有录入该订单的工厂产能信息'})
            # 计算产能
            try:
                ability = float(fac_ability.yields) * float(fac_ability.pass_rate)  # 实际产量 = 总产量 * 合格率
            except:
                print('无该工厂产能预测基础信息')
                return JsonResponse({'status': 'fail', 'msg': '无该工厂产能预测基础信息'})
            # 计算产量
            number = ability * float(after_order_days)          # 按照工厂计划的产量
            remain_product = float(i.amount) - float(number)    # 剩余产量
            now_product = round((float(i.amount) / float(producted_days)) * float(after_order_days), 1)  # 现在应有的产量
            remain_days = round(remain_product / ability, 1)    # 剩余天数
            # 构建邮件基础信息
            # -------------------------------------------------------------------------------------------
            # | email_user = 'zhangheng6cah@163.com'  # 发送者账号                                       |
            # | email_pwd = 'zh139891'  # 发送者密码(smtp授权码)                                          |
            # | maillist = ['1792690192@qq.com', '978205490@qq.com']  # 接收人列表应当使用factory.mail    |
            # -------------------------------------------------------------------------------------------
            email_user = '1792690192@qq.com'    # 发送者账号
            email_pwd = 'inodapsbunfaccig'      # 发送者密码(smtp授权码)
            maillist = ['zhangheng6cah@163.com', 'it-20@1bizmail.com']  # 接收人列表 应当使用factory.mail
            title = '产能提醒'  # 邮件标题
            content = '尊敬的：%s ，您好！贵司在 %s 接我司订单，今日距离接单日已是第 %s 天，贵厂的交货日期为：%s 。' \
                      '按照您厂的基础数据显示，您厂的日产量为：%s 件，人均产量总人数为：%s 件/人， 总人数为：%s 人，产品的合格率' \
                      '为：%s。产品 %s 至今的产量为：%s件。现在应有的产量为：%s 件, 下单的总订单数为：%s 件，还剩下：%s 件。' \
                      '按照贵厂数据，预计还需要 %s 天才能完成，请妥善安排生产进度。' % (i.factory, i.receive_date,
                                                            after_order_days, i.fac_send_date, fac_ability.yields,
                                                            fac_ability.per_person, fac_ability.person,
                                                            fac_ability.pass_rate, i.desc, round(number, 1), now_product,
                                                            i.amount, round(remain_product, 1), remain_days)  # 邮件正文
            send_mail(email_user, email_pwd, maillist, title, content)
            # break  # 用于测试的时候只发送一封邮件
            times += 1
    print('共计发出邮件%s封' % times)


# 工厂进度控制事项 -- 提醒工厂
def factory_process():
    po_point = PoPoint.objects.all()
    for i in po_point:
        # 字符串转datetime时间类型
        receive_date = datetime.datetime.strptime(i.receive_date, '%Y-%m-%d').date()    # 接单日期
        sale_date = datetime.datetime.strptime(i.sale_date, '%Y-%m-%d').date()          # 出货日期
        now = datetime.datetime.now().date()  # 当前日期
        # 计算时间间隔
        after_order_days = (now - receive_date).days    # 下单后多少天
        befor_sale_days = (sale_date - now).days        # 出货前多少天
        after_order_things = FactoryProcess.objects.filter(date_by='下单后',
                                                           remind_date=after_order_days)  # 下单后事项
        befor_sale_things = FactoryProcess.objects.filter(date_by='出货前',
                                                          remind_date=befor_sale_days)    # 出货前事项


# 提醒材质进度控制事项
def texture_reminds():
    po_point = PoPoint.objects.all()
    for i in po_point:
        receive_date = i.receive_date
        # 字符串转datetime时间类型
        receive_date = datetime.datetime.strptime(receive_date, '%Y-%m-%d').date()  # 接单时间
        now = datetime.datetime.now().date()  # 当前时间
        # 计算时间间隔
        after_order_days = (now - receive_date).days  # 下单时间距今多少天
        after_order_things = TextureReminds.objects.filter(texture_cate=i.texture,
                                                           date_by='下单后',
                                                           remind_date=after_order_days)  # 下单后事项


# 写入日常任务（每天自动生成每天都要做的日常task）
def daily_task():
    """
    设置定时器，写入日常任务（每天自动生成每天都要做的日常task）
    """
    # 任务发放给谁
    person_list = []
    # 循环发放日常任务
    for i in person_list:
        dict_info = {
            'is_order': 'False',
            'po': '',
            'item_no': '',
            'event_id': '',
            'person': i,
            'begin_time': datetime.datetime.now().strftime('%Y-%m-%d'),
            'end_time': datetime.datetime.now().strftime('%Y-%m-%d'),
            'rate': '',
            'plan_date': datetime.datetime.now().strftime('%Y-%m-%d'),
            'actual_date': '',
            'status': '',
            'pomm': '',
            'pomc': '',
            'is_upload_file': '',
            'file_path': '',
        }
        obj = Remind(**dict_info)
        obj.save()


# 开启定时器任务
def start_timer():
    # 选择后台运行模式
    scheduler = BackgroundScheduler()
    # 每间隔8个小时运行一次(po信息更新同步)主程序
    scheduler.add_job(po_data_check, 'interval', hours=8, id='po_data_check_id')
    # 每天的零时刷新日常任务
    # scheduler.add_job(daily_task, trigger='cron', day='*', hour='0', id='daily_task_id')
    # 每天的零时更新工厂产能提醒事项 - 并发送邮件
    scheduler.add_job(factory_ability, trigger='cron', day='*', hour='0', id='factory_ability_id')
    # 每天的零时更新工厂进度提醒事项
    # scheduler.add_job(factory_process, trigger='cron', day='*', hour='0', id='factory_process_id')
    # 记录运行日志
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler._logger = logging
    # 开启定时程序线程
    scheduler.start()
    return JsonResponse({'status': 'success', 'msg': '定时器启动成功'})


# 停止定时器任务
def stop_timer():
    scheduler = BackgroundScheduler()
    # 默认情况下，调度程序关闭其作业存储和执行器，并等待所有当前执行的作业完成。
    scheduler.shutdown()
    # 如果你不想等，你可以执行下列代码，这仍然会关闭作业存储和执行器，但不会等待任何正在运行的任务完成。
    # scheduler.shutdown(wait=False)
    print('定时器停止成功')
    return JsonResponse({'status': 'success', 'msg': '定时器停止成功'})


# if __name__ == '__main__':
#     # 选择后台运行模式
#     scheduler = BackgroundScheduler()
#     # 每间隔8个小时运行一次(po信息更新同步)主程序
#     scheduler.add_job(po_data_check, 'interval', hours=8, id='po_data_check_id')
#     # 每天的零时刷新日常任务
#     # scheduler.add_job(daily_task, trigger='cron', day='*', hour='0', id='daily_task_id')
#     # 每天的零时更新工厂产能提醒事项 - 并发送邮件
#     scheduler.add_job(factory_ability, trigger='cron', day='*', hour='0', id='factory_ability_id')
#     # 每天的零时更新工厂进度提醒事项
#     # scheduler.add_job(factory_process, trigger='cron', day='*', hour='0', id='factory_process_id')
#     # 记录运行日志
#     scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
#     scheduler._logger = logging
#     # 开启定时程序线程
#     scheduler.start()
