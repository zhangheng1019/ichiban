import xadmin
from xadmin import views
from .models import *


# Register your models here.
class User_extensionAdmin(object):
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
    list_display = ['user', 'field_permission']
    # 搜索字段
    search_fields = ['user']
    # 筛选字段
    list_filter = ['user']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    # exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Package_textureAdmin(object):
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
    list_display = ['name', 'edesc']
    # 搜索字段
    search_fields = ['name', 'edesc']
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


class Package_typeAdmin(object):
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
    list_filter = ['name', 'code']
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


class Sea_rateAdmin(object):
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
    list_display = ['tariff', 'rate']
    # 搜索字段
    search_fields = ['tariff', 'rate']
    # 筛选字段
    list_filter = ['tariff', 'rate']
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


class Develop_functionAdmin(object):
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
    list_display = ['func_name', 'func_desc']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'pay_time'
    # 搜索字段
    search_fields = ['func_name']
    # 筛选字段
    list_filter = ['func_name', 'func_desc']
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


class Sketch_typeAdmin(object):
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
    list_display = ['name', 'edesc']
    # 搜索字段
    search_fields = ['name']
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


class Sketch_designAdmin(object):
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
    list_display = ['code', 'name', 'developer', 'designer', 'category', 'date', 'customer',
                    'texture', 'sketch_type', 'photo1', 'photo1_remark', 'photo2', 'photo2_remark',
                    'photo3', 'photo3_remark']
    # 搜索字段
    search_fields = ['name', 'code']
    # 筛选字段
    list_filter = ['developer', 'designer', 'category', 'customer']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('developer', 'designer', 'category', 'customer', 'material', 'sketch_type')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'sketch1_path',
               'sketch2_path', 'sketch3_path', 'insert_date']


class Sketch_developAdmin(object):
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
    list_display = ['sketch_name', 'number', 'receive_date', 'category', 'developer', 'department', 'function',
                    'undertake', 'plan_date', 'customer', 'season', 'makesure_time', 'explain', 'is_finish']
    # 搜索字段
    search_fields = ['sketch_name', 'number']
    # 筛选字段
    list_filter = ['category', 'developer', 'department', 'undertake']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('category', 'developer', 'department', 'function', 'undertake', 'customer')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'last_date']


class Sketch_detailAdmin(object):
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
    list_display = ['number', 'item_number', 'name', 'ename', 'customer_price', 'customer_currency',
                    'factory', 'factory_price', 'factory_currency', 'texture', 'long',
                    'width', 'height', 'size_unit', 'amount', 'fmr_undertake', 'refer_data',
                    'refer_data_no', 'fmr_50', 'start_date', 'photo_src', 'fmr_plan_date',
                    'fmr_change_plan_date', 'fmr_change_act_date', 'receive_date', 'sent_date',
                    'mould_min', 'other_fee', 'express_fee', 'is_customer_price', 'is_finish', 'product_explain']
    # 搜索字段
    search_fields = ['number', 'item_number', 'name']
    # 筛选字段
    list_filter = ['factory', 'texture', 'fmr_undertake']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('customer_currency', 'factory', 'factory_currency', 'texture', 'fmr_undertake')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'sea_cuft_code',
               'delay_reason', 'case', 'first_sample_deadLine', 'first_sample_revised',
               'mould_cost', 'data_change_date', 'status']


class Sample_detailAdmin(object):
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
    list_display = ['item_no', 'item_number', 'parent_item', 'other_item', 'sketch_no', 'name', 'ename',
                    'category', 'texture', 'long', 'width', 'height', 'other', 'volume', 'volume_unit',
                    'omr', 'fmr', 'photo', 'photo_remark', 'sample_receive', 'company', 'desc']
    # 搜索字段
    search_fields = ['item_no', 'item_number', 'sketch_no', 'name', 'ename']
    # 筛选字段
    list_filter = ['category', 'texture', 'company']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('category', 'texture', 'omr', 'fmr', 'company')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'fac_volum', 'fac_volume_uni',
               'custome', 'customer_de', 'insert_dat', 'ass', 'check_m', 'check_dat', 'sea_rat', 'is_delet',
               'min_orde', 'leadtim', 'reroader_leadtim', 'size40_perp', 'size40_freigh', 'high_size40_freigh',
               'size45_freigh', 'pack_amoun', 'functio', 'shape']


class Item_noteAdmin(object):
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
    list_display = ['sample', 'code', 'desc']
    # 搜索字段
    search_fields = ['sample']
    # 筛选字段
    list_filter = ['code', 'sample']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('item',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Item_packageAdmin(object):
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
    list_display = ['sample', 'type', 'package_texture', 'long', 'width', 'height', 'unit',
                    'net_weight', 'gross_weight', 'amount']
    # 搜索字段
    search_fields = ['sample', 'type']
    # 筛选字段
    list_filter = ['package_texture']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('type', 'package_texture')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Factory_quoteAdmin(object):
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
    list_display = ['factory', 'sample', 'factory_number', 'cost', 'currency', 'pack_texture',
                    'shipping_method', 'shipping_port', 'sample_desc', 'is_default_quote']
    # 搜索字段
    search_fields = ['factory', 'sample']
    # 筛选字段
    list_filter = ['factory', 'sample', 'shipping_method', 'shipping_port']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('factory', 'currency', 'pack_texture', 'shipping_method', 'shipping_port')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'insert_date',
               'quote_staff', 'check_staff', 'input_staff', 'is_check_ok', 'not_reason', 'check_date']


class Repeat_sampleAdmin(object):
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
    list_display = ['number', 'customer', 'receive_date', 'fac_send_date', 'undertaker', 'explain']
    # 搜索字段
    search_fields = ['number']
    # 筛选字段
    list_filter = ['customer', 'undertaker']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('customer', 'undertaker')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'supervisor',
               'supervisor1', 'advance_days', 'insert_date']


class Repeat_sample_detailAdmin(object):
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
    list_display = ['number', 'item_no', 'specs', 'desc', 'edesc', 'customer_no', 'texture',
                    'samp_long', 'samp_width', 'samp_height', 'size_unit', 'fac_number', 'sketch_no',
                    'amount', 'amount_unit', 'order_date', 'factory', 'actual_date', 'cancle_date',
                    'fac_date', 'status', 'finish', 'finish_date', 'sample_remark']
    # 搜索字段
    search_fields = ['number', 'item_no']
    # 筛选字段
    list_filter = ['customer', 'texture', 'factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('texture', 'factory')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'supervisor',
               'supervisor1', 'advance_days', 'insert_date', 'new_no', 'sz_no', 'weight', 'estimate_ship',
               'project', 'color', 'season', 'type', 'peculiarity', 'to_tpe_qty', 'to_hk_qty', 'to_sz_qty',
               'to_usa_qty', 'date1', 'memo', 'net_weight', 'gross_weight', 'actual_qty', 'long', 'width',
               'height', 'each', 'inner', 'middle', 'box', 'cno', 'qc1', 'qc2', 'qc3', 'fqc', 'pum_id',
               'is_resample', 'sample_status', 'request', 'insert_date', 'is_omr_sure', 'omr_sure_date', 'fmr']


class Sample_targetAdmin(object):
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
    list_display = ['number', 'item_no', 'change_date', 'change_desc', 'omr_sure', 'omr_sure_date',
                    'fmr_sure', 'fmr_sure_date', 'omr_check', 'omr_check_date', 'fmr_check', 'fmr_check_date']
    # 搜索字段
    search_fields = ['sam_detail_no']
    # 筛选字段
    list_filter = ['omr_sure_date', 'fmr_sure_date', 'omr_check_date', 'fmr_check_date']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class PoAdmin(object):
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
    list_display = ['customer', 'customer_pono', 'cus_receive_date', 'fina_date', 'receive_date', 'order_number',
                    'fac_send_date', 'produce_native_date', 'delivery_condition', 'port', 'omr', 'pay_type']
    # 搜索字段
    search_fields = ['customer', 'order_number', 'customer_pono']
    # 筛选字段
    list_filter = ['customer', 'order_number', 'customer_pono', 'omr']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    readonly_fields = ['receive_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('customer', 'delivery_condition', 'port', 'omr')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'special_remark ',
               'special_remark2', 'special_remark3', 'order_status', 'mai', 'ce_mai', 'middle_mai',
               'inner_mai', 'fen_pi', 'parent_pono', 'supervise', 'supervise1', 'product_send',
               'product_receive', 'ship_style']


class Po_detailAdmin(object):
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
    list_display = ['po', 'item_no', 'customer_item', 'texture', 'fac_no', 'desc', 'edesc', 'amount',
                    'unit', 'costrate', 'currency', 'each_box', 'outside_box', 'middle_box',
                    'inner_box', 'box_unit', 'for_profit_report', 'special_remark', 'fac_delivery',
                    'fac_delivery_port', 'fmr', 'fqc', 'sale_date']
    # 搜索字段
    search_fields = ['po', 'item_no']
    # 筛选字段
    list_filter = ['po', 'item_no', 'customer_item', 'fac_no']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('texture', 'each_box', 'fac_delivery', 'fac_delivery_port')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'cancle_date']


class ContractAdmin(object):
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
    list_display = ['po', 'item_no', 'customer_item', 'desc', 'amount', 'unit',
                    'oa_sure_date', 'fac_amount', 'fac_unit', 'factory', 'fac_currency', 'fac_cost',
                    'fac_total', 'cancle_date']
    # 搜索字段
    search_fields = ['po', 'item_no']
    # 筛选字段
    list_filter = ['po', 'item_no', 'factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = ''
    # 在编辑页的只读字段
    # readonly_fields = []
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('po', 'item_no', 'fac_amount', 'fac_unit', 'factory', 'fac_currency')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Product_sendAdmin(object):
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
    list_display = ['po', 'item_no', 'customer_item', 'fac_no', 'amount', 'desc', 'unit', 'fmr', 'qc1', 'qc2', 'qc3',
                    'rqc1', 'rqc2', 'fqc', 'cancle_date', 'sale_date', 'no_pass', 'send_person']
    # 搜索字段
    search_fields = ['pono', 'item_no']
    # 筛选字段
    list_filter = ['fqc']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('fmr', 'qc1', 'qc2', 'qc3', 'rqc1', 'rqc2', 'fqc', 'send_person')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class OMRAdmin(object):
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
    list_display = ['po', 'customer_pono', 'receive_date', 'cus_receive_date', 'fac_send_date', 'omr', 'special_remark']
    # 搜索字段
    search_fields = ['po']
    # 筛选字段
    list_filter = ['omr']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('omr', )
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class OMR_po_detailAdmin(object):
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
    list_display = ['po', 'item_no', 'customer_pono', 'receive_date', 'cus_receive_date', 'fac_send_date', 'omr',
                    'desc', 'amount', 'unit', 'oa_sure_date', 'factory', 'texture', 'port', 'process',
                    'produce_record', 'mark_notice_date', 'label_sure_date', 'label_send_date',
                    'sample_send_date', 'sample_pass_date', 'product_send_date', 'product_sure_date',
                    'midterm_inspect', 'booking_so', 'ichiban_inspect', 'customer_inspect', 'pl_come_date',
                    'box_sure_date', 'box_send_date', 'shipping_data', 'special_remark', 'special_remark1']
    # 搜索字段
    search_fields = ['po', 'item_no']
    # 筛选字段
    list_filter = ['omr', 'factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('omr',  'unit', 'factory')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class FMRAdmin(object):
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
    list_display = ['po', 'item_no', 'receive_date', 'fac_send_date', 'name', 'amount', 'unit', 'factory',
                    'oa_sure_date', 'texture', 'process']
    # 搜索字段
    search_fields = ['po', 'item_no']
    # 筛选字段
    list_filter = ['factory', 'oa_sure_date']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('process',)
    # 在编辑页面隐藏的字段
    exclude = ['omr', 'remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Material_signAdmin(object):
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
    list_display = ['po', 'item_no', 'omr', 'amount', 'unit', 'name', 'customer_pono', 'customer_item', 'factory']
    # 搜索字段
    search_fields = ['po', 'item_no']
    # 筛选字段
    list_filter = ['factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('po', 'item_no', 'factory')
    # 在编辑页面隐藏的字段
    exclude = ['omr', 'remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class Material_sign_detailAdmin(object):
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
    list_display = ['po', 'item_no', 'texture', 'pc_count', 'pc_unit', 'need_qty', 'need_qty_unit',
                    'name', 'provide_type', 'provide_from', 'is_order', 'actual_qty', 'actual_qty_unit',
                    'send_material_date', 'sender', 'special_remark', 'accessory_cost', 'accessory_currency',
                    'accessory_cost_total', 'accessory_total_currency', 'deduct_invoice_no', 'factory', 'fac_qty',
                    'fac_qty_unit', 'price', 'order_currency', 'total', 'total_currency', 'order_date', 'pay_date',
                    'is_shipment', 'qc', 'fqc', 'actual_date']
    # 搜索字段
    search_fields = ['po', 'item_no']
    # 筛选字段
    list_filter = ['texture', 'name', 'sender', 'factory', 'order_date', 'qc', 'fqc']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('texture', 'sender', 'accessory_currency', 'accessory_total_currency', 'factory',
                     'order_currency', 'total_currency', 'qc', 'fqc')
    # 在编辑页面隐藏的字段
    exclude = ['omr', 'remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


xadmin.site.register(User_extension, User_extensionAdmin)
xadmin.site.register(Package_texture, Package_textureAdmin)
xadmin.site.register(Package_type, Package_typeAdmin)
xadmin.site.register(Sea_rate, Sea_rateAdmin)
xadmin.site.register(Develop_function, Develop_functionAdmin)
xadmin.site.register(Sketch_type, Sketch_typeAdmin)
xadmin.site.register(Sketch_design, Sketch_designAdmin)
xadmin.site.register(Sketch_develop, Sketch_developAdmin)
xadmin.site.register(Sketch_detail, Sketch_detailAdmin)
xadmin.site.register(Sample_detail, Sample_detailAdmin)
xadmin.site.register(Item_note, Item_noteAdmin)
xadmin.site.register(Item_package, Item_packageAdmin)
xadmin.site.register(Factory_quote, Factory_quoteAdmin)
xadmin.site.register(Repeat_sample, Repeat_sampleAdmin)
xadmin.site.register(Repeat_sample_detail, Repeat_sample_detailAdmin)
xadmin.site.register(Sample_target, Sample_targetAdmin)
xadmin.site.register(Po, PoAdmin)
xadmin.site.register(Po_detail, Po_detailAdmin)
xadmin.site.register(Contract, ContractAdmin)
xadmin.site.register(Product_send, Product_sendAdmin)
xadmin.site.register(OMR, OMRAdmin)
xadmin.site.register(OMR_po_detail, OMR_po_detailAdmin)
xadmin.site.register(FMR, FMRAdmin)
xadmin.site.register(Material_sign, Material_signAdmin)
xadmin.site.register(Material_sign_detail, Material_sign_detailAdmin)
