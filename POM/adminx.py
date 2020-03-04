import xadmin
from xadmin import views
from .models import *


# Register your models here.
class PointAdmin(object):
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
    list_display = ['source', 'name', 'code', 'last_date']
    # 搜索字段
    search_fields = ['name', 'code']
    # 筛选字段
    list_filter = ['source']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'last_date'
    # 在编辑页的只读字段
    readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class PoPointAdmin(object):
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
                    'fac_send_date', 'produce_native_date', 'delivery_condition', 'port', 'omr', 'pay_type',
                    'item_no', 'customer_item', 'desc', 'edesc', 'fac_no', 'texture', 'amount', 'unit', 'costrate',
                    'currency', 'each_box', 'outside_box', 'middle_box', 'inner_box', 'box_unit', 'for_profit_report',
                    'fac_delivery', 'fac_delivery_port', 'fmr', 'fqc', 'sale_date', 'factory', 'fac_currency',
                    'fac_cost', 'fac_total', 'cancle_date', 'qc1', 'qc2', 'qc3', 'rqc1', 'rqc2', 'no_pass',
                    'send_person', 'special_remark', 'process', 'produce_record', 'mark_notice_date',
                    'label_sure_date', 'label_send_date', 'sample_send_date', 'sample_pass_date', 'product_send_date',
                    'product_sure_date', 'midterm_inspect', 'booking_so', 'ichiban_inspect', 'customer_inspect',
                    'pl_come_date', 'box_sure_date', 'box_send_date', 'shipping_data']
    # 搜索字段
    search_fields = ['order_number', 'item_no']
    # 筛选字段
    list_filter = ['order_number', 'customer', 'factory', 'port', 'omr', 'fac_delivery']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'receive_date'
    # 在编辑页的只读字段
    # readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class EventAdmin(object):
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
    list_display = ['name', 'edesc', 'code', 'last_date']
    # 搜索字段
    search_fields = ['name', 'code']
    # 筛选字段
    list_filter = ['name']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'last_date'
    # 在编辑页的只读字段
    readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class PointEventAdmin(object):
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
    list_display = ['point_category', 'point', 'event', 'last_date']
    # 搜索字段
    search_fields = ['point', 'event']
    # 筛选字段
    list_filter = ['point_category']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'last_date'
    # 在编辑页的只读字段
    readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class RemindAdmin(object):
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
    list_display = ['po', 'item_no', 'event', 'event_edesc', 'person', 'begin_time', 'end_time', 'rate', 'plan_date',
                    'actual_date', 'status', 'pomm', 'pomc', 'is_upload_file', 'file_path', 'last_date']
    # 搜索字段
    search_fields = ['po', 'item_no']
    # 筛选字段
    list_filter = ['person', 'begin_time', 'end_time', 'rate', 'plan_date', 'status', 'pomm', 'pomc']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'last_date'
    # 在编辑页的只读字段
    readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class OtherPointAdmin(object):
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
    list_display = ['point', 'desc', 'edesc', 'last_date']
    # 搜索字段
    search_fields = ['point']
    # 筛选字段
    # list_filter = ['']
    # 在列表页的顶部增加时间选择器
    date_hierarchy = 'last_date'
    # 在编辑页的只读字段
    readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class FactoryAbilityAdmin(object):
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
    list_display = ['factory', 'yields', 'per_person', 'person', 'pass_rate', 'item']
    # 搜索字段
    search_fields = ['factory', 'item']
    # 筛选字段
    list_filter = ['yields', 'person', 'factory']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'last_date'
    # 在编辑页的只读字段
    # readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    raw_id_fields = ('factory', 'item')
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class FactoryProcessAdmin(object):
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
    list_display = ['things', 'types', 'remind_date', 'date_by']
    # 搜索字段
    search_fields = ['types', 'remind_date', 'date_by']
    # 筛选字段
    list_filter = ['types', 'remind_date', 'date_by']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'last_date'
    # 在编辑页的只读字段
    # readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


class TextureRemindsAdmin(object):
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
    list_display = ['texture_cate', 'things', 'remind_date', 'date_by']
    # 搜索字段
    search_fields = ['texture_cate']
    # 筛选字段
    list_filter = ['remind_date', 'date_by']
    # 在列表页的顶部增加时间选择器
    # date_hierarchy = 'last_date'
    # 在编辑页的只读字段
    # readonly_fields = ['last_date']
    # 设置在列表页就可以编辑的字段
    # list_editable = ['']
    # 在列表页提供快速显示详情信息
    # show_detail_fileds = ['']
    # 外键下拉框改成添加搜索按钮文本框显示
    # raw_id_fields = ('user',)
    # 在编辑页面隐藏的字段
    exclude = ['remark', 'preset1', 'preset2', 'preset3', 'preset4', 'preset5']


xadmin.site.register(Point, PointAdmin)
xadmin.site.register(PoPoint, PoPointAdmin)
xadmin.site.register(Event, EventAdmin)
xadmin.site.register(PointEvent, PointEventAdmin)
xadmin.site.register(Remind, RemindAdmin)
xadmin.site.register(OtherPoint, OtherPointAdmin)
xadmin.site.register(FactoryAbility, FactoryAbilityAdmin)
# xadmin.site.register(FactoryProcess, FactoryProcessAdmin)
# xadmin.site.register(TextureReminds, TextureRemindsAdmin)
