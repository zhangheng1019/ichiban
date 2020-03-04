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
from .timer import *
from django.urls import path, include


urlpatterns = [
    url(r'^store_reminds/', store_reminds_view),    # 新增提醒事项到数据库
    url(r'^show_reminds/', show_reminds_view),      # 根据用户展示提醒事项
    url(r'^show_all_reminds_detail/', show_all_reminds_detail_view),      # 根据用户展示提醒事项
    url(r'^refresh_status/', refresh_status_view),  # 员工更新事件状态
    url(r'^delay/', delay_view),                    # 员工时间延期
    url(r'^start_timer/', start_timer),             # 开启po数据同步、日常任务定时器任务
    url(r'^stop_timer/', stop_timer),               # 关闭po数据同步、日常任务定时器任务
    url(r'^get_field_data/', get_field_data),       # 获取字段所有列的信息
]
