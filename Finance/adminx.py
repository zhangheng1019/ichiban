import xadmin
from xadmin import views
from .models import *


# Register your models here.


class Claim_categoryAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['name', 'code']
    # 搜索字段
    search_fields = ['name', 'code']
    # 筛选字段
    list_filter = ['name']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class TypeAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['desc', 'edesc']
    # 搜索字段
    search_fields = ['desc', 'edesc']
    # 筛选字段
    list_filter = ['desc', 'edesc']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Finance_billAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['bill_number', 'out_number', 'place', 'date', 'extra_bill', 'is_check', 'is_pay', 'detail_id',
                    'abstract', 'code', 'subject', 'child_subject', 'inner_subject', 'currency', 'borrow', 'lend',
                    'rate_of_exchange', 'is_receipt', 'head_quarter', 'area', 'department', 'handle', 'explain']
    # 搜索字段
    search_fields = ['bill_number', 'place']
    # 筛选字段
    list_filter = ['place', 'area', 'department']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('place', 'code', 'currency', 'head_quarter', 'area', 'department', 'handle')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Ship_paymentAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['customer', 'factory', 'po', 'po_detail', 'customer_po', 'customer_item', 'product', 'amount',
                    'unit', 'final_date', 'qc1', 'omr', 'cus_price', 'cus_currency', 'cus_total', 'cus_total_currency',
                    'fac_cost', 'fac_cost_currency', 'fac_total', 'fac_total_currency', 'code', 'name', 'title',
                    'account_no', 'bank', 'invoice_no', 'currency', 'explain', 'pay_amount', 'remit_no', 'pay_date']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'pay_time'
    # 搜索字段
    search_fields = ['po', 'po_detail']
    # 筛选字段
    list_filter = ['customer', 'factory', 'omr']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('currency',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Accessory_payAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['customer', 'factory', 'po', 'po_detail', 'customer_po', 'customer_item', 'product', 'amount',
                    'unit', 'send_material_date', 'provide_type', 'omr', 'accessory_cost', 'accessory_cost_total',
                    'currency', 'sale_date', 'code', 'name', 'title', 'account_no', 'bank', 'invoice_no', 'explain',
                    'pay_currency', 'pay_remark', 'pay_amount', 'remit_no', 'pay_date']
    # 搜索字段
    search_fields = ['po', 'po_detail']
    # 筛选字段
    list_filter = ['customer', 'factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('pay_currency',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Claim_paymentAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['customer', 'factory', 'mr', 'explain', 'po', 'po_detail', 'customer_po', 'customer_item',
                    'product', 'amount', 'unit', 'final_date', 'qc1', 'pay_date', 'date', 'claim_amount',
                    'fac_amount', 'currency', 'invoice_no', 'claim_remark', 'clear_date', 'deduction_date',
                    'deduction_amount', 'deduction_fac_amount', 'deduction_currency', 'deduction_invoice_no',
                    'category_remark']
    # 搜索字段
    search_fields = ['po', 'po_detail', 'customer_po', 'customer_item']
    # 筛选字段
    list_filter = ['customer', 'factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('currency',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'sketch1_path',
               'sketch2_path', 'sketch3_path', 'insert_date']


class Claim_detailAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['claim_payment', 'claim_category', 'date', 'count', 'currency', 'amount', 'type',
                    'category_remark', 'claim_detail_explain', 'currency1', 'fac_amount', 'to_rmb',
                    'fac_claim_detail', 'invoice_no', 'pay_date']
    # 搜索字段
    search_fields = ['claim_payment']
    # 筛选字段
    list_filter = ['claim_category', 'date']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('claim_payment', 'claim_category', 'currency', 'type', 'currency1')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'last_date']


class Deduction_detailAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['claim_payment', 'method', 'material_from', 'is_order', 'factory', 'fac_order_qty', 'qty_unit',
                    'total', 'order_cost', 'order_currency', 'deducted_date', 'fac_actual_qty', 'fac_actual_unit',
                    'invoice_no', 'material']
    # 搜索字段
    search_fields = ['claim_payment']
    # 筛选字段
    list_filter = ['factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('claim_payment', 'factory', 'order_currency')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Accessory_deductionAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['customer', 'factory', 'mr', 'explain', 'po', 'po_detail', 'customer_po', 'customer_item',
                    'product', 'amount', 'unit', 'final_date', 'qc1', 'pay_date', 'deduction_clear_date', 'type',
                    'count', 'deduction_amount', 'fac_amount', 'currency', 'fac_total_amount',
                    'invoice_no', 'category_remark']
    # 搜索字段
    search_fields = ['po', 'po_detail', 'customer_po', 'customer_item']
    # 筛选字段
    list_filter = ['customer', 'factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('type', 'currency')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Accessory_deduction_detailAdmin(object):
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    # 是否显示选择个数
    actions_selection_counter = True
    # 每页显示的数据行数
    list_per_page = 15
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 首页展示字段
    list_display = ['deduction_detail', 'pay_date', 'reason', 'count', 'price', 'currency', 'total_amount',
                    'deduction_no', 'deduction_clear_date']
    # 搜索字段
    search_fields = ['deduction_detail']
    # 筛选字段
    list_filter = ['pay_date']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('deduction_detail', 'currency')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


xadmin.site.register(Claim_category, Claim_categoryAdmin)
xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Finance_bill, Finance_billAdmin)
xadmin.site.register(Ship_payment, Ship_paymentAdmin)
xadmin.site.register(Accessory_pay, Accessory_payAdmin)
xadmin.site.register(Claim_payment, Claim_paymentAdmin)
xadmin.site.register(Claim_detail, Claim_detailAdmin)
xadmin.site.register(Deduction_detail, Deduction_detailAdmin)
xadmin.site.register(Accessory_deduction, Accessory_deductionAdmin)
xadmin.site.register(Accessory_deduction_detail, Accessory_deduction_detailAdmin)
