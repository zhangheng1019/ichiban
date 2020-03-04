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
    # 订单所需基础信息
    url(r'^package_texture/', PackageTextureView.as_view()),
    url(r'^package_type/', PackageTypeView.as_view()),
    url(r'^sea_rate/', SeaRateView.as_view()),
    url(r'^develop_function/', DevelopFunctionView.as_view()),
    url(r'^sketch_type/', SketchTypeView.as_view()),
    # 业务
    url(r'^sketch_design/', sketch_design_view),
    url(r'^sketch_develop/', sketch_develop_view),
    url(r'^sketch_detail/', sketch_detail_view),
    url(r'^sample_detail/', sample_detail_view),
    url(r'^item_note/', item_note_view),
    url(r'^item_package/', item_package_view),
    url(r'^factory_quote/', factory_quote_view),
    url(r'^repeat_sample/', repeat_sample_view),
    url(r'^repeat_sample_detail/', repeat_sample_detail_view),
    url(r'^sample_target/', sample_target_view),
    url(r'^po/', po_view),
    url(r'^po_detail/', po_detail_view),
    url(r'^contract/', contract_view),
    url(r'^product_send/', product_send_view),
    url(r'^omr/', omr_view),
    url(r'^omr_po_detail/', omr_po_detail_view),
    url(r'^fmr/', fmr_view),
    url(r'^material_sign/', material_sign_view),
    url(r'^material_sign_detail/', material_sign_detail_view),
    # url(r'^test/', login_required(TestView.as_view()), name='test'),
]
