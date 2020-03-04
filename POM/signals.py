# models信号检测

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from .models import *
from POM.models import *
from POM.views import *
from POM.query_API import *


# 捕获Point（规则）增加后、修改后、删除后的动作 -- 该触发器待完成
# 循环扫描订单，当订单符合匹配上的规则就在remind中添加提醒事项
@receiver((post_save, post_delete), sender=Point)
def point_update(sender, instance, **kwargs):
    # order_remind_add(point=instance)
    print('======================%s正在新增、修改、删除', instance.code, datetime.datetime.now())


@receiver((post_save, post_delete), sender=PoPoint)
def popoint_update(sender, instance, **kwargs):
    order_remind_refresh(po=instance.order_number, item_no=instance.item_no)
    print('======================%s%s正在新增、修改、删除' % (instance.order_number, instance.item_no), datetime.datetime.now())


# 拼接事项筛选条件示例
# dic = [
#     'texture == "五金类" or texture == "材质2"',
#     'factory == "奕纶"',
#     'customer == "GHAAN"',
#     'amount >= 50',
# ]
#
# l = ['po_point.' + i for i in dic]
# express = ' and '.join(l)
"""
'po_point.texture == "五金类" or texture == "材质2" 
and po_point.factory == "奕纶" 
and po_point.customer == "GHAAN" 
and po_point.amount >= 50'
"""
# eval(express)  # True
