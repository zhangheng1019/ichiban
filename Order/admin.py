from django.contrib import admin
from .models import *


# Register your models here.
class User_extensionAdmin(admin.ModelAdmin):
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


admin.site.register(User_extension, User_extensionAdmin)
