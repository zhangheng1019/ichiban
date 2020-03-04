import os
from datetime import datetime
from Finance.query_API import *
from Order.query_API import *
from apple.views import *
from Basic_info.models import *
from Order.models import *
from apple.views import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.contrib.auth.models import User


# Create your views here.


# 索赔类型
@login_required()
def claim_category_view(request):
    if request.method == 'GET':
        return render(request, 'order/sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        code = request.POST.get('code')
        l = [i['code'] for i in Claim_category.objects.values()]
        if code in l:
            return JsonResponse({'status': 'fail', 'msg': '索赔类型已存在'})
        claim_category = claim_category_add(request)
        return JsonResponse({'status': 'success', 'msg': '添加成功'})
    elif 'delete' in request.POST:
        code = request.POST.get('code')
        l = [i['code'] for i in Claim_category.objects.values()]
        if code in l:
            return JsonResponse({'status': 'fail', 'msg': '索赔类型已存在'})
        claim_category = Sample_detail.objects.get(code=code)
        if claim_category:
            claim_category.delete()
            return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        code = request.POST.get('code')
        l = [i['code'] for i in Claim_category.objects.values()]
        if code not in l:
            return JsonResponse({'status': 'fail', 'msg': '索赔类型不存在'})
        claim_category = claim_category_modify(request)
    elif 'view' in request.POST:
        code = request.POST.get('code')
        l = [i['code'] for i in Claim_category.objects.values()]
        if code not in l:
            return JsonResponse({'status': 'fail', 'msg': '索赔类型不存在'})
        claim_category = Claim_category.objects.get(code=code)
        if claim_category:
            data = {}
            data['status'] = 'success'
            data['msg'] = '索赔类型查询成功'
            data['data'] = obj_to_json(claim_category)
            return JsonResponse(data)


# 索赔费用分类
@login_required()
def claim_type_view(request):
    if request.method == 'GET':
        return render(request, 'order/sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        claim_category = claim_category_add(request)
        return JsonResponse({'status': 'success', 'msg': '添加成功'})
    elif 'delete' in request.POST:
        type_id = request.POST.get('type_id')
        claim_category = Sample_detail.objects.get(id=type_id)
        if claim_category:
            claim_category.delete()
            return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        claim_category = claim_category_modify(request)
        return JsonResponse({'status': 'success', 'msg': '修改成功'})
    elif 'view' in request.POST:
        type_id = request.POST.get('type_id')
        types = Type.objects.get(id=type_id)
        data = {}
        data['data'] = obj_to_json(types)
        data['status'] = 'success'
        data['msg'] = '查询成功'
        return JsonResponse(data)


# 财务传票
@login_required()
def finance_bill_view(request):
    if request.method == 'GET':
        return render(request, 'order/sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        bill_number = request.POST.get('bill_number')
        l = [i['bill_number'] for i in Finance_bill.objects.values()]
        if bill_number in l:
            return JsonResponse({'status': 'fail', 'msg': '传票已存在'})
        finance_bill = finance_bill_add(request)
        return JsonResponse({'status': 'success', 'msg': '添加成功'})
    elif 'delete' in request.POST:
        bill_number = request.POST.get('bill_number')
        l = [i['bill_number'] for i in Finance_bill.objects.values()]
        if bill_number not in l:
            return JsonResponse({'status': 'fail', 'msg': '传票不存在'})
        finance_bill = Finance_bill.objects.get(bill_number=bill_number)
        finance_bill.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        bill_number = request.POST.get('bill_number')
        l = [i['bill_number'] for i in Finance_bill.objects.values()]
        if bill_number not in l:
            return JsonResponse({'status': 'fail', 'msg': '传票不存在'})
        finance_bill = finance_bill_modify(request)
        return JsonResponse({'status': 'success', 'msg': '修改成功'})
    elif 'view' in request.POST:
        bill_number = request.POST.get('bill_number')
        l = [i['bill_number'] for i in Finance_bill.objects.values()]
        if bill_number not in l:
            return JsonResponse({'status': 'fail', 'msg': '传票不存在'})
        finance_bill = Finance_bill.objects.get(bill_number=bill_number)
        data = {}
        data['data'] = obj_to_json(finance_bill)
        data['status'] = 'success'
        data['msg'] = '查询成功'
        return JsonResponse(data)


# 大货付款
@login_required()
def ship_payment_view(request):
    if request.method == 'GET':
        data = basic_info_json(('Currency', 'Factory', 'Customer', 'Staff', 'Export_company'))
        return render(request, 'finance/ship_payment.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        # po_detail数据
        try:
            po_detail = Po_detail.objects.all().order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            ship_payment = Ship_payment.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['ship_payment'] = {}
            # python对象遍历转换为json对象
            for i in ship_payment:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['ship_payment'][str(i.id)] = obj_to_json(i)
                data['data']['ship_payment'][str(i.id)]['currency'] = currency
        except ObjectDoesNotExist:
            data['data']['ship_payment'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(id__lt=n).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            ship_payment = Ship_payment.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['ship_payment'] = {}
            # python对象遍历转换为json对象
            for i in ship_payment:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['ship_payment'][str(i.id)] = obj_to_json(i)
                data['data']['ship_payment'][str(i.id)]['currency'] = currency
        except:
            data['data']['ship_payment'] = {}
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            ship_payment = Ship_payment.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['ship_payment'] = {}
            # python对象遍历转换为json对象
            for i in ship_payment:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['ship_payment'][str(i.id)] = obj_to_json(i)
                data['data']['ship_payment'][str(i.id)]['currency'] = currency
        except:
            data['data']['ship_payment'] = {}
        return JsonResponse(data)
    elif 'final' in request.POST:
        # po_detail数据
        try:
            po_detail = Po_detail.objects.all().order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            ship_payment = Ship_payment.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['ship_payment'] = {}
            # python对象遍历转换为json对象
            for i in ship_payment:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['ship_payment'][str(i.id)] = obj_to_json(i)
                data['data']['ship_payment'][str(i.id)]['currency'] = currency
        except:
            data['data']['ship_payment'] = {}
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        try:
            ship_payment = ship_payment_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.po_detail for i in Ship_payment.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': 'item号在索赔条目中不存在'})
        try:
            ship_payment = Ship_payment.objects.filter(po=order_number, po_detail=item_no)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        ship_payment.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.po_detail for i in Ship_payment.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': 'item号在索赔条目中不存在'})
        try:
            ship_payment = ship_payment_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        factory = request.POST.get('factory')
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        # 按照工厂查询
        if factory:
            try:
                fac = Factory.objects.filter(name__contains=factory)[0]
                contract = Contract.objects.filter(factory=fac)[0]
                order_number = contract.po  # 获取po号
                item_no = contract.item_no  # 获取item号
            except:
                return JsonResponse({'status': 'fail', 'msg': '该工厂无信息'})
        # 按照po+po_detail查找
        elif order_number and item_no:
            order_number = request.POST.get('po')
            item_no = request.POST.get('po_detail')
        # 按照po查询
        elif order_number:
            try:
                po_detail = Po_detail.objects.filter(po=order_number)[0]
                order_number = po_detail.po
                item_no = po_detail.item_no
            except:
                return JsonResponse({'status': 'fail', 'msg:': '该Po号不存在'})
        # 按照po_detail查询
        elif item_no:
            try:
                po_detail = Po_detail.objects.filter(item=item_no)[0]
                order_number = po_detail.po
                item_no = po_detail.item_no
            except:
                return JsonResponse({'status': 'fail', 'msg:': '该item不存在'})

        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po_detail不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            ship_payment = Ship_payment.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['ship_payment'] = {}
            # python对象遍历转换为json对象
            for i in ship_payment:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['ship_payment'][str(i.id)] = obj_to_json(i)
                data['data']['ship_payment'][str(i.id)]['currency'] = currency
        except:
            data['data']['ship_payment'] = {}
        return JsonResponse(data)


# 材料配件付款
@login_required()
def accessory_pay_view(request):
    if request.method == 'GET':
        data = basic_info_json(('Currency', 'Factory', 'Customer', 'Staff', 'Export_company'))
        return render(request, 'finance/accessory_pay.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        # po_detail数据
        try:
            po_detail = Po_detail.objects.all().order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            accessory_pay = Accessory_pay.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['accessory_pay'] = {}
            # python对象遍历转换为json对象
            for i in accessory_pay:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['accessory_pay'][str(i.id)] = obj_to_json(i)
                data['data']['accessory_pay'][str(i.id)]['currency'] = currency
        except ObjectDoesNotExist:
            data['data']['accessory_pay'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(id__lt=n).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            accessory_pay = Accessory_pay.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['ship_payment'] = {}
            # python对象遍历转换为json对象
            for i in accessory_pay:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['accessory_pay'][str(i.id)] = obj_to_json(i)
                data['data']['accessory_pay'][str(i.id)]['currency'] = currency
        except:
            data['data']['accessory_pay'] = {}
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            accessory_pay = Accessory_pay.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['accessory_pay'] = {}
            # python对象遍历转换为json对象
            for i in accessory_pay:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['accessory_pay'][str(i.id)] = obj_to_json(i)
                data['data']['accessory_pay'][str(i.id)]['currency'] = currency
        except:
            data['data']['accessory_pay'] = {}
        return JsonResponse(data)
    elif 'final' in request.POST:
        # po_detail数据
        try:
            po_detail = Po_detail.objects.all().order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 进出口公司及付款信息（ship_payment以作为付款条目主要信息，其他po，po_detai等作为客户、订单信息）
        try:
            accessory_pay = Accessory_pay.objects.filter(po=po_detail.po, po_detail=po_detail.item_no)
            data['data']['accessory_pay'] = {}
            # python对象遍历转换为json对象
            for i in accessory_pay:
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                data['data']['accessory_pay'][str(i.id)] = obj_to_json(i)
                data['data']['accessory_pay'][str(i.id)]['currency'] = currency
        except:
            data['data']['accessory_pay'] = {}
        return JsonResponse(data)
    elif 'add' in request.POST:
        l = [i['order_number'] for i in Po.objects.values()]
        l1 = [i['item_no'] for i in Po_detail.objects.values()]
        po = request.POST.get('po')
        po_detail = request.POST.get('po_detail')
        if po not in l:
            return JsonResponse({'status': 'fail', 'msg': '该Po不存在'})
        if po_detail not in l1:
            return JsonResponse({'status': 'fail', 'msg': '该Po_detail不存在'})
        try:
            accessory_pay = accessory_pay_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        pay_id = request.POST.get('pay_id')
        try:
            accessory_pay = Accessory_pay.objects.get(id=pay_id)
            accessory_pay.delete()
            return JsonResponse({'status': 'success', 'msg': '删除成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '删除对象不存在'})
    elif 'modify' in request.POST:
        l = [i['order_number'] for i in Po.objects.values()]
        l1 = [i['item_no'] for i in Po_detail.objects.values()]
        po = request.POST.get('po')
        po_detail = request.POST.get('po_detail')
        if po not in l:
            return JsonResponse({'status': 'fail', 'msg': '该Po不存在'})
        if po_detail not in l1:
            return JsonResponse({'status': 'fail', 'msg': '该Po_detail不存在'})
        try:
            accessory_pay = accessory_pay_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '修改失败'})
    elif 'view' in request.POST:
        l = [i['order_number'] for i in Po.objects.values()]
        l1 = [i['item_no'] for i in Po_detail.objects.values()]
        po = request.POST.get('po')
        po_detail = request.POST.get('po_detail')
        if po not in l:
            return JsonResponse({'status': 'fail', 'msg': '该Po不存在'})
        if po_detail not in l1:
            return JsonResponse({'status': 'fail', 'msg': '该Po_detail不存在'})
        data = {}
        try:
            accessory_pay = Accessory_pay.objects.filter(po=po, po_detail=po_detail)
            data['data'] = {}
            data['data']['accessory_pay'] = queryset_to_json(accessory_pay)
            data['status'] = 'success'
            data['msg'] = '查询成功'
        except:
            data['status'] = 'fail'
            data['msg'] = '查询对象不存在'
        return JsonResponse(data)


# 索赔扣款--已完成
@login_required()
def claim_payment_view(request):
    if request.method == 'GET':
        data = basic_info_json(('Currency', 'Factory', 'Claim_category', 'Type', 'Customer', 'Staff', 'Export_company'))
        return render(request, 'finance/claim_payment.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        # po_detail数据
        try:
            po_detail = Po_detail.objects.all().order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': 'po_detail未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except AttributeError:
            return JsonResponse({'status': 'unknown', 'msg': 'po未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 索赔信息
        try:
            claim_payment = Claim_payment.objects.get(po=po_detail.po, po_detail=po_detail.item_no)
            try:
                currency = obj_to_json(claim_payment.currency)
            except:
                currency = {}
            try:
                deduction_currency = obj_to_json(claim_payment.deduction_currency)
            except:
                deduction_currency = {}
            data['data']['claim_payment'] = obj_to_json(claim_payment)
            data['data']['claim_payment']['currency'] = currency
            data['data']['claim_payment']['deduction_currency'] = deduction_currency
        except:
            data['data']['claim_payment'] = {}
        # 索赔明细信息
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['claim_detail'] = {}
            for i in claim_detail:
                try:
                    claim_category = obj_to_json(i.claim_category)
                except:
                    claim_category = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    type = obj_to_json(i.type)
                except:
                    type = {}
                try:
                    currency1 = obj_to_json(i.currency1)
                except:
                    currency1 = {}
                data['data']['claim_detail'][str(i.id)] = obj_to_json(i)
                data['data']['claim_detail'][str(i.id)]['claim_category'] = claim_category
                data['data']['claim_detail'][str(i.id)]['currency'] = currency
                data['data']['claim_detail'][str(i.id)]['type'] = type
                data['data']['claim_detail'][str(i.id)]['currency1'] = currency1
        except:
            data['data']['claim_detail'] = {}
        # 扣款明细信息
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['deduction_detail'] = {}
            for i in deduction_detail:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                data['data']['deduction_detail'][str(i.id)] = obj_to_json(i)
                data['data']['deduction_detail'][str(i.id)]['factory'] = factory
                data['data']['deduction_detail'][str(i.id)]['order_currency'] = order_currency
        except:
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(id__lt=n).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 索赔信息
        try:
            claim_payment = Claim_payment.objects.get(po=po_detail.po, po_detail=po_detail.item_no)
            try:
                currency = obj_to_json(claim_payment.currency)
            except:
                currency = {}
            try:
                deduction_currency = obj_to_json(claim_payment.deduction_currency)
            except:
                deduction_currency = {}
            data['data']['claim_payment'] = obj_to_json(claim_payment)
            data['data']['claim_payment']['currency'] = currency
            data['data']['claim_payment']['deduction_currency'] = deduction_currency
        except:
            data['data']['claim_payment'] = {}
        # 索赔明细信息
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['claim_detail'] = {}
            for i in claim_detail:
                try:
                    claim_category = obj_to_json(i.claim_category)
                except:
                    claim_category = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    type = obj_to_json(i.type)
                except:
                    type = {}
                try:
                    currency1 = obj_to_json(i.currency1)
                except:
                    currency1 = {}
                data['data']['claim_detail'][str(i.id)] = obj_to_json(i)
                data['data']['claim_detail'][str(i.id)]['claim_category'] = claim_category
                data['data']['claim_detail'][str(i.id)]['currency'] = currency
                data['data']['claim_detail'][str(i.id)]['type'] = type
                data['data']['claim_detail'][str(i.id)]['currency1'] = currency1
        except:
            data['data']['claim_detail'] = {}
        # 扣款明细信息
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['deduction_detail'] = {}
            for i in deduction_detail:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                data['data']['deduction_detail'][str(i.id)] = obj_to_json(i)
                data['data']['deduction_detail'][str(i.id)]['factory'] = factory
                data['data']['deduction_detail'][str(i.id)]['order_currency'] = order_currency
        except:
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 索赔信息
        try:
            claim_payment = Claim_payment.objects.get(po=po_detail.po, po_detail=po_detail.item_no)
            try:
                currency = obj_to_json(claim_payment.currency)
            except:
                currency = {}
            try:
                deduction_currency = obj_to_json(claim_payment.deduction_currency)
            except:
                deduction_currency = {}
            data['data']['claim_payment'] = obj_to_json(claim_payment)
            data['data']['claim_payment']['currency'] = currency
            data['data']['claim_payment']['deduction_currency'] = deduction_currency
        except:
             data['data']['claim_payment'] = {}
        # 索赔明细信息
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['claim_detail'] = {}
            for i in claim_detail:
                try:
                    claim_category = obj_to_json(i.claim_category)
                except:
                    claim_category = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    type = obj_to_json(i.type)
                except:
                    type = {}
                try:
                    currency1 = obj_to_json(i.currency1)
                except:
                    currency1 = {}
                data['data']['claim_detail'][str(i.id)] = obj_to_json(i)
                data['data']['claim_detail'][str(i.id)]['claim_category'] = claim_category
                data['data']['claim_detail'][str(i.id)]['currency'] = currency
                data['data']['claim_detail'][str(i.id)]['type'] = type
                data['data']['claim_detail'][str(i.id)]['currency1'] = currency1
        except:
            data['data']['claim_detail'] = {}
        # 扣款明细信息
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['deduction_detail'] = {}
            for i in deduction_detail:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                data['data']['deduction_detail'][str(i.id)] = obj_to_json(i)
                data['data']['deduction_detail'][str(i.id)]['factory'] = factory
                data['data']['deduction_detail'][str(i.id)]['order_currency'] = order_currency
        except:
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)
    elif 'final' in request.POST:
        # po_detail数据
        try:
            po_detail = Po_detail.objects.all().order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 索赔信息
        try:
            claim_payment = Claim_payment.objects.get(po=po_detail.po, po_detail=po_detail.item_no)
            try:
                currency = obj_to_json(claim_payment.currency)
            except:
                currency = {}
            try:
                deduction_currency = obj_to_json(claim_payment.deduction_currency)
            except:
                deduction_currency = {}
            data['data']['claim_payment'] = obj_to_json(claim_payment)
            data['data']['claim_payment']['currency'] = currency
            data['data']['claim_payment']['deduction_currency'] = deduction_currency
        except:
            data['data']['claim_payment'] = {}
        # 索赔明细信息
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['claim_detail'] = {}
            for i in claim_detail:
                try:
                    claim_category = obj_to_json(i.claim_category)
                except:
                    claim_category = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    type = obj_to_json(i.type)
                except:
                    type = {}
                try:
                    currency1 = obj_to_json(i.currency1)
                except:
                    currency1 = {}
                data['data']['claim_detail'][str(i.id)] = obj_to_json(i)
                data['data']['claim_detail'][str(i.id)]['claim_category'] = claim_category
                data['data']['claim_detail'][str(i.id)]['currency'] = currency
                data['data']['claim_detail'][str(i.id)]['type'] = type
                data['data']['claim_detail'][str(i.id)]['currency1'] = currency1
        except:
            data['data']['claim_detail'] = {}
        # 扣款明细信息
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['deduction_detail'] = {}
            for i in deduction_detail:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                data['data']['deduction_detail'][str(i.id)] = obj_to_json(i)
                data['data']['deduction_detail'][str(i.id)]['factory'] = factory
                data['data']['deduction_detail'][str(i.id)]['order_currency'] = order_currency
        except:
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.po_detail for i in Claim_payment.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        if item_no in l2:
            return JsonResponse({'status': 'fail', 'msg': 'item号在索赔主条目中已存在'})
        try:
            claim_payment = claim_payment_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.po_detail for i in Claim_payment.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': 'item号在索赔条目中不存在'})
        try:
            claim_payment = Claim_payment.objects.get(po=order_number, po_detail=item_no)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        # except:
        #     return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        claim_payment.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.po_detail for i in Claim_payment.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': 'item号在索赔条目中不存在'})
        try:
            claim_payment = claim_payment_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '修改失败'})
    elif 'view' in request.POST:
        factory = request.POST.get('factory')
        order_number = request.POST.get('po')
        item_no = request.POST.get('po_detail')
        # 按照工厂查询
        if factory:
            try:
                fac = Factory.objects.filter(name__contains=factory)[0]
                contract = Contract.objects.filter(factory=fac)[0]
                order_number = contract.po  # 获取po号
                item_no = contract.item_no  # 获取item号
            except:
                return JsonResponse({'status': 'fail', 'msg': '该工厂无信息'})
        # 按照po+po_detail查找
        elif order_number and item_no:
            order_number = request.POST.get('po')
            item_no = request.POST.get('po_detail')

        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po_detail不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=po_detail.po, item_no=po_detail)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except:
            data['data']['product_send'] = {}
        # 索赔信息
        try:
            claim_payment = Claim_payment.objects.get(po=po_detail.po, po_detail=po_detail.item_no)
            try:
                currency = obj_to_json(claim_payment.currency)
            except:
                currency = {}
            try:
                deduction_currency = obj_to_json(claim_payment.deduction_currency)
            except:
                deduction_currency = {}
            data['data']['claim_payment'] = obj_to_json(claim_payment)
            data['data']['claim_payment']['currency'] = currency
            data['data']['claim_payment']['deduction_currency'] = deduction_currency
        except:
            data['data']['claim_payment'] = {}
        # 索赔明细信息
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['claim_detail'] = {}
            for i in claim_detail:
                try:
                    claim_category = obj_to_json(i.claim_category)
                except:
                    claim_category = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    type = obj_to_json(i.type)
                except:
                    type = {}
                try:
                    currency1 = obj_to_json(i.currency1)
                except:
                    currency1 = {}
                data['data']['claim_detail'][str(i.id)] = obj_to_json(i)
                data['data']['claim_detail'][str(i.id)]['claim_category'] = claim_category
                data['data']['claim_detail'][str(i.id)]['currency'] = currency
                data['data']['claim_detail'][str(i.id)]['type'] = type
                data['data']['claim_detail'][str(i.id)]['currency1'] = currency1
        except:
            data['data']['claim_detail'] = {}
        # 扣款明细信息
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=claim_payment.id)
            data['data']['deduction_detail'] = {}
            for i in deduction_detail:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                data['data']['deduction_detail'][str(i.id)] = obj_to_json(i)
                data['data']['deduction_detail'][str(i.id)]['factory'] = factory
                data['data']['deduction_detail'][str(i.id)]['order_currency'] = order_currency
        except:
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)


# 索赔明细
@login_required()
def claim_detail_view(request):
    # if request.method == 'GET':
    #     return render(request, 'order/sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        payment_id = request.POST.get('p_id')
        data = {}
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=payment_id).order_by("id").first()
            try:
                claim_category = obj_to_json(claim_detail.claim_category)
            except:
                claim_category = {}
            try:
                currency = obj_to_json(claim_detail.currency)
            except:
                currency = {}
            try:
                type = obj_to_json(claim_detail.type)
            except:
                type = {}
            try:
                currency1 = obj_to_json(claim_detail.currency1)
            except:
                currency1 = {}

            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['claim_detail'] = obj_to_json(claim_detail)
            data['data']['claim_detail']['claim_category'] = claim_category
            data['data']['claim_detail']['currency'] = currency
            data['data']['claim_detail']['type'] = type
            data['data']['claim_detail']['currency1'] = currency1
        except:
            data['status'] = 'fail'
            data['msg'] = '无索赔详情'
            data['data'] = {}
            data['data']['claim_detail'] = {}
        return JsonResponse(data)
    elif 'last' in request.POST:
        payment_id = request.POST.get('p_id')
        detail_id = request.POST.get('d_id')
        data = {}
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=payment_id, id__lt=detail_id).order_by("-id").first()
            try:
                claim_category = obj_to_json(claim_detail.claim_category)
            except:
                claim_category = {}
            try:
                currency = obj_to_json(claim_detail.currency)
            except:
                currency = {}
            try:
                type = obj_to_json(claim_detail.type)
            except:
                type = {}
            try:
                currency1 = obj_to_json(claim_detail.currency1)
            except:
                currency1 = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['claim_detail'] = obj_to_json(claim_detail)
            data['data']['claim_detail']['claim_category'] = claim_category
            data['data']['claim_detail']['currency'] = currency
            data['data']['claim_detail']['type'] = type
            data['data']['claim_detail']['currency1'] = currency1
        except:
            data['status'] = 'fail'
            data['msg'] = '无上一条'
            data['data'] = {}
            data['data']['claim_detail'] = {}
        return JsonResponse(data)
    elif 'next' in request.POST:
        payment_id = request.POST.get('p_id')
        detail_id = request.POST.get('d_id')
        data = {}
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=payment_id, id__gt=detail_id).order_by("id").first()
            try:
                claim_category = obj_to_json(claim_detail.claim_category)
            except:
                claim_category = {}
            try:
                currency = obj_to_json(claim_detail.currency)
            except:
                currency = {}
            try:
                type = obj_to_json(claim_detail.type)
            except:
                type = {}
            try:
                currency1 = obj_to_json(claim_detail.currency1)
            except:
                currency1 = {}

            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['claim_detail'] = obj_to_json(claim_detail)
            data['data']['claim_detail']['claim_category'] = claim_category
            data['data']['claim_detail']['currency'] = currency
            data['data']['claim_detail']['type'] = type
            data['data']['claim_detail']['currency1'] = currency1
        except:
            data['status'] = 'fail'
            data['msg'] = '无下一条'
            data['data'] = {}
            data['data']['claim_detail'] = {}
        return JsonResponse(data)
    elif 'final' in request.POST:
        payment_id = request.POST.get('p_id')
        data = {}
        try:
            claim_detail = Claim_detail.objects.filter(claim_payment_id=payment_id).order_by("-id").first()
            try:
                claim_category = obj_to_json(claim_detail.claim_category)
            except:
                claim_category = {}
            try:
                currency = obj_to_json(claim_detail.currency)
            except:
                currency = {}
            try:
                type = obj_to_json(claim_detail.type)
            except:
                type = {}
            try:
                currency1 = obj_to_json(claim_detail.currency1)
            except:
                currency1 = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['claim_detail'] = obj_to_json(claim_detail)
            data['data']['claim_detail']['claim_category'] = claim_category
            data['data']['claim_detail']['currency'] = currency
            data['data']['claim_detail']['type'] = type
            data['data']['claim_detail']['currency1'] = currency1
        except:
            data['status'] = 'fail'
            data['msg'] = '无索赔详情'
            data['data'] = {}
            data['data']['claim_detail'] = {}
        return JsonResponse(data)
    elif 'add' in request.POST:  # 根据claim_payment关联添加
        try:
            claim_detail = claim_detail_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        pass
    elif 'modify' in request.POST:  # 根据claim_payment关联修改
        try:
            claim_detail = claim_detail_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '修改失败'})
    elif 'view' in request.POST:
        payment_id = request.POST.get('p_id')
        detail_id = request.POST.get('d_id')
        data = {}
        try:
            claim_detail = Claim_detail.objects.get(id=detail_id)
            try:
                claim_category = obj_to_json(claim_detail.claim_category)
            except:
                claim_category = {}
            try:
                currency = obj_to_json(claim_detail.currency)
            except:
                currency = {}
            try:
                type = obj_to_json(claim_detail.type)
            except:
                type = {}
            try:
                currency1 = obj_to_json(claim_detail.currency1)
            except:
                currency1 = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['claim_detail'] = obj_to_json(claim_detail)
            data['data']['claim_detail']['claim_category'] = claim_category
            data['data']['claim_detail']['currency'] = currency
            data['data']['claim_detail']['type'] = type
            data['data']['claim_detail']['currency1'] = currency1
        except:
            data['status'] = 'fail'
            data['msg'] = '查找条目不存在'
            data['data'] = {}
            data['data']['claim_detail'] = {}
        return JsonResponse(data)


# 扣款明细
@login_required()
def deduction_detail_view(request):
    # if request.method == 'GET':
    #     return render(request, 'order/sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        payment_id = request.POST.get('p_id')
        data = {}
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=payment_id).order_by("id").first()
            try:
                factory = obj_to_json(deduction_detail.factory)
            except:
                factory = {}
            try:
                currency = obj_to_json(deduction_detail.currency)
            except:
                currency = {}

            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['deduction_detail'] = obj_to_json(deduction_detail)
            data['data']['deduction_detail']['factory'] = factory
            data['data']['deduction_detail']['currency'] = currency
        except:
            data['status'] = 'fail'
            data['msg'] = '无扣款详情'
            data['data'] = {}
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)
    elif 'last' in request.POST:
        payment_id = request.POST.get('p_id')
        deduction_id = request.POST.get('dd_id')
        data = {}
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=payment_id, id__lt=deduction_id).order_by("-id").first()
            try:
                factory = obj_to_json(deduction_detail.factory)
            except:
                factory = {}
            try:
                currency = obj_to_json(deduction_detail.currency)
            except:
                currency = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['deduction_detail'] = obj_to_json(deduction_detail)
            data['data']['deduction_detail']['factory'] = factory
            data['data']['deduction_detail']['currency'] = currency
        except:
            data['status'] = 'fail'
            data['msg'] = '无上一条'
            data['data'] = {}
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)
    elif 'next' in request.POST:
        payment_id = request.POST.get('p_id')
        deduction_id = request.POST.get('dd_id')
        data = {}
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=payment_id, id__gt=deduction_id).order_by("id").first()
            try:
                factory = obj_to_json(deduction_detail.factory)
            except:
                factory = {}
            try:
                currency = obj_to_json(deduction_detail.currency)
            except:
                currency = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['deduction_detail'] = obj_to_json(deduction_detail)
            data['data']['deduction_detail']['factory'] = factory
            data['data']['deduction_detail']['currency'] = currency
        except:
            data['status'] = 'fail'
            data['msg'] = '无下一条'
            data['data'] = {}
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)
    elif 'final' in request.POST:
        payment_id = request.POST.get('p_id')
        data = {}
        try:
            deduction_detail = Deduction_detail.objects.filter(claim_payment_id=payment_id).order_by("-id").first()
            try:
                factory = obj_to_json(deduction_detail.factory)
            except:
                factory = {}
            try:
                currency = obj_to_json(deduction_detail.currency)
            except:
                currency = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['deduction_detail'] = obj_to_json(deduction_detail)
            data['data']['deduction_detail']['factory'] = factory
            data['data']['deduction_detail']['currency'] = currency
        except:
            data['status'] = 'fail'
            data['msg'] = '无扣款详情'
            data['data'] = {}
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)
    elif 'add' in request.POST:
        try:
            deduction_detail = deduction_detail_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'success', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        pass
    elif 'modify' in request.POST:
        try:
            deduction_detail = deduction_detail_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'success', 'msg': '修改失败'})
    elif 'view' in request.POST:
        payment_id = request.POST.get('p_id')
        deduction_id = request.POST.get('dd_id')
        data = {}
        try:
            deduction_detail = Deduction_detail.objects.get(id=deduction_id)
            try:
                factory = obj_to_json(deduction_detail.factory)
            except:
                factory = {}
            try:
                currency = obj_to_json(deduction_detail.currency)
            except:
                currency = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['deduction_detail'] = obj_to_json(deduction_detail)
            data['data']['deduction_detail']['factory'] = factory
            data['data']['deduction_detail']['currency'] = currency
        except:
            data['status'] = 'fail'
            data['msg'] = '查找条目不存在'
            data['data'] = {}
            data['data']['deduction_detail'] = {}
        return JsonResponse(data)


# 材料配件扣款
@login_required()
def accessory_deduction_view(request):
    if request.method == 'GET':
        return render(request, 'order/sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        try:
            accessory_deduction = accessory_deduction_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'success', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        pass
    elif 'modify' in request.POST:
        try:
            deduction_detail = deduction_detail_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'success', 'msg': '修改失败'})
    elif 'view' in request.POST:
        pass


# 材料配件扣款明细
@login_required()
def accessory_deduction_detail_view(request):
    if request.method == 'GET':
        return render(request, 'order/sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        l = [i['order_number'] for i in Po.objects.values()]
        l1 = [i['item_no'] for i in Po_detail.objects.values()]
        po = request.POST.get('po')
        po_detail = request.POST.get('po_detail')
        if po not in l:
            return JsonResponse({'status': 'fail', 'msg': '该Po不存在'})
        if po_detail not in l1:
            return JsonResponse({'status': 'fail', 'msg': '该Po_detail不存在'})
        accessory_deduction_detail = accessory_deduction_detail_add(request)
        return JsonResponse({'status': 'success', 'msg': '添加成功'})
    elif 'delete' in request.POST:
        detail_id = request.POST.get('detail_id')
        accessory_deduction_detail = Accessory_deduction_detail.objects.get(id=detail_id)
        accessory_deduction_detail.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        accessory_deduction_detail = accessory_deduction_detail_modify(request)
    elif 'view' in request.POST:
        l = [i['order_number'] for i in Po.objects.values()]
        l1 = [i['item_no'] for i in Po_detail.objects.values()]
        po = request.POST.get('po')
        po_detail = request.POST.get('po_detail')
        if po not in l:
            return JsonResponse({'status': 'fail', 'msg': '该Po不存在'})
        if po_detail not in l1:
            return JsonResponse({'status': 'fail', 'msg': '该Po_detail不存在'})
        accessory_deduction = Accessory_deduction.objects.get(po=po, po_detail=po_detail)
        accessory_deduction_detail = Accessory_deduction_detail.objects.filter(deduction_detail=accessory_deduction.id)
        acc_de = obj_to_json(accessory_deduction)
        acc_de_de = queryset_to_json(accessory_deduction_detail)
        dic = {}
        dic['acc_de'] = acc_de
        dic['ded_de'] = acc_de_de
        data = {}
        data['data'] = dic
        data['status'] = 'success'
        data['msg'] = '查询成功'
        return JsonResponse(data)
