import os
from datetime import datetime
import json
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from Basic_info.models import *
from Order.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.views.generic.base import View, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apple.views import *
# Create your views here.


class TextureView(View):
    """材质"""
    template_name = 'basic_info/texture.html'

    # 给当前类的所有实例方法添加登陆装饰器，在验证用户身份后才能访问当前类方法
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TextureView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, locals())


class TextureProcessView(TextureView):
    """材质进度"""
    template_name = 'basic_info/texture_process.html'


class MaterialCateView(TextureView):
    """材料"""
    template_name = 'basic_info/material.html'  # 材料类别页面未找到


class MaterialView(TextureView):
    """配件"""
    template_name = 'basic_info/material.html'


class PositionView(TextureView):
    """职位"""
    template_name = 'basic_info/position.html'


class CurrencyView(TextureView):
    """货币类型"""
    template_name = 'basic_info/currency.html'


class CategoryView(TextureView):
    """材料类别"""
    template_name = 'basic_info/category.html'


class UnitView(TextureView):
    """单位"""
    template_name = 'basic_info/unit.html'


class AreaView(TextureView):
    """区域"""
    template_name = 'basic_info/area.html'


class DepartmentView(TextureView):
    """部门"""
    template_name = 'basic_info/department.html'


class HeadQuarterView(TextureView):
    """总部信息"""
    template_name = 'basic_info/head_quarter.html'


class CompanyView(TextureView):
    """公司信息"""
    template_name = 'basic_info/company.html'


class DeliveryView(TextureView):
    """付款类型"""
    template_name = 'basic_info/delivery.html'


class ExportPortView(TextureView):
    """港口"""
    template_name = 'basic_info/export_port.html'


class ExportTypeView(TextureView):
    """出口类型"""
    template_name = 'basic_info/export_type.html'


class CustomerView(TextureView):
    """客户"""
    template_name = 'basic_info/customer.html'


class CustomerMarkView(TextureView):
    """客户唛头"""
    template_name = 'basic_info/customer_mark.html'


class ExportCountryView(TextureView):
    """进出口国家"""
    template_name = 'basic_info/export_country.html'


class ExportCompanyView(TextureView):
    """进出口公司"""
    template_name = 'basic_info/export_company.html'


class StaffView(TextureView):
    """职工信息"""
    template_name = 'basic_info/staff.html'


class FactoryView(TextureView):
    """工厂"""
    template_name = 'basic_info/factory.html'


class CodeView(TextureView):
    """编码"""
    template_name = 'basic_info/code.html'


class StatusView(TextureView):
    """状态"""
    template_name = 'basic_info/status.html'


class MatrialProcessView(TextureView):
    """材质进度"""
    template_name = 'basic_info/matrial_process.html'
