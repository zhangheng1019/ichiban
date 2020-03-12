# models信号检测

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from .models import *
from POM.models import *
from POM.views import *
from POM.query_API import *


# 捕获Po增加后、修改后、删除后的动作
@receiver((post_save, post_delete), sender=Po)
def po_update(sender, instance, **kwargs):
    order_remind_refresh(po=instance)
    print('======================%s正在新增、修改、删除', instance.order_number, datetime.datetime.now())


# 捕获Po_detail增加后、修改后、删除后的动作
@receiver((post_save, post_delete), sender=Po_detail)
def po_detail_update(request, sender, instance, **kwargs):
    order_remind_refresh(po=instance.po, item_no=instance.item_no)
    print('======================%s正在新增、修改、删除', instance.po, datetime.datetime.now())


# 捕获Contract增加后、修改后、删除后的动作
@receiver((post_save, post_delete), sender=Contract)
def contract_update(request, sender, instance, **kwargs):
    # order_remind_refresh(po=instance.po, item_no=instance.item_no)
    print('======================%s正在新增、修改、删除', instance.po, datetime.datetime.now())


# 捕获Product_send增加后、修改后、删除后的动作
@receiver((post_save, post_delete), sender=Product_send)
def product_send_update(request, sender, instance, **kwargs):
    # order_remind_refresh(request, po=instance.po, item_no=instance.item_no)
    print('======================%s正在新增、修改、删除', instance.po, datetime.datetime.now())


# 捕获OMR增加后、修改后、删除后的动作
@receiver((post_save, post_delete), sender=OMR)
def omr_update(request, sender, instance, **kwargs):
    # order_remind_refresh(request, po=instance.po, item_no=instance.item_no)
    print('======================%s正在新增、修改、删除', instance.po, datetime.datetime.now())


# 捕获OMR_po_detail增加后、修改后、删除后的动作
@receiver((post_save, post_delete), sender=OMR_po_detail)
def omr_po_detail_update(request, sender, instance, **kwargs):
    # order_remind_refresh(request, po=instance.po, item_no=instance.item_no)
    print('======================%s正在新增、修改、删除', instance.po, datetime.datetime.now())
