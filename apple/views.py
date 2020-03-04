import os
import time
import json
from datetime import datetime
from django.forms import model_to_dict
from django.core.serializers import serialize
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from Basic_info.models import *
from Order.models import *
from Finance.models import *
from POM.models import *
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required


# 存储或者修改语言session
def save_language_view(request):
    language = request.POST.get('language')
    request.session['language'] = language


# 获取语言session
def get_language_view(request):
    language = request.session.get('language')
    return JsonResponse({'status': 'success', 'msg': '成功', 'language': language})


# 将字典中的None替换为空字符串
def none_to_blank(obj_dic):
    for key in obj_dic:
        if obj_dic[key] is None:
            obj_dic[key] = ""
    return obj_dic


# 将列表中的字典中的None值替换为空字符串
def set_none_to_blank(dict_list):
    for dic in dict_list:
        # print('=====================dic:', dic)
        for key in dic['fields']:
            if dic['fields'][key] is None:
                dic['fields'][key] = ""
    return dict_list


# models对象转json（用get查询出的单条数据）--返回字典json
def obj_to_json(get_obj):
    data = none_to_blank(model_to_dict(get_obj))
    return data


# models查询集转json（用all(),filter(),values()查询出的多条数据）--返回列表json--safe=False
def queryset_to_json(queryset):
    data = set_none_to_blank(json.loads(serialize('json', queryset)))
    return data


# 获取当前登录用户的限制字段权限
def get_permissions(request):
    user_id = request.user.id
    field_permissions = User_extension.objects.get(user=user_id).field_permission
    return eval(field_permissions)


# 获取某个模型下面的某个字段列表
def field_list(model, field):
    return [i[field] for i in eval(model).objects.values()]


# 将某个模型中的id转换为某个字段的值
def id_to_value(model, m_id, field):
    return eval(model).objects.filter(id=m_id).values()[0][field]


# 参数缺省默认所有的模型元组
models_tuple = ("Texture", "Texture_process", "Material_cate", "Material", "Position", "Currency", "Category",
                "Unit", "Area", "Department", "Head_quarter", "Company", "Delivery", "Export_port", "Export_type",
                "Customer", "Customer_mark", "Export_country", "Export_company", "Staff", "Factory", "Code",
                "Status", "Matrial_process", "User_extension", "Package_texture", "Package_type", "Sea_rate",
                "Develop_function", "Sketch_type", "Claim_category", "Type")


# 获取所有的基础信息，封装为json对象
def basic_info_json(model=models_tuple):
    data = {}
    data['data'] = {}
    for i in model:
        data['data'][i] = queryset_to_json(eval(i).objects.all())
    return data


# 根据名字查询工厂信息
def query_factory(name):
    factory = Factory.objects.filter(name__contains=name)
    if factory:
        return JsonResponse(queryset_to_json(factory), safe=False)
    else:
        return JsonResponse({})


# 字符串转日期时间类型
def stringToDate(string):
    # example '2013-07-22 09:44:15'
    dt = datetime.datetime.strptime(string, "%Y-%m-%d")
    return dt


# 日期时间类型转字符串
def dateToString(dt):
    ds = dt.strftime('%Y-%m-%d %H:%M:%S')
    return ds


# 根据指定日期时间字符串返回n天后的一个日期字符串
def getAfterDate(string, n):
    """
    n：可以是正负的小数
    string：只能是xxxx-xx-xx的时间字符串
    """
    dt = datetime.datetime.strptime(string, "%Y-%m-%d")
    dafter = dt + datetime.timedelta(days=n)
    return str(dafter)[:10]
