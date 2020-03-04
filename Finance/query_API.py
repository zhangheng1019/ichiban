import os
import time
import uuid
import hashlib
import random
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.shortcuts import render, redirect
from apple import settings
from Basic_info.models import *
from Order.models import *
from Finance.models import *
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required


@login_required()
def claim_category_add(request):
    name = request.POST.get('name')
    code = request.POST.get('code')
    dict_info = {
        'name': name,
        'code': code,
    }
    claim_category = Claim_category(code=code)
    if not claim_category:
        obj = Claim_category(**dict_info)
        obj.save()
        return dict_info


@login_required()
def claim_category_modify(request):
    name = request.POST.get('name')
    code = request.POST.get('code')
    claim_category = Claim_category(code=code)
    if claim_category:
        claim_category.name = name
        claim_category.code = code
        claim_category.save()
        return claim_category


@login_required()
def type_add(request):
    desc = request.POST.get('desc')
    edesc = request.POST.get('edesc')
    dict_info = {
        'desc': desc,
        'edesc': edesc,
    }
    obj = Type(**dict_info)
    obj.save()
    return dict_info


@login_required()
def type_modify(request):
    desc = request.POST.get('desc')
    edesc = request.POST.get('edesc')
    t_id = request.POST.get('id')
    type = Type.objects.get(id=t_id)
    if type:
        type.desc = desc
        type.edesc = edesc
        type.save()
        return type


# 以上为基础信息
@login_required()
def finance_bill_add(request):
    bill_number = request.POST.get('bill_number')
    out_number = request.POST.get('out_number')
    place = request.POST.get('place')
    date = request.POST.get('date')
    extra_bill = request.POST.get('extra_bill')
    is_check = request.POST.get('is_check')
    is_pay = request.POST.get('is_pay')
    detail_id = request.POST.get('detail_id')
    abstract = request.POST.get('abstract')
    code = request.POST.get('code')
    subject = request.POST.get('subject')
    child_subject = request.POST.get('child_subject')
    inner_subject = request.POST.get('inner_subject')
    currency = request.POST.get('currency')
    borrow = request.POST.get('borrow')
    lend = request.POST.get('lend')
    rate_of_exchange = request.POST.get('rate_of_exchange')
    is_receipt = request.POST.get('is_receipt')
    head_quarter = request.POST.get('head_quarter')
    area = request.POST.get('area')
    department = request.POST.get('department')
    handle = request.POST.get('handle')
    explain = request.POST.get('explain')
    dict_info = {
        'bill_number': bill_number,
        'out_number': out_number,
        'place': place,
        'date': date,
        'extra_bill': extra_bill,
        'is_check': is_check,
        'is_pay': is_pay,
        'detail_id': detail_id,
        'abstract': abstract,
        'code': code,
        'subject': subject,
        'child_subject': child_subject,
        'inner_subject': inner_subject,
        'currency': currency,
        'borrow': borrow,
        'lend': lend,
        'rate_of_exchange': rate_of_exchange,
        'is_receipt': is_receipt,
        'head_quarter': head_quarter,
        'area': area,
        'department': department,
        'handle': handle,
        'explain': explain,
    }
    finance_bill = Finance_bill.objects.get(bill_number=bill_number)
    if not finance_bill:
        obj = Finance_bill(**dict_info)
        obj.save()
        return dict_info


@login_required()
def finance_bill_modify(request):
    bill_number = request.POST.get('bill_number')
    out_number = request.POST.get('out_number')
    place = request.POST.get('place')
    date = request.POST.get('date')
    extra_bill = request.POST.get('extra_bill')
    is_check = request.POST.get('is_check')
    is_pay = request.POST.get('is_pay')
    detail_id = request.POST.get('detail_id')
    abstract = request.POST.get('abstract')
    code = request.POST.get('code')
    subject = request.POST.get('subject')
    child_subject = request.POST.get('child_subject')
    inner_subject = request.POST.get('inner_subject')
    currency = request.POST.get('currency')
    borrow = request.POST.get('borrow')
    lend = request.POST.get('lend')
    rate_of_exchange = request.POST.get('rate_of_exchange')
    is_receipt = request.POST.get('is_receipt')
    head_quarter = request.POST.get('head_quarter')
    area = request.POST.get('area')
    department = request.POST.get('department')
    handle = request.POST.get('handle')
    explain = request.POST.get('explain')
    # 创建对象
    finance_bill = Finance_bill.objects.get(bill_number=bill_number)
    if finance_bill:
        finance_bill.bill_number = bill_number
        finance_bill.out_number = out_number
        finance_bill.place = place
        finance_bill.date = date
        finance_bill.extra_bill = extra_bill
        finance_bill.is_check = is_check
        finance_bill.is_pay = is_pay
        finance_bill.detail_id = detail_id
        finance_bill.abstract = abstract
        finance_bill.code = code
        finance_bill.subject = subject
        finance_bill.child_subject = child_subject
        finance_bill.inner_subject = inner_subject
        finance_bill.currency = currency
        finance_bill.borrow = borrow
        finance_bill.lend = lend
        finance_bill.rate_of_exchange = rate_of_exchange
        finance_bill.is_receipt = is_receipt
        finance_bill.head_quarter = head_quarter
        finance_bill.area = area
        finance_bill.department = department
        finance_bill.handle = handle
        finance_bill.explain = explain
        finance_bill.save()
        return finance_bill


@login_required()
def ship_payment_add(request):
    customer = request.POST.get('customer')
    factory = request.POST.get('factory')
    po = request.POST.get('po')
    po_detail = request.POST.get('po_detail')
    customer_po = request.POST.get('customer_po')
    customer_item = request.POST.get('customer_item')
    product = request.POST.get('product')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    final_date = request.POST.get('final_date')
    qc1 = request.POST.get('qc1')
    omr = request.POST.get('omr')
    cus_price = request.POST.get('cus_price')
    cus_currency = request.POST.get('cus_currency')
    cus_total = request.POST.get('cus_total')
    cus_total_currency = request.POST.get('cus_total_currency')
    fac_cost = request.POST.get('fac_cost')
    fac_cost_currency = request.POST.get('fac_cost_currency')
    fac_total = request.POST.get('fac_total')
    fac_total_currency = request.POST.get('fac_total_currency')
    code = request.POST.get('code')
    name = request.POST.get('name')
    title = request.POST.get('title')
    account_no = request.POST.get('account_no')
    bank = request.POST.get('bank')
    invoice_no = request.POST.get('invoice_no')
    currency = request.POST.get('currency')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None
    explain = request.POST.get('explain')
    pay_amount = request.POST.get('pay_amount')
    remit_no = request.POST.get('remit_no')
    pay_date = request.POST.get('pay_date')
    dict_info = {
        'customer': customer,
        'factory': factory,
        'po': po,
        'po_detail': po_detail,
        'customer_po': customer_po,
        'customer_item': customer_item,
        'product': product,
        'amount': amount,
        'unit': unit,
        'final_date': final_date,
        'qc1': qc1,
        'omr': omr,
        'cus_price': cus_price,
        'cus_currency': cus_currency,
        'cus_total': cus_total,
        'cus_total_currency': cus_total_currency,
        'fac_cost': fac_cost,
        'fac_cost_currency': fac_cost_currency,
        'fac_total': fac_total,
        'fac_total_currency': fac_total_currency,
        'code': code,
        'name': name,
        'title': title,
        'account_no': account_no,
        'bank': bank,
        'invoice_no': invoice_no,
        'currency_id': currency_id,
        'explain': explain,
        'pay_amount': pay_amount,
        'remit_no': remit_no,
        'pay_date': pay_date,
    }
    obj = Ship_payment(**dict_info)
    obj.save()
    return dict_info


@login_required()
def ship_payment_modify(request):
    po = request.POST.get('po')
    po_detail = request.POST.get('po_detail')

    code = request.POST.get('code')
    name = request.POST.get('name')
    title = request.POST.get('title')
    account_no = request.POST.get('account_no')
    bank = request.POST.get('bank')

    invoice_no = request.POST.get('invoice_no')
    currency = request.POST.get('currency')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None
    explain = request.POST.get('explain')
    pay_amount = request.POST.get('pay_amount')
    remit_no = request.POST.get('remit_no')
    pay_date = request.POST.get('pay_date')
    # 创建对象
    ship_payment = Ship_payment.objects.get(po=po, po_detail=po_detail)
    # 修改对象信息
    # 进出口公司信息
    ship_payment.code = code
    ship_payment.name = name
    ship_payment.title = title
    ship_payment.account_no = account_no
    ship_payment.bank = bank
    # 大货付款主信息
    ship_payment.invoice_no = invoice_no
    ship_payment.currency_id = currency_id
    ship_payment.explain = explain
    ship_payment.pay_amount = pay_amount
    ship_payment.remit_no = remit_no
    ship_payment.pay_date = pay_date
    ship_payment.save()
    return ship_payment


@login_required()
def accessory_pay_add(request):
    customer = request.POST.get('customer')
    factory = request.POST.get('factory')
    po = request.POST.get('po')
    po_detail = request.POST.get('po_detail')
    customer_po = request.POST.get('customer_po')
    customer_item = request.POST.get('customer_item')
    product = request.POST.get('product')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    send_material_date = request.POST.get('send_material_date')
    provide_type = request.POST.get('provide_type')
    omr = request.POST.get('omr')
    accessory_cost = request.POST.get('accessory_cost')
    accessory_cost_total = request.POST.get('accessory_cost_total')
    currency = request.POST.get('currency')
    sale_date = request.POST.get('sale_date')
    code = request.POST.get('code')
    name = request.POST.get('name')
    title = request.POST.get('title')
    account_no = request.POST.get('account_no')
    bank = request.POST.get('bank')
    invoice_no = request.POST.get('invoice_no')
    explain = request.POST.get('explain')
    pay_currency = request.POST.get('pay_currency')
    pay_remark = request.POST.get('pay_remark')
    pay_amount = request.POST.get('pay_amount')
    remit_no = request.POST.get('remit_no')
    pay_date = request.POST.get('pay_date')
    dict_info = {
        'customer': customer,
        'factory': factory,
        'po': po,
        'po_detail': po_detail,
        'customer_po': customer_po,
        'customer_item': customer_item,
        'product': product,
        'amount': amount,
        'unit': unit,
        'send_material_date': send_material_date,
        'provide_type': provide_type,
        'omr': omr,
        'accessory_cost': accessory_cost,
        'accessory_cost_total': accessory_cost_total,
        'currency': currency,
        'sale_date': sale_date,
        'code': code,
        'name': name,
        'title': title,
        'account_no': account_no,
        'bank': bank,
        'invoice_no': invoice_no,
        'explain': explain,
        'pay_currency': pay_currency,
        'pay_remark': pay_remark,
        'pay_amount': pay_amount,
        'remit_no': remit_no,
        'pay_date': pay_date,
    }

    obj = Accessory_pay(**dict_info)
    obj.save()
    return dict_info


@login_required()
def accessory_pay_modify(request):
    customer = request.POST.get('customer')
    factory = request.POST.get('factory')
    po = request.POST.get('po')
    po_detail = request.POST.get('po_detail')
    customer_po = request.POST.get('customer_po')
    customer_item = request.POST.get('customer_item')
    product = request.POST.get('product')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    send_material_date = request.POST.get('send_material_date')
    provide_type = request.POST.get('provide_type')
    omr = request.POST.get('omr')
    accessory_cost = request.POST.get('accessory_cost')
    accessory_cost_total = request.POST.get('accessory_cost_total')
    currency = request.POST.get('currency')
    sale_date = request.POST.get('sale_date')
    code = request.POST.get('code')
    name = request.POST.get('name')
    title = request.POST.get('title')
    account_no = request.POST.get('account_no')
    bank = request.POST.get('bank')
    invoice_no = request.POST.get('invoice_no')
    explain = request.POST.get('explain')
    pay_currency = request.POST.get('pay_currency')
    pay_remark = request.POST.get('pay_remark')
    pay_amount = request.POST.get('pay_amount')
    remit_no = request.POST.get('remit_no')
    pay_date = request.POST.get('pay_date')
    accessory_pay = Accessory_pay.objects.get(po=po, po_detail=po_detail)
    if not accessory_pay:
        accessory_pay.customer = customer
        accessory_pay.factory = factory
        accessory_pay.po = po
        accessory_pay.po_detail = po_detail
        accessory_pay.customer_po = customer_po
        accessory_pay.customer_item = customer_item
        accessory_pay.product = product
        accessory_pay.amount = amount
        accessory_pay.unit = unit
        accessory_pay.send_material_date = send_material_date
        accessory_pay.provide_type = provide_type
        accessory_pay.omr = omr
        accessory_pay.accessory_cost = accessory_cost
        accessory_pay.accessory_cost_total = accessory_cost_total
        accessory_pay.currency = currency
        accessory_pay.sale_date = sale_date
        accessory_pay.code = code
        accessory_pay.name = name
        accessory_pay.title = title
        accessory_pay.account_no = account_no
        accessory_pay.bank = bank
        accessory_pay.invoice_no = invoice_no
        accessory_pay.explain = explain
        accessory_pay.pay_currency = pay_currency
        accessory_pay.pay_remark = pay_remark
        accessory_pay.pay_amount = pay_amount
        accessory_pay.remit_no = remit_no
        accessory_pay.pay_date = pay_date
        accessory_pay.save()
        return accessory_pay


@login_required()
def claim_payment_add(request):
    customer = request.POST.get('customer')
    factory = request.POST.get('factory')
    mr = request.POST.get('mr')
    explain = request.POST.get('explain')
    po = request.POST.get('po')
    po_detail = request.POST.get('po_detail')
    customer_po = request.POST.get('customer_po')
    customer_item = request.POST.get('customer_item')
    product = request.POST.get('product')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    final_date = request.POST.get('final_date')
    qc1 = request.POST.get('qc1')
    pay_date = request.POST.get('pay_date')
    date = request.POST.get('date')
    claim_amount = request.POST.get('claim_amount')
    fac_amount = request.POST.get('fac_amount')
    currency = request.POST.get('currency')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None
    invoice_no = request.POST.get('invoice_no')
    claim_remark = request.POST.get('claim_remark')
    dict_info = {
        'customer': customer,
        'factory': factory,
        'mr': mr,
        'explain': explain,
        'po': po,
        'po_detail': po_detail,
        'customer_po': customer_po,
        'customer_item': customer_item,
        'product': product,
        'amount': amount,
        'unit': unit,
        'final_date': final_date,
        'qc1': qc1,
        'pay_date': pay_date,
        'date': date,
        'claim_amount': claim_amount,
        'fac_amount': fac_amount,
        'currency_id': currency_id,
        'invoice_no': invoice_no,
        'claim_remark': claim_remark,
    }
    obj = Claim_payment(**dict_info)
    obj.save()
    return dict_info


@login_required()
def claim_payment_modify(request):
    customer = request.POST.get('customer')
    factory = request.POST.get('factory')
    mr = request.POST.get('mr')
    explain = request.POST.get('explain')
    po = request.POST.get('po')
    po_detail = request.POST.get('po_detail')
    customer_po = request.POST.get('customer_po')
    customer_item = request.POST.get('customer_item')
    product = request.POST.get('product')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    final_date = request.POST.get('final_date')
    qc1 = request.POST.get('qc1')
    pay_date = request.POST.get('pay_date')
    date = request.POST.get('date')
    claim_amount = request.POST.get('claim_amount')
    fac_amount = request.POST.get('fac_amount')
    currency = request.POST.get('currency')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None
    invoice_no = request.POST.get('invoice_no')
    claim_remark = request.POST.get('claim_remark')

    claim_payment = Claim_payment.objects.get(po=po, po_detail=po_detail)
    claim_payment.customer = customer
    claim_payment.factory = factory
    claim_payment.mr = mr
    claim_payment.explain = explain
    claim_payment.po = po
    claim_payment.po_detail = po_detail
    claim_payment.customer_po = customer_po
    claim_payment.customer_item = customer_item
    claim_payment.product = product
    claim_payment.amount = amount
    claim_payment.unit = unit
    claim_payment.final_date = final_date
    claim_payment.qc1 = qc1
    claim_payment.pay_date = pay_date
    claim_payment.date = date
    claim_payment.claim_amount = claim_amount
    claim_payment.fac_amount = fac_amount
    claim_payment.currency_id = currency_id
    claim_payment.invoice_no = invoice_no
    claim_payment.claim_remark = claim_remark
    claim_payment.save()
    return claim_payment


@login_required()
def claim_detail_add(request):
    claim_payment_id = request.POST.get('p_id')

    claim_category = request.POST.get('claim_category')
    try:
        claim_category_id = Claim_category.objects.get(code=claim_category).id
    except:
        claim_category_id = None

    currency = request.POST.get('currency ')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None

    type = request.POST.get('type')
    try:
        type_id = Type.objects.get(desc=type).id
    except:
        type_id = None

    currency1 = request.POST.get('currency1')
    try:
        currency1_id = Currency.objects.get(code=currency1).id
    except:
        currency1_id = None

    date = request.POST.get('date')
    count = request.POST.get('count')
    amount = request.POST.get('amount')
    category_remark = request.POST.get('category_remark')
    claim_detail = request.POST.get('claim_detail')
    fac_amount = request.POST.get('fac_amount')
    to_rmb = request.POST.get('to_rmb')
    fac_claim_deta = request.POST.get('fac_claim_deta')
    invoice_no = request.POST.get('invoice_no')
    pay_date = request.POST.get('pay_date')
    dict_info = {
        'claim_payment_id': claim_payment_id,
        'claim_category_id': claim_category_id,
        'date': date,
        'count': count,
        'currency_id': currency_id,
        'amount': amount,
        'type_id': type_id,
        'category_remark': category_remark,
        'claim_detail': claim_detail,
        'currency1_id': currency1_id,
        'fac_amount': fac_amount,
        'to_rmb': to_rmb,
        'fac_claim_deta': fac_claim_deta,
        'invoice_no': invoice_no,
        'pay_date': pay_date,
    }
    obj = Claim_detail(**dict_info)
    obj.save()
    return dict_info


@login_required()
def claim_detail_modify(request):
    claim_payment_id = request.POST.get('p_id')
    claim_id = request.POST.get('d_id')

    claim_category = request.POST.get('claim_category')
    try:
        claim_category_id = Claim_category.objects.get(code=claim_category).id
    except:
        claim_category_id = None

    currency = request.POST.get('currency ')
    try:
        currency_id = Currency.objects.get(code=currency).id
    except:
        currency_id = None

    type = request.POST.get('type')
    try:
        type_id = Type.objects.get(desc=type).id
    except:
        type_id = None

    currency1 = request.POST.get('currency1')
    try:
        currency1_id = Currency.objects.get(code=currency1).id
    except:
        currency1_id = None

    date = request.POST.get('date')
    count = request.POST.get('count')
    amount = request.POST.get('amount')
    category_remark = request.POST.get('category_remark')
    claim_detail_explain = request.POST.get('claim_detail_explain')
    fac_amount = request.POST.get('fac_amount')
    to_rmb = request.POST.get('to_rmb')
    fac_claim_deta = request.POST.get('fac_claim_deta')
    invoice_no = request.POST.get('invoice_no')
    pay_date = request.POST.get('pay_date')
    claim_detail = Claim_detail.objects.get(id=claim_id)

    claim_detail.claim_payment_id = claim_payment_id
    claim_detail.claim_category_id = claim_category_id
    claim_detail.date = date
    claim_detail.count = count
    claim_detail.currency_id = currency_id
    claim_detail.amount = amount
    claim_detail.type_id = type_id
    claim_detail.category_remark = category_remark
    claim_detail.claim_detail_explain = claim_detail_explain
    claim_detail.currency1_id = currency1_id
    claim_detail.fac_amount = fac_amount
    claim_detail.to_rmb = to_rmb
    claim_detail.fac_claim_deta = fac_claim_deta
    claim_detail.invoice_no = invoice_no
    claim_detail.pay_date = pay_date
    claim_detail.save()
    return claim_detail


@login_required()
def deduction_detail_add(request):
    claim_payment_id = request.POST.get('p_id')
    deduction_detail_id = request.POST.get('dd_id')
    method = request.POST.get('method')
    material_from = request.POST.get('material_from')
    is_order = request.POST.get('is_order')

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
    fac_order_qty = request.POST.get('fac_order_qty')
    qty_unit = request.POST.get('qty_unit')
    total = request.POST.get('total')
    order_cost = request.POST.get('order_cost')
    deducted_date = request.POST.get('deducted_date')
    fac_actual_qty = request.POST.get('fac_actual_qty')
    fac_actual_unit = request.POST.get('fac_actual_unit')
    invoice_no = request.POST.get('invoice_no')
    material = request.POST.get('material')
    dict_info = {
        'claim_payment_id': claim_payment_id,
        'method': method,
        'material_from': material_from,
        'is_order': is_order,
        'factory_id': factory_id,
        'fac_order_qty': fac_order_qty,
        'qty_unit': qty_unit,
        'total': total,
        'order_cost': order_cost,
        'order_currency_id': order_currency_id,
        'deducted_date': deducted_date,
        'fac_actual_qty': fac_actual_qty,
        'fac_actual_unit': fac_actual_unit,
        'invoice_no': invoice_no,
        'material': material,
    }
    obj = Deduction_detail(**dict_info)
    obj.save()
    return dict_info


@login_required()
def deduction_detail_modify(request):
    claim_payment_id = request.POST.get('p_id')
    deduction_detail_id = request.POST.get('dd_id')
    method = request.POST.get('method')
    material_from = request.POST.get('material_from')
    is_order = request.POST.get('is_order')

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
    fac_order_qty = request.POST.get('fac_order_qty')
    qty_unit = request.POST.get('qty_unit')
    total = request.POST.get('total')
    order_cost = request.POST.get('order_cost')
    deducted_date = request.POST.get('deducted_date')
    fac_actual_qty = request.POST.get('fac_actual_qty')
    fac_actual_unit = request.POST.get('fac_actual_unit')
    invoice_no = request.POST.get('invoice_no')
    material = request.POST.get('material')
    # 获取修改对象
    deduction_detail = Deduction_detail.objects.get(id=deduction_detail_id)
    # 修改
    deduction_detail.claim_payment_id = claim_payment_id
    deduction_detail.method = method
    deduction_detail.material_from = material_from
    deduction_detail.is_order = is_order
    deduction_detail.factory_id = factory_id
    deduction_detail.fac_order_qty = fac_order_qty
    deduction_detail.qty_unit = qty_unit
    deduction_detail.total = total
    deduction_detail.order_cost = order_cost
    deduction_detail.order_currency_id = order_currency_id
    deduction_detail.deducted_date = deducted_date
    deduction_detail.fac_actual_qty = fac_actual_qty
    deduction_detail.fac_actual_unit = fac_actual_unit
    deduction_detail.invoice_no = invoice_no
    deduction_detail.material = material
    deduction_detail.save()
    return deduction_detail


@login_required()
def accessory_deduction_add(request):
    customer = request.POST.get('customer')
    factory = request.POST.get('factory')
    mr = request.POST.get('mr')
    explain = request.POST.get('explain')
    po = request.POST.get('po')
    po_detail = request.POST.get('po_detail')
    customer_po = request.POST.get('customer_po')
    customer_item = request.POST.get('customer_item')
    product = request.POST.get('product')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    final_date = request.POST.get('final_date')
    qc1 = request.POST.get('qc1')
    pay_date = request.POST.get('pay_date')
    deduction_clear_date = request.POST.get('deduction_clear_date')
    type = request.POST.get('type')
    count = request.POST.get('count')
    deduction_amount = request.POST.get('deduction_amount')
    fac_amount = request.POST.get('fac_amount')
    currency = request.POST.get('currency')
    fac_total_amount = request.POST.get('fac_total_amount')
    invoice_no = request.POST.get('invoice_no')
    category_remark = request.POST.get('category_remark')
    dict_info = {
        'customer': customer,
        'factory': factory,
        'mr': mr,
        'explain': explain,
        'po': po,
        'po_detail': po_detail,
        'customer_po': customer_po,
        'customer_item': customer_item,
        'product': product,
        'amount': amount,
        'unit': unit,
        'final_date': final_date,
        'qc1': qc1,
        'pay_date': pay_date,
        'deduction_clear_date': deduction_clear_date,
        'type': type,
        'count': count,
        'deduction_amount': deduction_amount,
        'fac_amount': fac_amount,
        'currency': currency,
        'fac_total_amount': fac_total_amount,
        'invoice_no': invoice_no,
        'category_remark': category_remark,
    }

    accessory_deduction = Accessory_deduction.objects.get(po=po, po_detail=po_detail)
    if not accessory_deduction:
        obj = Accessory_deduction(**dict_info)
        obj.save()
        return dict_info


@login_required()
def accessory_deduction_modify(request):
    customer = request.POST.get('customer')
    factory = request.POST.get('factory')
    mr = request.POST.get('mr')
    explain = request.POST.get('explain')
    po = request.POST.get('po')
    po_detail = request.POST.get('po_detail')
    customer_po = request.POST.get('customer_po')
    customer_item = request.POST.get('customer_item')
    product = request.POST.get('product')
    amount = request.POST.get('amount')
    unit = request.POST.get('unit')
    final_date = request.POST.get('final_date')
    qc1 = request.POST.get('qc1')
    pay_date = request.POST.get('pay_date')
    deduction_clear_date = request.POST.get('deduction_clear_date')
    type = request.POST.get('type')
    count = request.POST.get('count')
    deduction_amount = request.POST.get('deduction_amount')
    fac_amount = request.POST.get('fac_amount')
    currency = request.POST.get('currency')
    fac_total_amount = request.POST.get('fac_total_amount')
    invoice_no = request.POST.get('invoice_no')
    category_remark = request.POST.get('category_remark')
    accessory_deduction = Accessory_deduction.objects.get(po=po, po_detail=po_detail)
    if accessory_deduction:
        accessory_deduction.customer = customer
        accessory_deduction.factory = factory
        accessory_deduction.mr = mr
        accessory_deduction.explain = explain
        accessory_deduction.po = po
        accessory_deduction.po_detail = po_detail
        accessory_deduction.customer_po = customer_po
        accessory_deduction.customer_item = customer_item
        accessory_deduction.product = product
        accessory_deduction.amount = amount
        accessory_deduction.unit = unit
        accessory_deduction.final_date = final_date
        accessory_deduction.qc1 = qc1
        accessory_deduction.pay_date = pay_date
        accessory_deduction.deduction_clear_date = deduction_clear_date
        accessory_deduction.type = type
        accessory_deduction.count = count
        accessory_deduction.deduction_amount = deduction_amount
        accessory_deduction.fac_amount = fac_amount
        accessory_deduction.currency = currency
        accessory_deduction.fac_total_amount = fac_total_amount
        accessory_deduction.invoice_no = invoice_no
        accessory_deduction.category_remark = category_remark
        accessory_deduction.save()
        return accessory_deduction


@login_required()
def accessory_deduction_detail_add(request):
    deduction_detail = request.POST.get('deduction_detail')
    pay_date = request.POST.get('pay_date')
    reason = request.POST.get('reason')
    count = request.POST.get('count')
    price = request.POST.get('price')
    currency = request.POST.get('currency')
    total_amount = request.POST.get('total_amount')
    deduction_no = request.POST.get('deduction_no')
    deduction_clear_date = request.POST.get('deduction_clear_date')
    dict_info = {
        'deduction_detail': deduction_detail,
        'pay_date': pay_date,
        'reason': reason,
        'count': count,
        'price': price,
        'currency': currency,
        'total_amount': total_amount,
        'deduction_no': deduction_no,
        'deduction_clear_date': deduction_clear_date,
    }
    obj = Accessory_deduction_detail(**dict_info)
    obj.save()
    return dict_info


@login_required()
def accessory_deduction_detail_modify(request):
    detail_id = request.POST.get('detail_id')
    deduction_detail = request.POST.get('deduction_detail')
    pay_date = request.POST.get('pay_date')
    reason = request.POST.get('reason')
    count = request.POST.get('count')
    price = request.POST.get('price')
    currency = request.POST.get('currency')
    total_amount = request.POST.get('total_amount')
    deduction_no = request.POST.get('deduction_no')
    deduction_clear_date = request.POST.get('deduction_clear_date')
    accessory_deduction_detail = Accessory_deduction_detail.objects.get(id=detail_id)
    if accessory_deduction_detail:
        accessory_deduction_detail.deduction_detail = deduction_detail
        accessory_deduction_detail.pay_date = pay_date
        accessory_deduction_detail.reason = reason
        accessory_deduction_detail.count = count
        accessory_deduction_detail.price = price
        accessory_deduction_detail.currency = currency
        accessory_deduction_detail.total_amount = total_amount
        accessory_deduction_detail.deduction_no = deduction_no
        accessory_deduction_detail.deduction_clear_date = deduction_clear_date
        accessory_deduction_detail.save()
        return accessory_deduction_detail
