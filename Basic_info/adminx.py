import xadmin
from xadmin import views
from .models import *


# Register your models here.

class TextureAdmin(object):
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
    list_display = ['name', 'ename', 'code', 'desc', 'edesc']
    # 搜索字段
    search_fields = ['name', 'ename', 'code']
    # 筛选字段
    list_filter = ['name', 'ename', 'code', 'lastdate']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['name']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['name', 'code']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['name', 'code']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['lastdate', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Texture_processAdmin(object):
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
    list_display = ['texture', 'texture_process', 'not_in_process', 'ahead_days', 'code']
    # 搜索字段
    search_fields = ['texture', 'texture_process', 'code']
    # 筛选字段
    list_filter = ['ahead_days']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('texture',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Material_cateAdmin(object):
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
    list_display = ['category', 'desc', 'child_cate_edesc', 'child_cate']
    # 搜索字段
    search_fields = ['category']
    # 筛选字段
    list_filter = ['category']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class MaterialAdmin(object):
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
    list_display = ['po', 'po_detail', 'to_factory_date', 'fac_qty', 'qty_unit', 'fac_order_qty',
                    'fac_actual_qty', 'sender', 'send_remark', 'fac_remark', 'method', 'material_from', 'is_order',
                    'deducted_date', 'invoice_no', 'mat_cost', 'currency', 'name', 'belong', 'factory',
                    'order_cost', 'order_currency', 'order_date', 'delivery_date', 'actual_delivery_date',
                    'special_remark', 'qc', 'fqc', 'is_complate']
    # 搜索字段
    search_fields = ['po', 'po_detail', 'factory']
    # 筛选字段
    list_filter = ['deducted_date', 'sender', 'material_from', 'factory', 'order_date', 'delivery_date',
                   'actual_delivery_date', 'qc', 'fqc']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('po', 'po_detail', 'qty_unit', 'currency', 'belong', 'factory', 'order_currency', 'qc', 'fqc')
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class PositionAdmin(object):
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
    list_display = ['job', 'code']
    # 搜索字段
    search_fields = ['job', 'code']
    # 筛选字段
    list_filter = ['job', 'code']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class CurrencyAdmin(object):
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
    list_display = ['name', 'code', 'to_rmb', 'to_us']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'pay_time'
    # 搜索字段
    search_fields = ['name', 'code']
    # 筛选字段
    list_filter = ['name', 'code']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sup_name', 'agent_name', 'order_number')
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class CategoryAdmin(object):
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
    list_display = ['code', 'parent_category']
    # 搜索字段
    search_fields = ['code', 'parent_category']
    # 筛选字段
    list_filter = ['code', 'parent_category']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class UnitAdmin(object):
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
    list_display = ['name', 'sign']
    # 搜索字段
    search_fields = ['name', 'sign']
    # 筛选字段
    list_filter = ['name', 'sign']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class AreaAdmin(object):
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
    list_display = ['name', 'code', 'desc', 'fmr', 'qc']
    # 搜索字段
    search_fields = ['name', 'code']
    # 筛选字段
    list_filter = ['name', 'code', 'fmr', 'qc']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('fmr', 'qc')
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class DepartmentAdmin(object):
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
    list_display = ['name', 'charge_id', 'charge_name', 'last_dept']
    # 搜索字段
    search_fields = ['name']
    # 筛选字段
    list_filter = ['name']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Head_quarterAdmin(object):
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
    list_display = ['name', 'code', 'city']
    # 搜索字段
    search_fields = ['name', 'code', 'city']
    # 筛选字段
    list_filter = ['city']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class CompanyAdmin(object):
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
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class DeliveryAdmin(object):
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
    list_display = ['code', 'desc', 'edesc']
    # 搜索字段
    search_fields = ['code']
    # 筛选字段
    list_filter = ['code']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Export_portAdmin(object):
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
    list_display = ['name', 'ename']
    # 搜索字段
    search_fields = ['name', 'ename']
    # 筛选字段
    list_filter = ['name', 'ename']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Export_typeAdmin(object):
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
    list_display = ['name', 'desc']
    # 搜索字段
    search_fields = ['name']
    # 筛选字段
    list_filter = ['name']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class CustomerAdmin(object):
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
    list_display = ['name', 'code', 'phone', 'fax', 'street', 'city', 'province', 'country',
                    'post_number', 'email', 'join_date', 'contact', 'avg_profit', 'is_agree']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'join_date'
    # 搜索字段
    search_fields = ['name', 'code', 'country', 'province', 'city', 'street']
    # 筛选字段
    list_filter = ['name', 'code', 'country', 'province', 'city', 'street']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Customer_markAdmin(object):
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
    list_display = ['code', 'request', 'zhenmai', 'cemai', 'neimai']
    # 搜索字段
    search_fields = ['code', 'zhenmai', 'cemai', 'neimai']
    # 筛选字段
    list_filter = ['code', 'zhenmai', 'cemai', 'neimai']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('code',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Export_countryAdmin(object):
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
    list_display = ['name', 'code', 'ename']
    # 搜索字段
    search_fields = ['name', 'code', 'ename']
    # 筛选字段
    list_filter = ['name', 'code', 'ename']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Export_companyAdmin(object):
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
    list_display = ['name', 'code', 'title', 'account_no', 'bank']
    # 搜索字段
    search_fields = ['name', 'code']
    # 筛选字段
    list_filter = ['name', 'code', 'bank']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class StaffAdmin(object):
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
    list_display = ['name', 'ename', 'emp_ename', 'emp_no', 'id_card', 'company', 'sex', 'birthday', 'is_marry',
                    'graduate_school', 'graduate_date', 'major', 'education', 'hometown', 'addr', 'home_tel',
                    'phone', 'department', 'position', 'offer_date', 'join_date', 'staff_form', 'become_real_date',
                    'contract_end_date', 'quit_date', 'quit_reason', 'quit_extend_date', 'quit_remark', 'clear',
                    'math_score', 'english_score', 'level', 'titled', 'email', 'charge', 'agent_charge', 'manager',
                    'agent_manager']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'join_date'
    # 搜索字段
    search_fields = ['name', 'ename', 'emp_no']
    # 筛选字段
    list_filter = ['company', 'sex', 'is_marry', 'graduate_school', 'education', 'hometown', 'department',
                   'position', 'join_date', 'staff_form']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('company', 'department', 'position')
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class EmployeeRelationshipAdmin(object):
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
    list_display = ['staff', 'leader', 'branch']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'join_date'
    # 搜索字段
    search_fields = ['staff']
    # 筛选字段
    list_filter = ['leader', 'branch']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('staff', 'leader', 'branch')
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class FactoryAdmin(object):
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
    list_display = ['name', 'code', 'ename', 'tel', 'fax', 'country', 'province', 'city', 'area',
                    'street', 'email', 'post_code', 'contact', 'export_company_code', 'fac_remark']
    # 搜索字段
    search_fields = ['name', 'ename', 'code']
    # 筛选字段
    list_filter = ['name', 'ename', 'code', 'province', 'city', 'export_company_code', 'fmr']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'insert_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('area', 'export_company_code', 'fac_texture', 'fmr')
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark', 'fac_texture', 'fac_master',
               'fac_texture', 'fac_master', 'fac_assess', 'arrive_type', 'insert_date', 'is_check', 'fmr']


class CodeAdmin(object):
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
    list_display = ['category_code', 'first', 'second', 'third', 'department', 'area']
    # 搜索字段
    search_fields = ['category_code']
    # 筛选字段
    list_filter = ['category_code', 'department', 'area']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('department', 'area')
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class StatusAdmin(object):
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
    list_display = ['name']
    # 搜索字段
    search_fields = ['name']
    # 筛选字段
    list_filter = ['name']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('sam_detail_no',)
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class Matrial_processAdmin(object):
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
    list_display = ['name', 'p_code', 'm_code', 'next_process', 'produce_days']
    # 搜索字段
    search_fields = ['name', 'p_code']
    # 筛选字段
    list_filter = ['p_code', 'next_process']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'change_date'
    # 在编辑页的只读字段
    # readonly_fields = ['']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('m_code', )
    # 在编辑页面隐藏的字段
    exclude = ['preset1', 'preset2', 'preset3', 'preset4', 'preset5', 'remark']


class BaseSetting(object):
    # 开启主题更换
    enable_themes = True
    use_bootswatch = True


# xadmin设置界面
class GlobalSetting(object):

    # 设置xadmin后台顶部标题
    site_title = '一品轩管理系统'
    # 设置xadmin后台底部标题
    site_footer = '一品轩食品有限公司'
    # 左侧菜单折叠
    menu_style = "accordion"
    # 模型图标
    model_icon = 'default'


# 视图注册
xadmin.site.register(Texture, TextureAdmin)
xadmin.site.register(Texture_process, Texture_processAdmin)
xadmin.site.register(Material_cate, Material_cateAdmin)
xadmin.site.register(Material, MaterialAdmin)
xadmin.site.register(Position, PositionAdmin)
xadmin.site.register(Currency, CurrencyAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Unit, UnitAdmin)
xadmin.site.register(Area, AreaAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Head_quarter, Head_quarterAdmin)
xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(Delivery, DeliveryAdmin)
xadmin.site.register(Export_port, Export_portAdmin)
xadmin.site.register(Export_type, Export_typeAdmin)
xadmin.site.register(Customer, CustomerAdmin)
xadmin.site.register(Customer_mark, Customer_markAdmin)
xadmin.site.register(Export_country, Export_countryAdmin)
xadmin.site.register(Export_company, Export_companyAdmin)
xadmin.site.register(Staff, StaffAdmin)
xadmin.site.register(EmployeeRelationship, EmployeeRelationshipAdmin)
xadmin.site.register(Factory, FactoryAdmin)
xadmin.site.register(Code, CodeAdmin)
xadmin.site.register(Status, StatusAdmin)
xadmin.site.register(Matrial_process, Matrial_processAdmin)

# 界面样式设置注册激活
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
