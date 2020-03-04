"""automall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from .views import *
from django.urls import path, include

urlpatterns = [
    # 财务合同
    url(r'^pay_notice/', pay_notice),  # 大货付款通知
    url(r'^material_pay/', material_pay),  # 材料付款通知
    url(r'^check_invoice/', check_invoice),  # 核对发票
    # 订单合同
    url(r'^profit_report/', profit_report),  # 利润报表
    url(r'^contract_report_by_id/', contract_report_by_id),  # 主合同
    url(r'^material_sign_report_by_id/', material_sign_report_by_id),  # 配件合同
    url(r'^order_confirmation/', order_confirmation),  # 订单确认信息
    url(r'^product_record/', product_record),  # 生产记录表
]
