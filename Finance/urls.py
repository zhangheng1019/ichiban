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

urlpatterns = [
    url(r'^finance_bill/', finance_bill_view),  # 财务传票
    url(r'^claim_payment/', claim_payment_view),  # 索赔扣款
    url(r'^claim_detail/', claim_detail_view),  # 扣款明细
    url(r'^deduction_detail/', deduction_detail_view),  # 索赔明细
    url(r'^ship_payment/', ship_payment_view),  # 大货付款
    url(r'^accessory_pay/', accessory_pay_view),  # 大货付款
]
