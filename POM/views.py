import os
import datetime
import send_email
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from Finance.query_API import *
from Order.query_API import *
from POM.query_API import *
from apple.views import *
from Basic_info.models import *
from Order.models import *
from Finance.models import *
from POM.models import *
# Create your views here.


# 用户筛选信息后生成提醒条目存储到数据库 -- 用于主管分配订单提醒到人 - ok
@login_required()
def store_reminds_view(request):
    # 1、判断是否拥有指派提醒任务的权限（是否主管  Staff--position）
    # 获取当前登录用户对象并验证权限
    staff = Staff.objects.filter(name=request.user.username)
    if len(staff) == 1:
        # 获取员工职位名称
        position = staff[0].position.job
        if position != '部门主管':
            return JsonResponse({'status': 'fail', 'msg': '当前操作为主管权限，您没有添加提醒事项的权限！！！'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '员工信息中不存在或含有两个及以上当前同名用户！！！'})
    # 2、权限验证通过后进入以下流程 - 开始指派提醒事项
    if request.method == 'GET':
        data = basic_info_json(('Staff',))
        return render(request, 'pom/caseImport.html', locals())
        # return JsonResponse(data, safe=False)
    else:
        action = request.POST.get('action')
        # 判断因素是否与订单相关
        if action == 'order':
            try:
                # 1、保存触发点信息
                point, order_point_list = order_point_add(request)
                # 2、触发点保存成功后根据触发点更新提醒事项
                kwargs = {
                    'point': point,
                    'order_point_list': order_point_list,
                    'event_name': request.POST.get('event_name'),
                    'event_edesc': request.POST.get('event_edesc'),
                    'is_upload_file': request.POST.get('is_upload_file', 'False')
                }
                remind_msg = order_remind_add(**kwargs)
            except:
                return JsonResponse({'status': 'fail', 'msg': '存储到数据库出错，请检查订单相关数据合法性！'})
        else:
            try:
                remind_msg = other_remind_add(request)
            except:
                return JsonResponse({'status': 'fail', 'msg': '存储到数据库出错，请检查数据合法性！'})
    return JsonResponse({'status': 'success', 'msg': '生成提醒事项并提交数据库成功。'})


# 用户登录后分页展示提醒条目 -- 用于提醒用户（ok）
@login_required()
def show_reminds_view(request):
    # 1、如果是get请求，则默认展示第一页
    if request.method == 'GET':
        page = 1  # 定义默认页
        page_size = 10  # 定义每页默认的条目数量
        all_reminds, all_page_info = all_page(request, page)  # 事项数据，分页器对象，分页数据对象
        today_reminds, today_paginator, today_page_obj = today_pager(request, page, page_size)  # 事项数据，分页器对象，分页数据对象
        data = {}
        data['data'] = {}
        # 历史事项
        data['data']['all_reminds'] = all_reminds
        data['all_page_info'] = all_page_info
        # 当日事项
        data['data']['today_reminds'] = set_none_to_blank(today_reminds)
        data['today_page_info'] = {}
        data['today_page_info']['page_min'] = today_paginator.page_range[0]  # 最小页码
        data['today_page_info']['page_now'] = today_page_obj.number  # 当前页面的页码
        data['today_page_info']['page_max'] = today_paginator.num_pages  # 总页数
        # 将事件id转化为models对象
        for k in data['data']['today_reminds']:
            try:
                eve = Event.objects.get(id=k['fields']['event'])
                k['fields']['event'] = obj_to_json(eve)
            except:
                k['fields']['event'] = ''
        # return JsonResponse(data, safe=False)
    # 2、如果是post请求，就根据请求的页码来
    else:
        # 构建json对象
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        page_type = request.POST.get('page_type')
        # 对全部事项的翻页或跳转页面
        if page_type == 'all':
            page = request.POST.get('page')  # 传递当前的页码
            if page:
                page = int(page)
            else:
                page = 1  # 默认页码为1
            page_size = request.POST.get('page_size')  # 每页的条目数
            if page_size:
                page_size = int(page_size)
            else:
                page_size = 10  # 每页默认条目数是10
            # 第一页
            if 'first' in request.POST:
                all_reminds, all_page_info = all_page(request, 1)  # 事项数据，分页数据对象
            # 最后一页
            if 'final' in request.POST:
                all_reminds, all_page_info = all_page(request, page - 1)
                all_reminds, all_page_info = all_page(request, all_page_info['page_max'])  # 事项数据，分页数据对象
            # 上一页
            if 'last' in request.POST:
                all_reminds, all_page_info = all_page(request, page - 1)  # 事项数据，分页数据对象
            # 下一页
            if 'next' in request.POST:
                all_reminds, all_page_info = all_page(request, page + 1)  # 事项数据，分页数据对象
            # 跳转到某页
            if 'turn' in request.POST:
                page_go = request.POST.get('page_go')
                all_reminds, all_page_info = all_page(request, page_go)  # 事项数据，分页数据对象
            # print('========================all_reminds', all_reminds)
            data['data']['all_reminds'] = all_reminds  # 历史提醒事项
            data['all_page_info'] = all_page_info
            return JsonResponse(data)
        # 对当日事项的翻页或跳转页面
        else:
            page = request.POST.get('page')  # 传递当前的页码
            try:
                page = int(page)
            except:
                page = 1  # 默认页码为1
            page_size = request.POST.get('page_size')  # 每页的条目数
            try:
                page_size = int(page_size)
            except:
                page_size = 10  # 每页默认条目数是10
            # 第一页
            if 'first' in request.POST:
                reminds, paginator, page_obj = today_pager(request, 1, page_size)  # 事项数据，分页器对象，分页数据对象
            # 最后一页
            if 'final' in request.POST:
                reminds, paginator, page_obj = today_pager(request, 1, page_size)  # 事项数据，分页器对象，分页数据对象
                reminds, paginator, page_obj = today_pager(request, paginator.num_pages, page_size)
            # 上一页
            if 'last' in request.POST:
                reminds, paginator, page_obj = today_pager(request, page - 1, page_size)  # 事项数据，分页器对象，分页数据对象
            # 下一页
            if 'next' in request.POST:
                reminds, paginator, page_obj = today_pager(request, page + 1, page_size)  # 事项数据，分页器对象，分页数据对象
            # 跳转到某页
            if 'turn' in request.POST:
                page_go = request.POST.get('page_go')
                reminds, paginator, page_obj = today_pager(request, page_go, page_size)  # 事项数据，分页器对象，分页数据对象

            data['data']['today_reminds'] = set_none_to_blank(reminds)  # 历史提醒事项
            data['today_page_info'] = {}
            data['today_page_info']['page_min'] = paginator.page_range[0]  # 最小页码
            data['today_page_info']['page_now'] = page_obj.number  # 当前页面的页码
            data['today_page_info']['page_max'] = paginator.num_pages  # 总页数
            # 将事件id转化为models对象
            for k in data['data']['today_reminds']:
                try:
                    eve = Event.objects.get(id=k['fields']['event'])
                    k['fields']['event'] = obj_to_json(eve)
                except:
                    k['fields']['event'] = ''
            return JsonResponse(data)
    return render(request, 'pom/case.html', locals())
    # return JsonResponse(data, safe=False)


# 用户所有提醒事项分时间分页展示 -- 用于查看remind条目的详情（ok）
@login_required()
def show_all_reminds_detail_view(request):
    if request.method == 'GET':
        plan_date = request.GET.get('plan_date')
        page_size = request.GET.get('page_size', 10)  # 每页的条目数
        try:
            page_size = int(page_size)
        except:
            page_size = 10  # 每页默认条目数是10
        reminds, paginator, page_obj = all_reminds_detail(request, 1, page_size, plan_date)
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['reminds'] = set_none_to_blank(reminds)  # 历史提醒事项
        data['page_info'] = {}
        data['page_info']['page_min'] = paginator.page_range[0]  # 最小页码
        data['page_info']['page_now'] = page_obj.number  # 当前页面的页码
        data['page_info']['page_max'] = paginator.num_pages  # 总页数
        # 将事件id转化为models对象
        for k in data['data']['reminds']:
            try:
                eve = Event.objects.get(id=k['fields']['event'])
                k['fields']['event'] = obj_to_json(eve)
            except:
                k['fields']['event'] = ''
        return render(request, 'pom/caseDetail.html', locals())
    else:
        plan_date = request.POST.get('plan_date')
        # plan_date = '2020-03-13'  # 测试
        page = request.POST.get('page', 1)
        try:
            page = int(page)
        except:
            page = 1  # 默认页码为1
        page_size = request.POST.get('page_size', 10)  # 每页的条目数
        try:
            page_size = int(page_size)
        except:
            page_size = 10  # 每页默认条目数是10
        # 第一页
        if 'first' in request.POST:
            reminds, paginator, page_obj = all_reminds_detail(request, 1, page_size, plan_date)  # 事项数据，分页器对象，分页数据对象
        # 最后一页
        if 'final' in request.POST:
            reminds, paginator, page_obj = all_reminds_detail(request, 1, page_size, plan_date)  # 事项数据，分页器对象，分页数据对象
            reminds, paginator, page_obj = all_reminds_detail(request, paginator.num_pages, page_size, plan_date)
        # 上一页
        if 'last' in request.POST:
            reminds, paginator, page_obj = all_reminds_detail(request, page - 1, page_size, plan_date)  # 事项数据，分页器对象，分页数据对象
        # 下一页
        if 'next' in request.POST:
            reminds, paginator, page_obj = all_reminds_detail(request, page + 1, page_size, plan_date)  # 事项数据，分页器对象，分页数据对象
        # 跳转到某页
        if 'turn' in request.POST:
            page_go = request.POST.get('page_go')
            reminds, paginator, page_obj = all_reminds_detail(request, page_go, page_size, plan_date)  # 事项数据，分页器对象，分页数据对象

        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['reminds'] = set_none_to_blank(reminds)        # 历史提醒事项
        data['page_info'] = {}
        data['page_info']['page_min'] = paginator.page_range[0]     # 最小页码
        data['page_info']['page_now'] = page_obj.number             # 当前页面的页码
        data['page_info']['page_max'] = paginator.num_pages         # 总页数
        # 将事件id转化为models对象
        for k in data['data']['reminds']:
            try:
                eve = Event.objects.get(id=k['fields']['event'])
                k['fields']['event'] = obj_to_json(eve)
            except:
                k['fields']['event'] = ''
        return JsonResponse(data)


# 用于用户更新提醒事项完成状态
@login_required()
def refresh_status_view(request):
    if request.method == 'GET':
        now = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当前日期
        # 筛选出能够被修改状态的事项 - 应完成时间在当前时间之后、且状态为未完成的
        try:
            reminds = Remind.objects.filter(person=request.user.username, plan_date__gt=now, status='False')
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['reminds'] = set_none_to_blank(queryset_to_json(reminds))
            for k in data['data']['reminds']:
                try:
                    eve = Event.objects.get(id=k['fields']['event'])
                    k['fields']['event'] = obj_to_json(eve)
                except:
                    k['fields']['event'] = ''
        except:
            return JsonResponse({'status': 'fail', 'msg': '查询失败或者无该数据信息'})
            # return render(request, 'pom/caseDetail.html', locals())
        return JsonResponse(data, safe=False)
    else:
        remind_id = int(request.POST.get('id'))  # 获取提醒事件
        remind = Remind.objects.get(id=remind_id)
        # 如果是领导提交的关于延期的批复，则重新更改员工的事项计划日期
        if remind.manage_id:  # 记录了延期事件的id，就是领导批复
            try:
                delay_remind = Remind.objects.get(id=remind.manage_id)
            except:
                return JsonResponse({'status': 'fail', 'msg': '未找到延期的该提醒事项'})
            delay_remind.plan_date = remind.delay_date
            delay_remind.last_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            delay_remind.save()
            return JsonResponse({'status': 'fail', 'msg': '延期成功'})
        # 普通提醒事项的完成提交
        else:
            try:
                modify_status = remind_status_modify(request)
                return JsonResponse(modify_status)
            except:
                return JsonResponse({'status': 'fail', 'msg': '事件状态更新失败'})


# 事项延期
@login_required()
def delay_view(request):
    if request.method == 'GET':
        return HttpResponse('test')
    else:
        remind_id = int(request.POST.get('id'))  # 获取提醒事件
        remind = Remind.objects.get(id=remind_id)
        # 1.如果是员工提交修改申请，则生成领导的员工申请事项
        if 'delay' in request.POST:
            new_plan_date = request.POST.get('plan_date')
            try:
                staff = Staff.objects.filter(name=remind.person)[0]
            except:
                return JsonResponse({'status': 'fail', 'msg': '该事件未关联人员，请检查remind表该条记录的person字段'})
            try:
                relation = EmployeeRelationship.objects.get(staff_id=staff.id)
                leader = relation.leader
            except:
                return JsonResponse({'status': 'fail', 'msg': '没有该员工的上司信息，请检查employee_relationship表'})
            try:
                leader_staff = Staff.objects.get(id=leader.id)
            except:
                return JsonResponse({'status': 'fail', 'msg': '没有该上司信息，请检查staff表'})
            # 保存事件 -- 用于提醒领导查看延期申请
            try:
                event = Event.objects.get(id=remind.event_id).name
            except:
                return JsonResponse({'status': 'fail', 'msg': '该提醒事项的事件不存在'})
            name = '员工：%s 的延期申请，请求将事件：%s，的计划日期从：%s，延期到：%s！' % (staff, event, remind.plan_date, new_plan_date)  # 事件
            edesc = '员工：%s 的延期申请，请求将事件：%s，的计划日期从：%s，延期到：%s！' % (staff, event, remind.plan_date, new_plan_date)  # 事件英文描述
            dic = {
                'name': name,
                'edesc': edesc,
                'last_date': datetime.datetime.now().strftime('%Y-%m-%d'),
            }
            event_obj = Event(**dic)
            event_obj.save()
            # 生成提醒领导事项并保存
            reminds_info = {
                'is_order': 'False',
                'person': leader_staff.name,
                'begin_time': datetime.datetime.now().strftime('%Y-%m-%d'),
                'end_time': new_plan_date,
                'plan_date': new_plan_date,
                'status': 'False',
                'is_upload_file': 'False',
                'last_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'event_id': event_obj.id,  # 提醒领导延期这个事件的id
                'manage_id': remind.id,  # 记录员工的申请延期的事项的id
                'delay_date': new_plan_date,  # 记录员工的申请延期的事项的id
            }
            remind_obj = Remind(**reminds_info)
            remind_obj.save()
            return JsonResponse({'status': 'fail', 'msg': '事项延期提交成功'})
