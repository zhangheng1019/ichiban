"""apple URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from Order.views import *
from .settings import STATIC_URL, MEDIA_ROOT  # 上传媒体加载包
from django.views.static import serve  # 上传媒体加载包

import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

from .test import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),  # 后台管理
    url(r'^$', IndexView.as_view(), name='index'),  # 全局首页
    url(r'^save_language/', save_language_view),  # 存储修改语言接口
    url(r'^get_language/', get_language_view),  # 获取语言session接口
    url(r'^login/', LoginView.as_view(), name='login'),  # 登陆
    url(r'^logout/', logout_view),  # 注销登录
    url(r'^query_factory/', query_factory),  # 根据工厂名字查询工厂信息
    url(r'^basic_info/', include('Basic_info.urls')),  # 基础信息
    url(r'^order/', include('Order.urls')),  # 业务
    url(r'^finance/', include('Finance.urls')),  # 财务
    url(r'^report/', include('Report.urls')),  # 报表
    url(r'^pom/', include('POM.urls')),  # POM
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_URL}),  # 静态文件目录
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),  # 媒体文件目录
    # url(r'^test/', pay_notices),  # 测试导出文件接口
]
