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
    url(r'^texture/', TextureView.as_view()),
    url(r'^texture_process/', TextureProcessView.as_view()),
    url(r'^material_cate/', MaterialCateView.as_view()),
    url(r'^material/', MaterialView.as_view()),
    url(r'^position/', PositionView.as_view()),
    url(r'^currency/', CurrencyView.as_view()),
    url(r'^category/', CategoryView.as_view()),
    url(r'^unit/', UnitView.as_view()),
    url(r'^area/', AreaView.as_view()),
    url(r'^department/', DepartmentView.as_view()),
    url(r'^head_quarter/', HeadQuarterView.as_view()),
    url(r'^company/', CompanyView.as_view()),
    url(r'^delivery/', DeliveryView.as_view()),
    url(r'^export_port/', ExportPortView.as_view()),
    url(r'^export_type/', ExportTypeView.as_view()),
    url(r'^customer/', CustomerView.as_view()),
    url(r'^customer_mark/', CustomerMarkView.as_view()),
    url(r'^export_country/', ExportCountryView.as_view()),
    url(r'^export_company/', ExportCompanyView.as_view()),
    url(r'^staff/', StaffView.as_view()),
    url(r'^factory/', FactoryView.as_view()),
    url(r'^code/', CodeView.as_view()),
    url(r'^status/', StatusView.as_view()),
    url(r'^matrial_process/', MatrialProcessView.as_view()),
]
