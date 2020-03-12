import os
import time
# from datetime import datetime
import datetime
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 获取所有事项分页接口 - 需要传入页码和每页的条目数 -- ok
def all_page(request, page=1):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    # 获取当前登录用户
    uname = request.user.username
    # 根据当前登录用户筛选事项
    # [{'plan_date': '2020-2-10'}, {'plan_date': '2020-3-5'}]
    queryset = Remind.objects.filter(person=uname).values('plan_date').distinct().order_by("plan_date")  # 获取所有提醒事项的查询集（去重后）
    # [{'date': '2018-11-25', 'status': '完成'}, {}, {}]
    all_reminds = []  # 存储字段信息
    for dic in queryset:
        l = [i.status for i in Remind.objects.filter(person=uname, plan_date=dic['plan_date'])]
        if 'False' in l:
            status = '未完成'
        else:
            status = '已完成'
        dic['status'] = status
        all_reminds.append(dic)

    number = len(queryset) // 10  # 整页数
    page_remain = len(queryset) % 10  # 整页数的余留条数
    if page_remain != 0:
        page_max = number + 1
    else:
        page_max = number

    if type(page) is not int:
        # 如果页码不是整数，则返回第一页
        page = 1
    elif page < 1:
        # 如果页码小于1，则返回第一页
        page = 1
    elif page > page_max:
        # 如果页码超出范围，则返回最后一页
        page = page_max
    # 确定提醒事项数据信息
    if page * 10 <= len(queryset):
        all_reminds = all_reminds[(page - 1) * 10:page * 10]
    else:
        all_reminds = all_reminds[(page - 1) * 10:]
    # 按照plan_date字段排序
    all_reminds = sorted(all_reminds, key=lambda all_reminds: all_reminds["plan_date"])
    all_page_info = {
        'page_min': 1,
        'page_now': page,
        'page_max': page_max,
    }
    return all_reminds, all_page_info


# 获取当日事项分页接口 - 需要传入页码和每页的条目数 -- ok
def today_pager(request, page, page_size):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    # 获取当前登录用户
    uname = request.user.username
    # 根据当前登录用户筛选事项
    now = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当前日期
    queryset = Remind.objects.filter(person=uname, begin_time__lt=now, end_time__gt=now).order_by("plan_date")  # 获取所有提醒事项的查询集（去重后）
    # 创建分页器对象
    paginator = Paginator(queryset, page_size)  # 每页page_size条
    try:
        page_obj = paginator.page(page)  # page_obj为Page对象！
    except PageNotAnInteger:
        # 如果页码不是整数，则返回第一页
        page_obj = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，则返回最后一页
        page_obj = paginator.page(paginator.num_pages)
    except:
        # 如果页码不合法，则返回第一页
        page_obj = paginator.page(1)
    # page_obj.has_previous()  # 是否有上一页
    # page_obj.has_next()  # 是否有下一页
    # page_obj.previous_page_number()  # 分页对象下一页的页码数
    # page_obj.next_page_number()  # 分页对象下一页的页码数
    # paginator.page_range  # 总页数范围

    # 序列化部分字段
    # defer_tuple = ('po', 'item_no', 'person', 'plan_date', 'status')  # 选择要序列化的字段
    # data = json.loads(serializers.serialize("json", page_obj, fields=defer_tuple))
    data = json.loads(serializers.serialize("json", page_obj))
    for i in data:
        if i['fields']['is_order'] == 'True':
            try:
                i['fields']['factory'] = Contract.objects.get(po=i['fields']['po'], item_no=i['fields']['item_no']).factory.name
            except:
                i['fields']['factory'] = ''
            try:
                i['fields']['desc'] = Po_detail.objects.get(po=i['fields']['po'], item_no=i['fields']['item_no']).desc
            except:
                i['fields']['desc'] = ''
            try:
                i['fields']['amount'] = Po_detail.objects.get(po=i['fields']['po'], item_no=i['fields']['item_no']).amount
            except:
                i['fields']['amount'] = ''
    return data, paginator, page_obj


# 根据日期获取该日期的所有事项明细资料
def all_reminds_detail(request, page, page_size, plan_date):
    # 获取当前登录用户
    uname = request.user.username
    # 根据当前登录用户筛选事项
    queryset = Remind.objects.filter(person=uname, plan_date=plan_date).order_by("plan_date")  # 获取所有提醒事项的查询集（去重后）
    # 创建分页器对象
    paginator = Paginator(queryset, page_size)  # 每页page_size条
    try:
        page_obj = paginator.page(page)  # page_obj为Page对象！
    except PageNotAnInteger:
        # 如果页码不是整数，则返回第一页
        page_obj = paginator.page(page)
    except EmptyPage:
        # 如果页码超出范围，则返回最后一页
        page_obj = paginator.page(paginator.num_pages)
    except:
        # 如果页码不合法，则返回第一页
        page_obj = paginator.page(1)
    data = json.loads(serializers.serialize("json", page_obj))
    for i in data:
        if i['fields']['is_order'] == 'True':
            try:
                i['fields']['factory'] = Contract.objects.get(po=i['fields']['po'], item_no=i['fields']['item_no']).factory.name
            except:
                i['fields']['factory'] = ''
            try:
                i['fields']['desc'] = Po_detail.objects.get(po=i['fields']['po'], item_no=i['fields']['item_no']).desc
            except:
                i['fields']['desc'] = ''
            try:
                i['fields']['amount'] = Po_detail.objects.get(po=i['fields']['po'], item_no=i['fields']['item_no']).amount
            except:
                i['fields']['amount'] = ''
    return data, paginator, page_obj  # 返回数据、分页器对象、Page对象


# 根据获取到的字段名返回该字段所有的列去重后的值 -- ok
def get_field_data(request):
    field_name_list = request.POST.getlist('field_name_list')
    # print('=================================field_name_list', field_name_list)
    data = {}
    data['data'] = {}
    for field in field_name_list:
        data['data'][field] = [i[field] for i in PoPoint.objects.values(field).order_by(field).distinct()]
    data['status'] = 'success'
    data['msg'] = '成功'
    # print('=================data:', data)
    return JsonResponse(data)


# 新增订单相关触发点 -- 主管新增触发点 -- ok
@login_required()
def order_point_add(request):
    # 获取触发点列表
    order_point_list = request.POST.getlist('order_point_list')  # 列表
    # print('========================order_point_list', order_point_list)
    # [
    #     "{'date_field': 'receive_date', 'rule': '-5'}"
    #     'texture == "五金类" or texture == "塑料类"',
    #     'factory == "奕纶"',
    #     'customer == "GHAAN"',
    #     'amount >= 50',
    # ]
    source = request.POST.get('source', 'order')
    edesc = request.POST.get('edesc')
    is_file = request.POST.get('is_upload_file', 'False')
    # print('=============is_file', is_file)
    l = []
    for i in order_point_list[1:]:
        if 'or' not in i:
            l.append('(po.' + i + ')')
        else:
            l.append('(' + i + ')')
    # print('=======================l', l)
    name = code = ' and '.join(l)
    # 获取日期信息，索引为0
    date_info = order_point_list[0]
    # print('=====================order_point_list[0]', order_point_list[0])
    # 创建储存对象
    dict_info = {
        'source': source,
        'name': name,
        'code': code,
        'edesc': edesc,
        'date_info': date_info,
        'is_file': is_file,
        'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
    }
    obj = Point(**dict_info)
    obj.save()
    return obj, order_point_list


# 每当添加了新规则后就循环扫描一次订单（popoint），当订单符合匹配上的规则就在remind中添加提醒事项 -- ok
def order_remind_add(**kwargs):
    point = kwargs['point']
    order_point_list = kwargs['order_point_list']
    event_name = kwargs['event_name']
    event_edesc = kwargs['event_edesc']
    is_upload_file = kwargs['is_upload_file']
    # print('==================point', point)
    # print('==================kwargs', kwargs)
    # 保存事件信息
    dic = {
        'name': event_name,
        'edesc': event_edesc,
        'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
    }
    event_obj = Event(**dic)
    event_obj.save()
    # 保存触发点 - 事件多对多对应表
    dic1 = {
        'event_id': event_obj.id,
        'order_point_id': point.id,
        'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
    }
    point_event_obj = PointEvent(**dic1)
    point_event_obj.save()
    # print('=======================point_list', kwargs['order_point_list'])
    # print('=======================point', point)
    # 循环订单匹配规则
    po_point = PoPoint.objects.all()
    for po in po_point:
        # '[
        #     'po.texture == "五金类" or po.texture == "塑料类"',
        #     'po.factory == "奕纶"',
        #     'po.customer == "GHAAN"',
        #     'po.amount >= 50',
        #     "{'date_field': 'receive_date', 'rule': '-5'}"
        # ]'
        # 生成规则表达式语句 - '(point.texture == "五金类" or point.texture == "塑料类") and (point.factory == "奕纶") and
        # (po.customer == "" or po.customer == "GHBBB" or po.customer == "GHBC" or po.customer == "GHBCT") and
        # (po.factory == "" or po.factory == "昌盛五金塑料制品厂" or po.factory == "成发实业有限公司" or
        # po.factory == "澄海市和发纸品工艺有限公司")'
        # 1、如果条件符合，找到该触发点对应的所有事件，循环写入到该订单的提醒事件中去，不删除原有事项
        if eval(point.code):
            # 根据触发点筛选事件
            point_event = PointEvent.objects.filter(order_point_id=point.id)
            # print('========================================根据触发点筛选到的事件:', point_event)
            # 循环触发点对应的每一个事件，依次写入到数据库
            for k in point_event:
                # print('================point_event的id', k.id)
                # print('================point_event的触发点id', k.order_point_id)
                # print('================point_event的事件id', k.event_id)
                event_id = k.event_id
                # 确定提醒事件，计划时间等等...
                try:
                    string = 'po.' + eval(order_point_list[0])['date_field']
                    n = int(eval(order_point_list[0])['rule'])
                except:
                    return JsonResponse({'status': 'fail', 'msg': '日期信息不存在。'})
                begin_time = po.receive_date
                end_time = getAfterDate(eval(string), n)  # 这个n不是确定的，是根据指定，可以是负数、正数、整数、小数
                plan_date = getAfterDate(eval(string), n)
                # print('-------------------------开始保存提醒事件')
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
                    'pomm': '',  # 逻辑未知 - 取员工直系领导
                    'pomc': '',  # 逻辑未知
                    'is_upload_file': is_upload_file,  # 逻辑未知
                    'file_path': '',  # 逻辑未知
                    'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
                }
                obj = Remind(**dict_info)
                obj.save()
    return {'status': 'success', 'msg': '生成提醒事项并存储数据库成功。'}


# 提交订单相关提醒事项修改，是否完成，上传文档等等 -- 管理员使用(暂留接口)
@login_required()
def order_remind_modify(request):
    remind_id = request.POST.get('remind_id')  # 提醒事项的id
    is_order = request.POST.get('is_order', 'True')
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    event = request.POST.get('event')
    person = request.POST.get('person')
    begin_time = request.POST.get('begin_time')
    end_time = request.POST.get('end_time')
    rate = request.POST.get('rate')
    plan_date = request.POST.get('plan_date')
    actual_date = request.POST.get('actual_date')
    status = request.POST.get('status', 'False')
    pomm = request.POST.get('pomm')
    pomc = request.POST.get('pomc')
    is_upload_file = request.POST.get('is_upload_file', 'False')
    file = request.POST.get('file')
    # 文件转储
    if file:
        fix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        file_paths = os.path.join(settings.MEDIA_ROOT, 'pom', fix + file.name)  # 该路径用于存储文件
        file_path = '/pom/' + fix + file.name  # 该路径用于存储文件路径到数据库
        with open(file_paths, 'wb+') as f:  # 文件写入操作
            for k in file.chunks():
                f.write(k)
    else:
        file_path = ''
    try:
        remind = Remind.objects.get(id=remind_id)
    except:
        return JsonResponse({'status': 'fail', 'msg': '修改条目不存在，id：%s' % remind_id})
    remind.is_order = is_order
    remind.po = po
    remind.item_no = item_no
    remind.event = event
    remind.person = person
    remind.begin_time = begin_time
    remind.end_time = end_time
    remind.rate = rate
    remind.plan_date = plan_date
    remind.actual_date = actual_date
    remind.status = status
    remind.pomm = pomm
    remind.pomc = pomc
    remind.is_upload_file = is_upload_file
    remind.file_path = file_path
    remind.last_date = datetime.datetime.now().strftime('%Y-%m-%d')
    remind.save()
    return remind


# 每当相关订单更改(新增、修改、删除)后，修改（已有更新）提醒事项 -- ok
def order_remind_refresh(**kwargs):
    # 只修改Po的信息
    if 'po' in kwargs and 'item_no' not in kwargs:
        # 如果订单不存在，也就是进行了删除操作
        if not Po.objects.filter(order_number=kwargs['po'].order_number).exists():
            return JsonResponse({'status': 'success', 'msg': '该订单在Po表中中已被删除，无需添加事项。'})
        # 如果该订单原本就无事项存在
        remind = Remind.objects.filter(po=kwargs['po'].order_number)
        if not remind.exists():
            return JsonResponse({'status': 'success', 'msg': '该订单在数据库中无事项。'})
        # 计算原先日期间隔，应用于修改后的最终提醒时间上
        _start = datetime.datetime.strptime(remind[0].end_time, '%Y-%m-%d').date()
        _end = datetime.datetime.strptime(remind[0].begin_time, '%Y-%m-%d').date()
        rec_date = datetime.datetime.strptime(kwargs['po'].receive_date, '%Y-%m-%d').date()
        days = _end - _start
        end_date = str(rec_date + days)
        remind.update(person=kwargs['po'].omr.name,
                      begin_time=kwargs['po'].receive_date,
                      end_time=end_date,
                      plan_date=end_date)
        return JsonResponse({'status': 'success', 'msg': '事项更新成功'})
    # 筛选出所有相关该订单的提醒事项
    if 'po' and 'item_no' in kwargs:
        remind = Remind.objects.filter(po=kwargs['po'], item_no=kwargs['item_no'])
        # 1、如果该订单存在事项，则删除所有该订单相关的提醒事项
        if remind.exists():
            remind.delete()
        # 2、查询该popoint条目是否还存在（po信息是否删除） - 不存在直接终止函数，经过则添加提醒事项
        try:
            # 数据库里面的订单实例变量名 - po
            po = PoPoint.objects.get(order_number=kwargs['po'], item_no=kwargs['item_no'])
            for point in Point.objects.all():
                # 3、如果满足表达式，添加该触发点的所有事件到数据库
                if eval(point.code):
                    try:
                        # 获取触发点的id
                        point_id = Point.objects.filter(code=point.code)[0].id
                        # 得到该触发点对应的所有事件
                        point_event = PointEvent.objects.filter(order_point_id=point_id)
                        string = eval('po.' + eval(point.date_info)['date_field'])
                        n = int(eval(point.date_info)['rule'])
                        # 根据指定日期返回n天后的一个日期字符串，在po_point.receive_date这个日期的多少天后
                        begin_time = getAfterDate(string, n)  # 这个n不是确定的，是人为指定，可以是正数、负数、小数、整数
                        end_time = getAfterDate(string, n)
                        plan_date = getAfterDate(string, n)
                        try:
                            pomm = Staff.objects.filter(name=po.omr)[0].charge
                        except:
                            pomm = ''
                        try:
                            pomc = Staff.objects.filter(name=pomm)[0].charge
                        except:
                            pomc = ''
                        # 遍历所有的事件依次存储到remind（事件提醒）表
                        for k in point_event:
                            # 获取事件对象
                            dict_info = {
                                'is_order': 'True',
                                'po': kwargs['po'],
                                'item_no': kwargs['item_no'],
                                'event_id': k.event_id,
                                'person': po.omr,
                                'begin_time': begin_time,  # 逻辑未知
                                'end_time': end_time,  # 逻辑未知
                                'rate': 3,  # 逻辑未知
                                'plan_date': plan_date,  # 逻辑未知
                                'actual_date': '',
                                'status': 'False',
                                'pomm': pomm,
                                'pomc': pomc,
                                'is_upload_file': point.is_file,
                                'file_path': '',
                                'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
                            }
                            obj = Remind(**dict_info)
                            obj.save()
                    except:
                        pass
                    break  # 一旦匹配到规则，立即终止循环(有没有可能一个po有多个触发点)
            return JsonResponse({'status': 'success', 'msg': '订单%s%s修改后，事项更新成功。' % (kwargs['po'], kwargs['item_no'])})
        except:
            return JsonResponse({'status': 'success', 'msg': '该订单在popoint表中已经被删除。无需添加事项'})


# 新增与订单无关提醒事项 -- 主管新增其他提醒事项 -- ok
@login_required()
def other_remind_add(request):
    if request.method == 'GET':
        pass
    # 保存事件
    name = request.POST.get('name')  # 事件
    edesc = request.POST.get('edesc')  # 事件英文描述
    dic = {
        'name': name,
        'edesc': edesc,
        'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
    }
    event_obj = Event(**dic)
    event_obj.save()
    # 保存提醒
    is_order = request.POST.get('is_order', 'False')
    person_list = request.POST.getlist('person_list')
    print('******************************person_list', person_list)
    begin_time = request.POST.get('begin_time')
    end_time = request.POST.get('end_time')
    rate = request.POST.get('rate')
    plan_date = request.POST.get('plan_date')
    is_upload_file = request.POST.get('is_upload_file', 'False')
    for person in person_list:
        if person:
            try:
                pomm = Staff.objects.filter(name=person)[0].charge
            except:
                pomm = ''
            try:
                pomc = Staff.objects.filter(name=pomm)[0].charge
            except:
                pomc = ''
            people = Staff.objects.get(id=int(person))
            dict_info = {
                'is_order': is_order,
                'event_id': event_obj.id,
                'person': people.name,
                'begin_time': begin_time,
                'end_time': end_time,
                'rate': rate,
                'plan_date': plan_date,
                'actual_date': '',
                'status': 'False',
                'pomm': pomm,
                'pomc': pomc,
                'is_upload_file': is_upload_file,
                'file_path': '',
                'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
            }
            print('***********************dict_info', dict_info)
            obj = Remind(**dict_info)
            obj.save()
    return obj


# 提交其他（无关订单）相关提醒事项修改，是否完成，上传文档等等 -- 暂留接口
@login_required()
def other_remind_modify(request):
    remind_id = request.POST.get('remind_id')  # 提醒事项的id
    is_order = request.POST.get('is_order', 'False')
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    event = request.POST.get('event')
    event_edesc = request.POST.get('event_edesc')
    person = request.POST.get('person')
    begin_time = request.POST.get('begin_time')
    end_time = request.POST.get('end_time')
    rate = request.POST.get('rate')
    plan_date = request.POST.get('plan_date')
    actual_date = request.POST.get('actual_date')
    status = request.POST.get('status', 'False')
    pomm = request.POST.get('pomm')
    pomc = request.POST.get('pomc')
    is_upload_file = request.POST.get('is_upload_file', 'False')
    file = request.POST.get('file')
    # 文件转储
    if file:
        fix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        file_paths = os.path.join(settings.MEDIA_ROOT, 'pom', fix + file.name)  # 该路径用于存储文件
        file_path = '/pom/' + fix + file.name  # 该路径用于存储文件路径到数据库
        with open(file_paths, 'wb+') as f:  # 文件写入操作
            for k in file.chunks():
                f.write(k)
    else:
        file_path = ''
    try:
        remind = Remind.objects.get(id=remind_id)
    except:
        return JsonResponse({'status': 'fail', 'msg': '修改条目不存在，id：%s' % remind_id})
    remind.is_order = is_order
    remind.po = po
    remind.item_no = item_no
    remind.event = event
    remind.event_edesc = event_edesc
    remind.person = person
    remind.begin_time = begin_time
    remind.end_time = end_time
    remind.rate = rate
    remind.plan_date = plan_date
    remind.actual_date = actual_date
    remind.status = status
    remind.pomm = pomm
    remind.pomc = pomc
    remind.is_upload_file = is_upload_file
    remind.file_path = file_path
    remind.last_date = datetime.datetime.now().strftime('%Y-%m-%d')
    remind.save()
    return remind


# 员工提交修改事项状态 -- ok
@login_required()
def remind_status_modify(request):
    try:
        remind_id = int(request.POST.get('id'))  # 提醒事项的id，必须有
    except:
        return {'status': 'fail', 'msg': '提交的提醒事项的id格式不正确。'}
    # 判断该事项状态能否被修改（取出计划完成时间和当日期比较）
    # remind_obj = Remind.objects.get(id=remind_id)
    # if remind_obj.plan_date < datetime.datetime.now().strftime('%Y-%m-%d'):
    #     return {'status': 'fail', 'msg': '计划完成时间已过，不能修改该事件状态。'}
    status = request.POST.get('status', 'True')
    is_upload_file = Remind.objects.get(id=remind_id).is_upload_file
    file = request.FILES.get('file')
    # print('===============remind_id', remind_id)
    # print('===============file', file.name)
    # 如果勾选了上传文件，则必须上传文件才能提交
    if is_upload_file == 'True' and not file:
        return {'status': 'fail', 'msg': '必须上传文件才能提交。'}
    # 文件转储
    if file:
        fix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        file_paths = os.path.join(settings.MEDIA_ROOT, 'pom', fix + file.name)  # 该路径用于存储文件实际的路径
        file_path = '/pom/' + fix + file.name  # 该路径用于存储文件相对路径到数据库
        with open(file_paths, 'wb+') as f:  # 文件写入操作
            for k in file.chunks():
                f.write(k)
    else:
        file_path = ''
    try:
        remind = Remind.objects.get(id=remind_id)
    except:
        return {'status': 'fail', 'msg': '修改的提醒事项条目不存在，id：%s' % remind_id}
    remind.status = status
    remind.file_path = file_path
    remind.actual_date = datetime.datetime.now().strftime('%Y-%m-%d')
    remind.last_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    remind.save()
    # print('===============================remind', remind)
    return {'status': 'success', 'msg': '事件状态更新成功', 'file_url': file_path}
