import os
import time
import uuid
import hashlib
import random
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.shortcuts import render, redirect

from apple import settings
from Basic_info.models import *
from Order.models import *
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from apple.views import *


# 图稿设计添加数据
@login_required()
def sketch_design_add(request):
    # 获取表单信息
    code = request.POST.get('code')  # 不能为空且唯一
    name = request.POST.get('name')
    date = request.POST.get('date')
    photo1 = request.FILES.get('photo1')
    photo1_remark = request.POST.get('photo1_remark')
    photo2 = request.FILES.get('photo2')
    photo2_remark = request.POST.get('photo2_remark')
    photo3 = request.FILES.get('photo3')
    photo3_remark = request.POST.get('photo3_remark')
    category = request.POST.get('category')
    try:
        category_id = Category.objects.get(code=category).id
    except ObjectDoesNotExist:
        category_id = None
    customer = request.POST.get('customer')
    try:
        customer_id = Customer.objects.get(code=customer).id
    except ObjectDoesNotExist:
        customer_id = None
    designer = request.POST.get('designer')
    try:
        designer_id = Staff.objects.get(name=designer).id
    except ObjectDoesNotExist:
        designer_id = None
    developer = request.POST.get('developer')
    try:
        developer_id = Staff.objects.get(name=developer).id
    except ObjectDoesNotExist:
        developer_id = None
    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except ObjectDoesNotExist:
        texture_id = None
    sketch_type = request.POST.get('sketch_type')
    try:
        sketch_type_id = Sketch_type.objects.get(name=sketch_type).id
    except ObjectDoesNotExist:
        sketch_type_id = None
    # 构造上传的文件信息
    fix = datetime.now().strftime('%Y%m%d%H%M%S')
    p1 = p2 = p3 = None
    if photo1:
        img_path1 = os.path.join(settings.MEDIA_ROOT, 'picture/sketch', fix + photo1.name)
        p1 = '/picture/sketch/' + fix + photo1.name
        with open(img_path1, 'wb+') as f:
            for j in photo1.chunks():
                f.write(j)
    if photo2:
        img_path2 = os.path.join(settings.MEDIA_ROOT, 'picture/sketch', fix + photo2.name)
        p2 = '/picture/sketch/' + fix + photo2.name
        with open(img_path2, 'wb+') as f:
            for k in photo2.chunks():
                f.write(k)
    if photo3:
        img_path3 = os.path.join(settings.MEDIA_ROOT, 'picture/sketch', fix + photo3.name)
        p3 = '/picture/sketch/' + fix + photo3.name
        with open(img_path3, 'wb+') as f:
            for l in photo3.chunks():
                f.write(l)
    # 构造数据库存储映射字典
    dict_info = {
        'code': code,
        'name': name,
        'date': date,
        'photo1': p1,
        'photo1_remark': photo1_remark,
        'photo2': p2,
        'photo2_remark': photo2_remark,
        'photo3': p3,
        'photo3_remark': photo3_remark,
        'category_id': category_id,
        'customer_id': customer_id,
        'designer_id': designer_id,
        'developer_id': developer_id,
        'texture_id': texture_id,
        'sketch_type_id': sketch_type_id,
    }
    obj = Sketch_design(**dict_info)
    obj.save()
    return dict_info


# 图稿设计修改数据
@login_required()
def sketch_design_modify(request):
    # 获取表单信息
    code = request.POST.get('code')  # 不能为空且唯一
    name = request.POST.get('name')
    date = request.POST.get('date')
    photo1 = request.FILES.get('photo1')
    photo1_remark = request.POST.get('photo1_remark')
    photo2 = request.FILES.get('photo2')
    photo2_remark = request.POST.get('photo2_remark')
    photo3 = request.FILES.get('photo3')
    photo3_remark = request.POST.get('photo3_remark')
    category = request.POST.get('category')
    try:
        category_id = Category.objects.get(code=category).id
    except ObjectDoesNotExist:
        category_id = None
    customer = request.POST.get('customer')
    try:
        customer_id = Customer.objects.get(code=customer).id
    except ObjectDoesNotExist:
        customer_id = None
    designer = request.POST.get('designer')
    try:
        designer_id = Staff.objects.get(name=designer).id
    except ObjectDoesNotExist:
        designer_id = None
    developer = request.POST.get('developer')
    try:
        developer_id = Staff.objects.get(name=developer).id
    except ObjectDoesNotExist:
        developer_id = None
    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except ObjectDoesNotExist:
        texture_id = None
    sketch_type = request.POST.get('sketch_type')
    try:
        sketch_type_id = Sketch_type.objects.get(name=sketch_type).id
    except ObjectDoesNotExist:
        sketch_type_id = None
    # 判断图片信息是否修改
    sketch_design = Sketch_design.objects.get(code=code)
    fix = datetime.now().strftime('%Y%m%d%H%M%S')
    if photo1 is None:
        p1 = sketch_design.photo1
    else:
        img_path1 = os.path.join(settings.MEDIA_ROOT, 'picture/sketch', fix + photo1.name)
        p1 = '/picture/sketch/' + fix + photo1.name
        with open(img_path1, 'wb+') as f:
            for j in photo1.chunks():
                f.write(j)
    if photo2 is None:
        p2 = sketch_design.photo2
    else:
        img_path2 = os.path.join(settings.MEDIA_ROOT, 'picture/sketch', fix + photo2.name)
        p2 = '/picture/sketch/' + fix + photo2.name
        with open(img_path2, 'wb+') as f:
            for k in photo2.chunks():
                f.write(k)
    if photo3 is None:
        p3 = sketch_design.photo3
    else:
        img_path3 = os.path.join(settings.MEDIA_ROOT, 'picture/sketch', fix + photo3.name)
        p3 = '/picture/sketch/' + fix + photo3.name
        with open(img_path3, 'wb+') as f:
            for l in photo3.chunks():
                f.write(l)
    # 修改数据库条目信息
    sketch_design.code = code
    sketch_design.name = name
    sketch_design.date = date
    sketch_design.photo1 = p1
    sketch_design.photo1_remark = photo1_remark
    sketch_design.photo2 = p2
    sketch_design.photo2_remark = photo2_remark
    sketch_design.photo3 = p3
    sketch_design.photo3_remark = photo3_remark
    sketch_design.category_id = category_id
    sketch_design.customer_id = customer_id
    sketch_design.designer_id = designer_id
    sketch_design.developer_id = developer_id
    sketch_design.texture_id = texture_id
    sketch_design.sketch_type_id = sketch_type_id
    sketch_design.save()
    return sketch_design


# 图稿开发添加数据
@login_required()
def sketch_develop_add(request):
    number = request.POST.get('number')  # 不能为空且唯一
    receive_date = request.POST.get('receive_date')
    category = request.POST.get('category')
    try:
        category_id = Category.objects.get(code=category).id
    except ObjectDoesNotExist:
        category_id = None

    developer = request.POST.get('developer')
    try:
        developer_id = Staff.objects.get(name=developer).id
    except ObjectDoesNotExist:
        developer_id = None

    customer = request.POST.get('customer')
    try:
        customer_id = Customer.objects.get(code=customer).id
    except ObjectDoesNotExist:
        customer_id = None

    department = request.POST.get('department')
    try:
        department_id = Department.objects.get(name=department).id
    except ObjectDoesNotExist:
        department_id = None

    function = request.POST.get('function')
    try:
        function_id = Develop_function.objects.get(func_name=function).id
    except ObjectDoesNotExist:
        function_id = None

    undertake = request.POST.get('undertake')
    try:
        undertake_id = Staff.objects.get(name=undertake).id
    except ObjectDoesNotExist:
        undertake_id = None

    season = request.POST.get('season')
    plan_date = request.POST.get('plan_date')
    is_finish = request.POST.get('is_finish')
    makesure_time = request.POST.get('makesure_time')
    explain = request.POST.get('explain')
    # 构造数据库存储映射字典
    dict_info = {
        'number': number,
        'receive_date': receive_date,
        'category_id': category_id,
        'developer_id': developer_id,
        'customer_id': customer_id,
        'season': season,
        'department_id': department_id,
        'function_id': function_id,
        'undertake_id': undertake_id,
        'sketch_name': '',
        'plan_date': plan_date,
        'is_finish': is_finish,
        'makesure_time': makesure_time,
        'explain': explain,
    }
    print('==================================', dict_info)
    obj = Sketch_develop(**dict_info)
    obj.save()
    return dict_info


# 图稿开发修改数据
@login_required()
def sketch_develop_modify(request):
    number = request.POST.get('number')  # 不能为空且唯一
    receive_date = request.POST.get('receive_date')
    category = request.POST.get('category')
    try:
        category_id = Category.objects.get(code=category).id
    except ObjectDoesNotExist:
        category_id = None

    developer = request.POST.get('developer')
    try:
        developer_id = Staff.objects.get(name=developer).id
    except ObjectDoesNotExist:
        developer_id = None

    customer = request.POST.get('customer')
    try:
        customer_id = Customer.objects.get(code=customer).id
    except ObjectDoesNotExist:
        customer_id = None

    department = request.POST.get('department')
    try:
        department_id = Department.objects.get(name=department).id
    except ObjectDoesNotExist:
        department_id = None

    function = request.POST.get('function')
    try:
        function_id = Develop_function.objects.get(func_name=function).id
    except ObjectDoesNotExist:
        function_id = None

    undertake = request.POST.get('undertake')
    try:
        undertake_id = Staff.objects.get(name=undertake).id
    except ObjectDoesNotExist:
        undertake_id = None

    season = request.POST.get('season')
    plan_date = request.POST.get('plan_date')
    is_finish = request.POST.get('is_finish')
    makesure_time = request.POST.get('makesure_time')
    explain = request.POST.get('explain')
    # 创建对象
    sketch_develop = Sketch_develop.objects.get(number=number)
    # 修改对象
    sketch_develop.number = number
    sketch_develop.receive_date = receive_date
    sketch_develop.category_id = category_id
    sketch_develop.developer_id = developer_id
    sketch_develop.customer_id = customer_id
    sketch_develop.season = season
    sketch_develop.sketch_name = ''
    sketch_develop.department_id = department_id
    sketch_develop.function_id = function_id
    sketch_develop.undertake_id = undertake_id
    sketch_develop.plan_date = plan_date
    sketch_develop.is_finish = is_finish
    sketch_develop.makesure_time = makesure_time
    sketch_develop.explain = explain
    # 保存对象
    sketch_develop.save()
    return sketch_develop


# 图稿开发明细添加数据
@login_required()
def sketch_detail_add(request):
    number = request.POST.get('number')
    item_number = request.POST.get('item_number')
    name = request.POST.get('name')
    customer_price = request.POST.get('customer_price')
    customer_currency = request.POST.get('customer_currency')
    try:
        customer_currency_id = Currency.objects.get(code=customer_currency).id
    except:
        customer_currency_id = None

    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None

    factory_currency = request.POST.get('factory_currency')
    try:
        factory_currency_id = Currency.objects.get(code=factory_currency).id
    except:
        factory_currency_id = None

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except:
        texture_id = None

    fmr_undertake = request.POST.get('fmr_undertake')
    try:
        fmr_undertake_id = Staff.objects.get(name=fmr_undertake).id
    except:
        fmr_undertake_id = None
    ename = request.POST.get('ename')
    factory_price = request.POST.get('factory_price')
    fmr_plan_date = request.POST.get('fmr_plan_date')
    long_ = request.POST.get('long')
    width = request.POST.get('width')
    height = request.POST.get('height')
    fmr_change_plan_date = request.POST.get('fmr_change_plan_date')
    amount = request.POST.get('amount')
    fmr_change_act_date = request.POST.get('fmr_change_act_date')
    receive_date = request.POST.get('receive_date')
    refer_data = request.POST.getlist('refer_data')
    sent_date = request.POST.get('send_date')
    refer_data_no = request.POST.get('refer_data_no')
    mould_min = request.POST.get('mould_min')
    photo_src = request.FILES.get('photo_src')
    # 文件写入
    # 构造上传的文件信息
    fix = datetime.now().strftime('%Y%m%d%H%M%S')
    p1 = None
    if photo_src:
        photo_path = os.path.join(settings.MEDIA_ROOT, 'picture/sketch', fix + photo_src.name)
        p1 = 'picture/sketch' + fix + photo_src.name
        with open(photo_path, 'wb+') as f:
            for j in photo_src.chunks():
                f.write(j)
    other_fee = request.POST.get('other_fee')
    express_fee = request.POST.get('express_fee')
    fmr_50 = request.POST.get('fmr_50')
    start_date = request.POST.get('start_date')
    size_unit = request.POST.get('size_unit')
    is_customer_price = request.POST.get('is_customer_price')
    is_finish = request.POST.get('is_finish')
    product_explain = request.POST.get('product_explain')
    # 构建数据字典
    sketch_detail_info = {
        'number': number,
        'item_number': item_number,
        'name': name,
        'customer_price': customer_price,
        'customer_currency_id': customer_currency_id,
        'ename': ename,
        'factory_id': factory_id,
        'factory_price': factory_price,
        'factory_currency_id': factory_currency_id,
        'texture_id': texture_id,
        'fmr_plan_date': fmr_plan_date,
        'long': long_,
        'width': width,
        'height': height,
        'fmr_change_plan_date': fmr_change_plan_date,
        'amount': amount,
        'fmr_change_act_date': fmr_change_act_date,
        'fmr_undertake_id': fmr_undertake_id,
        'receive_date': receive_date,
        'refer_data': refer_data,
        'sent_date': sent_date,
        'refer_data_no': refer_data_no,
        'mould_min': mould_min,
        'photo_src': p1,
        'other_fee': other_fee,
        'express_fee': express_fee,
        'fmr_50': fmr_50,
        'start_date': start_date,
        'size_unit': size_unit,
        'is_customer_price': is_customer_price,
        'is_finish': is_finish,
        'product_explain': product_explain,
    }
    sketch_detail = Sketch_detail(**sketch_detail_info)
    sketch_detail.save()
    return sketch_detail_info


# 图稿开发明细修改数据
@login_required()
def sketch_detail_modify(request):
    number = request.POST.get('number')
    item_number = request.POST.get('item_number')
    name = request.POST.get('name')
    customer_price = request.POST.get('customer_price')
    customer_currency = request.POST.get('customer_currency')
    try:
        customer_currency_id = Currency.objects.get(code=customer_currency).id
    except ObjectDoesNotExist:
        customer_currency_id = None

    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None

    factory_currency = request.POST.get('factory_currency')
    try:
        factory_currency_id = Currency.objects.get(code=factory_currency).id
    except ObjectDoesNotExist:
        factory_currency_id = None

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except ObjectDoesNotExist:
        texture_id = None

    fmr_undertake = request.POST.get('fmr_undertake')
    try:
        fmr_undertake_id = Staff.objects.get(name=fmr_undertake).id
    except:
        fmr_undertake_id = None
    ename = request.POST.get('ename')
    factory_price = request.POST.get('factory_price')
    fmr_plan_date = request.POST.get('fmr_plan_date')
    long_ = request.POST.get('long')
    width = request.POST.get('width')
    height = request.POST.get('height')
    fmr_change_plan_date = request.POST.get('fmr_change_plan_date')
    amount = request.POST.get('amount')
    fmr_change_act_date = request.POST.get('fmr_change_act_date')
    receive_date = request.POST.get('receive_date')
    refer_data = request.POST.getlist('refer_data')
    sent_date = request.POST.get('send_date')
    refer_data_no = request.POST.get('refer_data_no')
    mould_min = request.POST.get('mould_min')
    photo_src = request.FILES.get('photo_src')
    # 文件写入
    # 构造上传的文件信息
    fix = datetime.now().strftime('%Y%m%d%H%M%S')
    p1 = Sketch_detail.objects.get(number=number, item_number=item_number).photo_src
    if photo_src:
        photo_path = os.path.join(settings.MEDIA_ROOT, 'picture/sketch', fix + photo_src.name)
        p1 = '/picture/sketch/' + fix + photo_src.name
        with open(photo_path, 'wb+') as f:
            for j in photo_src.chunks():
                f.write(j)
    other_fee = request.POST.get('other_fee')
    express_fee = request.POST.get('express_fee')
    fmr_50 = request.POST.get('fmr_50')
    start_date = request.POST.get('start_date')
    size_unit = request.POST.get('size_unit')
    is_customer_price = request.POST.get('is_customer_price')
    is_finish = request.POST.get('is_finish')
    product_explain = request.POST.get('product_explain')
    # 创建修改对象
    num = Sketch_develop.objects.get(number=number)
    sketch_detail = Sketch_detail.objects.get(number=num, item_number=item_number)
    # 修改对象
    if sketch_detail:
        sketch_detail.number = number
        sketch_detail.item_number = item_number
        sketch_detail.name = name
        sketch_detail.customer_price = customer_price
        sketch_detail.customer_currency_id = customer_currency_id
        sketch_detail.ename = ename
        sketch_detail.factory_price = factory_price
        sketch_detail.factory_currency_id = factory_currency_id
        sketch_detail.texture_id = texture_id
        sketch_detail.fmr_plan_date = fmr_plan_date
        sketch_detail.long_ = long_
        sketch_detail.width = width
        sketch_detail.height = height
        sketch_detail.fmr_change_plan_date = fmr_change_plan_date
        sketch_detail.amount = amount
        sketch_detail.fmr_change_act_date = fmr_change_act_date
        sketch_detail.fmr_undertake_id = fmr_undertake_id
        sketch_detail.receive_date = receive_date
        sketch_detail.refer_data = refer_data
        sketch_detail.sent_date = sent_date
        sketch_detail.refer_data_no = refer_data_no
        sketch_detail.mould_min = mould_min
        sketch_detail.photo_src = p1
        sketch_detail.other_fee = other_fee
        sketch_detail.factory_id = factory_id
        sketch_detail.express_fee = express_fee
        sketch_detail.fmr_50 = fmr_50
        sketch_detail.start_date = start_date
        sketch_detail.size_unit = size_unit
        sketch_detail.is_customer_price = is_customer_price
        sketch_detail.is_finish = is_finish
        sketch_detail.product_explain = product_explain
        sketch_detail.save()
        return sketch_detail


# 样品添加数据
@login_required()
def sample_detail_add(request):
    item_no = request.POST.get('item_no')
    item_number = request.POST.get('item_number')
    parent_item = request.POST.get('parent_item')
    other_item = request.POST.get('other_item')
    sketch_no = request.POST.get('sketch_no')
    name = request.POST.get('name')
    ename = request.POST.get('ename')

    category = request.POST.get('category')
    try:
        category_id = Category.objects.get(code=category).id
    except:
        category_id = None

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except:
        texture_id = None

    omr = request.POST.get('omr')
    try:
        omr_id = Staff.objects.get(name=omr).id
    except:
        omr_id = None

    fmr = request.POST.get('fmr')
    try:
        fmr_id = Staff.objects.get(name=fmr).id
    except:
        fmr_id = None

    company = request.POST.get('company')
    try:
        company_id = Company.objects.get(name=company).id
    except:
        company_id = None

    long = request.POST.get('long')
    width = request.POST.get('width')
    height = request.POST.get('height')
    other = request.POST.get('other')
    volume = request.POST.get('volume')
    volume_unit = request.POST.get('volume_unit')
    photo = request.POST.get('photo')
    # 文件写入
    # 构造上传的文件信息
    fix = datetime.now().strftime('%Y%m%d%H%M%S')
    p1 = None
    if photo:
        photo_path = os.path.join(settings.MEDIA_ROOT, 'picture/sample', fix + photo.name)
        p1 = '/picture/sample/' + fix + photo.name
        with open(photo_path, 'wb+') as f:
            for j in photo.chunks():
                f.write(j)
    photo_remark = request.POST.get('photo_remark')
    sample_receive = request.POST.get('sample_receive')
    desc = request.POST.get('desc')
    # 创建数据字典
    dict_info = {
        'item_no': item_no,
        'item_number': item_number,
        'parent_item': parent_item,
        'other_item': other_item,
        'sketch_no': sketch_no,
        'name': name,
        'ename': ename,
        'category_id': category_id,
        'texture_id': texture_id,
        'long': long,
        'width': width,
        'height': height,
        'other': other,
        'volume': volume,
        'volume_unit': volume_unit,
        'omr_id': omr_id,
        'fmr_id': fmr_id,
        'photo': photo,
        'photo_remark': photo_remark,
        'sample_receive': sample_receive,
        'company_id': company_id,
        'desc': desc,
    }
    # 创建对象
    obj = Sample_detail(**dict_info)
    # 存储对象
    obj.save()
    return Sample_detail


# 样品修改数据
@login_required()
def sample_detail_modify(request):
    item_no = request.POST.get('item_no')
    item_number = request.POST.get('item_number')
    parent_item = request.POST.get('parent_item')
    other_item = request.POST.get('other_item')
    sketch_no = request.POST.get('sketch_no')
    name = request.POST.get('name')
    ename = request.POST.get('ename')

    category = request.POST.get('category')
    try:
        category_id = Category.objects.get(code=category).id
    except:
        category_id = None

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except:
        texture_id = None

    omr = request.POST.get('omr')
    try:
        omr_id = Staff.objects.get(name=omr).id
    except:
        omr_id = None

    fmr = request.POST.get('fmr')
    try:
        fmr_id = Staff.objects.get(name=fmr).id
    except:
        fmr_id = None

    company = request.POST.get('company')
    try:
        company_id = Company.objects.get(name=company).id
    except:
        company_id = None

    long = request.POST.get('long')
    width = request.POST.get('width')
    height = request.POST.get('height')
    other = request.POST.get('other')
    volume = request.POST.get('volume')
    volume_unit = request.POST.get('volume_unit')
    photo = request.POST.get('photo')
    # 文件写入
    # 构造上传的文件信息
    fix = datetime.now().strftime('%Y%m%d%H%M%S')
    p1 = Sample_detail.objects.get(item_no=item_no).photo
    if photo:
        photo_path = os.path.join(settings.MEDIA_ROOT, 'picture/sample', fix + photo.name)
        p1 = '/picture/sample/' + fix + photo.name
        with open(photo_path, 'wb+') as f:
            for j in photo.chunks():
                f.write(j)
    photo_remark = request.POST.get('photo_remark')
    sample_receive = request.POST.get('sample_receive')
    desc = request.POST.get('desc')
    # 创建对象
    sample_detail = Sample_detail.objects.get(item_no=item_no)
    sample_detail.item_no = item_no
    sample_detail.item_number = item_number
    sample_detail.parent_item = parent_item
    sample_detail.other_item = other_item
    sample_detail.sketch_no = sketch_no
    sample_detail.name = name
    sample_detail.ename = ename
    sample_detail.category_id = category_id
    sample_detail.texture_id = texture_id
    sample_detail.long = long
    sample_detail.width = width
    sample_detail.height = height
    sample_detail.other = other
    sample_detail.volume = volume
    sample_detail.volume_unit = volume_unit
    sample_detail.omr_id = omr_id
    sample_detail.fmr_id = fmr_id
    sample_detail.photo = p1
    sample_detail.photo_remark = photo_remark
    sample_detail.sample_receive = sample_receive
    sample_detail.company_id = company_id
    sample_detail.desc = desc
    sample_detail.save()
    return sample_detail


# 样品注释添加数据
@login_required()
def item_note_add(request):
    item = request.POST.get('item')
    code = request.POST.get('code')
    desc = request.POST.get('desc')

    dict_info = {
        'item': item,
        'code': code,
        'desc': desc,
    }
    obj = Item_note(**dict_info)
    obj.save()
    return dict_info


# 样品注释修改数据
@login_required()
def item_note_modify(request):
    item = request.POST.get('item')
    code = request.POST.get('code')
    desc = request.POST.get('desc')

    item_note = Item_note.objects.get(item=item, code=code)
    item_note.item = item
    item_note.code = code
    item_note.desc = desc
    item_note.save()
    return item_note


# item包装添加数据
@login_required()
def item_package_add(request):
    sample = request.POST.get('sample')

    type = request.POST.get('type')
    try:
        type_id = Package_texture.objects.get(name=type).id
    except:
        type_id = None

    package_texture = request.POST.get('package_texture')
    try:
        package_texture_id = Texture.objects.get(name=package_texture).id
    except:
        package_texture_id = None

    long = request.POST.get('long')
    width = request.POST.get('width')
    height = request.POST.get('height')
    unit = request.POST.get('unit')
    net_weight = request.POST.get('net_weight')
    gross_weight = request.POST.get('gross_weight')
    amount = request.POST.get('amount')
    dict_info = {
        'sample': sample,
        'type_id': type_id,
        'package_texture_id': package_texture_id,
        'long': long,
        'width': width,
        'height': height,
        'unit': unit,
        'net_weight': net_weight,
        'gross_weight': gross_weight,
        'amount': amount,
    }
    obj = Item_package(**dict_info)
    obj.save()
    return dict_info


# item包装修改数据
@login_required()
def item_package_modify(request):
    sample = request.POST.get('sample')

    type = request.POST.get('type')
    try:
        type_id = Package_texture.objects.get(name=type).id
    except:
        type_id = None

    package_texture = request.POST.get('package_texture')
    try:
        package_texture_id = Texture.objects.get(name=package_texture).id
    except:
        package_texture_id = None

    long = request.POST.get('long')
    width = request.POST.get('width')
    height = request.POST.get('height')
    unit = request.POST.get('unit')
    net_weight = request.POST.get('net_weight')
    gross_weight = request.POST.get('gross_weight')
    amount = request.POST.get('amount')
    # 创建修改对象
    item_package = Item_package.objects.get(sample=sample)  # 暂未实现查询唯一
    if item_package:
        item_package.sample = sample
        item_package.type = type
        item_package.package_texture = package_texture
        item_package.long = long
        item_package.width = width
        item_package.height = height
        item_package.unit = unit
        item_package.net_weight = net_weight
        item_package.gross_weight = gross_weight
        item_package.amount = amount
        # 保存对象
        item_package.save()
        return item_package


# 工厂报价添加数据
@login_required()
def factory_quote_add(request):
    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None

    currency = request.POST.get('currency')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None

    pack_texture = request.POST.get('pack_texture')
    try:
        pack_texture_id = Package_texture.objects.get(name=pack_texture)
    except:
        pack_texture_id = None

    shipping_method = request.POST.get('shipping_method')
    try:
        shipping_method_id = Delivery.objects.get(code=shipping_method)
    except:
        shipping_method_id = None

    shipping_port = request.POST.get('shipping_port')
    try:
        shipping_port_id = Export_port.objects.get(name=shipping_port)
    except:
        shipping_port_id = None

    sample = request.POST.get('sample')
    factory_number = request.POST.get('factory_number')
    cost = request.POST.get('cost')
    sample_desc = request.POST.get('sample_desc')
    is_default_quote = request.POST.get('is_default_quote')
    dict_info = {
        'factory_id': factory_id,
        'sample': sample,
        'factory_number': factory_number,
        'cost': cost,
        'currency_id': currency_id,
        'pack_texture_id': pack_texture_id,
        'shipping_method_id': shipping_method_id,
        'shipping_port_id': shipping_port_id,
        'sample_desc': sample_desc,
        'is_default_quote': is_default_quote,
    }
    obj = Factory_quote(**dict_info)
    obj.save()
    return dict_info


# 工厂报价修改数据
@login_required()
def factory_quote_modify(request):
    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None

    currency = request.POST.get('currency')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None

    pack_texture = request.POST.get('pack_texture')
    try:
        pack_texture_id = Package_texture.objects.get(name=pack_texture)
    except:
        pack_texture_id = None

    shipping_method = request.POST.get('shipping_method')
    try:
        shipping_method_id = Delivery.objects.get(code=shipping_method)
    except:
        shipping_method_id = None

    shipping_port = request.POST.get('shipping_port')
    try:
        shipping_port_id = Export_port.objects.get(name=shipping_port)
    except:
        shipping_port_id = None

    sample = request.POST.get('sample')
    factory_number = request.POST.get('factory_number')
    cost = request.POST.get('cost')
    sample_desc = request.POST.get('sample_desc')
    is_default_quote = request.POST.get('is_default_quote')
    factory_quote = Factory_quote.objects.get(factory=factory_id, sample=sample, factory_number=factory_number)
    factory_quote.factory_id = factory_id
    factory_quote.sample = sample
    factory_quote.factory_number = factory_number
    factory_quote.cost = cost
    factory_quote.currency_id = currency_id
    factory_quote.pack_texture_id = pack_texture_id
    factory_quote.shipping_method_id = shipping_method_id
    factory_quote.shipping_port_id = shipping_port_id
    factory_quote.sample_desc = sample_desc
    factory_quote.is_default_quote = is_default_quote
    factory_quote.save()
    return factory_quote


# 复样总表添加数据
@login_required()
def repeat_sample_add(request):
    number = request.POST.get('number')
    receive_date = request.POST.get('receive_date')
    fac_send_date = request.POST.get('fac_send_date')
    customer = request.POST.get('customer')
    try:
        customer_id = Customer.objects.get(code=customer).id
    except:
        customer_id = None

    undertaker = request.POST.get('undertaker')
    try:
        undertaker_id = Staff.objects.get(name=undertaker).id
    except:
        undertaker_id = None
    explain = request.POST.get('explain')

    dict_info = {
        'number': number,
        'customer_id': customer_id,
        'receive_date': receive_date,
        'fac_send_date': fac_send_date,
        'undertaker_id': undertaker_id,
        'explain': explain,
    }
    obj = Repeat_sample(**dict_info)
    obj.save()
    return dict_info


# 复样总表添加数据
@login_required()
def repeat_sample_modify(request):
    number = request.POST.get('number')
    receive_date = request.POST.get('receive_date')
    fac_send_date = request.POST.get('fac_send_date')
    customer = request.POST.get('customer')
    try:
        customer_id = Customer.objects.get(code=customer).id
    except:
        customer_id = None

    undertaker = request.POST.get('undertaker')
    try:
        undertaker_id = Staff.objects.get(name=undertaker).id
    except:
        undertaker_id = None
    explain = request.POST.get('explain')
    repeat_sample = Repeat_sample.objects.get(number=number)
    if repeat_sample:
        repeat_sample.number = number
        repeat_sample.customer_id = customer_id
        repeat_sample.receive_date = receive_date
        repeat_sample.fac_send_date = fac_send_date
        repeat_sample.undertaker_id = undertaker_id
        repeat_sample.explain = explain
        repeat_sample.save()
        return repeat_sample


# 复样明细表添加数据
@login_required()
def repeat_sample_detail_add(request):
    number = request.POST.get('number')
    item_no = request.POST.get('item_no')
    specs = request.POST.get('specs')
    desc = request.POST.get('desc')
    edesc = request.POST.get('edesc')
    customer_no = request.POST.get('customer_no')
    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except:
        texture_id = None

    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None

    samp_long = request.POST.get('samp_long')
    samp_width = request.POST.get('samp_width')
    samp_height = request.POST.get('samp_height')
    size_unit = request.POST.get('size_unit')
    fac_number = request.POST.get('fac_number')
    sketch_no = request.POST.get('sketch_no')
    amount = request.POST.get('amount')
    amount_unit = request.POST.get('amount_unit')
    order_date = request.POST.get('order_date')
    actual_date = request.POST.get('actual_date')
    cancle_date = request.POST.get('cancle_date')
    fac_date = request.POST.get('fac_date')
    status = request.POST.get('status')
    finish = request.POST.get('finish')
    finish_date = request.POST.get('finish_date')
    sample_remark = request.POST.get('sample_remark')

    dict_info = {
        'number': number,
        'item_no': item_no,
        'specs': specs,
        'desc': desc,
        'edesc': edesc,
        'customer_no': customer_no,
        'texture_id': texture_id,
        'samp_long': samp_long,
        'samp_width': samp_width,
        'samp_height': samp_height,
        'size_unit': size_unit,
        'fac_number': fac_number,
        'sketch_no': sketch_no,
        'amount': amount,
        'amount_unit': amount_unit,
        'order_date': order_date,
        'factory_id': factory_id,
        'actual_date': actual_date,
        'cancle_date': cancle_date,
        'fac_date': fac_date,
        'status': status,
        'finish': finish,
        'finish_date': finish_date,
        'sample_remark': sample_remark,
    }
    obj = Repeat_sample_detail(**dict_info)
    obj.save()
    return dict_info


# 复样明细表修改数据
@login_required()
def repeat_sample_detail_modify(request):
    number = request.POST.get('number')
    item_no = request.POST.get('item_no')
    specs = request.POST.get('specs')
    desc = request.POST.get('desc')
    edesc = request.POST.get('edesc')
    customer_no = request.POST.get('customer_no')

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except:
        texture_id = None

    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None

    samp_long = request.POST.get('samp_long')
    samp_width = request.POST.get('samp_width')
    samp_height = request.POST.get('samp_height')
    size_unit = request.POST.get('size_unit')
    fac_number = request.POST.get('fac_number')
    sketch_no = request.POST.get('sketch_no')
    amount = request.POST.get('amount')
    amount_unit = request.POST.get('amount_unit')
    order_date = request.POST.get('order_date')
    actual_date = request.POST.get('actual_date')
    cancle_date = request.POST.get('cancle_date')
    fac_date = request.POST.get('fac_date')
    status = request.POST.get('status')
    finish = request.POST.get('finish')
    finish_date = request.POST.get('finish_date')
    sample_remark = request.POST.get('sample_remark')
    # 创建修改对象
    repeat_sample_detail = Repeat_sample_detail.objects.get(number=number, item_no=item_no)
    # 修改数据
    repeat_sample_detail.number = number
    repeat_sample_detail.item_no = item_no
    repeat_sample_detail.specs = specs
    repeat_sample_detail.desc = desc
    repeat_sample_detail.edesc = edesc
    repeat_sample_detail.customer_no = customer_no
    repeat_sample_detail.texture_id = texture_id
    repeat_sample_detail.samp_long = samp_long
    repeat_sample_detail.samp_width = samp_width
    repeat_sample_detail.samp_height = samp_height
    repeat_sample_detail.size_unit = size_unit
    repeat_sample_detail.fac_number = fac_number
    repeat_sample_detail.sketch_no = sketch_no
    repeat_sample_detail.amount = amount
    repeat_sample_detail.amount_unit = amount_unit
    repeat_sample_detail.order_date = order_date
    repeat_sample_detail.factory_id = factory_id
    repeat_sample_detail.actual_date = actual_date
    repeat_sample_detail.cancle_date = cancle_date
    repeat_sample_detail.fac_date = fac_date
    repeat_sample_detail.status = status
    repeat_sample_detail.finish = finish
    repeat_sample_detail.finish_date = finish_date
    repeat_sample_detail.sample_remark = sample_remark
    repeat_sample_detail.save()
    return repeat_sample_detail


# 复样单签名添加数据
@login_required()
def sample_target_add(request):
    number = request.POST.get('number')
    item_no = request.POST.get('item_no')
    change_date = request.POST.get('change_date')
    change_desc = request.POST.get('change_desc')
    omr_sure = request.POST.get('omr_sure')
    omr_sure_date = request.POST.get('omr_sure_date')
    fmr_sure = request.POST.get('fmr_sure')
    fmr_sure_date = request.POST.get('fmr_sure_date')
    omr_check = request.POST.get('omr_check')
    omr_check_date = request.POST.get('omr_check_date')
    fmr_check = request.POST.get('fmr_check')
    fmr_check_date = request.POST.get('fmr_check_date')
    dict_info = {
        'number': number,
        'item_no': item_no,
        'change_date': change_date,
        'change_desc': change_desc,
        'omr_sure': omr_sure,
        'omr_sure_date': omr_sure_date,
        'fmr_sure': fmr_sure,
        'fmr_sure_date': fmr_sure_date,
        'omr_check': omr_check,
        'omr_check_date': omr_check_date,
        'fmr_check': fmr_check,
        'fmr_check_date': fmr_check_date,
    }
    sample_target = Sample_target.objects.get(number=number, item_no=item_no)  # 未实现条目唯一性,唯一性主键不明确
    if not sample_target:
        obj = Sample_target(**dict_info)
        obj.save()
        return dict_info


# 复样单签名修改数据
@login_required()
def sample_target_modify(request):
    sam_detail_no = request.POST.get('sam_detail_no')
    change_date = request.POST.get('change_date')
    change_desc = request.POST.get('change_desc')
    omr_sure = request.POST.get('omr_sure')
    omr_sure_date = request.POST.get('omr_sure_date')
    fmr_sure = request.POST.get('fmr_sure')
    fmr_sure_date = request.POST.get('fmr_sure_date')
    omr_check = request.POST.get('omr_check')
    omr_check_date = request.POST.get('omr_check_date')
    fmr_check = request.POST.get('fmr_check')
    fmr_check_date = request.POST.get('fmr_check_date')

    sample_target = Sample_target.objects.get(sam_detail_no=sam_detail_no)  # 未实现条目唯一性,唯一性主键不明确
    if sample_target:
        sample_target.sam_detail_no = sam_detail_no
        sample_target.change_date = change_date
        sample_target.change_desc = change_desc
        sample_target.omr_sure = omr_sure
        sample_target.omr_sure_date = omr_sure_date
        sample_target.fmr_sure = fmr_sure
        sample_target.fmr_sure_date = fmr_sure_date
        sample_target.omr_check = omr_check
        sample_target.omr_check_date = omr_check_date
        sample_target.fmr_check = fmr_check
        sample_target.fmr_check_date = fmr_check_date
        sample_target.save()
        return sample_target


# 资讯部Po添加数据
@login_required()
def po_add(request):
    customer = request.POST.get('customer')
    try:
        customer_id = Customer.objects.get(code=customer).id
    except:
        customer_id = None

    delivery_condition = request.POST.get('delivery_condition')
    try:
        delivery_condition_id = Delivery.objects.get(desc=delivery_condition).id
    except:
        delivery_condition_id = None
    port = request.POST.get('port')
    try:
        port_id = Export_port.objects.get(ename=port).id
    except:
        port_id = None

    omr = request.POST.get('omr')
    try:
        omr_id = Staff.objects.get(name=omr).id
    except:
        omr_id = None

    customer_pono = request.POST.get('customer_pono')
    cus_receive_date = request.POST.get('cus_receive_date')
    fina_date = request.POST.get('fina_date')
    receive_date = request.POST.get('receive_date')
    order_number = request.POST.get('order_number')
    fac_send_date = request.POST.get('fac_send_date')
    produce_native_date = request.POST.get('produce_native_date')
    pay_type = request.POST.get('pay_type')
    dict_info = {
        'customer_id': customer_id,
        'customer_pono': customer_pono,
        'cus_receive_date': cus_receive_date,
        'fina_date': fina_date,
        'receive_date': receive_date,
        'order_number': order_number,
        'fac_send_date': fac_send_date,
        'produce_native_date': produce_native_date,
        'delivery_condition_id': delivery_condition_id,
        'port_id': port_id,
        'omr_id': omr_id,
        'pay_type': pay_type,
    }
    obj = Po(**dict_info)
    obj.save()
    return dict_info


# 资讯部Po修改数据
@login_required()
def po_modify(request):
    customer = request.POST.get('customer')
    try:
        customer_id = Customer.objects.get(code=customer).id
    except:
        customer_id = None

    delivery_condition = request.POST.get('delivery_condition')
    try:
        delivery_condition_id = Delivery.objects.get(desc=delivery_condition).id
    except:
        delivery_condition_id = None

    port = request.POST.get('port')
    try:
        port_id = Export_port.objects.get(ename=port).id
    except:
        port_id = None

    omr = request.POST.get('omr')
    try:
        omr_id = Staff.objects.get(name=omr).id
    except:
        omr_id = None

    customer_pono = request.POST.get('customer_pono')
    cus_receive_date = request.POST.get('cus_receive_date')
    fina_date = request.POST.get('fina_date')
    receive_date = request.POST.get('receive_date')
    order_number = request.POST.get('order_number')
    fac_send_date = request.POST.get('fac_send_date')
    produce_native_date = request.POST.get('produce_native_date')
    pay_type = request.POST.get('pay_type')
    po = Po.objects.get(order_number=order_number)
    po.customer_id = customer_id
    po.customer_pono = customer_pono
    po.cus_receive_date = cus_receive_date
    po.fina_date = fina_date
    po.receive_date = receive_date
    po.order_number = order_number
    po.fac_send_date = fac_send_date
    po.produce_native_date = produce_native_date
    po.delivery_condition_id = delivery_condition_id
    po.port_id = port_id
    po.omr_id = omr_id
    po.pay_type = pay_type
    po.save()
    return po


# 资讯部Po_detail添加数据
@login_required()
def po_detail_add(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    customer_item = request.POST.get('customer_item')
    desc = request.POST.get('desc')
    edesc = request.POST.get('edesc')
    fac_no = request.POST.get('fac_no')

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except:
        texture_id = None
    currency = request.POST.get('currency')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None
    each_box = request.POST.get('each_box')
    try:
        each_box_id = Package_texture.objects.get(name=each_box).id
    except:
        each_box_id = None
    fac_delivery = request.POST.get('fac_delivery')
    try:
        fac_delivery_id = Delivery.objects.get(desc=fac_delivery).id
    except:
        fac_delivery_id = None
    fac_delivery_port = request.POST.get('fac_delivery_port')
    try:
        fac_delivery_port_id = Export_port.objects.get(ename=fac_delivery_port).id
    except:
        fac_delivery_port_id = None
    fmr = request.POST.get('fmr')
    try:
        fmr_id = Staff.objects.get(name=fmr).id
    except:
        fmr_id = None
    fqc = request.POST.get('fqc')
    try:
        fqc_id = Staff.objects.get(name=fqc).id
    except:
        fqc_id = None

    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    costrate = request.POST.get('costrate')
    outside_box = request.POST.get('outside_box')
    middle_box = request.POST.get('middle_box ')
    inner_box = request.POST.get('inner_box')
    box_unit = request.POST.get('box_unit')
    for_profit_report = request.POST.get('for_profit_report')
    special_remark = request.POST.get('special_remark')
    sale_date = request.POST.get('sale_date')

    dict_info = {
        'po': po,
        'item_no': item_no,
        'customer_item': customer_item,
        'desc': desc,
        'edesc': edesc,
        'fac_no': fac_no,
        'texture_id': texture_id,
        'amount': amount,
        'unit': unit,
        'costrate': costrate,
        'currency_id': currency_id,
        'each_box_id': each_box_id,
        'outside_box': outside_box,
        'middle_box': middle_box,
        'inner_box': inner_box,
        'box_unit': box_unit,
        'for_profit_report': for_profit_report,
        'special_remark': special_remark,
        'fac_delivery_id': fac_delivery_id,
        'fac_delivery_port_id': fac_delivery_port_id,
        'fmr_id': fmr_id,
        'fqc_id': fqc_id,
        'sale_date': sale_date,
    }
    obj = Po_detail(**dict_info)
    obj.save()
    return dict_info


# 资讯部Po_detail修改数据
@login_required()
def po_detail_modify(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    customer_item = request.POST.get('customer_item')
    desc = request.POST.get('desc')
    edesc = request.POST.get('edesc')
    fac_no = request.POST.get('fac_no')

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(name=texture).id
    except:
        texture_id = None
    currency = request.POST.get('currency')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None
    each_box = request.POST.get('each_box')
    try:
        each_box_id = Package_texture.objects.get(name=each_box).id
    except:
        each_box_id = None
    fac_delivery = request.POST.get('fac_delivery')
    try:
        fac_delivery_id = Delivery.objects.get(desc=fac_delivery).id
    except:
        fac_delivery_id = None
    fac_delivery_port = request.POST.get('fac_delivery_port')
    try:
        fac_delivery_port_id = Export_port.objects.get(ename=fac_delivery_port).id
    except:
        fac_delivery_port_id = None
    fmr = request.POST.get('fmr')
    try:
        fmr_id = Staff.objects.get(name=fmr).id
    except:
        fmr_id = None
    fqc = request.POST.get('fqc')
    try:
        fqc_id = Staff.objects.get(name=fqc).id
    except:
        fqc_id = None

    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    costrate = request.POST.get('costrate')
    outside_box = request.POST.get('outside_box')
    middle_box = request.POST.get('middle_box ')
    inner_box = request.POST.get('inner_box')
    box_unit = request.POST.get('box_unit')
    for_profit_report = request.POST.get('for_profit_report')
    special_remark = request.POST.get('special_remark')
    sale_date = request.POST.get('sale_date')
    # 创建对象
    po_detail = Po_detail.objects.get(po=po, item_no=item_no)
    po_detail.po = po
    po_detail.item_no = item_no
    po_detail.customer_item = customer_item
    po_detail.desc = desc
    po_detail.edesc = edesc
    po_detail.fac_no = fac_no
    po_detail.texture_id = texture_id
    po_detail.amount = amount
    po_detail.unit = unit
    po_detail.costrate = costrate
    po_detail.currency_id = currency_id
    po_detail.each_box_id = each_box_id
    po_detail.outside_box = outside_box
    po_detail.middle_box = middle_box
    po_detail.inner_box = inner_box
    po_detail.box_unit = box_unit
    po_detail.for_profit_report = for_profit_report
    po_detail.special_remark = special_remark
    po_detail.fac_delivery_id = fac_delivery_id
    po_detail.fac_delivery_port_id = fac_delivery_port_id
    po_detail.fmr_id = fmr_id
    po_detail.fqc_id = fqc_id
    po_detail.sale_date = sale_date
    po_detail.save()
    return po_detail


# 资讯部Po_detail合同添加数据
@login_required()
def contract_add(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    customer_item = request.POST.get('customer_item')
    desc = request.POST.get('desc')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    oa_sure_date = request.POST.get('oa_sure_date')
    fac_amount = request.POST.get('fac_amount')
    fac_unit = request.POST.get('fac_unit')

    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None
    fac_currency = request.POST.get('fac_currency')
    try:
        fac_currency_id = Currency.objects.get(code=fac_currency).id
    except:
        fac_currency_id = None

    fac_cost = request.POST.get('fac_cost')
    fac_total = request.POST.get('fac_total')
    cancle_date = request.POST.get('cancle_date')
    dict_info = {
        'po': po,
        'item_no': item_no,
        'customer_item': customer_item,
        'desc': desc,
        'amount': amount,
        'unit': unit,
        'oa_sure_date': oa_sure_date,
        'fac_amount': fac_amount,
        'fac_unit': fac_unit,
        'factory_id': factory_id,
        'fac_currency_id': fac_currency_id,
        'fac_cost': fac_cost,
        'fac_total': fac_total,
        'cancle_date': cancle_date,
    }
    obj = Contract(**dict_info)
    obj.save()
    return dict_info


# 资讯部Po_detail合同修改数据
@login_required()
def contract_modify(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    customer_item = request.POST.get('customer_item')
    desc = request.POST.get('desc')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    oa_sure_date = request.POST.get('oa_sure_date')
    fac_amount = request.POST.get('fac_amount')
    fac_unit = request.POST.get('fac_unit')

    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None
    fac_currency = request.POST.get('fac_currency')
    try:
        fac_currency_id = Currency.objects.get(code=fac_currency).id
    except:
        fac_currency_id = None

    fac_cost = request.POST.get('fac_cost')
    fac_total = request.POST.get('fac_total')
    cancle_date = request.POST.get('cancle_date')
    contract = Contract.objects.get(po=po, item_no=item_no)
    contract.po = po
    contract.item_no = item_no
    contract.customer_item = customer_item
    contract.desc = desc
    contract.amount = amount
    contract.unit = unit
    contract.oa_sure_date = oa_sure_date
    contract.fac_amount = fac_amount
    contract.fac_unit = fac_unit
    contract.factory_id = factory_id
    contract.fac_currency_id = fac_currency_id
    contract.fac_cost = fac_cost
    contract.fac_total = fac_total
    contract.cancle_date = cancle_date
    contract.save()
    return contract


# 资讯部Po_detail消出货添加数据
@login_required()
def product_send_add(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    po_detail = Po_detail.objects.get(po=po, item_no=item_no)
    customer_item = po_detail.customer_item
    fac_no = po_detail.fac_no
    desc = po_detail.desc
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')

    fmr = request.POST.get('fmr')
    try:
        fmr_id = Staff.objects.get(name=fmr).id
    except:
        fmr_id = None

    qc1 = request.POST.get('qc1')
    try:
        qc1_id = Staff.objects.get(name=qc1).id
    except:
        qc1_id = None

    qc2 = request.POST.get('qc2')
    try:
        qc2_id = Staff.objects.get(name=qc2).id
    except:
        qc2_id = None

    qc3 = request.POST.get('qc3')
    try:
        qc3_id = Staff.objects.get(name=qc3).id
    except:
        qc3_id = None

    rqc1 = request.POST.get('rqc1')
    try:
        rqc1_id = Staff.objects.get(name=rqc1).id
    except:
        rqc1_id = None

    rqc2 = request.POST.get('rqc2')
    try:
        rqc2_id = Staff.objects.get(name=rqc2).id
    except:
        rqc2_id = None

    fqc = request.POST.get('fqc')
    try:
        fqc_id = Staff.objects.get(name=fqc).id
    except:
        fqc_id = None

    send_person = request.POST.get('send_person')
    try:
        send_person_id = Staff.objects.get(name=send_person).id
    except:
        send_person_id = None

    cancle_date = request.POST.get('cancle_date')
    sale_date = request.POST.get('sale_date')
    no_pass = request.POST.get('no_pass')

    dict_info = {
        'po': po,
        'item_no': item_no,
        'customer_item': customer_item,
        'fac_no': fac_no,
        'desc': desc,
        'amount': amount,
        'unit': unit,
        'fmr_id': fmr_id,
        'qc1_id': qc1_id,
        'qc2_id': qc2_id,
        'qc3_id': qc3_id,
        'rqc1_id': rqc1_id,
        'rqc2_id': rqc2_id,
        'fqc_id': fqc_id,
        'cancle_date': cancle_date,
        'sale_date': sale_date,
        'no_pass': no_pass,
        'send_person_id': send_person_id,
    }
    obj = Product_send(**dict_info)
    obj.save()
    return dict_info


# 资讯部Po_detail消出货修改数据
@login_required()
def product_send_modify(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    po_detail = Po_detail.objects.get(po=po, item_no=item_no)
    customer_item = po_detail.customer_item
    fac_no = po_detail.fac_no
    desc = po_detail.desc
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')

    fmr = request.POST.get('fmr')
    try:
        fmr_id = Staff.objects.get(name=fmr).id
    except:
        fmr_id = None

    qc1 = request.POST.get('qc1')
    try:
        qc1_id = Staff.objects.get(name=qc1).id
    except:
        qc1_id = None

    qc2 = request.POST.get('qc2')
    try:
        qc2_id = Staff.objects.get(name=qc2).id
    except:
        qc2_id = None

    qc3 = request.POST.get('qc3')
    try:
        qc3_id = Staff.objects.get(name=qc3).id
    except:
        qc3_id = None

    rqc1 = request.POST.get('rqc1')
    try:
        rqc1_id = Staff.objects.get(name=rqc1).id
    except:
        rqc1_id = None

    rqc2 = request.POST.get('rqc2')
    try:
        rqc2_id = Staff.objects.get(name=rqc2).id
    except:
        rqc2_id = None

    fqc = request.POST.get('fqc')
    try:
        fqc_id = Staff.objects.get(name=fqc).id
    except:
        fqc_id = None

    send_person = request.POST.get('send_person')
    try:
        send_person_id = Staff.objects.get(name=send_person).id
    except:
        send_person_id = None

    cancle_date = request.POST.get('cancle_date')
    sale_date = request.POST.get('sale_date')
    no_pass = request.POST.get('no_pass')

    product_send = Product_send.objects.get(po=po, item_no=item_no)
    product_send.po = po
    product_send.item_no = item_no
    product_send.customer_item = customer_item
    product_send.fac_no = fac_no
    product_send.desc = desc
    product_send.amount = amount
    product_send.unit = unit
    product_send.fmr_id = fmr_id
    product_send.qc1_id = qc1_id
    product_send.qc2_id = qc2_id
    product_send.qc3_id = qc3_id
    product_send.rqc1_id = rqc1_id
    product_send.rqc2_id = rqc2_id
    product_send.fqc_id = fqc_id
    product_send.cancle_date = cancle_date
    product_send.sale_date = sale_date
    product_send.no_pass = no_pass
    product_send.send_person_id = send_person_id
    product_send.save()
    return product_send


# omr添加数据
@login_required()
def omr_add(request):
    po = request.POST.get('po')
    omr = request.POST.get('omr')
    special_remark = request.POST.get('special_remark')
    po_ = Po.objects.get(order_number=po)
    customer_pono = po_.customer_pono
    receive_date = po_.receive_date
    cus_receive_date = po_.cus_receive_date
    fac_send_date = po_.fac_send_date
    dict_info = {
        'po': po,
        'customer_pono': customer_pono,
        'receive_date': receive_date,
        'cus_receive_date': cus_receive_date,
        'fac_send_date': fac_send_date,
        'omr': omr,
        'special_remark': special_remark,
    }
    obj = OMR(**dict_info)
    obj.save()
    return dict_info


# omr修改数据
@login_required()
def omr_modify(request):
    po = request.POST.get('po')
    omr1 = request.POST.get('omr')
    special_remark = request.POST.get('special_remark')
    po_ = Po.objects.get(order_number=po)
    customer_pono = po_.customer_pono
    receive_date = po_.receive_date
    cus_receive_date = po_.cus_receive_date
    fac_send_date = po_.fac_send_date

    omr_ = OMR.objects.get(po=po)
    omr_.po = po
    omr_.omr = omr1
    omr_.special_remark = special_remark
    omr_.customer_pono = customer_pono
    omr_.receive_date = receive_date
    omr_.cus_receive_date = cus_receive_date
    omr_.fac_send_date = fac_send_date
    omr_.save()
    return omr_


# omr详情添加数据
@login_required()
def omr_po_detail_add(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    customer_pono = request.POST.get('customer_pono')
    receive_date = request.POST.get('receive_date')
    cus_receive_date = request.POST.get('cus_receive_date')
    fac_send_date = request.POST.get('fac_send_date')
    omr = request.POST.get('omr')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    oa_sure_date = request.POST.get('oa_sure_date')
    factory = request.POST.get('factory')
    desc = request.POST.get('desc')
    texture = request.POST.get('texture')
    port = request.POST.get('port')
    process = request.POST.get('process')
    produce_record = request.POST.get('produce_record')
    mark_notice_date = request.POST.get('mark_notice_date')
    label_sure_date = request.POST.get('label_sure_date')
    label_send_date = request.POST.get('label_send_date')
    sample_send_date = request.POST.get('sample_send_date')
    sample_pass_date = request.POST.get('sample_pass_date')
    product_send_date = request.POST.get('product_send_date')
    product_sure_date = request.POST.get('product_sure_date')
    midterm_inspect = request.POST.get('midterm_inspect')
    booking_so = request.POST.get('booking_so')
    ichiban_inspect = request.POST.get('ichiban_inspect')
    customer_inspect = request.POST.get('customer_inspect')
    pl_come_date = request.POST.get('pl_come_date')
    box_sure_date = request.POST.get('box_sure_date')
    box_send_date = request.POST.get('box_send_date')
    shipping_data = request.POST.get('shipping_data')
    special_remark = request.POST.get('special_remark')
    special_remark1 = request.POST.get('special_remark1')
    dict_info = {
        'po': po,
        'item_no': item_no,
        'customer_pono': customer_pono,
        'receive_date': receive_date,
        'cus_receive_date': cus_receive_date,
        'fac_send_date': fac_send_date,
        'omr': omr,
        'desc': desc,
        'amount': amount,
        'unit': unit,
        'oa_sure_date': oa_sure_date,
        'factory': factory,
        'texture': texture,
        'port': port,
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
        'special_remark': special_remark,
        'special_remark1': special_remark1,
    }
    obj = OMR_po_detail(**dict_info)  # 不知道是否存在
    obj.save()
    return dict_info


# omr详情修改
@login_required()
def omr_po_detail_modify(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    customer_pono = request.POST.get('customer_pono')
    receive_date = request.POST.get('receive_date')
    cus_receive_date = request.POST.get('cus_receive_date')
    fac_send_date = request.POST.get('fac_send_date')
    omr = request.POST.get('omr')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    oa_sure_date = request.POST.get('oa_sure_date')
    factory = request.POST.get('factory')
    desc = request.POST.get('desc')
    texture = request.POST.get('texture')
    port = request.POST.get('port')
    process = request.POST.get('process')
    produce_record = request.POST.get('produce_record')
    mark_notice_date = request.POST.get('mark_notice_date')
    label_sure_date = request.POST.get('label_sure_date')
    label_send_date = request.POST.get('label_send_date')
    sample_send_date = request.POST.get('sample_send_date')
    sample_pass_date = request.POST.get('sample_pass_date')
    product_send_date = request.POST.get('product_send_date')
    product_sure_date = request.POST.get('product_sure_date')
    midterm_inspect = request.POST.get('midterm_inspect')
    booking_so = request.POST.get('booking_so')
    ichiban_inspect = request.POST.get('ichiban_inspect')
    customer_inspect = request.POST.get('customer_inspect')
    pl_come_date = request.POST.get('pl_come_date')
    box_sure_date = request.POST.get('box_sure_date')
    box_send_date = request.POST.get('box_send_date')
    shipping_data = request.POST.get('shipping_data')
    special_remark = request.POST.get('special_remark')
    special_remark1 = request.POST.get('special_remark1')
    # 创建存储对象
    omr_po_detail = OMR_po_detail.objects.get(po=po, item_no=item_no)
    if omr_po_detail:
        omr_po_detail.po = po
        omr_po_detail.item_no = item_no
        omr_po_detail.customer_pono = customer_pono
        omr_po_detail.receive_date = receive_date
        omr_po_detail.cus_receive_date = cus_receive_date
        omr_po_detail.fac_send_date = fac_send_date
        omr_po_detail.omr = omr
        omr_po_detail.amount = amount
        omr_po_detail.unit = unit
        omr_po_detail.oa_sure_date = oa_sure_date
        omr_po_detail.factory = factory
        omr_po_detail.desc = desc
        omr_po_detail.texture = texture
        omr_po_detail.port = port
        omr_po_detail.process = process
        omr_po_detail.produce_record = produce_record
        omr_po_detail.mark_notice_date = mark_notice_date
        omr_po_detail.label_sure_date = label_sure_date
        omr_po_detail.label_send_date = label_send_date
        omr_po_detail.sample_send_date = sample_send_date
        omr_po_detail.sample_pass_date = sample_pass_date
        omr_po_detail.product_send_date = product_send_date
        omr_po_detail.product_sure_date = product_sure_date
        omr_po_detail.midterm_inspect = midterm_inspect
        omr_po_detail.booking_so = booking_so
        omr_po_detail.ichiban_inspect = ichiban_inspect
        omr_po_detail.customer_inspect = customer_inspect
        omr_po_detail.pl_come_date = pl_come_date
        omr_po_detail.box_sure_date = box_sure_date
        omr_po_detail.box_send_date = box_send_date
        omr_po_detail.shipping_data = shipping_data
        omr_po_detail.special_remark = special_remark
        omr_po_detail.special_remark1 = special_remark1
        omr_po_detail.save()
        return omr_po_detail


# 暂时不使用
@login_required()
def fmr_add(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    receive_date = request.POST.get('receive_date')
    fac_send_date = request.POST.get('fac_send_date')
    name = request.POST.get('name')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    factory = request.POST.get('factory')
    oa_sure_date = request.POST.get('oa_sure_date')
    texture = request.POST.get('texture')
    process = request.POST.get('process')
    dict_info = {
        'po': po,
        'item_no': item_no,
        'receive_date': receive_date,
        'fac_send_date': fac_send_date,
        'name': name,
        'amount': amount,
        'unit': unit,
        'factory': factory,
        'oa_sure_date': oa_sure_date,
        'texture': texture,
        'process': process,
    }
    obj = FMR(**dict_info)
    obj.save()
    return dict_info


# 暂时不使用
@login_required()
def fmr_modify(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    receive_date = request.POST.get('receive_date')
    fac_send_date = request.POST.get('fac_send_date')
    name = request.POST.get('name')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    factory = request.POST.get('factory')
    oa_sure_date = request.POST.get('oa_sure_date')
    texture = request.POST.get('texture')
    process = request.POST.get('process')
    fmr = FMR.objects.get(po=po, item_no=item_no)
    fmr.po = po
    fmr.item_no = item_no
    fmr.receive_date = receive_date
    fmr.fac_send_date = fac_send_date
    fmr.name = name
    fmr.amount = amount
    fmr.unit = unit
    fmr.factory = factory
    fmr.oa_sure_date = oa_sure_date
    fmr.texture = texture
    fmr.process = process
    fmr.save()
    return fmr


# 材料签收添加数据
@login_required()
def material_sign_add(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    omr = request.POST.get('omr')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    name = request.POST.get('name')
    customer_pono = request.POST.get('customer_pono')
    customer_item = request.POST.get('customer_item')
    factory = request.POST.get('factory')
    dict_info = {
        'po': po,
        'item_no': item_no,
        'omr': omr,
        'amount': amount,
        'unit': unit,
        'name': name,
        'customer_pono': customer_pono,
        'customer_item': customer_item,
        'factory': factory,
    }
    obj = Material_sign(**dict_info)
    obj.save()
    return dict_info


# 材料签收修改数据
@login_required()
def material_sign_modify(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    omr = request.POST.get('omr')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    name = request.POST.get('name')
    customer_pono = request.POST.get('customer_pono')
    customer_item = request.POST.get('customer_item')
    factory = request.POST.get('factory')
    material_sign = Material_sign.objects.get(po=po, item_no=item_no)
    material_sign.po = po
    material_sign.item_no = item_no
    material_sign.omr = omr
    material_sign.amount = amount
    material_sign.unit = unit
    material_sign.name = name
    material_sign.customer_pono = customer_pono
    material_sign.customer_item = customer_item
    material_sign.factory = factory
    material_sign.save()
    return material_sign


# 材料签收明细添加数据
@login_required()
def material_sign_detail_add(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(code=texture).id
    except:
        texture_id = None

    sender = request.POST.get('sender')
    try:
        sender_id = Staff.objects.get(name=sender).id
    except:
        sender_id = None

    accessory_currency = request.POST.get('accessory_currency')
    try:
        accessory_currency_id = Currency.objects.get(code=accessory_currency).id
    except:
        accessory_currency_id = None

    accessory_total_currency = request.POST.get('accessory_total_currency')
    try:
        accessory_total_currency_id = Currency.objects.get(code=accessory_total_currency).id
    except:
        accessory_total_currency_id = None

    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None

    order_currency = request.POST.get('order_currency')
    try:
        order_currency_id = Currency.objects.get(code=order_currency).id
    except:
        order_currency_id = None

    total_currency = request.POST.get('total_currency')
    try:
        total_currency_id = Currency.objects.get(code=total_currency).id
    except:
        total_currency_id = None

    qc = request.POST.get('qc')
    try:
        qc_id = Staff.objects.get(name=qc).id
    except:
        qc_id = None

    fqc = request.POST.get('fqc')
    try:
        fqc_id = Staff.objects.get(name=fqc).id
    except:
        fqc_id = None

    pc_count = request.POST.get('pc_count')
    pc_unit = request.POST.get('pc_unit')
    need_qty = request.POST.get('need_qty')
    need_qty_unit = request.POST.get('need_qty_unit')
    name = request.POST.get('name')
    provide_type = request.POST.get('provide_type')
    provide_from = request.POST.get('provide_from')
    is_order = request.POST.get('is_order')
    actual_qty = request.POST.get('actual_qty')
    actual_qty_unit = request.POST.get('actual_qty_unit')
    send_material_date = request.POST.get('send_material_date')
    special_remark = request.POST.get('special_remark')
    accessory_cost = request.POST.get('accessory_cost')
    accessory_cost_total = request.POST.get('accessory_cost_total')
    deduct_invoice_no = request.POST.get('deduct_invoice_no')
    fac_qty = request.POST.get('fac_qty')
    fac_qty_unit = request.POST.get('fac_qty_unit')
    price = request.POST.get('price')
    total = request.POST.get('total')
    order_date = request.POST.get('order_date')
    pay_date = request.POST.get('pay_date')
    is_shipment = request.POST.get('is_shipment')
    actual_date = request.POST.get('actual_date')

    dict_info = {
        'po': po,
        'item_no': item_no,
        'texture_id': texture_id,
        'pc_count': pc_count,
        'pc_unit': pc_unit,
        'need_qty': need_qty,
        'need_qty_unit': need_qty_unit,
        'name': name,
        'provide_type': provide_type,
        'provide_from': provide_from,
        'is_order': is_order,
        'actual_qty': actual_qty,
        'actual_qty_unit': actual_qty_unit,
        'send_material_date': send_material_date,
        'sender_id': sender_id,
        'special_remark': special_remark,
        'accessory_cost': accessory_cost,
        'accessory_currency_id': accessory_currency_id,
        'accessory_cost_total': accessory_cost_total,
        'accessory_total_currency_id': accessory_total_currency_id,
        'deduct_invoice_no': deduct_invoice_no,
        'factory_id': factory_id,
        'fac_qty': fac_qty,
        'fac_qty_unit': fac_qty_unit,
        'price': price,
        'order_currency_id': order_currency_id,
        'total': total,
        'total_currency_id': total_currency_id,
        'order_date': order_date,
        'pay_date': pay_date,
        'is_shipment': is_shipment,
        'qc_id': qc_id,
        'fqc_id': fqc_id,
        'actual_date': actual_date,
    }
    obj = Material_sign_detail(**dict_info)
    obj.save()
    return dict_info


# 材料签收明细修改数据
@login_required()
def material_sign_detail_modify(request):
    po = request.POST.get('po')
    item_no = request.POST.get('item_no')
    m_id = request.POST.get('id')

    texture = request.POST.get('texture')
    try:
        texture_id = Texture.objects.get(code=texture).id
    except:
        texture_id = None

    sender = request.POST.get('sender')
    try:
        sender_id = Staff.objects.get(name=sender).id
    except:
        sender_id = None

    accessory_currency = request.POST.get('accessory_currency')
    try:
        accessory_currency_id = Currency.objects.get(code=accessory_currency).id
    except:
        accessory_currency_id = None

    accessory_total_currency = request.POST.get('accessory_total_currency')
    try:
        accessory_total_currency_id = Currency.objects.get(code=accessory_total_currency).id
    except:
        accessory_total_currency_id = None

    factory = request.POST.get('factory')
    try:
        factory_id = Factory.objects.get(code=factory).id
    except:
        factory_id = None

    order_currency = request.POST.get('order_currency')
    try:
        order_currency_id = Currency.objects.get(code=order_currency).id
    except:
        order_currency_id = None

    total_currency = request.POST.get('total_currency')
    try:
        total_currency_id = Currency.objects.get(code=total_currency).id
    except:
        total_currency_id = None

    qc = request.POST.get('qc')
    try:
        qc_id = Staff.objects.get(name=qc).id
    except:
        qc_id = None

    fqc = request.POST.get('fqc')
    try:
        fqc_id = Staff.objects.get(name=fqc).id
    except:
        fqc_id = None

    pc_count = request.POST.get('pc_count')
    pc_unit = request.POST.get('pc_unit')
    need_qty = request.POST.get('need_qty')
    need_qty_unit = request.POST.get('need_qty_unit')
    name = request.POST.get('name')
    provide_type = request.POST.get('provide_type')
    provide_from = request.POST.get('provide_from')
    is_order = request.POST.get('is_order')
    actual_qty = request.POST.get('actual_qty')
    actual_qty_unit = request.POST.get('actual_qty_unit')
    send_material_date = request.POST.get('send_material_date')
    special_remark = request.POST.get('special_remark')
    accessory_cost = request.POST.get('accessory_cost')
    accessory_cost_total = request.POST.get('accessory_cost_total')
    deduct_invoice_no = request.POST.get('deduct_invoice_no')
    fac_qty = request.POST.get('fac_qty')
    fac_qty_unit = request.POST.get('fac_qty_unit')
    price = request.POST.get('price')
    total = request.POST.get('total')
    order_date = request.POST.get('order_date')
    pay_date = request.POST.get('pay_date')
    is_shipment = request.POST.get('is_shipment')
    actual_date = request.POST.get('actual_date')
    # 创建修改对象
    material_sign_detail = Material_sign_detail.objects.get(id=m_id)
    material_sign_detail.po = po
    material_sign_detail.item_no = item_no
    material_sign_detail.texture_id = texture_id
    material_sign_detail.pc_count = pc_count
    material_sign_detail.pc_unit = pc_unit
    material_sign_detail.need_qty = need_qty
    material_sign_detail.need_qty_unit = need_qty_unit
    material_sign_detail.name = name
    material_sign_detail.provide_type = provide_type
    material_sign_detail.provide_from = provide_from
    material_sign_detail.is_order = is_order
    material_sign_detail.actual_qty = actual_qty
    material_sign_detail.actual_qty_unit = actual_qty_unit
    material_sign_detail.send_material_date = send_material_date
    material_sign_detail.sender_id = sender_id
    material_sign_detail.special_remark = special_remark
    material_sign_detail.accessory_cost = accessory_cost
    material_sign_detail.accessory_currency_id = accessory_currency_id
    material_sign_detail.accessory_cost_total = accessory_cost_total
    material_sign_detail.accessory_total_currency_id = accessory_total_currency_id
    material_sign_detail.deduct_invoice_no = deduct_invoice_no
    material_sign_detail.factory_id = factory_id
    material_sign_detail.fac_qty = fac_qty
    material_sign_detail.fac_qty_unit = fac_qty_unit
    material_sign_detail.price = price
    material_sign_detail.order_currency_id = order_currency_id
    material_sign_detail.total = total
    material_sign_detail.total_currency_id = total_currency_id
    material_sign_detail.order_date = order_date
    material_sign_detail.pay_date = pay_date
    material_sign_detail.is_shipment = is_shipment
    material_sign_detail.qc_id = qc_id
    material_sign_detail.fqc_id = fqc_id
    material_sign_detail.actual_date = actual_date
    material_sign_detail.save()
    return material_sign_detail
