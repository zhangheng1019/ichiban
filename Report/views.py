# -*- encoding: utf-8 -*-
from django.shortcuts import render
import xlwt
import os
from io import BytesIO
import datetime
from Order.query_API import *
from Finance.query_API import *
from Basic_info.models import *
from Order.models import *
from Finance.models import *
from apple.views import *
from win32com import client
# Create your views here.


# ================================== 表格样式 ==================================
# -------------------------- 标题抬头样式
# 标题抬头字体
font1 = xlwt.Font()
# 字体类型
font1.name = '宋体'
# 字体大小，18为字号，20为衡量单位
font1.height = 20 * 18
# 字体加粗
font1.bold = True
# 下划线
font1.underline = False
# 斜体字
font1.italic = False
# ------------------- 对齐方式设置 -------------------
# -----------------居中对齐，18号宋体-------------------
# 单元格对齐方式
alignment1 = xlwt.Alignment()
# 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
alignment1.horz = 0x02  # 水平方向
# 0x00(上端对齐)、0x01(垂直方向上居中对齐)、0x02(底端对齐)
alignment1.vert = 0x01  # 垂直方向
# 设置自动换行
alignment1.wrap = 1

title_style = xlwt.XFStyle()
title_style.font = font1
title_style.alignment = alignment1
# ---------------左对齐，8号宋体-------------------
# 正文字体设置
font2 = xlwt.Font()
font2.name = '宋体'
font2.height = 20 * 11
font2.bold = False

alignment2 = xlwt.Alignment()
alignment2.horz = 0x01
alignment2.vert = 0x01
# 设置自动换行
alignment2.wrap = 1

# borders = xlwt.Borders()
# 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
# 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
# ----------------------- 边框设置 ----------------------
border_t = xlwt.Borders()  # 上边框
border_t.top = 1
border_r = xlwt.Borders()  # 右边框
border_r.right = 1
border_b = xlwt.Borders()  # 下边框
border_b.bottom = 1
border_l = xlwt.Borders()  # 左边框
border_l.left = 1
border_tl = xlwt.Borders()  # 上左边框
border_tl.top = 1
border_tl.left = 1
border_bl = xlwt.Borders()  # 下左边框
border_bl.bottom = 1
border_bl.left = 1
border_tr = xlwt.Borders()  # 上右边框
border_tr.top = 1
border_tr.right = 1
border_br = xlwt.Borders()  # 下右边框
border_br.bottom = 1
border_br.right = 1
border_lr = xlwt.Borders()  # 左右边框
border_lr.left = 1
border_lr.right = 1
border_tlr = xlwt.Borders()  # 上左右边框
border_tlr.top = 1
border_tlr.left = 1
border_tlr.right = 1
border_blr = xlwt.Borders()  # 下左右边框
border_blr.bottom = 1
border_blr.left = 1
border_blr.right = 1
border_all = xlwt.Borders()  # 全边框
border_all.left = 1
border_all.right = 1
border_all.top = 1
border_all.bottom = 1


# 上边框
top_border = xlwt.XFStyle()
top_border.font = font2
top_border.alignment = alignment2
top_border.borders = border_t
# 右边框
right_border = xlwt.XFStyle()
right_border.font = font2
right_border.alignment = alignment2
right_border.borders = border_r
# 下边框
bottom_border = xlwt.XFStyle()
bottom_border.font = font2
bottom_border.alignment = alignment2
bottom_border.borders = border_b
# 左边框
left_border = xlwt.XFStyle()
left_border.font = font2
left_border.alignment = alignment2
left_border.borders = border_l
# 上左边框
top_left_border = xlwt.XFStyle()
top_left_border.font = font2
top_left_border.alignment = alignment2
top_left_border.borders = border_tl
# 上右边框
top_right_border = xlwt.XFStyle()
top_right_border.font = font2
top_right_border.alignment = alignment2
top_right_border.borders = border_tr
# 下左边框
bottom_left_border = xlwt.XFStyle()
bottom_left_border.font = font2
bottom_left_border.alignment = alignment2
bottom_left_border.borders = border_bl
# 下右边框
bottom_right_border = xlwt.XFStyle()
bottom_right_border.font = font2
bottom_right_border.alignment = alignment2
bottom_right_border.borders = border_br
# 左右边框
left_right_border = xlwt.XFStyle()
left_right_border.font = font2
left_right_border.alignment = alignment2
left_right_border.borders = border_lr
# 上左右边框
top_left_right_border = xlwt.XFStyle()
top_left_right_border.font = font2
top_left_right_border.alignment = alignment2
top_left_right_border.borders = border_tlr
# 下左右边框
bottom_left_right_border = xlwt.XFStyle()
bottom_left_right_border.font = font2
bottom_left_right_border.alignment = alignment2
bottom_left_right_border.borders = border_blr
# 无边框
body_style = xlwt.XFStyle()
body_style.font = font2
body_style.alignment = alignment2
# 全边框
all_border = xlwt.XFStyle()
all_border.font = font2
all_border.alignment = alignment2
all_border.borders = border_all
# ==============================表格样式===============================


# 导出大货付款付款通知 -- ok
@login_required()
def pay_notice(request):

    if request.method == 'GET':
        data = basic_info_json(('Company', 'Currency'))
        return render(request, 'report/pay_notice.html', locals())
    invoice_list = request.POST.get('invoice_list')
    company = request.POST.get('company')
    currency = request.POST.get('currency')
    invoice_list = invoice_list.split(',')

    if not invoice_list:
        return JsonResponse({'status': 'fail', 'msg': '发票列表无数据'})
    # 创建表格
    book = xlwt.Workbook(encoding='utf-8')
    for invoice in invoice_list:
        sheet = book.add_sheet('%s' % invoice, cell_overwrite_ok=True)
        # 设置页眉页脚
        sheet.show_headers = True
        sheet.header_str = b''
        sheet.footer_str = b''
        # 设置列宽度
        for i in range(14):
            sheet.col(i).width = 7 * 256
        # 设置行高
        sheet.row(1).set_style(xlwt.easyxf('font:height 720'))  # 36pt的行高
        # 通过发票信息找到所有大货付款条目
        ship_payment = Ship_payment.objects.filter(invoice_no=invoice)
        if not ship_payment:
            return JsonResponse({'status': 'fail', 'msg': 'Po不存在'})
        # 获取工厂对象信息
        factory = Contract.objects.get(po=ship_payment[0].po, item_no=ship_payment[0].po_detail).factory
        # 根据工厂对象信息获取所有索赔条目
        claim_payment = Claim_payment.objects.filter(factory=factory)
        # 根据工厂对象信息获取所有合同条目
        contract = Contract.objects.filter(factory=factory)
        # 根据工厂对象信息获取所有消出货条目
        # product_send = Product_send.objects.filter(po=contract[0].po, item_no=contract[0].item_no)  # sale_date

        # 订单主体
        sheet.write_merge(7, 7, 0, 1, u'订单号码', bottom_border)
        sheet.write_merge(7, 7, 2, 3, u'ITEM#', bottom_border)
        sheet.write_merge(7, 7, 4, 5, u'出货日期', bottom_border)
        sheet.write_merge(7, 7, 6, 6, u'货币', bottom_border)
        sheet.write_merge(7, 7, 7, 8, u'金额', bottom_border)
        sheet.write_merge(7, 7, 9, 11, u'厂商', bottom_border)
        sheet.write_merge(7, 7, 12, 13, u'备注', bottom_border)

        j = 8
        sum_con = 0
        for i in contract:
            date = Product_send.objects.get(po=i.po, item_no=i.item_no).sale_date  # 消出货日期
            sheet.write_merge(j, j, 0, 1, i.po, body_style)
            sheet.write_merge(j, j, 2, 3, i.item_no, body_style)
            sheet.write_merge(j, j, 4, 5, date, body_style)
            sheet.write_merge(j, j, 6, 6, i.fac_currency.code, body_style)
            sheet.write_merge(j, j, 7, 8, format(float(i.fac_total), ','), body_style)
            sheet.write_merge(j, j, 9, 11, i.factory.name, body_style)
            sheet.write_merge(j, j, 12, 13, u'', body_style)
            j += 1
            sum_con += float(i.fac_total)
        sheet.write_merge(j, j, 0, 13, u'共计%s%s' % (contract[0].fac_currency, format(round(sum_con, 3), ',')), body_style)
        # 构建扣款明细主体
        sheet.write_merge(j + 2, j + 2, 0, 13, u'扣款明细', top_left_right_border)

        sheet.write_merge(j + 3, j + 3, 0, 0, u'Po_id', bottom_left_border)
        sheet.write_merge(j + 3, j + 3, 1, 4, u'厂商', bottom_border)
        sheet.write_merge(j + 3, j + 3, 5, 6, u'订单号码', bottom_border)
        sheet.write_merge(j + 3, j + 3, 7, 7, u'货币', bottom_border)
        sheet.write_merge(j + 3, j + 3, 8, 9, u'扣款金额', bottom_border)
        sheet.write_merge(j + 3, j + 3, 10, 13, u'备注', bottom_right_border)
        k = j + 4
        sum_c = 0
        # 遍历数据
        for i in claim_payment:
            po_detail = Po_detail.objects.get(po=i.po, item_no=i.po_detail)
            sheet.write_merge(k, k, 0, 0, po_detail.id, left_border)
            sheet.write_merge(k, k, 1, 4, i.factory, body_style)
            sheet.write_merge(k, k, 5, 6, i.customer_po, body_style)
            sheet.write_merge(k, k, 7, 7, i.deduction_currency.code, body_style)
            sheet.write_merge(k, k, 8, 9, format(float(i.deduction_amount), ','), body_style)
            sheet.write_merge(k, k, 10, 13, i.claim_remark, right_border)
            k += 1
            sum_c += float(i.deduction_amount)
        sheet.write_merge(k, k, 0, 13, u'共计 %s%s' % (claim_payment[0].deduction_currency, format(round(sum_c, 3), ',')), left_right_border)
        sheet.write_merge(k + 1, k + 1, 0, 13, u'注：如需所有扣款明细，请向我司业务部各负责人员查询。', bottom_left_right_border)
        # 签名栏
        sheet.write_merge(54, 54, 0, 0, u'承办员', body_style)
        sheet.write_merge(54, 54, 1, 2, u'', bottom_border)
        sheet.write_merge(54, 54, 3, 3, u'科长', body_style)
        sheet.write_merge(54, 54, 4, 6, u'', bottom_border)
        sheet.write_merge(54, 54, 7, 7, u'财务', body_style)
        sheet.write_merge(54, 54, 8, 9, u'', bottom_border)
        sheet.write_merge(54, 54, 10, 10, u'经理', body_style)
        sheet.write_merge(54, 54, 11, 13, u'', bottom_border)
        # 抬头
        sheet.write_merge(0, 0, 0, 13, u'%s.  付款通知' % company, title_style)
        text = '''敬启者 %s
          您好，以下为贵公司最近所传发票请款的明细。敝司已经将结算后的金额汇款到以下所指定的银行账户，请查收。若有问题请马上告知。''' % ship_payment[0].factory
        sheet.write_merge(1, 1, 0, 13, text, body_style)
        # 款项信息主体
        i = ship_payment[0]
        sheet.write_merge(2, 2, 0, 1, u'户口抬头', body_style)
        sheet.write_merge(2, 2, 2, 13, i.title, body_style)
        sheet.write_merge(3, 3, 0, 1, u'发票号码', body_style)
        sheet.write_merge(3, 3, 2, 8, i.invoice_no, body_style)
        sheet.write_merge(3, 3, 9, 10, u'总金额', body_style)
        sheet.write_merge(3, 3, 11, 13, u'%s%s' % (i.fac_cost_currency, format(float(sum_c + sum_con), ',')), body_style)
        sheet.write_merge(4, 4, 0, 1, u'户口号码', body_style)
        sheet.write_merge(4, 4, 2, 8, i.account_no, body_style)
        sheet.write_merge(4, 4, 9, 10, u'应付金额', body_style)
        sheet.write_merge(4, 4, 11, 13, u'%s%s' % (i.fac_cost_currency, format(float(sum_c + sum_con), ',')), body_style)
        sheet.write_merge(5, 5, 0, 1, u'银行', body_style)
        sheet.write_merge(5, 5, 2, 13, i.bank, body_style)
    # 导出报表
    ############################
    # exist_file = os.path.exists("test.xls")
    # if exist_file:
    #     os.remove(r"test.xls")
    # book.save("test.xls")
    ############################
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response.write(sio.getvalue())
    return response


# 导出材料付款付款通知 -- ok
@login_required()
def material_pay(request):
    if request.method == 'GET':
        data = basic_info_json(('Company', 'Currency'))
        return render(request, 'report/pay_notice.html', locals())
    invoice_list = request.POST.get('invoice_list')
    company = request.POST.get('company')
    currency = request.POST.get('currency')
    invoice_list = invoice_list.split(',')

    if not invoice_list:
        return JsonResponse({'status': 'fail', 'msg': '发票列表无数据'})
    # 创建表格
    book = xlwt.Workbook(encoding='utf-8')
    for invoice in invoice_list:
        sheet = book.add_sheet('%s' % invoice, cell_overwrite_ok=True)
        # 设置页眉页脚
        sheet.show_headers = True
        sheet.header_str = b''
        sheet.footer_str = b''
        # 设置列宽度
        for i in range(14):
            sheet.col(i).width = 7 * 256
        # 设置行高
        sheet.row(1).set_style(xlwt.easyxf('font:height 720'))  # 36pt的行高
        # 通过发票信息找到所有材料付款条目
        accessory_pay = Accessory_pay.objects.filter(invoice_no=invoice)
        if not accessory_pay:
            return JsonResponse({'status': 'fail', 'msg': 'Po不存在'})
        # 获取工厂对象信息
        factory = Contract.objects.get(po=accessory_pay[0].po, item_no=accessory_pay[0].po_detail).factory
        # 根据工厂对象信息获取所有索赔条目
        claim_payment = Claim_payment.objects.filter(factory=factory)
        # 根据工厂对象信息获取所有合同条目
        contract = Contract.objects.filter(factory=factory)

        # 订单主体
        sheet.write_merge(7, 7, 0, 1, u'订单号码', bottom_border)
        sheet.write_merge(7, 7, 2, 3, u'ITEM#', bottom_border)
        sheet.write_merge(7, 7, 4, 5, u'出货日期', bottom_border)
        sheet.write_merge(7, 7, 6, 6, u'货币', bottom_border)
        sheet.write_merge(7, 7, 7, 8, u'金额', bottom_border)
        sheet.write_merge(7, 7, 9, 11, u'厂商', bottom_border)
        sheet.write_merge(7, 7, 12, 13, u'备注', bottom_border)

        j = 8
        sum_acc = 0
        for i in accessory_pay:
            sheet.write_merge(j, j, 0, 1, i.po, body_style)
            sheet.write_merge(j, j, 2, 3, i.po_detail, body_style)
            sheet.write_merge(j, j, 4, 5, i.sale_date, body_style)
            sheet.write_merge(j, j, 6, 6, i.currency, body_style)
            sheet.write_merge(j, j, 7, 8, format(float(i.accessory_cost_total), ','), body_style)
            sheet.write_merge(j, j, 9, 11, i.factory, body_style)
            sheet.write_merge(j, j, 12, 13, u'', body_style)
            j += 1
            sum_acc += float(i.accessory_cost_total)
        sheet.write_merge(j, j, 0, 13, u'共计%s%s' % (accessory_pay[0].currency, format(round(sum_acc, 3), ',')), body_style)
        # 构建扣款明细主体
        sheet.write_merge(j + 2, j + 2, 0, 13, u'扣款明细', top_left_right_border)

        sheet.write_merge(j + 3, j + 3, 0, 0, u'Po_id', bottom_left_border)
        sheet.write_merge(j + 3, j + 3, 1, 4, u'厂商', bottom_border)
        sheet.write_merge(j + 3, j + 3, 5, 6, u'订单号码', bottom_border)
        sheet.write_merge(j + 3, j + 3, 7, 7, u'货币', bottom_border)
        sheet.write_merge(j + 3, j + 3, 8, 9, u'扣款金额', bottom_border)
        sheet.write_merge(j + 3, j + 3, 10, 13, u'备注', bottom_right_border)
        k = j + 4
        sum_c = 0
        # 遍历数据
        for i in claim_payment:
            po_detail = Po_detail.objects.get(po=i.po, item_no=i.po_detail)
            sheet.write_merge(k, k, 0, 0, po_detail.id, left_border)
            sheet.write_merge(k, k, 1, 4, i.factory, body_style)
            sheet.write_merge(k, k, 5, 6, i.customer_po, body_style)
            sheet.write_merge(k, k, 7, 7, i.deduction_currency.code, body_style)
            sheet.write_merge(k, k, 8, 9, format(float(i.deduction_amount), ','), body_style)
            sheet.write_merge(k, k, 10, 13, i.claim_remark, right_border)
            k += 1
            sum_c += float(i.deduction_amount)
        sheet.write_merge(k, k, 0, 13, u'共计 %s%s' % (claim_payment[0].deduction_currency, format(round(sum_c, 3), ',')), left_right_border)
        sheet.write_merge(k + 1, k + 1, 0, 13, u'注：如需所有扣款明细，请向我司业务部各负责人员查询。', bottom_left_right_border)
        # 签名栏
        sheet.write_merge(54, 54, 0, 0, u'承办员', body_style)
        sheet.write_merge(54, 54, 1, 2, u'', bottom_border)
        sheet.write_merge(54, 54, 3, 3, u'科长', body_style)
        sheet.write_merge(54, 54, 4, 6, u'', bottom_border)
        sheet.write_merge(54, 54, 7, 7, u'财务', body_style)
        sheet.write_merge(54, 54, 8, 9, u'', bottom_border)
        sheet.write_merge(54, 54, 10, 10, u'经理', body_style)
        sheet.write_merge(54, 54, 11, 13, u'', bottom_border)
        # 抬头
        sheet.write_merge(0, 0, 0, 13, u'%s.  付款通知' % company, title_style)
        text = '''敬启者 %s
          您好，以下为贵公司最近所传发票请款的明细。敝司已经将结算后的金额汇款到以下所指定的银行账户，请查收。若有问题请马上告知。''' % accessory_pay[0].factory
        sheet.write_merge(1, 1, 0, 13, text, body_style)
        # 款项信息主体
        i = accessory_pay[0]
        sheet.write_merge(2, 2, 0, 1, u'户口抬头', body_style)
        sheet.write_merge(2, 2, 2, 13, i.title, body_style)
        sheet.write_merge(3, 3, 0, 1, u'发票号码', body_style)
        sheet.write_merge(3, 3, 2, 8, i.invoice_no, body_style)
        sheet.write_merge(3, 3, 9, 10, u'总金额', body_style)
        sheet.write_merge(3, 3, 11, 13, u'%s%s' % (i.pay_currency, format(float(sum_c + sum_acc), ',')), body_style)
        sheet.write_merge(4, 4, 0, 1, u'户口号码', body_style)
        sheet.write_merge(4, 4, 2, 8, i.account_no, body_style)
        sheet.write_merge(4, 4, 9, 10, u'应付金额', body_style)
        sheet.write_merge(4, 4, 11, 13, u'%s%s' % (i.pay_currency, format(float(sum_c + sum_acc), ',')), body_style)
        sheet.write_merge(5, 5, 0, 1, u'银行', body_style)
        sheet.write_merge(5, 5, 2, 13, i.bank, body_style)
    # 导出报表
    ############################
    # exist_file = os.path.exists("配件付款通知.xls")
    # if exist_file:
    #     os.remove(r"配件付款通知.xls")
    # book.save("配件付款通知.xls")
    ############################
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response.write(sio.getvalue())
    return response


# 核对发票明细 -- ok
@login_required()
def check_invoice(request):
    if request.method == 'GET':
        data = basic_info_json(('Company', 'Currency'))
        return render(request, 'report/check_invoice.html', locals())
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    if start_date >= end_date:
        return JsonResponse({'status': 'fail', 'msg': '起始日期不能在结束日期后面'})
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
    # 设置页眉页脚
    sheet.show_headers = True
    sheet.header_str = b''
    sheet.footer_str = b''
    for i in range(14):
        sheet.col(i).width = 7 * 256
    # 抬头
    sheet.write_merge(0, 0, 0, 11, u'核对发票明细表', title_style)
    sheet.write_merge(2, 2, 0, 1, u'出货时间：', body_style)
    sheet.write_merge(2, 2, 2, 6, u'%s 至 %s' % (start_date, end_date), body_style)
    sheet.write_merge(2, 2, 7, 8, u'付款时间：', body_style)
    sheet.write_merge(2, 2, 9, 11, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), body_style)
    # 主体内容
    sheet.write_merge(4, 4, 0, 3, u'工厂', bottom_border)
    sheet.write_merge(4, 4, 4, 5, u'P.O.NO.', bottom_border)
    sheet.write_merge(4, 4, 6, 7, u'金额', bottom_border)
    sheet.write_merge(4, 4, 8, 8, u'单位', bottom_border)
    sheet.write_merge(4, 4, 9, 10, u'已收发票金额', bottom_border)
    sheet.write_merge(4, 4, 11, 11, u'备注', bottom_border)

    product_send = Product_send.objects.filter(sale_date__gt=start_date, sale_date__lt=end_date)
    total = 0
    row = 4
    for i in product_send:
        row += 1
        contract = Contract.objects.get(po=i.po, item_no=i.item_no)
        sheet.write_merge(row, row, 0, 3, contract.factory.name, bottom_border)
        sheet.write_merge(row, row, 4, 5, i.po, bottom_border)
        sheet.write_merge(row, row, 6, 7, contract.fac_total, bottom_border)
        sheet.write_merge(row, row, 8, 8, contract.fac_currency.code, bottom_border)
        sheet.write_merge(row, row, 9, 10, u'', bottom_border)
        sheet.write_merge(row, row, 11, 11, u'', bottom_border)
        total += float(contract.fac_total)
    sheet.write_merge(row + 1, row + 1, 6, 8, u'合计：%s' % round(total, 2), body_style)
    # 导出报表
    ############################
    # exist_file = os.path.exists("test.xls")
    # if exist_file:
    #     os.remove(r"test.xls")
    # book.save("test.xls")
    ############################
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response.write(sio.getvalue())
    return response


# 导出利润报表 --- ok
@login_required()
def profit_report(request):
    if request.method == 'GET':
        data = {}
        data['po'] = field_list('Po', 'order_number')
        return render(request, 'report/profit_report.html', locals())
    order_number = request.POST.get('order_number')
    send_to = request.POST.get('send_to')
    # 创建表格
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
    # 设置页眉页脚
    sheet.show_headers = True
    sheet.header_str = b''
    sheet.footer_str = b''
    # 设置列宽度
    for i in range(16):
        sheet.col(i).width = 8 * 256

    po = Po.objects.filter(order_number=order_number)
    if not po:
        return JsonResponse({'status': 'fail', 'msg': 'Po不存在'})
    po = po[0]
    po_detail = Po_detail.objects.filter(po=po.order_number)
    # po信息
    title_row = 0  # 表的初始行
    sheet.write_merge(title_row, title_row, 0, 2, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), body_style)
    sheet.write_merge(title_row, title_row, 3, 14, u'ORDER CONFIRMATION & PROFIT REPORT BY PO', title_style)
    # --
    sheet.write_merge(title_row + 1, title_row + 1, 0, 3, u'EWB PO#：%s' % po.order_number, body_style)
    sheet.write_merge(title_row + 1, title_row + 1, 4, 7, u'FOB：%s' % po.port.name, body_style)
    sheet.write_merge(title_row + 1, title_row + 1, 8, 12, u'Payment：%s' % po.pay_type, body_style)
    # --
    sheet.write_merge(title_row + 2, title_row + 2, 0, 3, u'Customer PO#：%s' % po.customer_pono, body_style)  # 客人PO
    sheet.write_merge(title_row + 2, title_row + 2, 4, 7, u'Customer del：%s' % po.cus_receive_date, body_style)  # 客人收货日期
    sheet.write_merge(title_row + 2, title_row + 2, 8, 12, u'Scheduled ship date：%s' % po.fac_send_date, body_style)  # 工厂交货日期
    # 表头栏
    sheet.write_merge(title_row + 3, title_row + 3, 0, 1, u'Item#', top_border)  # item号
    sheet.write_merge(title_row + 3, title_row + 3, 2, 4, u'DESCRITION', top_border)  # 描述
    sheet.write_merge(title_row + 3, title_row + 3, 5, 5, u'Vendor', top_border)  # 工厂代码
    sheet.write_merge(title_row + 3, title_row + 3, 6, 6, u'FOB', top_border)  # 出货条件
    sheet.write_merge(title_row + 3, title_row + 3, 7, 7, u'Q’TY', top_border)  # 工厂数量
    sheet.write_merge(title_row + 3, title_row + 3, 8, 8, u'FacCost', top_border)  # 工厂价格
    sheet.write_merge(title_row + 3, title_row + 3, 9, 10, u'OtherCost', top_border)  # 材料签收明细中所有单价之和
    sheet.write_merge(title_row + 3, title_row + 3, 11, 11, u'LA(8%)', top_border)
    sheet.write_merge(title_row + 3, title_row + 3, 12, 12, u'FinalCost', top_border)  # 最终价格
    sheet.write_merge(title_row + 3, title_row + 3, 13, 13, u'Selling', top_border)  # 客人要价
    sheet.write_merge(title_row + 3, title_row + 3, 14, 14, u'GP', top_border)  # 利润
    sheet.write_merge(title_row + 3, title_row + 3, 15, 15, u'GM', top_border)  # 利润比
    sheet.write_merge(title_row + 3, title_row + 3, 16, 16, u'MU', top_border)  # 客人要价 / 最终价格
    # 表的主体信息
    text_row = title_row + 3
    amount_sum = cost_sum = gp_sum = 0  # 初始化  客人要价合计、成本合计、利润合计
    for i in po_detail:
        po = Po.objects.get(order_number=i.po)
        contract = Contract.objects.get(po=i.po, item_no=i.item_no)
        material_sign_detail = Material_sign_detail.objects.filter(po=i.po, item_no=i.item_no)  # 材料签收明细
        mat_accessory_cost_sum = sum([float(j.accessory_cost) for j in material_sign_detail])  # 材料签收明细中所有单价之和
        text_row += 1
        sheet.write_merge(text_row, text_row, 0, 1, i.item_no, body_style)  # item号
        sheet.write_merge(text_row, text_row, 2, 4, i.edesc, body_style)  # 描述
        sheet.write_merge(text_row, text_row, 5, 5, contract.factory.code, body_style)  # 工厂代码
        sheet.write_merge(text_row, text_row, 6, 6, po.delivery_condition.code, body_style)  # 出货条件
        sheet.write_merge(text_row, text_row, 7, 7, u'%s EA' % format(float(i.amount), ','), body_style)  # 工厂数量
        sheet.write_merge(text_row, text_row, 8, 8, u'$%s' % format(float(contract.fac_cost), ','), body_style)  # 工厂价格
        sheet.write_merge(text_row, text_row, 9, 10, u'$%s' % format(float(mat_accessory_cost_sum), ','), body_style)  # 材料签收明细中所有单价之和
        sheet.write_merge(text_row, text_row, 11, 11, u'$0.000', body_style)  # LA(8%)
        final_cost = float(contract.fac_cost) + float(mat_accessory_cost_sum)  # 最终价格
        # final_cost = 5  # 最终价格
        sheet.write_merge(text_row, text_row, 12, 12, u'$%s' % format(round(float(final_cost), 3), ','), body_style)  # 最终价格
        sheet.write_merge(text_row, text_row, 13, 13, u'$%s' % format(float(i.costrate), ','), body_style)  # 客人要价
        gp = float(format(float(i.costrate) - final_cost, ','))  # 利润
        sheet.write_merge(text_row, text_row, 14, 14, u'$%s' % format(round(float(gp), 3), ','), body_style)  # 利润
        gm = format(gp / float(i.costrate), '.2%')  # 利润比
        sheet.write_merge(text_row, text_row, 15, 15, gm, body_style)  # 利润比
        mu = float(i.costrate) / final_cost  # 客人要价 / 最终价格
        sheet.write_merge(text_row, text_row, 16, 16, format(round(float(mu), 2), ','), body_style)  # 客人要价 / 最终价格
        amount_sum += float(i.amount) * float(i.costrate)
        cost_sum += float(i.amount) * float(final_cost)
        gp_sum += gp
    # 表的签名行
    extra_row = text_row + 1  # 信息行
    sheet.write_merge(extra_row, extra_row, 0, 8, u'US office:', top_border)
    sheet.write_merge(extra_row, extra_row, 9, 16, u'SZ Manager:', top_border)
    # 表的合计信息
    sheet.write_merge(extra_row + 2, extra_row + 2, 6, 8, u'Total  order  amount:', body_style)
    sheet.write_merge(extra_row + 2, extra_row + 2, 9, 11, u'$%s' % format(round(float(amount_sum), 3), ','), bottom_border)
    sheet.write_merge(extra_row + 3, extra_row + 3, 6, 8, u'Total  cost:', body_style)
    sheet.write_merge(extra_row + 3, extra_row + 3, 9, 11, u'$%s' % format(round(float(cost_sum), 3), ','), bottom_border)
    sheet.write_merge(extra_row + 4, extra_row + 4, 6, 8, u'Total  gross:', body_style)
    sheet.write_merge(extra_row + 4, extra_row + 4, 9, 11, u'$%s' % format(round(float(gp_sum), 3), ','), bottom_border)
    gross_margin = (float(amount_sum) - float(cost_sum)) / float(amount_sum)  # 利润比例
    sheet.write_merge(extra_row + 5, extra_row + 5, 1, 8, u'Gross  margin  (calculated  from  selling  price):', body_style)
    sheet.write_merge(extra_row + 5, extra_row + 5, 9, 11, format(gross_margin, '.2%'), bottom_border)
    # 表的最终签名行
    # 表头行
    sheet.write_merge(extra_row + 7, extra_row + 7, 1, 1, u'', top_left_border)
    sheet.write_merge(extra_row + 7, extra_row + 7, 2, 4, u'Sales agent', top_border)
    sheet.write_merge(extra_row + 7, extra_row + 7, 5, 5, u'', top_border)
    sheet.write_merge(extra_row + 7, extra_row + 7, 6, 8, u'Commission', top_border)
    sheet.write_merge(extra_row + 7, extra_row + 7, 9, 9, u'', top_border)
    sheet.write_merge(extra_row + 7, extra_row + 7, 10, 12, u'Commission amount', top_border)
    sheet.write_merge(extra_row + 7, extra_row + 7, 13, 15, u'', top_right_border)
    # 签名第一行
    sheet.write_merge(extra_row + 8, extra_row + 8, 1, 1,  u'1.', left_border)
    sheet.write_merge(extra_row + 8, extra_row + 8, 2, 4,  u'', bottom_border)
    sheet.write_merge(extra_row + 8, extra_row + 8, 6, 8,  u'', bottom_border)
    sheet.write_merge(extra_row + 8, extra_row + 8, 10, 12, u'', bottom_border)
    sheet.write_merge(extra_row + 8, extra_row + 8, 13, 15, u'', right_border)
    # 签名第二行
    sheet.write_merge(extra_row + 9, extra_row + 9, 1, 1,  u'2.', left_border)
    sheet.write_merge(extra_row + 9, extra_row + 9, 2, 4,  u'', bottom_border)
    sheet.write_merge(extra_row + 9, extra_row + 9, 6, 8,  u'', bottom_border)
    sheet.write_merge(extra_row + 9, extra_row + 9, 10, 12, u'', bottom_border)
    sheet.write_merge(extra_row + 9, extra_row + 9, 13, 15, u'', right_border)
    # 说明行
    text = 'If there is EWB profit split item or any sales agent commission,please fax to HK Kamily for calculation.'
    sheet.write_merge(extra_row + 10, extra_row + 10, 1, 15, text, bottom_left_right_border)
    # 导出报表
    ############################
    # exist_file = os.path.exists("test.xls")
    # if exist_file:
    #     os.remove(r"test.xls")
    # book.save("test.xls")
    ############################
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response.write(sio.getvalue())
    return response


# 根据输入po_detail的id导出主合同 -- ok
@login_required()
def contract_report_by_id(request):
    if request.method == 'GET':
        return render(request, 'report/contract_report.html', locals())
    action = request.POST.get('action')
    if action == 'list':  # 不连续detail id
        detail_id_list = request.POST.get('detail_id_list')  # 获取po_detail的id列表
        detail_id_list = detail_id_list.split(',')
    else:  # 给定范围的连续detail_id
        start_id = request.POST.get('start_id')
        end_id = request.POST.get('end_id')
        detail_id_list = [i for i in range(int(start_id), int(end_id) + 1)]

    # 正文字体不加粗设置
    font3 = xlwt.Font()
    font3.name = '宋体'
    font3.height = 20 * 11
    font3.bold = False
    # 正文字体加粗设置
    font4 = xlwt.Font()
    font4.name = '宋体'
    font4.height = 20 * 11
    font4.bold = True
    # ---------------右对齐方式--------------
    alignment_r = xlwt.Alignment()
    alignment_r.horz = 0x03  # 水平方向右对齐
    alignment_r.vert = 0x01  # 垂直方向居中对齐
    # 设置自动换行
    alignment2.wrap = 1
    body_right_style = xlwt.XFStyle()
    body_right_style.font = font3
    body_right_style.alignment = alignment_r
    # ---------------设置边框--------------
    border1 = xlwt.Borders()  # 下边框
    border1.bottom = 4  # 虚线边框
    bottom_border = xlwt.XFStyle()
    bottom_border.font = font3
    bottom_border.alignment = alignment2
    bottom_border.borders = border1
    # -------------------------------------
    # 获取所有的工厂信息，根据工厂分类导出合同
    factory_list = []  # 存储工厂对象
    item_list = []
    for i in detail_id_list:
        try:
            po_detail = Po_detail.objects.get(id=int(i))
        except:
            return JsonResponse({'status': 'fail', 'msg': 'id %s 不存在' % i})
        item_list.append(po_detail.item_no)
        factory = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no).factory
        if factory not in factory_list:
            factory_list.append(factory)
    # 写入数据
    text_row = 3
    order_number = Po_detail.objects.get(id=int(detail_id_list[0])).po
    po = Po.objects.get(order_number=order_number)
    # 循环获取po下的所有工厂
    # 创建表格
    book = xlwt.Workbook(encoding='utf-8')
    for i in factory_list:
        # 每一个工厂建立一个sheet
        sheet = book.add_sheet('sheet%s' % factory_list.index(i), cell_overwrite_ok=True)
        # 设置页眉页脚
        sheet.show_headers = True
        sheet.header_str = b''
        sheet.footer_str = b''
        # 设置列宽度
        for x in range(16):
            sheet.col(x).width = 8 * 256
        body_style.font = font3
        # 写入合同信息
        sheet.write_merge(text_row, text_row, 0, 4, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), body_style)
        sheet.write_merge(text_row + 1, text_row + 1, 2, 4, po.order_number, body_style)
        sheet.write_merge(text_row + 1, text_row + 1, 6, 9, i.name, body_style)  # 工厂name
        sheet.write_merge(text_row + 3, text_row + 3, 2, 4, po.customer_pono, body_style)
        sheet.write_merge(text_row + 3, text_row + 3, 6, 9, i.tel, body_style)  # 工厂tel
        sheet.write_merge(text_row + 5, text_row + 5, 2, 4, po.receive_date, body_style)
        sheet.write_merge(text_row + 5, text_row + 5, 6, 9, i.fax, body_style)  # 工厂fax
        sheet.write_merge(text_row + 7, text_row + 7, 2, 4, po.fac_send_date, body_style)
        sheet.write_merge(text_row + 7, text_row + 7, 6, 9, i.city, body_style)  # 工厂city
        try:
            sheet.write_merge(text_row + 9, text_row + 9, 2, 4, po.delivery_condition.code, body_style)
        except:
            sheet.write_merge(text_row + 9, text_row + 9, 2, 4, '', body_style)
        sheet.write_merge(text_row + 9, text_row + 9, 6, 9, i.street, body_style)  # 工厂street
        # 写入订单信息
        order_row = text_row + 13
        # 获取当前po下某个工厂下的所有合同
        contracts = Contract.objects.filter(item_no__in=item_list, factory=i)
        amount_sum = fac_total_sum = 0
        for contract in contracts:
            po_detail = Po_detail.objects.get(po=contract.po, item_no=contract.item_no)
            # 第一行
            sheet.write_merge(order_row, order_row, 0, 2, u'工厂货号:', body_style)
            sheet.write_merge(order_row, order_row, 3, 5, po_detail.desc, body_style)
            # 第二行
            sheet.write_merge(order_row + 1, order_row + 1, 0, 2, po_detail.fac_no, body_style)
            sheet.write_merge(order_row + 1, order_row + 1, 3, 5, u'每只产品包装:', body_style)
            sheet.write_merge(order_row + 1, order_row + 1, 6, 7, contract.amount, body_right_style)
            sheet.write_merge(order_row + 1, order_row + 1, 8, 9, contract.fac_cost, body_right_style)
            sheet.write_merge(order_row + 1, order_row + 1, 10, 11, contract.fac_total, body_right_style)
            # 第三行
            sheet.write_merge(order_row + 2, order_row + 2, 0, 2, u'升辉货号:', body_style)
            sheet.write_merge(order_row + 2, order_row + 2, 3, 5, u'内盒数量：%s EA' % po_detail.inner_box, body_style)
            sheet.write_merge(order_row + 2, order_row + 2, 6, 7, contract.unit, body_right_style)
            sheet.write_merge(order_row + 2, order_row + 2, 8, 9, contract.fac_currency.code, body_right_style)
            sheet.write_merge(order_row + 2, order_row + 2, 10, 11, contract.fac_currency.code, body_right_style)
            # 第四行
            sheet.write_merge(order_row + 3, order_row + 3, 0, 2, po_detail.item_no, body_style)
            sheet.write_merge(order_row + 3, order_row + 3, 3, 5, u'中盒数量：%s EA' % po_detail.middle_box, body_style)
            # 第五行
            sheet.write_merge(order_row + 4, order_row + 4, 0, 2, po_detail.id, bottom_border)
            sheet.write_merge(order_row + 4, order_row + 4, 3, 6, u'外盒数量：%s EA' % po_detail.outside_box, bottom_border)
            if not po_detail.outside_box:
                ea_sum = 0
            else:
                ea_sum = float(contract.amount) / float(po_detail.outside_box)

            sheet.write_merge(order_row + 4, order_row + 4, 7, 11, u'共：%s' % round(ea_sum, 4), bottom_border)
            amount_sum += ea_sum
            fac_total_sum += float(contract.fac_total)
            order_row += 5
        # 订单最后一行合计信息
        body_style.font = font4
        sheet.write_merge(order_row, order_row, 1, 2, u'%s 件' % round(amount_sum, 4), body_style)
        sheet.write_merge(order_row, order_row, 4, 5, u'共 %s 项' % len(contracts), body_style)
        sheet.write_merge(order_row, order_row, 7, 11, u'总金额：%s%s' % (contracts[0].fac_currency.code,
                                                                      format(round(fac_total_sum, 3), ',')), body_style)
        body_style.font = font3
        # 注意事项
        try:
            omr = OMR.objects.get(po=order_number)
            sheet.write_merge(order_row + 2, 59, 0, 11, omr.special_remark, body_style)
        except:
            sheet.write_merge(order_row + 2, 59, 0, 11, u'', body_style)
    # 导出报表
    ############################
    # exist_file = os.path.exists("test.xls")
    # if exist_file:
    #     os.remove(r"test.xls")
    # book.save("test.xls")
    ############################
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response.write(sio.getvalue())
    return response


# 根据材料签收明细id导出材料签收(配件)合同 -- ok
@login_required()
def material_sign_report_by_id(request):
    if request.method == 'GET':
        return render(request, 'report/material_sign_report.html', locals())
    action = request.POST.get('action')
    if action == 'list':
        mat_detail_id_list = request.POST.get('mat_detail_id_list')  # 获取po_detail的id列表
        mat_detail_id_list = mat_detail_id_list.split(',')
    else:
        start_id = request.POST.get('start_id')
        end_id = request.POST.get('end_id')
        mat_detail_id_list = [i for i in range(int(start_id), int(end_id) + 1)]

    # 正文字体不加粗设置
    font3 = xlwt.Font()
    font3.name = '宋体'
    font3.height = 20 * 11
    font3.bold = False
    # 正文字体加粗设置
    font4 = xlwt.Font()
    font4.name = '宋体'
    font4.height = 20 * 11
    font4.bold = True
    # ---------------右对齐方式--------------
    alignment_r = xlwt.Alignment()
    alignment_r.horz = 0x03  # 水平方向右对齐
    alignment_r.vert = 0x01  # 垂直方向居中对齐
    # 设置自动换行
    alignment2.wrap = 1
    body_right_style = xlwt.XFStyle()
    body_right_style.font = font3
    body_right_style.alignment = alignment_r
    # ---------------设置边框--------------
    border1 = xlwt.Borders()  # 下边框
    border1.bottom = 4  # 虚线边框
    bottom_border = xlwt.XFStyle()
    bottom_border.font = font3
    bottom_border.alignment = alignment2
    bottom_border.borders = border1
    # -------------------------------------
    # 获取所有的工厂信息，根据工厂分类导出合同
    factory_list = []  # 存储工厂对象
    item_list = []  # 存储根据id号查出来的item号，用于过滤筛选数据
    for i in mat_detail_id_list:
        try:
            mat_sign_detail = Material_sign_detail.objects.get(id=int(i))
        except:
            return JsonResponse({'status:': 'fail', 'msg:': 'id %s 不存在' % i})
        po_detail = Po_detail.objects.get(po=mat_sign_detail.po, item_no=mat_sign_detail.item_no)
        item_list.append(po_detail.item_no)
        factory = mat_sign_detail.factory
        if factory not in factory_list:
            factory_list.append(factory)
        print('=============================factory_list:', factory_list)
    # 写入数据
    text_row = 3
    order_number = Material_sign_detail.objects.get(id=int(mat_detail_id_list[0])).po
    po = Po.objects.get(order_number=order_number)
    # 循环获取po下的所有工厂
    # 创建表格
    book = xlwt.Workbook(encoding='utf-8')
    for i in factory_list:
        # 每一个工厂创建一个sheet
        sheet = book.add_sheet('%s' % i.name, cell_overwrite_ok=True)
        # 设置页眉页脚
        sheet.show_headers = True
        sheet.header_str = b''
        sheet.footer_str = b''
        # 设置列宽度
        for x in range(16):
            sheet.col(x).width = 8 * 256
        body_style.font = font3
        # 写入合同信息
        sheet.write_merge(text_row, text_row, 0, 4, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), body_style)
        sheet.write_merge(text_row + 1, text_row + 1, 2, 4, po.order_number, body_style)
        sheet.write_merge(text_row + 1, text_row + 1, 6, 10, i.name, body_style)  # 工厂name
        sheet.write_merge(text_row + 3, text_row + 3, 2, 4, po.customer_pono, body_style)
        sheet.write_merge(text_row + 3, text_row + 3, 6, 10, i.tel, body_style)  # 工厂tel
        sheet.write_merge(text_row + 5, text_row + 5, 2, 4, u'', body_style)
        sheet.write_merge(text_row + 5, text_row + 5, 6, 10, i.fax, body_style)  # 工厂fax
        sheet.write_merge(text_row + 7, text_row + 7, 2, 4, po.fac_send_date, body_style)
        sheet.write_merge(text_row + 7, text_row + 7, 6, 10, u'', body_style)
        sheet.write_merge(text_row + 9, text_row + 9, 2, 4, u'', body_style)
        sheet.write_merge(text_row + 9, text_row + 9, 6, 10, i.street, body_style)  # 工厂street
        # 写入订单信息
        order_row = text_row + 13
        # 获取当前po下某个工厂下符合item列表的所有合同
        material_sign_details = Material_sign_detail.objects.filter(item_no__in=item_list, factory=i)
        amount_sum = material_total_sum = 0  # 计数计价合计
        for material_sign_detail in material_sign_details:
            po_detail = Po_detail.objects.get(po=material_sign_detail.po, item_no=material_sign_detail.item_no)
            # 第一行
            sheet.write_merge(order_row, order_row, 0, 2, u'客户货号:', body_style)
            sheet.write_merge(order_row, order_row, 3, 5, material_sign_detail.name, body_style)
            sheet.write_merge(order_row, order_row, 6, 7, material_sign_detail.actual_qty, body_style)
            sheet.write_merge(order_row, order_row, 8, 9, round(float(material_sign_detail.accessory_cost), 2), body_style)
            total = float(material_sign_detail.actual_qty) * float(material_sign_detail.accessory_cost)
            sheet.write_merge(order_row, order_row, 10, 11, round(total, 2), body_style)
            # 第二行
            sheet.write_merge(order_row + 1, order_row + 1, 0, 2, po_detail.customer_item, body_style)
            sheet.write_merge(order_row + 1, order_row + 1, 3, 5, u'', body_style)
            sheet.write_merge(order_row + 1, order_row + 1, 6, 7, material_sign_detail.actual_qty_unit, body_style)
            try:
                sheet.write_merge(order_row + 1, order_row + 1, 8, 9, material_sign_detail.accessory_currency.code, body_style)
            except:
                sheet.write_merge(order_row + 1, order_row + 1, 8, 9, u'', body_style)
            try:
                sheet.write_merge(order_row + 1, order_row + 1, 10, 11, material_sign_detail.accessory_total_currency.code, body_style)
            except:
                sheet.write_merge(order_row + 1, order_row + 1, 10, 11, u'', body_style)
            # 第三行
            sheet.write_merge(order_row + 2, order_row + 2, 0, 2, u'升辉货号:', body_style)
            # 第四行
            sheet.write_merge(order_row + 3, order_row + 3, 0, 2, po_detail.item_no, body_style)
            # 第五行
            sheet.write_merge(order_row + 4, order_row + 4, 0, 11, material_sign_detail.id, bottom_border)
            amount_sum += float(material_sign_detail.actual_qty)
            material_total_sum += total
            order_row += 5
        # 订单最后一行合计信息
        body_style.font = font4
        border2 = xlwt.Borders()  # 下边框
        border2.bottom = 1  # 实线边框
        bottom_border1 = xlwt.XFStyle()
        bottom_border1.font = font3
        bottom_border1.alignment = alignment2
        bottom_border1.borders = border2
        sheet.write_merge(order_row, order_row, 0, 1, u'%s 件' % round(amount_sum, 2), body_style)
        sheet.write_merge(order_row, order_row, 2, 4, u'', bottom_border1)
        sheet.write_merge(order_row, order_row, 5, 6, u'厂提供或代购或DN#', body_style)
        sheet.write_merge(order_row, order_row, 7, 8, u'', bottom_border1)
        sheet.write_merge(order_row, order_row, 9, 11, u'总金额：%s%s' % (material_sign_details[0].accessory_currency,
                                                                      format(round(material_total_sum, 2), ',')), body_style)
    # 导出报表
    # #############创建本地文件##############
    # exist_file = os.path.exists("test.xls")
    # if exist_file:
    #     os.remove(r"test.xls")
    # book.save("test.xls")
    # #############创建本地文件##############
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response.write(sio.getvalue())
    return response


# 订单信息确认 -- ok
@login_required()
def order_confirmation(request):
    if request.method == 'GET':
        data = {}
        data['po'] = field_list('Po', 'order_number')
        return render(request, 'report/order_confirmation.html', locals())
    order_number = request.POST.get('order_number')
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
    # 设置页眉页脚
    sheet.show_headers = True
    sheet.header_str = b''
    sheet.footer_str = b'''FMR:                        OMR:                          OMR Supervisor:                       SZ Manager:'''
    for i in range(20):
        sheet.col(i).width = 8 * 256
    try:
        po = Po.objects.get(order_number=order_number)
    except:
        return JsonResponse({'status': 'fail', 'msg': 'po号不存在'})
    text_row = 0
    sheet.write_merge(text_row, text_row, 0, 17, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), body_style)
    # 标题
    sheet.write_merge(text_row + 1, text_row + 1, 0, 17, u'Order Information', title_style)
    # po信息
    sheet.write_merge(text_row + 2, text_row + 2, 2, 7, u'Cust  ID:%s' % po.customer.code, body_style)
    sheet.write_merge(text_row + 2, text_row + 2, 8, 14, u'Customer date:%s' % po.cus_receive_date, body_style)
    sheet.write_merge(text_row + 3, text_row + 3, 2, 7, u'EWB PO#:%s' % order_number, body_style)
    sheet.write_merge(text_row + 3, text_row + 3, 8, 14, u'Term of payment:%s' % po.pay_type, body_style)
    sheet.write_merge(text_row + 4, text_row + 4, 2, 7, u'Cust Po#:%s' % po.customer_pono, body_style)
    sheet.write_merge(text_row + 4, text_row + 4, 8, 14, u'%s:%s' % (po.delivery_condition.code, po.port.ename), body_style)
    # item标题栏信息
    sheet.write_merge(text_row + 5, text_row + 5, 0, 1, u'Item#', body_style)  # item no
    sheet.write_merge(text_row + 5, text_row + 5, 2, 3, u'description', body_style)  # 英文描述
    sheet.write_merge(text_row + 5, text_row + 5, 4, 4, u'FTY', body_style)  # 工厂代码
    sheet.write_merge(text_row + 5, text_row + 5, 5, 5, u'Term', body_style)  # 工厂出货港口
    sheet.write_merge(text_row + 5, text_row + 5, 6, 8, u'Packing Inner/Middle/Ctn/CUF', body_style)  # 单一包装
    sheet.write_merge(text_row + 5, text_row + 5, 9, 10, u'Q’t', body_style)  # 工厂送货数量
    sheet.write_merge(text_row + 5, text_row + 5, 11, 12, u'Fty.cost', body_style)  # 工厂报价
    sheet.write_merge(text_row + 5, text_row + 5, 13, 14, u'OtherCost', body_style)  # 配件单价之和
    sheet.write_merge(text_row + 5, text_row + 5, 15, 16, u'Price', body_style)  # 客人要价
    sheet.write_merge(text_row + 5, text_row + 5, 17, 17, u'MU', body_style)  # 利润比
    # item信息
    po_detail = Po_detail.objects.filter(po=order_number)
    item_row = text_row + 6  # 初始化item信息第一行
    for i in po_detail:
        contract = Contract.objects.get(po=i.po, item_no=i.item_no)
        material_sign_detail = Material_sign_detail.objects.filter(po=i.po, item_no=i.item_no)  # 材料签收明细
        mat_accessory_cost_sum = sum([float(j.accessory_cost) for j in material_sign_detail])  # 材料签收明细中所有单价之和
        sheet.write_merge(item_row, item_row, 0, 1, i.item_no, top_border)
        sheet.write_merge(item_row, item_row, 2, 3, i.edesc, top_border)
        sheet.write_merge(item_row, item_row, 4, 4, contract.factory.code, top_border)
        sheet.write_merge(item_row, item_row, 5, 5, i.fac_delivery_port.ename, top_border)
        sheet.write_merge(item_row, item_row, 6, 8, u'', top_border)
        sheet.write_merge(item_row, item_row, 9, 10, u'%s %s' % (i.amount, i.unit), top_border)
        sheet.write_merge(item_row, item_row, 11, 12, u'%s%s' % (contract.fac_currency.code,
                                                                 contract.fac_cost), top_border)
        sheet.write_merge(item_row, item_row, 13, 14, u'%s%s' % (material_sign_detail[0].accessory_currency,
                                                                 round(mat_accessory_cost_sum, 3)), top_border)
        sheet.write_merge(item_row, item_row, 15, 16, u'%s%s' % (i.currency.code, i.costrate), top_border)
        mu = float(i.costrate) / (float(contract.fac_cost) + float(mat_accessory_cost_sum))
        sheet.write_merge(item_row, item_row, 17, 17, round(mu, 3), top_border)
        # 括号
        sheet.write_merge(item_row + 1, item_row + 1, 0, 1, u'(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 2, 3, u')(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 4, 4, u')(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 5, 5, u')(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 6, 8, u')(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 9, 10, u')(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 11, 12, u')(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 13, 14, u')(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 15, 16, u')(', body_style)
        sheet.write_merge(item_row + 1, item_row + 1, 17, 17, u')', body_style)
        # 签字表格
        excel_row = item_row + 3
        sheet.write_merge(excel_row, excel_row + 1, 0, 1, u'', all_border)
        sheet.write_merge(excel_row, excel_row + 1, 2, 2, u'菲林', all_border)
        sheet.write_merge(excel_row, excel_row + 1, 3, 4, u'贴标/吊牌', all_border)
        sheet.write_merge(excel_row, excel_row + 1, 5, 5, u'彩盒', all_border)
        sheet.write_merge(excel_row, excel_row + 1, 6, 6, u'配件1', all_border)
        sheet.write_merge(excel_row, excel_row + 1, 7, 7, u'配件2', all_border)
        sheet.write_merge(excel_row, excel_row + 1, 8, 9, u'设计师佣金', all_border)
        sheet.write_merge(excel_row, excel_row, 10, 14, u'出货费用', all_border)
        sheet.write_merge(excel_row, excel_row, 15, 17, u'其他（请注明）', all_border)
        sheet.write_merge(excel_row + 1, excel_row + 1, 10, 11, u'HK或大陆码头费用', all_border)
        sheet.write_merge(excel_row + 1, excel_row + 1, 12, 12, u'海运费', all_border)
        sheet.write_merge(excel_row + 1, excel_row + 1, 13, 14, u'美国码头及内陆费用', all_border)
        sheet.write_merge(excel_row + 1, excel_row + 1, 15, 15, u'', all_border)
        sheet.write_merge(excel_row + 1, excel_row + 1, 16, 16, u'', all_border)
        sheet.write_merge(excel_row + 1, excel_row + 1, 17, 17, u'', all_border)
        sheet.row(excel_row + 1).set_style(xlwt.easyxf('font:height 500'))  # 36pt的行高
        # 批量化边框
        for y in range(2, 9):
            for j in range(2, 18):
                sheet.write(excel_row + y, j, u'', all_border)
                sheet.write_merge(excel_row + y, excel_row + y, 3, 4, u'', all_border)
                sheet.write_merge(excel_row + y, excel_row + y, 10, 11, u'', all_border)
                sheet.write_merge(excel_row + y, excel_row + y, 13, 14, u'', all_border)
        sheet.write_merge(excel_row + 2, excel_row + 2, 0, 1, u'预计总金额', all_border)
        sheet.write_merge(excel_row + 3, excel_row + 3, 0, 1, u'实际下单工厂', all_border)
        sheet.write_merge(excel_row + 4, excel_row + 4, 0, 1, u'下单单价', all_border)
        sheet.write_merge(excel_row + 5, excel_row + 5, 0, 1, u'下单数量', all_border)
        sheet.write_merge(excel_row + 6, excel_row + 6, 0, 1, u'经理确认', all_border)
        sheet.write_merge(excel_row + 7, excel_row + 7, 0, 1, u'财务确认', all_border)
        sheet.write_merge(excel_row + 8, excel_row + 8, 0, 1, u'Keyin确认', all_border)
        item_row += 14  # 下一条item信息的起始行
    # book.save("订单信息.xls")
    # 导出报表
    ############################
    # exist_file = os.path.exists("test.xls")
    # if exist_file:
    #     os.remove(r"test.xls")
    # book.save("test.xls")
    ############################
    # 输出xls到本地
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response.write(sio.getvalue())
    return response


# 生产记录表 -- ok
@login_required()
def product_record(request):
    if request.method == 'GET':
        return render(request, 'report/product_record.html', locals())
    action = request.POST.get('action')
    if action == 'list':
        detail_id_list = request.POST.get('detail_id_list')  # 获取po_detail的id列表
        detail_id_list = detail_id_list.split(',')
    else:
        start_id = request.POST.get('start_id')
        end_id = request.POST.get('end_id')
        detail_id_list = [i for i in range(int(start_id), int(end_id) + 1)]

    # 正文字体不加粗设置
    font3 = xlwt.Font()
    font3.name = '宋体'
    font3.height = 20 * 11
    font3.bold = False
    body_style.font = font3

    # 初始化表格
    book = xlwt.Workbook(encoding='utf-8')
    # 检测数据有效性
    if not detail_id_list:
        return JsonResponse({'status': 'fail', 'msg': '未收到任何detai_id号'})
    # 遍历po_detail
    for i in detail_id_list:
        sheet = book.add_sheet('sheet%s' % i, cell_overwrite_ok=True)
        # 设置页眉页脚
        sheet.show_headers = True
        sheet.header_str = b''
        sheet.footer_str = b''
        for j in range(15):
            sheet.col(j).width = 8 * 256
        # 标题
        sheet.write_merge(0, 0, 0, 11, u'EAST  WEST  BASICS  ITEM  生产记录表', title_style)
        po_detail = Po_detail.objects.get(id=int(i))
        po = Po.objects.get(order_number=po_detail.po)
        contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
        text_row = 1  # 定义表格初始行的参考行
        # 第一行
        sheet.write_merge(text_row + 1, text_row + 1, 0, 1, u'升辉订单号:', all_border)
        sheet.write_merge(text_row + 1, text_row + 1, 2, 5, po.order_number, all_border)
        sheet.write_merge(text_row + 1, text_row + 1, 6, 7, u'工厂:', all_border)
        sheet.write_merge(text_row + 1, text_row + 1, 8, 11, contract.factory.code, all_border)
        # 第二行
        sheet.write_merge(text_row + 2, text_row + 2, 0, 1, u'客人订单号:', all_border)
        sheet.write_merge(text_row + 2, text_row + 2, 2, 5, po.customer_pono, all_border)
        sheet.write_merge(text_row + 2, text_row + 2, 6, 7, u'出货港口:', all_border)
        sheet.write_merge(text_row + 2, text_row + 2, 8, 11, po_detail.fac_delivery_port.ename, all_border)
        # 第三行
        sheet.write_merge(text_row + 3, text_row + 3, 0, 1, u'ITEM#:', all_border)
        sheet.write_merge(text_row + 3, text_row + 3, 2, 5, po_detail.item_no, all_border)
        sheet.write_merge(text_row + 3, text_row + 3, 6, 7, u'中期验货时间:', all_border)
        sheet.write_merge(text_row + 3, text_row + 3, 8, 11, u'', all_border)
        # 第四行
        sheet.write_merge(text_row + 4, text_row + 4, 0, 1, u'工厂货号:', all_border)
        sheet.write_merge(text_row + 4, text_row + 4, 2, 5, po_detail.fac_no, all_border)
        sheet.write_merge(text_row + 4, text_row + 4, 6, 7, u'期末验货时间:', all_border)
        sheet.write_merge(text_row + 4, text_row + 4, 8, 11, u'', all_border)
        # 第五行
        sheet.write_merge(text_row + 5, text_row + 5, 0, 1, u'英文品名:', all_border)
        sheet.write_merge(text_row + 5, text_row + 5, 2, 5, po_detail.edesc, all_border)
        sheet.write_merge(text_row + 5, text_row + 5, 6, 7, u'出货时间:', all_border)
        sheet.write_merge(text_row + 5, text_row + 5, 8, 11, po_detail.sale_date, all_border)
        # 第六行
        sheet.write_merge(text_row + 6, text_row + 6, 0, 1, u'中文品名:', all_border)
        sheet.write_merge(text_row + 6, text_row + 6, 2, 5, po_detail.desc, all_border)
        sheet.write_merge(text_row + 6, text_row + 6, 6, 7, u'UPC#:', all_border)
        sheet.write_merge(text_row + 6, text_row + 6, 8, 11, u'', all_border)
        # 第七行
        sheet.write_merge(text_row + 7, text_row + 7, 0, 1, u'订单数量:', all_border)
        sheet.write_merge(text_row + 7, text_row + 7, 2, 5, po_detail.amount, all_border)
        sheet.write_merge(text_row + 7, text_row + 7, 6, 7, u'单一包装:', all_border)
        sheet.write_merge(text_row + 7, text_row + 7, 8, 11, po_detail.each_box.name, all_border)
        # 第八行
        sheet.write_merge(text_row + 8, text_row + 8, 0, 1, u'内盒数量:', all_border)
        sheet.write_merge(text_row + 8, text_row + 8, 2, 5, po_detail.inner_box, all_border)
        sheet.write_merge(text_row + 8, text_row + 8, 6, 7, u'中盒数量:', all_border)
        sheet.write_merge(text_row + 8, text_row + 8, 8, 11, po_detail.middle_box, all_border)
        # 第九行
        sheet.write_merge(text_row + 8, text_row + 8, 0, 1, u'外盒数量:', all_border)
        sheet.write_merge(text_row + 8, text_row + 8, 2, 5, po_detail.outside_box, all_border)
        sheet.write_merge(text_row + 8, text_row + 8, 6, 11, u'升辉公司提供配件:', all_border)
        # 唛头及注意事项
        sheet.write_merge(text_row + 10, text_row + 10, 0, 11, u'唛头及注意事项:', body_style)
        try:
            omr = OMR.objects.get(po=po_detail.po)
            sheet.write_merge(text_row + 11, 59, 0, 11, omr.special_remark, body_style)
        except:
            sheet.write_merge(text_row + 11, 59, 0, 11, u'', body_style)
    # book.save('生产记录表.xls')
    # 导出报表
    ############################
    # exist_file = os.path.exists("test.xls")
    # if exist_file:
    #     os.remove(r"test.xls")
    # book.save("test.xls")
    ############################
    # 输出xls到本地
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response.write(sio.getvalue())
    return response
