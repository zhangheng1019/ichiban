import os
from datetime import datetime
from Finance.query_API import *
from Order.query_API import *
from apple.views import *
from Basic_info.models import *
from Order.models import *
from apple.views import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.views.generic.base import View, TemplateView
from django.utils.decorators import method_decorator
# Create your views here.


class IndexView(View):
    """首页视图"""
    template_name = 'order/index.html'

    def get(self, request):
        return render(request, self.template_name, locals())

    # 给当前类的所有实例方法添加登陆装饰器，在验证用户身份后才能访问当前类方法
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class LoginView(IndexView):
    """演示类视图的定义和使用"""
    template_name = 'order/login.html'

    def get(self, request):
        """处理GET请求业务逻辑"""
        # 记录用户登录前所取得地址，用于登陆成功后重定向
        next_url = request.GET.get('next')
        if next_url == '/login/':
            request.session['next_url'] = '/'
        else:
            request.session['next_url'] = next_url  # 存储session信息
        # print('======================================next_url--get', request.session['next_url'])
        return render(request, self.template_name, locals())

    def post(self, request):
        """处理POST请求业务逻辑"""
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # print('====================================request.user.id:', request.user.id)  # 获取当前登录用户
            return HttpResponseRedirect(request.session['next_url'], locals())
        else:
            return HttpResponse('您输入的密码错误或者当前用户不存在，请检查后重新登陆')


@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/', locals())


class PackageTextureView(IndexView):
    """包装材质"""
    template_name = 'order/package_texture.html'

    def post(self, request):
        name = request.POST.get('name')
        edesc = request.POST.get('edesc')
        package_texture = Package_texture.objects.values()
        name_list = [i['name'] for i in package_texture]
        if not name:
            return HttpResponse('材质名字未输入，请输入')
        if name in name_list:
            return HttpResponse('该材质已经存在！')
        info_dict = {
            'name': name,
            'edesc': edesc,
        }
        obj = Package_texture(**info_dict)
        obj.save()
        return HttpResponse('保存%s成功' % name)


class PackageTypeView(IndexView):
    """包装类型"""
    template_name = 'order/package_type.html'


class SeaRateView(IndexView):
    """海关税率"""
    template_name = 'order/sea_rate.html'


class DevelopFunctionView(IndexView):
    """开发产品用途"""
    template_name = 'order/develop_function.html'


class SketchTypeView(IndexView):
    """图稿类型"""
    template_name = 'order/sketch_type.html'


# ↑↑↑↑↑以上为基础资料↑↑↑↑↑
# ↓↓↓↓↓以下为业务逻辑↓↓↓↓↓
@login_required()
def sketch_design_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Staff', 'Category', 'Customer', 'Texture', 'Sketch_type')))
        return render(request, 'order/sketch_design.html', locals())
    else:
        # 实现增删改查等按钮功能
        if 'first' in request.POST:
            try:
                sketch_design = Sketch_design.objects.all().order_by("id").first()
                try:
                    developer = obj_to_json(sketch_design.developer)
                except:
                    developer = {}
                try:
                    designer = obj_to_json(sketch_design.designer)
                except:
                    designer = {}
                try:
                    category = obj_to_json(sketch_design.category)
                except:
                    category = {}
                try:
                    customer = obj_to_json(sketch_design.customer)
                except:
                    customer = {}
                try:
                    texture = obj_to_json(sketch_design.texture)
                except:
                    texture = {}
                try:
                    sketch_type = obj_to_json(sketch_design.sketch_type)
                except:
                    sketch_type = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = 'first'
                data['data'] = {}
                data['data']['sketch_design'] = obj_to_json(sketch_design)
                data['data']['sketch_design']['developer'] = developer
                data['data']['sketch_design']['designer'] = designer
                data['data']['sketch_design']['category'] = category
                data['data']['sketch_design']['customer'] = customer
                data['data']['sketch_design']['texture'] = texture
                data['data']['sketch_design']['sketch_type'] = sketch_type
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '当前表中没有条目'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'last' in request.POST:
            code = request.POST.get('code')  # 不能为空且唯一
            try:
                n = Sketch_design.objects.get(code=code).id
                sketch_design = Sketch_design.objects.all().filter(id__lt=n).order_by("-id").first()
                try:
                    developer = obj_to_json(sketch_design.developer)
                except:
                    developer = {}
                try:
                    designer = obj_to_json(sketch_design.designer)
                except:
                    designer = {}
                try:
                    category = obj_to_json(sketch_design.category)
                except:
                    category = {}
                try:
                    customer = obj_to_json(sketch_design.customer)
                except:
                    customer = {}
                try:
                    texture = obj_to_json(sketch_design.texture)
                except:
                    texture = {}
                try:
                    sketch_type = obj_to_json(sketch_design.sketch_type)
                except:
                    sketch_type = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = 'last'
                data['data'] = {}
                data['data']['sketch_design'] = obj_to_json(sketch_design)
                data['data']['sketch_design']['developer'] = developer
                data['data']['sketch_design']['designer'] = designer
                data['data']['sketch_design']['category'] = category
                data['data']['sketch_design']['customer'] = customer
                data['data']['sketch_design']['texture'] = texture
                data['data']['sketch_design']['sketch_type'] = sketch_type
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '当前条目不存在'})
            except AttributeError:
                return JsonResponse({'status': 'fail', 'msg': '当前条目已是第一条'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'next' in request.POST:
            code = request.POST.get('code')  # 不能为空且唯一
            try:
                n = Sketch_design.objects.get(code=code).id
                sketch_design = Sketch_design.objects.all().filter(id__gt=n).order_by("id").first()
                try:
                    developer = obj_to_json(sketch_design.developer)
                except:
                    developer = {}
                try:
                    designer = obj_to_json(sketch_design.designer)
                except:
                    designer = {}
                try:
                    category = obj_to_json(sketch_design.category)
                except:
                    category = {}
                try:
                    customer = obj_to_json(sketch_design.customer)
                except:
                    customer = {}
                try:
                    texture = obj_to_json(sketch_design.texture)
                except:
                    texture = {}
                try:
                    sketch_type = obj_to_json(sketch_design.sketch_type)
                except:
                    sketch_type = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = 'next'
                data['data'] = {}
                data['data']['sketch_design'] = obj_to_json(sketch_design)
                data['data']['sketch_design']['developer'] = developer
                data['data']['sketch_design']['designer'] = designer
                data['data']['sketch_design']['category'] = category
                data['data']['sketch_design']['customer'] = customer
                data['data']['sketch_design']['texture'] = texture
                data['data']['sketch_design']['sketch_type'] = sketch_type
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '当前条目不存在或已是最后一条'})
            except AttributeError:
                return JsonResponse({'status': 'fail', 'msg': '当前条目已是最后一条'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'final' in request.POST:
            try:
                sketch_design = Sketch_design.objects.all().order_by("-id").first()
                try:
                    developer = obj_to_json(sketch_design.developer)
                except:
                    developer = {}
                try:
                    designer = obj_to_json(sketch_design.designer)
                except:
                    designer = {}
                try:
                    category = obj_to_json(sketch_design.category)
                except:
                    category = {}
                try:
                    customer = obj_to_json(sketch_design.customer)
                except:
                    customer = {}
                try:
                    texture = obj_to_json(sketch_design.texture)
                except:
                    texture = {}
                try:
                    sketch_type = obj_to_json(sketch_design.sketch_type)
                except:
                    sketch_type = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = 'final'
                data['data'] = {}
                data['data']['sketch_design'] = obj_to_json(sketch_design)
                data['data']['sketch_design']['developer'] = developer
                data['data']['sketch_design']['designer'] = designer
                data['data']['sketch_design']['category'] = category
                data['data']['sketch_design']['customer'] = customer
                data['data']['sketch_design']['texture'] = texture
                data['data']['sketch_design']['sketch_type'] = sketch_type
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '当前表中没有条目'})
        elif 'add' in request.POST:
            code = request.POST.get('code')  # 不能为空且唯一
            l = [i['code'] for i in Sketch_design.objects.values()]
            if code in l:
                return JsonResponse({'status': 'fail', 'msg': '保存失败，图稿已存在'})
            try:
                sketch_design = sketch_design_add(request)
                data = {}
                data['status'] = 'success'
                data['msg'] = '添加成功'
                return JsonResponse(data)
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'delete' in request.POST:
            code = request.POST.get('code')  # 不能为空且唯一
            try:
                sketch_design = Sketch_design.objects.get(code=code)
                sketch_design.delete()
                return JsonResponse({'status': 'success', 'msg': '图稿删除成功'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '操作的图稿不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'modify' in request.POST:
            code = request.POST.get('code')  # 不能为空且唯一
            try:
                sketch_design = sketch_design_modify(request)
                return JsonResponse({'status': 'success', 'msg': '图稿修改成功'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '操作的图稿不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'view' in request.POST:
            code = request.POST.get('code')  # 不能为空且唯一
            try:
                sketch_design = Sketch_design.objects.get(code=code)
                try:
                    developer = obj_to_json(Staff.objects.get(id=sketch_design.developer.id))
                except:
                    developer = {}
                try:
                    designer = obj_to_json(Staff.objects.get(id=sketch_design.designer.id))
                except:
                    designer = {}
                try:
                    category = obj_to_json(Category.objects.get(id=sketch_design.category.id))
                except:
                    category = {}
                try:
                    customer = obj_to_json(Customer.objects.get(id=sketch_design.customer.id))
                except:
                    customer = {}
                try:
                    texture = obj_to_json(Texture.objects.get(id=sketch_design.texture.id))
                except:
                    texture = {}
                try:
                    sketch_type = obj_to_json(Sketch_type.objects.get(id=sketch_design.sketch_type.id))
                except:
                    sketch_type = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = '查询成功'
                data['data'] = {}
                data['data']['sketch_design'] = obj_to_json(sketch_design)
                data['data']['sketch_design']['developer'] = developer
                data['data']['sketch_design']['designer'] = designer
                data['data']['sketch_design']['category'] = category
                data['data']['sketch_design']['customer'] = customer
                data['data']['sketch_design']['texture'] = texture
                data['data']['sketch_design']['sketch_type'] = sketch_type
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '查询的图稿不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})


@login_required()
def sketch_develop_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Category', 'Staff', 'Customer', 'Department', 'Develop_function')))
        return render(request, 'order/sketch_develop.html', locals())
    else:
        # 实现增删改查等按钮功能
        if 'first' in request.POST:
            # 获取开发单信息
            try:
                sketch_develop = Sketch_develop.objects.all().order_by("id").first()
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}

                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '无开发单数据'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
            # 获取某个开发单下面的所有开发明细单
            try:
                sketch_develop_number = sketch_develop.number
                sketch_detail = Sketch_detail.objects.filter(number=sketch_develop_number)
                # 将detail中的id值转为json对象
                data['data']['sketch_detail'] = {}
                for i in sketch_detail.values():
                    try:
                        customer_currency = obj_to_json(Currency.objects.get(id=i['customer_currency_id']))
                    except:
                        customer_currency = {}
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        factory_currency = obj_to_json(Factory.objects.get(id=i['factory_currency_id']))
                    except:
                        factory_currency = {}
                    try:
                        texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                    except:
                        texture = {}
                    try:
                        fmr_undertake = obj_to_json(Staff.objects.get(id=i['fmr_undertake_id']))
                    except:
                        fmr_undertake = {}
                    data['data']['sketch_detail'][str(i['id'])] = i
                    i['customer_currency_id'] = customer_currency
                    i['factory_id'] = factory
                    i['factory_currency_id'] = factory_currency
                    i['texture_id'] = texture
                    i['fmr_undertake_id'] = fmr_undertake
                return JsonResponse(data)
            except:
                data['data']['sketch_detail'] = {}
                return JsonResponse(data)
        elif 'last' in request.POST:
            number = request.POST.get('number')  # 不能为空且唯一
            # 获取开发单信息
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                n = sketch_develop.id
                sketch_develop = Sketch_develop.objects.all().filter(id__lt=n).order_by("-id").first()
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except:
                return JsonResponse({'status': 'fail', 'msg': '当前条目不存在或已是第一条'})
            # 获取某个开发单下面的所有开发明细单
            try:
                sketch_detail = Sketch_detail.objects.filter(number=sketch_develop.number)
                # 将detail中的id值转为json对象
                data['data']['sketch_detail'] = {}
                for i in sketch_detail.values():
                    try:
                        customer_currency = obj_to_json(Currency.objects.get(id=i['customer_currency_id']))
                    except:
                        customer_currency = {}
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        factory_currency = obj_to_json(Factory.objects.get(id=i['factory_currency_id']))
                    except:
                        factory_currency = {}
                    try:
                        texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                    except:
                        texture = {}
                    try:
                        fmr_undertake = obj_to_json(Staff.objects.get(id=i['fmr_undertake_id']))
                    except:
                        fmr_undertake = {}
                    data['data']['sketch_detail'][str(i['id'])] = i
                    i['customer_currency_id'] = customer_currency
                    i['factory_id'] = factory
                    i['factory_currency_id'] = factory_currency
                    i['texture_id'] = texture
                    i['fmr_undertake_id'] = fmr_undertake
            except:
                data['data']['sketch_detail'] = {}
            return JsonResponse(data)
        elif 'next' in request.POST:
            number = request.POST.get('number')  # 不能为空且唯一
            # 获取开发单信息
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                n = sketch_develop.id
                sketch_develop = Sketch_develop.objects.all().filter(id__gt=n).order_by("id").first()
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except:
                return JsonResponse({'status': 'fail', 'msg': '当前条目不存在或已是最后一条'})
            # 获取某个开发单下面的所有开发明细单
            try:
                sketch_detail = Sketch_detail.objects.filter(number=sketch_develop.number)
                # 将detail中的id值转为json对象
                data['data']['sketch_detail'] = {}
                for i in sketch_detail.values():
                    try:
                        customer_currency = obj_to_json(Currency.objects.get(id=i['customer_currency_id']))
                    except:
                        customer_currency = {}
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        factory_currency = obj_to_json(Factory.objects.get(id=i['factory_currency_id']))
                    except:
                        factory_currency = {}
                    try:
                        texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                    except:
                        texture = {}
                    try:
                        fmr_undertake = obj_to_json(Staff.objects.get(id=i['fmr_undertake_id']))
                    except:
                        fmr_undertake = {}
                    data['data']['sketch_detail'][str(i['id'])] = i
                    i['customer_currency_id'] = customer_currency
                    i['factory_id'] = factory
                    i['factory_currency_id'] = factory_currency
                    i['texture_id'] = texture
                    i['fmr_undertake_id'] = fmr_undertake
            except:
                data['data']['sketch_detail'] = {}
            return JsonResponse(data)
        elif 'final' in request.POST:
            sketch_develop = Sketch_develop.objects.all().order_by("-id").first()
            # 获取开发单信息
            try:
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except:
                return JsonResponse({'status': 'fail', 'msg': '无开发单数据'})
            # 获取某个开发单下面的所有开发明细单
            try:
                sketch_develop_number = sketch_develop.number
                sketch_detail = Sketch_detail.objects.filter(number=sketch_develop_number)
                # 将detail中的id值转为json对象
                data['data']['sketch_detail'] = {}
                for i in sketch_detail.values():
                    try:
                        customer_currency = obj_to_json(Currency.objects.get(id=i['customer_currency_id']))
                    except:
                        customer_currency = {}
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        factory_currency = obj_to_json(Factory.objects.get(id=i['factory_currency_id']))
                    except:
                        factory_currency = {}
                    try:
                        texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                    except:
                        texture = {}
                    try:
                        fmr_undertake = obj_to_json(Staff.objects.get(id=i['fmr_undertake_id']))
                    except:
                        fmr_undertake = {}
                    data['data']['sketch_detail'][str(i['id'])] = i
                    i['customer_currency_id'] = customer_currency
                    i['factory_id'] = factory
                    i['factory_currency_id'] = factory_currency
                    i['texture_id'] = texture
                    i['fmr_undertake_id'] = fmr_undertake
            except:
                data['data']['sketch_detail'] = {}
            return JsonResponse(data)
        elif 'add' in request.POST:
            # 验证开发单是否存在
            number = request.POST.get('number')
            l = [i['number'] for i in Sketch_develop.objects.values()]
            if number in l:
                return JsonResponse({'status': 'fail', 'msg': '开发单已存在'})
            try:
                sketch_develop = sketch_develop_add(request)
                return JsonResponse({'status': 'success', 'msg': '开发单添加成功'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '开发图稿不存在'})
            # except:
            #     return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'delete' in request.POST:
            number = request.POST.get('number')  # 不能为空且唯一
            # 验证开发单是否存在
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                sketch_develop.delete()
                return JsonResponse({'status': 'success', 'msg': '开发单删除成功'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '开发单不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'modify' in request.POST:
            number = request.POST.get('number')  # 不能为空且唯一
            # 验证开发单是否存在
            l = field_list('Sketch_develop', 'number')
            if number not in l:
                return JsonResponse({'status': 'fail', 'msg': '开发单不存在'})
            try:
                sketch_develop = sketch_develop_modify(request)
                return JsonResponse({'status': 'success', 'msg': '开发单修改成功'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '开发单不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'view' in request.POST:
            number = request.POST.get('number')  # 不能为空且唯一
            # 获取开发单信息
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}
                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except:
                return JsonResponse({'status': 'fail', 'msg': '无开发单数据'})
            # 获取某个开发单下面的所有开发明细单
            try:
                sketch_develop_number = sketch_develop.number
                sketch_detail = Sketch_detail.objects.filter(number=sketch_develop_number)
                # 将detail中的id值转为json对象
                data['data']['sketch_detail'] = {}
                for i in sketch_detail.values():
                    try:
                        customer_currency = obj_to_json(Currency.objects.get(id=i['customer_currency_id']))
                    except:
                        customer_currency = {}
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        factory_currency = obj_to_json(Factory.objects.get(id=i['factory_currency_id']))
                    except:
                        factory_currency = {}
                    try:
                        texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                    except:
                        texture = {}
                    try:
                        fmr_undertake = obj_to_json(Staff.objects.get(id=i['fmr_undertake_id']))
                    except:
                        fmr_undertake = {}
                    data['data']['sketch_detail'][str(i['id'])] = i
                    i['customer_currency_id'] = customer_currency
                    i['factory_id'] = factory
                    i['factory_currency_id'] = factory_currency
                    i['texture_id'] = texture
                    i['fmr_undertake_id'] = fmr_undertake
            except:
                data['data']['sketch_detail'] = {}
            return JsonResponse(data)


@login_required()
def sketch_detail_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Currency', 'Factory', 'Staff', 'Customer', 'Texture')))
        return render(request, 'order/sketch_detail.html', locals())
    else:
        # 实现增删改查等按钮功能
        if 'first' in request.POST:
            # 获取开发单信息
            number = request.POST.get('number')  # 不能为空且唯一
            print('==============================', number)
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}

                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '无开发单数据'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
            # 获取开发单详情信息
            try:
                sketch_detail = Sketch_detail.objects.filter(number=number).order_by("id").first()
                try:
                    customer_currency = obj_to_json(sketch_detail.customer_currency)
                except:
                    customer_currency = {}
                try:
                    factory = obj_to_json(sketch_detail.factory)
                except:
                    factory = {}
                try:
                    factory_currency = obj_to_json(sketch_detail.factory_currency)
                except:
                    factory_currency = {}
                try:
                    texture = obj_to_json(sketch_detail.texture)
                except:
                    texture = {}
                try:
                    fmr_undertake = obj_to_json(sketch_detail.fmr_undertake)
                except:
                    fmr_undertake = {}
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '无数据'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
            data['data']['sketch_detail'] = obj_to_json(sketch_detail)
            data['data']['sketch_detail']['customer_currency'] = customer_currency
            data['data']['sketch_detail']['factory'] = factory
            data['data']['sketch_detail']['factory_currency'] = factory_currency
            data['data']['sketch_detail']['texture'] = texture
            data['data']['sketch_detail']['fmr_undertake'] = fmr_undertake
            return JsonResponse(data)
        elif 'last' in request.POST:
            item_number = request.POST.get('item_number')  # 不能为空且唯一
            number = request.POST.get('number')  # 不能为空且唯一
            # 获取开发单信息
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}

                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '无开发单数据'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
            # 获取开发单详情信息
            # 获取当前页面开发单详情的id
            try:
                number = Sketch_develop.objects.get(number=number)
                n = Sketch_detail.objects.get(number=number, item_number=item_number).id
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '图稿号或item号不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
            # 获取开发单详情的上一条的信息
            try:
                sketch_detail = Sketch_detail.objects.all().filter(number=number, id__lt=n).order_by("-id").first()
                data['data']['sketch_detail'] = obj_to_json(sketch_detail)
            except:
                return JsonResponse({'status': 'fail', 'msg': '当前item不存在或已是第一条'})
            # python对象转json对象
            try:
                customer_currency = obj_to_json(sketch_detail.customer_currency)
            except:
                customer_currency = {}
            try:
                factory = obj_to_json(sketch_detail.factory)
            except:
                factory = {}
            try:
                factory_currency = obj_to_json(sketch_detail.factory_currency)
            except:
                factory_currency = {}
            try:
                texture = obj_to_json(sketch_detail.texture)
            except:
                texture = {}
            try:
                fmr_undertake = obj_to_json(sketch_detail.fmr_undertake)
            except:
                fmr_undertake = {}
            # 构建json
            data['data']['sketch_detail']['customer_currency'] = customer_currency
            data['data']['sketch_detail']['factory'] = factory
            data['data']['sketch_detail']['factory_currency'] = factory_currency
            data['data']['sketch_detail']['texture'] = texture
            data['data']['sketch_detail']['fmr_undertake'] = fmr_undertake
            return JsonResponse(data)
        elif 'next' in request.POST:
            item_number = request.POST.get('item_number')  # 不能为空且唯一
            number = request.POST.get('number')  # 不能为空且唯一
            # 获取开发单信息
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}

                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '无开发单数据'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
            # 获取开发单详情信息
            # 获取当前开发单详情的id
            try:
                number = Sketch_develop.objects.get(number=number)
                n = Sketch_detail.objects.get(number=number, item_number=item_number).id
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '图稿号或item号不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
            # 获取当前条目的下一条目的信息
            try:
                sketch_detail = Sketch_detail.objects.all().filter(number=number, id__gt=n).order_by("id").first()
                data['data']['sketch_detail'] = obj_to_json(sketch_detail)
            except:
                return JsonResponse({'status': 'fail', 'msg': '当前item不存在或已是最后一条'})
            # python对象转json对象
            try:
                customer_currency = obj_to_json(sketch_detail.customer_currency)
            except:
                customer_currency = {}
            try:
                factory = obj_to_json(sketch_detail.factory)
            except:
                factory = {}
            try:
                factory_currency = obj_to_json(sketch_detail.factory_currency)
            except:
                factory_currency = {}
            try:
                texture = obj_to_json(sketch_detail.texture)
            except:
                texture = {}
            try:
                fmr_undertake = obj_to_json(sketch_detail.fmr_undertake)
            except:
                fmr_undertake = {}

            data['data']['sketch_detail']['customer_currency'] = customer_currency
            data['data']['sketch_detail']['factory'] = factory
            data['data']['sketch_detail']['factory_currency'] = factory_currency
            data['data']['sketch_detail']['texture'] = texture
            data['data']['sketch_detail']['fmr_undertake'] = fmr_undertake
            return JsonResponse(data)
        elif 'final' in request.POST:
            # 获取开发单信息
            number = request.POST.get('number')  # 不能为空且唯一
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}

                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '无开发单数据'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
            # 获取开发单详情信息
            try:
                sketch_detail = Sketch_detail.objects.filter(number=number).order_by("-id").first()
                # python对象转json对象
                try:
                    customer_currency = obj_to_json(sketch_detail.customer_currency)
                except:
                    customer_currency = {}
                try:
                    factory = obj_to_json(sketch_detail.factory)
                except:
                    factory = {}
                try:
                    factory_currency = obj_to_json(sketch_detail.factory_currency)
                except:
                    factory_currency = {}
                try:
                    texture = obj_to_json(sketch_detail.texture)
                except:
                    texture = {}
                try:
                    fmr_undertake = obj_to_json(sketch_detail.fmr_undertake)
                except:
                    fmr_undertake = {}
                # 构建json对象信息
                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_detail'] = obj_to_json(sketch_detail)
                data['data']['sketch_detail']['customer_currency'] = customer_currency
                data['data']['sketch_detail']['factory'] = factory
                data['data']['sketch_detail']['factory_currency'] = factory_currency
                data['data']['sketch_detail']['texture'] = texture
                data['data']['sketch_detail']['fmr_undertake'] = fmr_undertake
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '无数据'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'add' in request.POST:
            number = request.POST.get('number')
            item_number = request.POST.get('item_number')
            # 验证开发单是否存在
            l = field_list('Sketch_develop', 'number')
            try:
                l1 = [i['item_number'] for i in Sketch_detail.objects.all().filter(number=number).values()]
            except:
                l1 = []
            if number not in l:
                return JsonResponse({'status': 'fail', 'msg': '开发总单不存在'})
            if item_number in l1:
                return JsonResponse({'status': 'fail', 'msg': '开发单明细已存在'})
            try:
                sketch_detail_info = sketch_detail_add(request)
                return JsonResponse({'status': 'success', 'msg': '开发单明细添加成功'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'delete' in request.POST:
            number = request.POST.get('number')  # 不能为空且唯一
            item_number = request.POST.get('item_number')
            l = field_list('Sketch_develop', 'number')
            if number not in l:
                return JsonResponse({'status': 'fail', 'msg': '开发总单不存在'})
            try:
                l1 = [i['item_number'] for i in Sketch_detail.objects.all().filter(number=number).values()]
            except:
                l1 = []
            if item_number not in l1:
                return JsonResponse({'status': 'fail', 'msg': '开发单明细不存在'})
            try:
                sketch_detail = Sketch_detail.objects.get(number=number, item_number=item_number)
                sketch_detail.delete()
                return JsonResponse({'status': 'success', 'msg': '开发单明细删除成功'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '开发单明细不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'modify' in request.POST:
            number = request.POST.get('number')  # 不能为空且唯一
            item_number = request.POST.get('item_number')
            l = field_list('Sketch_develop', 'number')
            if number not in l:
                return JsonResponse({'status': 'fail', 'msg': '开发总单不存在'})
            try:
                l1 = [i['item_number'] for i in Sketch_detail.objects.all().filter(number=number).values()]
            except:
                l1 = []
            if item_number not in l1:
                return JsonResponse({'status': 'fail', 'msg': '开发单明细不存在'})
            try:
                sketch_develop = sketch_detail_modify(request)
                return JsonResponse({'status': 'success', 'msg': '开发单明细修改成功'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '删除对象不存在'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        elif 'view' in request.POST:
            number = request.POST.get('number')  # 不能为空且唯一
            item_number = request.POST.get('item_number')
            l = field_list('Sketch_develop', 'number')
            if number not in l:
                return JsonResponse({'status': 'fail', 'msg': '开发总单不存在'})
            try:
                l1 = [i['item_number'] for i in Sketch_detail.objects.all().filter(number=number).values()]
            except:
                l1 = []
            if item_number not in l1:
                return JsonResponse({'status': 'fail', 'msg': '开发单明细不存在'})

            # 获取开发单信息
            try:
                sketch_develop = Sketch_develop.objects.get(number=number)
                # 将develop中的id值转为json对象
                try:
                    category = obj_to_json(sketch_develop.category)
                except:
                    category = {}
                try:
                    developer = obj_to_json(sketch_develop.developer)
                except:
                    developer = {}
                try:
                    department = obj_to_json(sketch_develop.department)
                except:
                    department = {}
                try:
                    function = obj_to_json(sketch_develop.function)
                except:
                    function = {}
                try:
                    undertake = obj_to_json(sketch_develop.undertake)
                except:
                    undertake = {}
                try:
                    customer = obj_to_json(sketch_develop.customer)
                except:
                    customer = {}

                data = {}
                data['status'] = 'success'
                data['msg'] = '成功'
                data['data'] = {}
                data['data']['sketch_develop'] = obj_to_json(sketch_develop)
                data['data']['sketch_develop']['category'] = category
                data['data']['sketch_develop']['developer'] = developer
                data['data']['sketch_develop']['department'] = department
                data['data']['sketch_develop']['function'] = function
                data['data']['sketch_develop']['undertake'] = undertake
                data['data']['sketch_develop']['customer'] = customer
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'fail', 'msg': '无开发单数据'})
            except:
                return JsonResponse({'status': 'unknown', 'msg': '未知错误'})

            # 根据number和item_number查询开发详情信息
            try:
                sketch_detail = Sketch_detail.objects.get(number=number, item_number=item_number)
                # python对象转json对象
                try:
                    customer_currency = obj_to_json(sketch_detail.customer_currency)
                except:
                    customer_currency = {}
                try:
                    factory = obj_to_json(sketch_detail.factory)
                except:
                    factory = {}
                try:
                    factory_currency = obj_to_json(sketch_detail.factory_currency)
                except:
                    factory_currency = {}
                try:
                    texture = obj_to_json(sketch_detail.texture)
                except:
                    texture = {}
                try:
                    fmr_undertake = obj_to_json(sketch_detail.fmr_undertake)
                except:
                    fmr_undertake = {}
                # 构建json对象信息
                data['data']['sketch_detail'] = obj_to_json(sketch_detail)
                data['data']['sketch_detail']['customer_currency'] = customer_currency
                data['data']['sketch_detail']['factory'] = factory
                data['data']['sketch_detail']['factory_currency'] = factory_currency
                data['data']['sketch_detail']['texture'] = texture
                data['data']['sketch_detail']['fmr_undertake'] = fmr_undertake
                return JsonResponse(data)
            except:
                return JsonResponse({'status': 'fail', 'msg': '查询对象不存在'})


@login_required()
def sample_detail_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Category', 'Texture', 'Staff', 'Company')))
        return render(request, 'order/sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        # 获取样品详情信息
        try:
            sample_detail = Sample_detail.objects.all().order_by('id').first()
            # 样品注释信息
            try:
                item_note = queryset_to_json(Item_note.objects.filter(sample=sample_detail.item_no))
            except:
                item_note = {}
            data = {}
            data['data'] = {}
            data['data']['item_note'] = item_note
            # 样品包装信息
            try:
                item_package = Item_package.objects.filter(sample=sample_detail.item_no)
                data['data']['item_package'] = {}
                # 将python对象遍历转化为json对象
                for i in item_package.values():
                    try:
                        type = obj_to_json(Package_type.objects.get(id=i['type_id']))
                    except:
                        type = {}
                    try:
                        package_texture = obj_to_json(Package_texture.objects.get(id=i['package_texture_id']))
                    except:
                        package_texture = {}
                    data['data']['item_package'][str(i['id'])] = i
                    i['type_id'] = type
                    i['package_texture_id'] = package_texture
            except:
                item_package = {}
            # 工厂报价信息
            try:
                factory_quote = Factory_quote.objects.filter(sample=sample_detail.item_no)
                data['data']['factory_quote'] = {}
                for i in factory_quote.values():
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        currency = obj_to_json(Factory.objects.get(id=i['currency_id']))
                    except:
                        currency = {}
                    try:
                        pack_texture = obj_to_json(Package_texture.objects.get(id=i['pack_texture_id']))
                    except:
                        pack_texture = {}
                    try:
                        shipping_method = obj_to_json(Delivery.objects.get(id=i['shipping_method_id']))
                    except:
                        shipping_method = {}
                    try:
                        shipping_port = obj_to_json(Export_port.objects.get(id=i['shipping_port_id']))
                    except:
                        shipping_port = {}
                    data['data']['factory_quote'][str(i['id'])] = i
                    i['factory_id'] = factory
                    i['currency_id'] = currency
                    i['pack_texture_id'] = pack_texture
                    i['shipping_method_id'] = shipping_method
                    i['shipping_port_id'] = shipping_port
            except:
                factory_quote = {}
            # 将样品详情中的python对象转化为json对象
            try:
                category = obj_to_json(sample_detail.texture)
            except:
                category = {}
            try:
                texture = obj_to_json(sample_detail.texture)
            except:
                texture = {}
            try:
                omr = obj_to_json(sample_detail.omr)
            except:
                omr = {}
            try:
                fmr = obj_to_json(sample_detail.fmr)
            except:
                fmr = {}
            try:
                company = obj_to_json(sample_detail.company)
            except:
                company = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data']['sample_detail'] = obj_to_json(sample_detail)
            data['data']['sample_detail']['category'] = category
            data['data']['sample_detail']['texture'] = texture
            data['data']['sample_detail']['omr'] = omr
            data['data']['sample_detail']['fmr'] = fmr
            data['data']['sample_detail']['company'] = company
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        item_no = request.POST.get('item_no')
        # 获取样品详情信息
        try:
            n = Sample_detail.objects.get(item_no=item_no).id
            sample_detail = Sample_detail.objects.all().filter(id__lt=n).order_by("-id").first()
           # 样品注释
            try:
                item_note = queryset_to_json(Item_note.objects.filter(sample=sample_detail.item_no))
            except:
                item_note = {}
            data = {}
            data['data'] = {}
            data['data']['item_note'] = item_note
            # 样品包装
            try:
                item_package = Item_package.objects.filter(sample=sample_detail.item_no)
                data['data']['item_package'] = {}
                for i in item_package.values():
                    try:
                        type = obj_to_json(Package_type.objects.get(id=i['type_id']))
                    except:
                        type = {}
                    try:
                        package_texture = obj_to_json(Package_texture.objects.get(id=i['package_texture_id']))
                    except:
                        package_texture = {}
                    data['data']['item_package'][str(i['id'])] = i
                    i['type_id'] = type
                    i['package_texture_id'] = package_texture
            except:
                item_package = {}
            # 工厂报价信息
            try:
                factory_quote = Factory_quote.objects.filter(sample=sample_detail.item_no)
                data['data']['factory_quote'] = {}
                # 将python对象遍历转化为json对象
                for i in factory_quote.values():
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        currency = obj_to_json(Factory.objects.get(id=i['currency_id']))
                    except:
                        currency = {}
                    try:
                        pack_texture = obj_to_json(Package_texture.objects.get(id=i['pack_texture_id']))
                    except:
                        pack_texture = {}
                    try:
                        shipping_method = obj_to_json(Delivery.objects.get(id=i['shipping_method_id']))
                    except:
                        shipping_method = {}
                    try:
                        shipping_port = obj_to_json(Export_port.objects.get(id=i['shipping_port_id']))
                    except:
                        shipping_port = {}
                    data['data']['factory_quote'][str(i['id'])] = i
                    i['factory_id'] = factory
                    i['currency_id'] = currency
                    i['pack_texture_id'] = pack_texture
                    i['shipping_method_id'] = shipping_method
                    i['shipping_port_id'] = shipping_port
            except:
                factory_quote = {}
            # 将样品详情中的python对象转化为json对象
            try:
                category = obj_to_json(sample_detail.texture)
            except:
                category = {}
            try:
                texture = obj_to_json(sample_detail.texture)
            except:
                texture = {}
            try:
                omr = obj_to_json(sample_detail.omr)
            except:
                omr = {}
            try:
                fmr = obj_to_json(sample_detail.fmr)
            except:
                fmr = {}
            try:
                company = obj_to_json(sample_detail.company)
            except:
                company = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data']['sample_detail'] = obj_to_json(sample_detail)
            data['data']['sample_detail']['category'] = category
            data['data']['sample_detail']['texture'] = texture
            data['data']['sample_detail']['omr'] = omr
            data['data']['sample_detail']['fmr'] = fmr
            data['data']['sample_detail']['company'] = company
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前item不存在或已是第一条'})
        return JsonResponse(data)
    elif 'next' in request.POST:
        item_no = request.POST.get('item_no')
        # 获取样品详情信息
        try:
            n = Sample_detail.objects.get(item_no=item_no).id
            sample_detail = Sample_detail.objects.all().filter(id__gt=n).order_by('id').first()
            # 样品注释
            try:
                item_note = queryset_to_json(Item_note.objects.filter(sample=sample_detail.item_no))
            except:
                item_note = {}
            data = {}
            data['data'] = {}
            data['data']['item_note'] = item_note
            # 样品包装
            try:
                item_package = Item_package.objects.filter(sample=sample_detail.item_no)
                data['data']['item_package'] = {}
                # 将python对象遍历转化为json对象
                for i in item_package.values():
                    try:
                        type = obj_to_json(Package_type.objects.get(id=i['type_id']))
                    except:
                        type = {}
                    try:
                        package_texture = obj_to_json(Package_texture.objects.get(id=i['package_texture_id']))
                    except:
                        package_texture = {}
                    data['data']['item_package'][str(i['id'])] = i
                    i['type_id'] = type
                    i['package_texture_id'] = package_texture
            except:
                item_package = {}
            # 工厂报价
            try:
                factory_quote = Factory_quote.objects.filter(sample=sample_detail.item_no)
                data['data']['factory_quote'] = {}
                # 将python对象遍历转化为json对象
                for i in factory_quote.values():
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        currency = obj_to_json(Factory.objects.get(id=i['currency_id']))
                    except:
                        currency = {}
                    try:
                        pack_texture = obj_to_json(Package_texture.objects.get(id=i['pack_texture_id']))
                    except:
                        pack_texture = {}
                    try:
                        shipping_method = obj_to_json(Delivery.objects.get(id=i['shipping_method_id']))
                    except:
                        shipping_method = {}
                    try:
                        shipping_port = obj_to_json(Export_port.objects.get(id=i['shipping_port_id']))
                    except:
                        shipping_port = {}
                    data['data']['factory_quote'][str(i['id'])] = i
                    i['factory_id'] = factory
                    i['currency_id'] = currency
                    i['pack_texture_id'] = pack_texture
                    i['shipping_method_id'] = shipping_method
                    i['shipping_port_id'] = shipping_port
            except:
                factory_quote = {}
            # 将样品详情中的python对象转化为json对象
            try:
                category = obj_to_json(sample_detail.texture)
            except:
                category = {}
            try:
                texture = obj_to_json(sample_detail.texture)
            except:
                texture = {}
            try:
                omr = obj_to_json(sample_detail.omr)
            except:
                omr = {}
            try:
                fmr = obj_to_json(sample_detail.fmr)
            except:
                fmr = {}
            try:
                company = obj_to_json(sample_detail.company)
            except:
                company = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data']['sample_detail'] = obj_to_json(sample_detail)
            data['data']['sample_detail']['category'] = category
            data['data']['sample_detail']['texture'] = texture
            data['data']['sample_detail']['omr'] = omr
            data['data']['sample_detail']['fmr'] = fmr
            data['data']['sample_detail']['company'] = company
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前item不存在或已是最后一条'})
        return JsonResponse(data)
    elif 'final' in request.POST:
        try:
            sample_detail = Sample_detail.objects.all().order_by('-id').first()
            # 样品注释
            try:
                item_note = queryset_to_json(Item_note.objects.filter(sample=sample_detail.item_no))
            except:
                item_note = {}
            data = {}
            data['data'] = {}
            data['data']['item_note'] = item_note
            # 样品包装
            try:
                item_package = Item_package.objects.filter(sample=sample_detail.item_no)
                data['data']['item_package'] = {}
                for i in item_package.values():
                    try:
                        type = obj_to_json(Package_type.objects.get(id=i['type_id']))
                    except:
                        type = {}
                    try:
                        package_texture = obj_to_json(Package_texture.objects.get(id=i['package_texture_id']))
                    except:
                        package_texture = {}
                    data['data']['item_package'][str(i['id'])] = i
                    i['type_id'] = type
                    i['package_texture_id'] = package_texture
            except:
                item_package = {}
            # 工厂报价
            try:
                factory_quote = Factory_quote.objects.filter(sample=sample_detail.item_no)
                data['data']['factory_quote'] = {}
                for i in factory_quote.values():
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        currency = obj_to_json(Factory.objects.get(id=i['currency_id']))
                    except:
                        currency = {}
                    try:
                        pack_texture = obj_to_json(Package_texture.objects.get(id=i['pack_texture_id']))
                    except:
                        pack_texture = {}
                    try:
                        shipping_method = obj_to_json(Delivery.objects.get(id=i['shipping_method_id']))
                    except:
                        shipping_method = {}
                    try:
                        shipping_port = obj_to_json(Export_port.objects.get(id=i['shipping_port_id']))
                    except:
                        shipping_port = {}
                    data['data']['factory_quote'][str(i['id'])] = i
                    i['factory_id'] = factory
                    i['currency_id'] = currency
                    i['pack_texture_id'] = pack_texture
                    i['shipping_method_id'] = shipping_method
                    i['shipping_port_id'] = shipping_port
            except:
                factory_quote = {}
            # 将样品详情中python对象转化为json对象
            try:
                category = obj_to_json(sample_detail.texture)
            except:
                category = {}
            try:
                texture = obj_to_json(sample_detail.texture)
            except:
                texture = {}
            try:
                omr = obj_to_json(sample_detail.omr)
            except:
                omr = {}
            try:
                fmr = obj_to_json(sample_detail.fmr)
            except:
                fmr = {}
            try:
                company = obj_to_json(sample_detail.company)
            except:
                company = {}
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data']['sample_detail'] = obj_to_json(sample_detail)
        data['data']['sample_detail']['category'] = category
        data['data']['sample_detail']['texture'] = texture
        data['data']['sample_detail']['omr'] = omr
        data['data']['sample_detail']['fmr'] = fmr
        data['data']['sample_detail']['company'] = company
        return JsonResponse(data)
    elif 'add' in request.POST:
        item_no = request.POST.get('item_no')
        l = field_list('Sample_detail', 'item_no')
        if item_no in l:
            return JsonResponse({'status': 'fail', 'msg': '样品已存在'})
        try:
            sample_detail = sample_detail_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'delete' in request.POST:
        item_no = request.POST.get('item_no')
        try:
            sample_detail = Sample_detail.objects.get(item_no=item_no)
            sample_detail.delete()
            return JsonResponse({'status': 'success', 'msg': '删除成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '样品不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'modify' in request.POST:
        item_no = request.POST.get('item_no')
        l = field_list('Sample_detail', 'item_no')
        if item_no not in l:
            return JsonResponse({'status': 'fail', 'msg': '样品不存在'})
        try:
            sample_detail = sample_detail_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '样品--不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        item_no = request.POST.get('item_no')
        l = field_list('Sample_detail', 'item_no')
        if item_no not in l:
            return JsonResponse({'status': 'fail', 'msg': '样品不存在'})
        try:
            sample_detail = Sample_detail.objects.get(item_no=item_no)
            # 样品注释
            try:
                item_note = queryset_to_json(Item_note.objects.filter(sample=sample_detail.item_no))
            except:
                item_note = {}
            data = {}
            data['data'] = {}
            data['data']['item_note'] = item_note
            # 样品包装
            try:
                item_package = Item_package.objects.filter(sample=sample_detail.item_no)
                data['data']['item_package'] = {}
                for i in item_package.values():
                    try:
                        type = obj_to_json(Package_type.objects.get(id=i['type_id']))
                    except:
                        type = {}
                    try:
                        package_texture = obj_to_json(Package_texture.objects.get(id=i['package_texture_id']))
                    except:
                        package_texture = {}
                    data['data']['item_package'][str(i['id'])] = i
                    i['type_id'] = type
                    i['package_texture_id'] = package_texture
            except:
                item_package = {}
            # 工厂报价
            try:
                factory_quote = Factory_quote.objects.filter(sample=sample_detail.item_no)
                data['data']['factory_quote'] = {}
                for i in factory_quote.values():
                    try:
                        factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                    except:
                        factory = {}
                    try:
                        currency = obj_to_json(Factory.objects.get(id=i['currency_id']))
                    except:
                        currency = {}
                    try:
                        pack_texture = obj_to_json(Package_texture.objects.get(id=i['pack_texture_id']))
                    except:
                        pack_texture = {}
                    try:
                        shipping_method = obj_to_json(Delivery.objects.get(id=i['shipping_method_id']))
                    except:
                        shipping_method = {}
                    try:
                        shipping_port = obj_to_json(Export_port.objects.get(id=i['shipping_port_id']))
                    except:
                        shipping_port = {}
                    data['data']['factory_quote'][str(i['id'])] = i
                    i['factory_id'] = factory
                    i['currency_id'] = currency
                    i['pack_texture_id'] = pack_texture
                    i['shipping_method_id'] = shipping_method
                    i['shipping_port_id'] = shipping_port
            except:
                factory_quote = {}
            # 将样品详情中的pytohn对象转化为json对象
            try:
                category = obj_to_json(sample_detail.texture)
            except:
                category = {}
            try:
                texture = obj_to_json(sample_detail.texture)
            except:
                texture = {}
            try:
                omr = obj_to_json(sample_detail.omr)
            except:
                omr = {}
            try:
                fmr = obj_to_json(sample_detail.fmr)
            except:
                fmr = {}
            try:
                company = obj_to_json(sample_detail.company)
            except:
                company = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data']['sample_detail'] = obj_to_json(sample_detail)
            data['data']['sample_detail']['category'] = category
            data['data']['sample_detail']['texture'] = texture
            data['data']['sample_detail']['omr'] = omr
            data['data']['sample_detail']['fmr'] = fmr
            data['data']['sample_detail']['company'] = company
        except:
            return JsonResponse({'status': 'fail', 'msg': '样品不存在'})
        return JsonResponse(data)


@login_required()
def item_note_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json())
        return render(request, 'order/item_note.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        item_no = request.POST.get('item_no')
        code = request.POST.get('code')
        l = field_list('Sample_detail', 'item_no')
        l1 = [i.code for i in Item_note.objects.filter(sample=item_no)]
        if item_no not in l:
            return JsonResponse({'status': 'fail', 'msg': '样品不存在'})
        if code in l1:
            return JsonResponse({'status': 'fail', 'msg': '注释已存在'})
        try:
            item_note = item_note_add(request)
            return JsonResponse({'status': 'success', 'msg': '注释添加成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'delete' in request.POST:
        pass
    elif 'modify' in request.POST:
        pass
    elif 'view' in request.POST:
        pass


@login_required()
def item_package_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json())
        return render(request, 'order/item_package.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        sample = request.POST.get('sample')
        l = field_list('Sample_detail', 'item_no')
        if sample not in l:
            return JsonResponse({'status': 'fail', 'msg': '样品item_no不存在'})
        try:
            item_package = item_package_add(request)
            return JsonResponse({'status': 'success', 'msg': 'Item包装添加成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'delete' in request.POST:  # 必须在查询后做,或者前端将item_package的id传过来（以便确定唯一条目）
        pass
    elif 'modify' in request.POST:
        pass
    elif 'view' in request.POST:
        pass


@login_required()
def factory_quote_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json())
        return render(request, 'order/item_package.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        try:
            factory_quote = factory_quote_add(request)
            return JsonResponse({'status': 'success', 'msg': 'Item包装添加成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'delete' in request.POST:  # 必须在查询后做,或者前端将item_package的id传过来（以便确定唯一条目）
        pass
    elif 'modify' in request.POST:
        pass
    elif 'view' in request.POST:
        pass


@login_required()
def repeat_sample_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Staff', 'Customer')))
        return render(request, 'order/repeat_sample.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        # 获取repeat_sample信息
        try:
            repeat_sample = Repeat_sample.objects.all().order_by('id').first()
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['repeat_sample'] = obj_to_json(repeat_sample)
            data['data']['repeat_sample']['customer'] = customer
            data['data']['repeat_sample']['undertaker'] = undertaker
        except:
            return JsonResponse({'status': 'fail', 'msg': '无数据'})
        # 将python对象遍历转化为json对象
        # 获取repeat_sample_detail信息
        try:
            repeat_sample_detail = Repeat_sample_detail.objects.filter(number=repeat_sample.number)
            data['data']['repeat_sample_detail'] = {}
            for i in repeat_sample_detail.values():
                try:
                    customer = obj_to_json(Customer.objects.get(id=i['customer_id']))
                except:
                    customer = {}
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                except:
                    factory = {}
                data['data']['repeat_sample_detail'][str(i['id'])] = i
                i['customer_id'] = customer
                i['texture_id'] = texture
                i['factory_id'] = factory
        except:
            repeat_sample_detail = {}
        return JsonResponse(data)
    elif 'last' in request.POST:
        number = request.POST.get('number')
        # 获取repeat_sample信息
        try:
            n = Repeat_sample.objects.get(number=number).id
            repeat_sample = Repeat_sample.objects.all().filter(id__lt=n).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['repeat_sample'] = obj_to_json(repeat_sample)
            data['data']['repeat_sample']['customer'] = customer
            data['data']['repeat_sample']['undertaker'] = undertaker
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # 将python对象遍历转化为json对象
        # 获取repeat_sample_detail信息
        try:
            repeat_sample_detail = Repeat_sample_detail.objects.filter(number=repeat_sample.number)
            data['data']['repeat_sample_detail'] = {}
            for i in repeat_sample_detail.values():
                try:
                    customer = obj_to_json(Customer.objects.get(id=i['customer_id']))
                except:
                    customer = {}
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                except:
                    factory = {}
                data['data']['repeat_sample_detail'][str(i['id'])] = i
                i['customer_id'] = customer
                i['texture_id'] = texture
                i['factory_id'] = factory
        except:
            repeat_sample_detail = {}
        return JsonResponse(data)
    elif 'next' in request.POST:
        number = request.POST.get('number')
        # 获取repeat_sample数据
        try:
            n = Repeat_sample.objects.get(number=number).id
            repeat_sample = Repeat_sample.objects.all().filter(id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['repeat_sample'] = obj_to_json(repeat_sample)
            data['data']['repeat_sample']['customer'] = customer
            data['data']['repeat_sample']['undertaker'] = undertaker
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # 将python对象遍历转化为json对象
        # 获取repeat_sample_detail信息
        try:
            repeat_sample_detail = Repeat_sample_detail.objects.filter(number=repeat_sample.number)
            data['data']['repeat_sample_detail'] = {}
            for i in repeat_sample_detail.values():
                try:
                    customer = obj_to_json(Customer.objects.get(id=i['customer_id']))
                except:
                    customer = {}
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                except:
                    factory = {}
                data['data']['repeat_sample_detail'][str(i['id'])] = i
                i['customer_id'] = customer
                i['texture_id'] = texture
                i['factory_id'] = factory
        except:
            repeat_sample_detail = {}
        return JsonResponse(data)
    elif 'final' in request.POST:
        number = request.POST.get('number')
        # 获取repeat_sample信息
        try:
            repeat_sample = Repeat_sample.objects.all().order_by('-id').first()
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
        except:
            return JsonResponse({'status': 'fail', 'msg': '无数据'})
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['repeat_sample'] = obj_to_json(repeat_sample)
        data['data']['repeat_sample']['customer'] = customer
        data['data']['repeat_sample']['undertaker'] = undertaker
        # 将python对象遍历转化为json对象
        # 获取repeat_sample_detail信息
        try:
            repeat_sample_detail = Repeat_sample_detail.objects.filter(number=repeat_sample.number)
            data['data']['repeat_sample_detail'] = {}
            for i in repeat_sample_detail.values():
                try:
                    customer = obj_to_json(Customer.objects.get(id=i['customer_id']))
                except:
                    customer = {}
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                except:
                    factory = {}
                data['data']['repeat_sample_detail'][str(i['id'])] = i
                i['customer_id'] = customer
                i['texture_id'] = texture
                i['factory_id'] = factory
        except:
            repeat_sample_detail = {}
        return JsonResponse(data)
    elif 'add' in request.POST:
        number = request.POST.get('number')
        l = field_list('Repeat_sample', 'number')
        if number in l:
            return JsonResponse({'status': 'fail', 'msg': '复样已存在'})
        try:
            repeat_sample = repeat_sample_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '发生未知错误，添加失败'})
    elif 'delete' in request.POST:
        number = request.POST.get('number')
        try:
            repeat_sample = Repeat_sample.objects.get(number=number)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '复样不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        repeat_sample.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        number = request.POST.get('number')
        l = field_list('Repeat_sample', 'number')
        if number not in l:
            return JsonResponse({'status': 'fail', 'msg': '复样不存在'})
        try:
            repeat_sample = repeat_sample_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '发生未知错误，修改失败'})
    elif 'view' in request.POST:
        number = request.POST.get('number')
        try:
            repeat_sample = Repeat_sample.objects.get(number=number)
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '复样不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '发生未知错误，查询失败'})
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['repeat_sample'] = obj_to_json(repeat_sample)
        data['data']['repeat_sample']['customer'] = customer
        data['data']['repeat_sample']['undertaker'] = undertaker
        # 将python对象遍历转化为json对象
        try:
            repeat_sample_detail = Repeat_sample_detail.objects.filter(number=repeat_sample.number)
            data['data']['repeat_sample_detail'] = {}
            for i in repeat_sample_detail.values():
                try:
                    customer = obj_to_json(Customer.objects.get(id=i['customer_id']))
                except:
                    customer = {}
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    factory = obj_to_json(Factory.objects.get(id=i['factory_id']))
                except:
                    factory = {}
                data['data']['repeat_sample_detail'][str(i['id'])] = i
                i['customer_id'] = customer
                i['texture_id'] = texture
                i['factory_id'] = factory
        except:
            repeat_sample_detail = {}
        return JsonResponse(data)


@login_required()
def repeat_sample_detail_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Texture', 'Factory')))
        return render(request, 'order/repeat_sample_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        number = request.POST.get('number')
        # sample信息
        try:
            repeat_sample = Repeat_sample.objects.get(number=number)
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
        except:
            return JsonResponse({'status': 'fail', 'msg': '无数据'})
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['repeat_sample'] = obj_to_json(repeat_sample)
        data['data']['repeat_sample']['customer'] = customer
        data['data']['repeat_sample']['undertaker'] = undertaker
        # detail信息
        repeat_sample_detail = Repeat_sample_detail.objects.filter(number=number).order_by('id').first()
        try:
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample_detail.customer)
            except:
                customer = {}
            try:
                texture = obj_to_json(repeat_sample_detail.texture)
            except:
                texture = {}
            try:
                factory = obj_to_json(repeat_sample_detail.factory)
            except:
                factory = {}
            data['data']['repeat_sample_detail'] = obj_to_json(repeat_sample_detail)
            data['data']['repeat_sample_detail']['customer'] = customer
            data['data']['repeat_sample_detail']['texture'] = texture
            data['data']['repeat_sample_detail']['factory'] = factory
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        number = request.POST.get('number')
        item_no = request.POST.get('item_no')
        # sample信息
        try:
            repeat_sample = Repeat_sample.objects.get(number=number)
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
        except:
            return JsonResponse({'status': 'fail', 'msg': '无样品数据'})
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['repeat_sample'] = obj_to_json(repeat_sample)
        data['data']['repeat_sample']['customer'] = customer
        data['data']['repeat_sample']['undertaker'] = undertaker
        # detail信息
        try:
            n = Repeat_sample_detail.objects.get(number=number, item_no=item_no).id
            repeat_sample_detail = Repeat_sample_detail.objects.all().filter(number=number, id__lt=n).order_by('-id').first()
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample_detail.customer)
            except:
                customer = {}
            try:
                texture = obj_to_json(repeat_sample_detail.texture)
            except:
                texture = {}
            try:
                factory = obj_to_json(repeat_sample_detail.factory)
            except:
                factory = {}
            data['data']['repeat_sample_detail'] = obj_to_json(repeat_sample_detail)
            data['data']['repeat_sample_detail']['customer'] = customer
            data['data']['repeat_sample_detail']['texture'] = texture
            data['data']['repeat_sample_detail']['factory'] = factory
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目不存在或已是第一条'})
        return JsonResponse(data)
    elif 'next' in request.POST:
        number = request.POST.get('number')
        item_no = request.POST.get('item_no')
        # sample数据
        try:
            repeat_sample = Repeat_sample.objects.get(number=number)
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
        except:
            return JsonResponse({'status': 'fail', 'msg': '无样品数据'})
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['repeat_sample'] = obj_to_json(repeat_sample)
        data['data']['repeat_sample']['customer'] = customer
        data['data']['repeat_sample']['undertaker'] = undertaker
        # detail数据
        try:
            n = Repeat_sample_detail.objects.get(number=number, item_no=item_no).id
            repeat_sample_detail = Repeat_sample_detail.objects.all().filter(number=number, id__gt=n).order_by('id').first()
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample_detail.customer)
            except:
                customer = {}
            try:
                texture = obj_to_json(repeat_sample_detail.texture)
            except:
                texture = {}
            try:
                factory = obj_to_json(repeat_sample_detail.factory)
            except:
                factory = {}
            data['data']['repeat_sample_detail'] = obj_to_json(repeat_sample_detail)
            data['data']['repeat_sample_detail']['customer'] = customer
            data['data']['repeat_sample_detail']['texture'] = texture
            data['data']['repeat_sample_detail']['factory'] = factory
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目不存在或已是最后一条'})
        return JsonResponse(data)
    elif 'final' in request.POST:
        number = request.POST.get('number')
        # sample信息
        try:
            repeat_sample = Repeat_sample.objects.get(number=number)
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
        except:
            return JsonResponse({'status': 'fail', 'msg': '无样品数据'})
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['repeat_sample'] = obj_to_json(repeat_sample)
        data['data']['repeat_sample']['customer'] = customer
        data['data']['repeat_sample']['undertaker'] = undertaker
        # detail信息
        repeat_sample_detail = Repeat_sample_detail.objects.filter(number=number).order_by('-id').first()
        try:
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample_detail.customer)
            except:
                customer = {}
            try:
                texture = obj_to_json(repeat_sample_detail.texture)
            except:
                texture = {}
            try:
                factory = obj_to_json(repeat_sample_detail.factory)
            except:
                factory = {}
            data['data']['repeat_sample_detail'] = obj_to_json(repeat_sample_detail)
            data['data']['repeat_sample_detail']['customer'] = customer
            data['data']['repeat_sample_detail']['texture'] = texture
            data['data']['repeat_sample_detail']['factory'] = factory
        except:
            return JsonResponse({'status': 'fail', 'msg': '无样品详情数据'})
        return JsonResponse(data)
    elif 'add' in request.POST:
        number = request.POST.get('number')
        item_no = request.POST.get('item_no')
        l = field_list('Repeat_sample', 'number')
        if number not in l:
            return JsonResponse({'status': 'fail', 'msg': '复样单号不存在'})
        l1 = [i['item_no'] for i in Repeat_sample_detail.objects.filter(number=number).values()]
        if item_no in l1:
            return JsonResponse({'status': 'fail', 'msg': '复样明细已存在'})
        try:
            repeat_sample_detail = repeat_sample_detail_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'delete' in request.POST:
        number = request.POST.get('number')
        item_no = request.POST.get('item_no')
        try:
            repeat_sample_detail = Repeat_sample_detail.objects.get(item_no=item_no, number=number)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '复样单号或明细单号不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        repeat_sample_detail.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        number = request.POST.get('number')
        item_no = request.POST.get('item_no')
        l = field_list('Repeat_sample', 'number')
        l1 = [i['item_no'] for i in Repeat_sample_detail.objects.filter(number=number).values()]
        if number not in l:
            return JsonResponse({'status': 'fail', 'msg': '复样单号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': '复样明细不存在'})
        try:
            repeat_sample_detail = repeat_sample_detail_modify(request)
            customer_no = request.POST.get('customer_no')
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '修改失败'})
    elif 'view' in request.POST:
        number = request.POST.get('number')
        item_no = request.POST.get('item_no')
        # sample数据
        # sample信息
        try:
            repeat_sample = Repeat_sample.objects.get(number=number)
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample.customer)
            except:
                customer = {}
            try:
                undertaker = obj_to_json(repeat_sample.undertaker)
            except:
                undertaker = {}
        except:
            return JsonResponse({'status': 'fail', 'msg': '查询数据不存在'})
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['repeat_sample'] = obj_to_json(repeat_sample)
        data['data']['repeat_sample']['customer'] = customer
        data['data']['repeat_sample']['undertaker'] = undertaker
        # detail信息
        try:
            repeat_sample_detail = Repeat_sample_detail.objects.get(item_no=item_no, number=number)
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(repeat_sample_detail.customer)
            except:
                customer = {}
            try:
                texture = obj_to_json(repeat_sample_detail.texture)
            except:
                texture = {}
            try:
                factory = obj_to_json(repeat_sample_detail.factory)
            except:
                factory = {}
            data['data']['repeat_sample_detail'] = obj_to_json(repeat_sample_detail)
            data['data']['repeat_sample_detail']['customer'] = customer
            data['data']['repeat_sample_detail']['texture'] = texture
            data['data']['repeat_sample_detail']['factory'] = factory
        except:
            return JsonResponse({'status': 'fail', 'msg': '查询条目不存在'})
        return JsonResponse(data)


@login_required()
def sample_target_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json())
        return render(request, 'order/sample_target.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        pass
    elif 'last' in request.POST:
        pass
    elif 'next' in request.POST:
        pass
    elif 'final' in request.POST:
        pass
    elif 'add' in request.POST:
        number = request.POST.get('number')
        item_no = request.POST.get('item_no')
        l = [i['number'] for i in Repeat_sample.objects.values()]
        l1 = [i.item_no for i in Repeat_sample_detail.objects.filter(number=number).values()]
        if number not in l:
            return JsonResponse({'status': 'fail', 'msg': '复样单号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': '复样明细不存在'})
        try:
            sample_target = sample_target_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'delete' in request.POST:
        pass
    elif 'modify' in request.POST:
        number = request.POST.get('number')
        item_no = request.POST.get('item_no')
        l = field_list('Repeat_sample', 'number')
        l1 = [i['item_no'] for i in Repeat_sample_detail.objects.filter(number=number).values()]
        if number not in l:
            return JsonResponse({'status': 'fail', 'msg': '复样单号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': '复样明细不存在'})
        try:
            sample_target = sample_target_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        pass


@login_required()
def po_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Customer', 'Delivery', 'Export_port', 'Staff')))
        return render(request, 'order/po.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        po = Po.objects.all().order_by('id').first()
        # Po数据
        try:
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            order_number = po.order_number
            po_detail = Po_detail.objects.filter(po=order_number)
            data['data']['po_detail'] = {}
            # 将python对象遍历转化为json对象
            for i in po_detail.values():
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    currency = obj_to_json(Currency.objects.get(id=i['currency_id']))
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(Package_texture.objects.get(id=i['each_box_id']))
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(Delivery.objects.get(id=i['fac_delivery_id']))
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(Export_port.objects.get(id=i['fac_delivery_port_id']))
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(Staff.objects.get(id=i['fmr_id']))
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(Staff.objects.get(id=i['fqc_id']))
                except:
                    fqc = {}
                data['data']['po_detail'][str(i['id'])] = i
                i['texture_id'] = texture
                i['currency_id'] = currency
                i['each_box_id'] = each_box
                i['fac_delivery_id'] = fac_delivery
                i['fac_delivery_port_id'] = fac_delivery_port
                i['fmr_id'] = fmr
                i['fqc_id'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.filter(po=po.order_number)
            data['data']['contract'] = {}
            for i in contract:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    fac_currency = obj_to_json(i.fac_currency)
                except:
                    fac_currency = {}
                data['data']['contract'][str(i.id)] = obj_to_json(i)
                data['data']['contract'][str(i.id)]['factory'] = factory
                data['data']['contract'][str(i.id)]['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 消出货信息
        try:
            product_send = Product_send.objects.filter(po=po.order_number)
            data['data']['product_send'] = {}
            for i in product_send:
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    qc1 = obj_to_json(i.qc1)
                except:
                    qc1 = {}
                try:
                    qc2 = obj_to_json(i.qc2)
                except:
                    qc2 = {}
                try:
                    qc3 = obj_to_json(i.qc3)
                except:
                    qc3 = {}
                try:
                    rqc1 = obj_to_json(i.rqc1)
                except:
                    rqc1 = {}
                try:
                    rqc2 = obj_to_json(i.rqc2)
                except:
                    rqc2 = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                try:
                    send_person = obj_to_json(i.send_person)
                except:
                    send_person = {}
                data['data']['product_send'][str(i.id)] = obj_to_json(i)
                data['data']['product_send'][str(i.id)]['fmr'] = fmr
                data['data']['product_send'][str(i.id)]['qc1'] = qc1
                data['data']['product_send'][str(i.id)]['qc2'] = qc2
                data['data']['product_send'][str(i.id)]['qc3'] = qc3
                data['data']['product_send'][str(i.id)]['rqc1'] = rqc1
                data['data']['product_send'][str(i.id)]['rqc2'] = rqc2
                data['data']['product_send'][str(i.id)]['fqc'] = fqc
                data['data']['product_send'][str(i.id)]['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('order_number')
        try:
            n = Po.objects.get(order_number=order_number).id
            po = Po.objects.all().filter(id__lt=n).order_by('-id').first()
            num = po.order_number
            # Po数据
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=po.order_number)
            data['data']['po_detail'] = {}
            # 将python对象遍历转化为json对象
            for i in po_detail.values():
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    currency = obj_to_json(Currency.objects.get(id=i['currency_id']))
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(Package_texture.objects.get(id=i['each_box_id']))
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(Delivery.objects.get(id=i['fac_delivery_id']))
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(Export_port.objects.get(id=i['fac_delivery_port_id']))
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(Staff.objects.get(id=i['fmr_id']))
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(Staff.objects.get(id=i['fqc_id']))
                except:
                    fqc = {}
                i['texture_id'] = texture
                i['currency_id'] = currency
                i['each_box_id'] = each_box
                i['fac_delivery_id'] = fac_delivery
                i['fac_delivery_port_id'] = fac_delivery_port
                i['fmr_id'] = fmr
                i['fqc_id'] = fqc
                data['data']['po_detail'][str(i['id'])] = i
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # 合同信息
        try:
            contract = Contract.objects.filter(po=po.order_number)
            data['data']['contract'] = {}
            for i in contract:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    fac_currency = obj_to_json(i.fac_currency)
                except:
                    fac_currency = {}
                data['data']['contract'][str(i.id)] = obj_to_json(i)
                data['data']['contract'][str(i.id)]['factory'] = factory
                data['data']['contract'][str(i.id)]['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 消出货信息
        try:
            product_send = Product_send.objects.filter(po=po.order_number)
            data['data']['product_send'] = {}
            for i in product_send:
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    qc1 = obj_to_json(i.qc1)
                except:
                    qc1 = {}
                try:
                    qc2 = obj_to_json(i.qc2)
                except:
                    qc2 = {}
                try:
                    qc3 = obj_to_json(i.qc3)
                except:
                    qc3 = {}
                try:
                    rqc1 = obj_to_json(i.rqc1)
                except:
                    rqc1 = {}
                try:
                    rqc2 = obj_to_json(i.rqc2)
                except:
                    rqc2 = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                try:
                    send_person = obj_to_json(i.send_person)
                except:
                    send_person = {}
                data['data']['product_send'][str(i.id)] = obj_to_json(i)
                data['data']['product_send'][str(i.id)]['fmr'] = fmr
                data['data']['product_send'][str(i.id)]['qc1'] = qc1
                data['data']['product_send'][str(i.id)]['qc2'] = qc2
                data['data']['product_send'][str(i.id)]['qc3'] = qc3
                data['data']['product_send'][str(i.id)]['rqc1'] = rqc1
                data['data']['product_send'][str(i.id)]['rqc2'] = rqc2
                data['data']['product_send'][str(i.id)]['fqc'] = fqc
                data['data']['product_send'][str(i.id)]['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('order_number')
        try:
            # 获取上一条数据信息
            n = Po.objects.get(order_number=order_number).id
            po = Po.objects.all().filter(id__gt=n).order_by('id').first()
            # Po数据
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=po.order_number)
            data['data']['po_detail'] = {}
            # 将python对象遍历转化为json对象
            for i in po_detail.values():
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    currency = obj_to_json(Currency.objects.get(id=i['currency_id']))
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(Package_texture.objects.get(id=i['each_box_id']))
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(Delivery.objects.get(id=i['fac_delivery_id']))
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(Export_port.objects.get(id=i['fac_delivery_port_id']))
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(Staff.objects.get(id=i['fmr_id']))
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(Staff.objects.get(id=i['fqc_id']))
                except:
                    fqc = {}
                i['texture_id'] = texture
                i['currency_id'] = currency
                i['each_box_id'] = each_box
                i['fac_delivery_id'] = fac_delivery
                i['fac_delivery_port_id'] = fac_delivery_port
                i['fmr_id'] = fmr
                i['fqc_id'] = fqc
                data['data']['po_detail'][str(i['id'])] = i
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # 合同信息
        try:
            contract = Contract.objects.filter(po=po.order_number)
            data['data']['contract'] = {}
            for i in contract:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    fac_currency = obj_to_json(i.fac_currency)
                except:
                    fac_currency = {}
                data['data']['contract'][str(i.id)] = obj_to_json(i)
                data['data']['contract'][str(i.id)]['factory'] = factory
                data['data']['contract'][str(i.id)]['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 消出货信息
        try:
            product_send = Product_send.objects.filter(po=po.order_number)
            data['data']['product_send'] = {}
            for i in product_send:
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    qc1 = obj_to_json(i.qc1)
                except:
                    qc1 = {}
                try:
                    qc2 = obj_to_json(i.qc2)
                except:
                    qc2 = {}
                try:
                    qc3 = obj_to_json(i.qc3)
                except:
                    qc3 = {}
                try:
                    rqc1 = obj_to_json(i.rqc1)
                except:
                    rqc1 = {}
                try:
                    rqc2 = obj_to_json(i.rqc2)
                except:
                    rqc2 = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                try:
                    send_person = obj_to_json(i.send_person)
                except:
                    send_person = {}
                data['data']['product_send'][str(i.id)] = obj_to_json(i)
                data['data']['product_send'][str(i.id)]['fmr'] = fmr
                data['data']['product_send'][str(i.id)]['qc1'] = qc1
                data['data']['product_send'][str(i.id)]['qc2'] = qc2
                data['data']['product_send'][str(i.id)]['qc3'] = qc3
                data['data']['product_send'][str(i.id)]['rqc1'] = rqc1
                data['data']['product_send'][str(i.id)]['rqc2'] = rqc2
                data['data']['product_send'][str(i.id)]['fqc'] = fqc
                data['data']['product_send'][str(i.id)]['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'final' in request.POST:
        po = Po.objects.all().order_by('-id').first()
        try:
            # Po数据
            # 将python对象转化为json对象
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        # po_detail数据
        try:
            order_number = po.order_number
            po_detail = Po_detail.objects.filter(po=order_number)
            data['data']['po_detail'] = {}
            # 将python对象遍历转化为json对象
            for i in po_detail.values():
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    currency = obj_to_json(Currency.objects.get(id=i['currency_id']))
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(Package_texture.objects.get(id=i['each_box_id']))
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(Delivery.objects.get(id=i['fac_delivery_id']))
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(Export_port.objects.get(id=i['fac_delivery_port_id']))
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(Staff.objects.get(id=i['fmr_id']))
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(Staff.objects.get(id=i['fqc_id']))
                except:
                    fqc = {}
                data['data']['po_detail'][str(i['id'])] = i
                i['texture_id'] = texture
                i['currency_id'] = currency
                i['each_box_id'] = each_box
                i['fac_delivery_id'] = fac_delivery
                i['fac_delivery_port_id'] = fac_delivery_port
                i['fmr_id'] = fmr
                i['fqc_id'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.filter(po=po.order_number)
            data['data']['contract'] = {}
            for i in contract:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    fac_currency = obj_to_json(i.fac_currency)
                except:
                    fac_currency = {}
                data['data']['contract'][str(i.id)] = obj_to_json(i)
                data['data']['contract'][str(i.id)]['factory'] = factory
                data['data']['contract'][str(i.id)]['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 消出货信息
        try:
            product_send = Product_send.objects.filter(po=po.order_number)
            data['data']['product_send'] = {}
            for i in product_send:
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    qc1 = obj_to_json(i.qc1)
                except:
                    qc1 = {}
                try:
                    qc2 = obj_to_json(i.qc2)
                except:
                    qc2 = {}
                try:
                    qc3 = obj_to_json(i.qc3)
                except:
                    qc3 = {}
                try:
                    rqc1 = obj_to_json(i.rqc1)
                except:
                    rqc1 = {}
                try:
                    rqc2 = obj_to_json(i.rqc2)
                except:
                    rqc2 = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                try:
                    send_person = obj_to_json(i.send_person)
                except:
                    send_person = {}
                data['data']['product_send'][str(i.id)] = obj_to_json(i)
                data['data']['product_send'][str(i.id)]['fmr'] = fmr
                data['data']['product_send'][str(i.id)]['qc1'] = qc1
                data['data']['product_send'][str(i.id)]['qc2'] = qc2
                data['data']['product_send'][str(i.id)]['qc3'] = qc3
                data['data']['product_send'][str(i.id)]['rqc1'] = rqc1
                data['data']['product_send'][str(i.id)]['rqc2'] = rqc2
                data['data']['product_send'][str(i.id)]['fqc'] = fqc
                data['data']['product_send'][str(i.id)]['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('order_number')
        l = field_list('Po', 'order_number')
        if order_number in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号已存在'})
        try:
            po = po_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('order_number')
        # print('=======================', order_number)
        try:
            po = Po.objects.get(order_number=order_number)
        except:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        po.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('order_number')
        l = field_list('Po', 'order_number')
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        try:
            po = po_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '修改失败'})
    elif 'view' in request.POST:
        order_number = request.POST.get('order_number')
        try:
            po = Po.objects.get(order_number=order_number)
            # Po数据
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '查询的po不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number)
            data['data']['po_detail'] = {}
            # 将python对象遍历转化为json对象
            for i in po_detail.values():
                try:
                    texture = obj_to_json(Texture.objects.get(id=i['texture_id']))
                except:
                    texture = {}
                try:
                    currency = obj_to_json(Currency.objects.get(id=i['currency_id']))
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(Package_texture.objects.get(id=i['each_box_id']))
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(Delivery.objects.get(id=i['fac_delivery_id']))
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(Export_port.objects.get(id=i['fac_delivery_port_id']))
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(Staff.objects.get(id=i['fmr_id']))
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(Staff.objects.get(id=i['fqc_id']))
                except:
                    fqc = {}
                data['data']['po_detail'][str(i['id'])] = i
                i['texture_id'] = texture
                i['currency_id'] = currency
                i['each_box_id'] = each_box
                i['fac_delivery_id'] = fac_delivery
                i['fac_delivery_port_id'] = fac_delivery_port
                i['fmr_id'] = fmr
                i['fqc_id'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.filter(po=po.order_number)
            data['data']['contract'] = {}
            for i in contract:
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    fac_currency = obj_to_json(i.fac_currency)
                except:
                    fac_currency = {}
                data['data']['contract'][str(i.id)] = obj_to_json(i)
                data['data']['contract'][str(i.id)]['factory'] = factory
                data['data']['contract'][str(i.id)]['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 消出货信息
        try:
            product_send = Product_send.objects.filter(po=po.order_number)
            data['data']['product_send'] = {}
            for i in product_send:
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    qc1 = obj_to_json(i.qc1)
                except:
                    qc1 = {}
                try:
                    qc2 = obj_to_json(i.qc2)
                except:
                    qc2 = {}
                try:
                    qc3 = obj_to_json(i.qc3)
                except:
                    qc3 = {}
                try:
                    rqc1 = obj_to_json(i.rqc1)
                except:
                    rqc1 = {}
                try:
                    rqc2 = obj_to_json(i.rqc2)
                except:
                    rqc2 = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                try:
                    send_person = obj_to_json(i.send_person)
                except:
                    send_person = {}
                data['data']['product_send'][str(i.id)] = obj_to_json(i)
                data['data']['product_send'][str(i.id)]['fmr'] = fmr
                data['data']['product_send'][str(i.id)]['qc1'] = qc1
                data['data']['product_send'][str(i.id)]['qc2'] = qc2
                data['data']['product_send'][str(i.id)]['qc3'] = qc3
                data['data']['product_send'][str(i.id)]['rqc1'] = rqc1
                data['data']['product_send'][str(i.id)]['rqc2'] = rqc2
                data['data']['product_send'][str(i.id)]['fqc'] = fqc
                data['data']['product_send'][str(i.id)]['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)


@login_required()
def po_detail_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Texture', 'Currency', 'Package_texture', 'Delivery', 'Export_port', 'Staff')))
        return render(request, 'order/po_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(po=order_number, id__lt=n).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(po=order_number, id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        return JsonResponse(data)
    elif 'final' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号已存在'})
        try:
            po_detail = po_detail_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号不存在'})
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        po_detail.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号不存在'})
        try:
            po_detail = po_detail_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)


@login_required()
def contract_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Factory', 'Currency')))
        return render(request, 'order/contract.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po数据不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(po=order_number, id__lt=n).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(po=order_number, id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'final' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Contract.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 存在这个合同
        if item_no in l2:
            return JsonResponse({'status': 'fail', 'msg': '该合同已存在'})
        try:
            contract = contract_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Contract.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 存在这个合同
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': '该合同不存在'})
        try:
            contract = Contract.objects.filter(po=order_number, item_no=item_no)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        contract.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Contract.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 存在这个合同
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': '该合同不存在'})
        try:
            contract = contract_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)


@login_required()
def product_send_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Staff',)))
        return render(request, 'order/product_send.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'Po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(po=order_number, id__lt=n).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        try:
            # po_detail数据
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(po=order_number, id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'final' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Product_send.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 存在这个合同
        if item_no in l2:
            return JsonResponse({'status': 'fail', 'msg': '该消出货条目已存在'})
        try:
            product_send = product_send_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Product_send.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 存在这个合同
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': '该消出货条目不存在'})
        try:
            product_send = Product_send.objects.filter(po=order_number, item_no=item_no)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        product_send.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Product_send.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 存在这个合同
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': '该消出货条目不存在'})
        try:
            product_send = product_send_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 消出货信息
        try:
            product_send = Product_send.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                fmr = obj_to_json(product_send.fmr)
            except:
                fmr = {}
            try:
                qc1 = obj_to_json(product_send.qc1)
            except:
                qc1 = {}
            try:
                qc2 = obj_to_json(product_send.qc2)
            except:
                qc2 = {}
            try:
                qc3 = obj_to_json(product_send.qc3)
            except:
                qc3 = {}
            try:
                rqc1 = obj_to_json(product_send.rqc1)
            except:
                rqc1 = {}
            try:
                rqc2 = obj_to_json(product_send.rqc2)
            except:
                rqc2 = {}
            try:
                fqc = obj_to_json(product_send.fqc)
            except:
                fqc = {}
            try:
                send_person = obj_to_json(product_send.send_person)
            except:
                send_person = {}
            data['data']['product_send'] = obj_to_json(product_send)
            data['data']['product_send']['fmr'] = fmr
            data['data']['product_send']['qc1'] = qc1
            data['data']['product_send']['qc2'] = qc2
            data['data']['product_send']['qc3'] = qc3
            data['data']['product_send']['rqc1'] = rqc1
            data['data']['product_send']['rqc2'] = rqc2
            data['data']['product_send']['fqc'] = fqc
            data['data']['product_send']['send_person'] = send_person
        except ObjectDoesNotExist:
            data['data']['product_send'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)


@login_required()
def omr_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Staff',)))
        return render(request, 'order/omr.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        # Po数据
        try:
            po = Po.objects.all().order_by("id").first()
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'Po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=po.order_number)
            # 将python对象遍历转化为json对象
            data['data']['po_detail'] = {}
            for i in po_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(i.each_box)
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(i.fac_delivery)
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(i.fac_delivery_port)
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['po_detail'][str(i.id)] = obj_to_json(i)
                obj_to_json(i)['texture'] = texture
                obj_to_json(i)['currency'] = currency
                obj_to_json(i)['each_box'] = each_box
                obj_to_json(i)['fac_delivery'] = fac_delivery
                obj_to_json(i)['fac_delivery_port'] = fac_delivery_port
                obj_to_json(i)['fmr'] = fmr
                obj_to_json(i)['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr注意事项信息
        try:
            omr = OMR.objects.get(po=po.order_number)
            data['data']['omr'] = obj_to_json(omr)
        except ObjectDoesNotExist:
            data['data']['omr'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            n = Po.objects.get(order_number=order_number).id
            po = Po.objects.filter(id__lt=n).order_by("-id").first()
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'Po无数据'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=po.order_number)
            # 将python对象遍历转化为json对象
            data['data']['po_detail'] = {}
            for i in po_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(i.each_box)
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(i.fac_delivery)
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(i.fac_delivery_port)
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['po_detail'][str(i.id)] = obj_to_json(i)
                obj_to_json(i)['texture'] = texture
                obj_to_json(i)['currency'] = currency
                obj_to_json(i)['each_box'] = each_box
                obj_to_json(i)['fac_delivery'] = fac_delivery
                obj_to_json(i)['fac_delivery_port'] = fac_delivery_port
                obj_to_json(i)['fmr'] = fmr
                obj_to_json(i)['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr注意事项信息
        try:
            omr = OMR.objects.get(po=po.order_number)
            data['data']['omr'] = obj_to_json(omr)
        except ObjectDoesNotExist:
            data['data']['omr'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            n = Po.objects.get(order_number=order_number).id
            po = Po.objects.filter(id__gt=n).order_by("id").first()
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'Po无数据'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=po.order_number)
            # 将python对象遍历转化为json对象
            data['data']['po_detail'] = {}
            for i in po_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(i.each_box)
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(i.fac_delivery)
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(i.fac_delivery_port)
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['po_detail'][str(i.id)] = obj_to_json(i)
                obj_to_json(i)['texture'] = texture
                obj_to_json(i)['currency'] = currency
                obj_to_json(i)['each_box'] = each_box
                obj_to_json(i)['fac_delivery'] = fac_delivery
                obj_to_json(i)['fac_delivery_port'] = fac_delivery_port
                obj_to_json(i)['fmr'] = fmr
                obj_to_json(i)['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': 'po_detail未知错误'})
        # omr注意事项信息
        try:
            omr = OMR.objects.get(po=po.order_number)
            data['data']['omr'] = obj_to_json(omr)
        except ObjectDoesNotExist:
            data['data']['omr'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': 'omr未知错误'})
        return JsonResponse(data)
    elif 'final' in request.POST:
        # Po数据
        try:
            po = Po.objects.all().order_by("-id").first()
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'Po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=po.order_number)
            # 将python对象遍历转化为json对象
            data['data']['po_detail'] = {}
            for i in po_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(i.each_box)
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(i.fac_delivery)
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(i.fac_delivery_port)
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['po_detail'][str(i.id)] = obj_to_json(i)
                obj_to_json(i)['texture'] = texture
                obj_to_json(i)['currency'] = currency
                obj_to_json(i)['each_box'] = each_box
                obj_to_json(i)['fac_delivery'] = fac_delivery
                obj_to_json(i)['fac_delivery_port'] = fac_delivery_port
                obj_to_json(i)['fmr'] = fmr
                obj_to_json(i)['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr注意事项信息
        try:
            omr = OMR.objects.get(po=po.order_number)
            data['data']['omr'] = obj_to_json(omr)
        except ObjectDoesNotExist:
            data['data']['omr'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('po')
        l = field_list("Po", "order_number")
        l1 = field_list("OMR", "po")
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 存在这个omr条目
        if order_number in l1:
            return JsonResponse({'status': 'fail', 'msg': '该omr条目已存在'})
        try:
            omr = omr_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('po')
        l = field_list("Po", "order_number")
        l1 = field_list("OMR", "po")
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 不存在这个omr条目
        if order_number not in l1:
            return JsonResponse({'status': 'fail', 'msg': '该omr条目不存在'})
        try:
            omr = OMR.objects.filter(po=order_number)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        omr.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('po')
        l = field_list("Po", "order_number")
        l1 = field_list("OMR", "po")
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 不存在这个omr条目
        if order_number not in l1:
            return JsonResponse({'status': 'fail', 'msg': '该omr条目不存在'})
        try:
            omr = omr_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=po.order_number)
            # 将python对象遍历转化为json对象
            data['data']['po_detail'] = {}
            for i in po_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    currency = obj_to_json(i.currency)
                except:
                    currency = {}
                try:
                    each_box = obj_to_json(i.each_box)
                except:
                    each_box = {}
                try:
                    fac_delivery = obj_to_json(i.fac_delivery)
                except:
                    fac_delivery = {}
                try:
                    fac_delivery_port = obj_to_json(i.fac_delivery_port)
                except:
                    fac_delivery_port = {}
                try:
                    fmr = obj_to_json(i.fmr)
                except:
                    fmr = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['po_detail'][str(i.id)] = obj_to_json(i)
                obj_to_json(i)['texture'] = texture
                obj_to_json(i)['currency'] = currency
                obj_to_json(i)['each_box'] = each_box
                obj_to_json(i)['fac_delivery'] = fac_delivery
                obj_to_json(i)['fac_delivery_port'] = fac_delivery_port
                obj_to_json(i)['fmr'] = fmr
                obj_to_json(i)['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr注意事项信息
        try:
            omr = OMR.objects.get(po=po.order_number)
            data['data']['omr'] = obj_to_json(omr)
        except ObjectDoesNotExist:
            data['data']['omr'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)


@login_required()
def omr_po_detail_view(request):
    if request.method == 'GET':
        data = json.dumps(basic_info_json())
        return render(request, 'order/omr_po_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=po_detail.item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id  # 当前条目
            po_detail = Po_detail.objects.filter(po=order_number, id__lt=n).order_by("-id").first()  # 前一条目
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            # 信息取自po_detail的每个item以及Po的合同中
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=po_detail.item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        try:
            # Po数据
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        try:
            # po_detail数据
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(po=order_number, id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=po_detail.item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'final' in request.POST:
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=po_detail.item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in OMR_po_detail.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 已存在这个omr_po_detail
        if item_no in l2:
            return JsonResponse({'status': 'fail', 'msg': '该omr_po_detail已存在'})
        try:
            omr_po_detail = omr_po_detail_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in OMR_po_detail.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 不存在这个合同
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': '该omr_po_detail不存在'})
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=item_no)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        omr_po_detail.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in OMR_po_detail.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 不存在这个omr_po_detail
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': '该omr_po_detail不存在'})
        try:
            omr_po_detail = omr_po_detail_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)


@login_required()
def fmr_view(request):
    if request.method == 'GET':
        data = {}
        data['status'] = 'success'
        data['msg'] = '成功'
        data['data'] = {}
        data['data']['texture_process'] = basic_info_json(('Texture_process',))

        data['data']['fmr_info'] = {}
        po_detail = Po_detail.objects.all()
        for i in po_detail:
            po_ = Po.objects.get(order_number=i.po)
            contract = Contract.objects.get(po=i.po, item_no=i.item_no)
            try:
                fac_name = contract.factory.name
            except:
                fac_name = ''
            try:
                texture_name = i.texture.name
            except:
                texture_name = ''

            data['data']['fmr_info'][str(i.id)] = {
                'po': i.po,
                'item_no': i.item_no,
                'receive_date': po_.receive_date,
                'fac_send_date': po_.fac_send_date,
                'name': i.desc,
                'amount': i.amount,
                'unit': i.unit,
                'factory': fac_name,
                'oa_sure_date': contract.oa_sure_date,
                'texture': texture_name,
            }
        # return JsonResponse(data)

        # Po数据
        # try:
        #     po = Po.objects.all()
        #     data['data']['po'] = {}
        #     for i in po:
        #         try:
        #             customer = obj_to_json(i.customer)
        #         except:
        #             customer = {}
        #         try:
        #             delivery_condition = obj_to_json(i.delivery_condition)
        #         except:
        #             delivery_condition = {}
        #         try:
        #             port = obj_to_json(i.port)
        #         except:
        #             port = {}
        #         try:
        #             omr = obj_to_json(i.omr)
        #         except:
        #             omr = {}
        #         data['data']['po'][str(i.id)] = obj_to_json(i)
        #         data['data']['po'][str(i.id)]['delivery_condition'] = delivery_condition
        #         data['data']['po'][str(i.id)]['port'] = port
        #         data['data']['po'][str(i.id)]['omr'] = omr
        # except ObjectDoesNotExist:
        #     return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        # except:
        #     return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # # po_detail数据
        # try:
        #     po_detail = Po_detail.objects.all()
        #     # 将python对象转化为json对象
        #     data['data']['po_detail'] = {}
        #     for i in po_detail:
        #         try:
        #             texture = obj_to_json(i.texture)
        #         except:
        #             texture = {}
        #         try:
        #             currency = obj_to_json(i.currency)
        #         except:
        #             currency = {}
        #         try:
        #             each_box = obj_to_json(i.each_box)
        #         except:
        #             each_box = {}
        #         try:
        #             fac_delivery = obj_to_json(i.fac_delivery)
        #         except:
        #             fac_delivery = {}
        #         try:
        #             fac_delivery_port = obj_to_json(i.fac_delivery_port)
        #         except:
        #             fac_delivery_port = {}
        #         try:
        #             fmr = obj_to_json(i.fmr)
        #         except:
        #             fmr = {}
        #         try:
        #             fqc = obj_to_json(i.fqc)
        #         except:
        #             fqc = {}
        #         data['data']['po_detail'][str(i.id)] = obj_to_json(i)
        #         data['data']['po_detail'][str(i.id)]['texture'] = texture
        #         data['data']['po_detail'][str(i.id)]['currency'] = currency
        #         data['data']['po_detail'][str(i.id)]['each_box'] = each_box
        #         data['data']['po_detail'][str(i.id)]['fac_delivery'] = fac_delivery
        #         data['data']['po_detail'][str(i.id)]['fac_delivery_port'] = fac_delivery_port
        #         data['data']['po_detail'][str(i.id)]['fmr'] = fmr
        #         data['data']['po_detail'][str(i.id)]['fqc'] = fqc
        # except ObjectDoesNotExist:
        #     return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        # except:
        #     return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # # 合同信息
        # try:
        #     contract = Contract.objects.all()
        #     data['data']['contract'] = {}
        #     for i in contract:
        #         try:
        #             factory = obj_to_json(i.factory)
        #         except:
        #             factory = {}
        #         try:
        #             fac_currency = obj_to_json(i.fac_currency)
        #         except:
        #             fac_currency = {}
        #         data['data']['contract'][str(i.id)] = obj_to_json(i)
        #         data['data']['contract'][str(i.id)]['factory'] = factory
        #         data['data']['contract'][str(i.id)]['fac_currency'] = fac_currency
        # except ObjectDoesNotExist:
        #     data['data']['contract'] = {}
        # except:
        #     return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return render(request, 'order/fmr.html', locals())
    if 'first' in request.POST:  # 写入不用
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=po_detail.item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'last' in request.POST:  # 写入不用
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id  # 当前条目
            po_detail = Po_detail.objects.filter(po=order_number, id__lt=n).order_by("-id").first()  # 前一条目
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            # 信息取自po_detail的每个item以及Po的合同中
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=po_detail.item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'next' in request.POST:  # 写入不用
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        try:
            # Po数据
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        try:
            # po_detail数据
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(po=order_number, id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=po_detail.item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'final' in request.POST:  # 写入不用
        order_number = request.POST.get('po')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)  # 从po跳转过来的时候需要带过来的po号
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.filter(po=order_number).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        print('=======================================', order_number)
        print('=======================================', po_detail.item_no)
        # omr_po_detail信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=po_detail.item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)
    elif 'add' in request.POST:  # 写入不用
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in FMR.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 已存在这个omr_po_detail
        if item_no in l2:
            return JsonResponse({'status': 'fail', 'msg': '该FMR已存在'})
        try:
            fmr = fmr_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:  # 写入不用
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in FMR.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 不存在这个合同
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': '该fmr不存在'})
        try:
            fmr = FMR.objects.get(po=order_number, item_no=item_no)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        fmr.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:  # 写入不用
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in FMR.objects.filter(po=order_number)]
        # 没有这个Po
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        # 没有这个item
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'Po_detail中不存在该item'})
        # 不存在这个omr_po_detail
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': '该omr_po_detail不存在'})
        try:
            fmr = fmr_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # Po数据
        try:
            po = Po.objects.get(order_number=order_number)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=order_number, item_no=item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # omr_po_detail信息
        try:
            omr_po_detail = OMR_po_detail.objects.get(po=order_number, item_no=item_no)
            data['data']['omr_po_detail'] = obj_to_json(omr_po_detail)
        except ObjectDoesNotExist:
            data['data']['omr_po_detail'] = {}
            return JsonResponse(data)
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        return JsonResponse(data)


@login_required()
def material_sign_view(request):
    if request.method == 'GET':
        # data = json.dumps(basic_info_json())
        return render(request, 'order/material_sign.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        # po_detail数据
        try:
            po_detail = Po_detail.objects.all().order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        # material_detail签收信息
        try:
            material_sign_detail = Material_sign_detail.objects.filter(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign_detail'] = {}
            for i in material_sign_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    sender = obj_to_json(i.sender)
                except:
                    sender = {}
                try:
                    accessory_currency = obj_to_json(i.accessory_currency)
                except:
                    accessory_currency = {}
                try:
                    accessory_total_currency = obj_to_json(i.accessory_total_currency)
                except:
                    accessory_total_currency = {}
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                try:
                    total_currency = obj_to_json(i.total_currency)
                except:
                    total_currency = {}
                try:
                    qc = obj_to_json(i.qc)
                except:
                    qc = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['material_sign_detail'][str(i.id)] = obj_to_json(i)
                data['data']['material_sign_detail'][str(i.id)]['texture'] = texture
                data['data']['material_sign_detail'][str(i.id)]['sender'] = sender
                data['data']['material_sign_detail'][str(i.id)]['accessory_currency'] = accessory_currency
                data['data']['material_sign_detail'][str(i.id)]['accessory_total_currency'] = accessory_total_currency
                data['data']['material_sign_detail'][str(i.id)]['factory'] = factory
                data['data']['material_sign_detail'][str(i.id)]['order_currency'] = order_currency
                data['data']['material_sign_detail'][str(i.id)]['total_currency'] = total_currency
                data['data']['material_sign_detail'][str(i.id)]['qc'] = qc
                data['data']['material_sign_detail'][str(i.id)]['fqc'] = fqc
        except:
            data['data']['material_sign_detail'] = {}
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(id__lt=n).order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po_detail不存在或已是第一条'})
        # except:
        #     return JsonResponse({'status': 'unknown', 'msg': 'detail未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        # material_detail签收信息
        try:
            material_sign_detail = Material_sign_detail.objects.filter(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign_detail'] = {}
            for i in material_sign_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    sender = obj_to_json(i.sender)
                except:
                    sender = {}
                try:
                    accessory_currency = obj_to_json(i.accessory_currency)
                except:
                    accessory_currency = {}
                try:
                    accessory_total_currency = obj_to_json(i.accessory_total_currency)
                except:
                    accessory_total_currency = {}
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                try:
                    total_currency = obj_to_json(i.total_currency)
                except:
                    total_currency = {}
                try:
                    qc = obj_to_json(i.qc)
                except:
                    qc = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['material_sign_detail'][str(i.id)] = obj_to_json(i)
                data['data']['material_sign_detail'][str(i.id)]['texture'] = texture
                data['data']['material_sign_detail'][str(i.id)]['sender'] = sender
                data['data']['material_sign_detail'][str(i.id)]['accessory_currency'] = accessory_currency
                data['data']['material_sign_detail'][str(i.id)]['accessory_total_currency'] = accessory_total_currency
                data['data']['material_sign_detail'][str(i.id)]['factory'] = factory
                data['data']['material_sign_detail'][str(i.id)]['order_currency'] = order_currency
                data['data']['material_sign_detail'][str(i.id)]['total_currency'] = total_currency
                data['data']['material_sign_detail'][str(i.id)]['qc'] = qc
                data['data']['material_sign_detail'][str(i.id)]['fqc'] = fqc
        except:
            data['data']['material_sign_detail'] = {}
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # po_detail数据
        try:
            n = Po_detail.objects.get(po=order_number, item_no=item_no).id
            po_detail = Po_detail.objects.filter(id__gt=n).order_by("id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是最后一条'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        # material_detail签收信息
        try:
            material_sign_detail = Material_sign_detail.objects.filter(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign_detail'] = {}
            for i in material_sign_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    sender = obj_to_json(i.sender)
                except:
                    sender = {}
                try:
                    accessory_currency = obj_to_json(i.accessory_currency)
                except:
                    accessory_currency = {}
                try:
                    accessory_total_currency = obj_to_json(i.accessory_total_currency)
                except:
                    accessory_total_currency = {}
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                try:
                    total_currency = obj_to_json(i.total_currency)
                except:
                    total_currency = {}
                try:
                    qc = obj_to_json(i.qc)
                except:
                    qc = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['material_sign_detail'][str(i.id)] = obj_to_json(i)
                data['data']['material_sign_detail'][str(i.id)]['texture'] = texture
                data['data']['material_sign_detail'][str(i.id)]['sender'] = sender
                data['data']['material_sign_detail'][str(i.id)]['accessory_currency'] = accessory_currency
                data['data']['material_sign_detail'][str(i.id)]['accessory_total_currency'] = accessory_total_currency
                data['data']['material_sign_detail'][str(i.id)]['factory'] = factory
                data['data']['material_sign_detail'][str(i.id)]['order_currency'] = order_currency
                data['data']['material_sign_detail'][str(i.id)]['total_currency'] = total_currency
                data['data']['material_sign_detail'][str(i.id)]['qc'] = qc
                data['data']['material_sign_detail'][str(i.id)]['fqc'] = fqc
        except:
            data['data']['material_sign_detail'] = {}
        return JsonResponse(data)
    elif 'final' in request.POST:
        # po_detail数据
        try:
            po_detail = Po_detail.objects.all().order_by("-id").first()
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po_detail无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': 'po无数据'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        # material_detail签收信息
        try:
            material_sign_detail = Material_sign_detail.objects.filter(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign_detail'] = {}
            for i in material_sign_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    sender = obj_to_json(i.sender)
                except:
                    sender = {}
                try:
                    accessory_currency = obj_to_json(i.accessory_currency)
                except:
                    accessory_currency = {}
                try:
                    accessory_total_currency = obj_to_json(i.accessory_total_currency)
                except:
                    accessory_total_currency = {}
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                try:
                    total_currency = obj_to_json(i.total_currency)
                except:
                    total_currency = {}
                try:
                    qc = obj_to_json(i.qc)
                except:
                    qc = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['material_sign_detail'][str(i.id)] = obj_to_json(i)
                data['data']['material_sign_detail'][str(i.id)]['texture'] = texture
                data['data']['material_sign_detail'][str(i.id)]['sender'] = sender
                data['data']['material_sign_detail'][str(i.id)]['accessory_currency'] = accessory_currency
                data['data']['material_sign_detail'][str(i.id)]['accessory_total_currency'] = accessory_total_currency
                data['data']['material_sign_detail'][str(i.id)]['factory'] = factory
                data['data']['material_sign_detail'][str(i.id)]['order_currency'] = order_currency
                data['data']['material_sign_detail'][str(i.id)]['total_currency'] = total_currency
                data['data']['material_sign_detail'][str(i.id)]['qc'] = qc
                data['data']['material_sign_detail'][str(i.id)]['fqc'] = fqc
        except:
            data['data']['material_sign_detail'] = {}
        return JsonResponse(data)
    elif 'add' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Material_sign.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        if item_no in l2:
            return JsonResponse({'status': 'fail', 'msg': 'item号在材料签收表中已存在'})
        try:
            material_sign = material_sign_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Material_sign.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': 'item号在材料签收表中不存在'})
        try:
            material_sign_detail = Material_sign.objects.get(po=order_number, item_no=item_no)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        material_sign_detail.delete()
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        l = field_list("Po", "order_number")
        l1 = [i.item_no for i in Po_detail.objects.filter(po=order_number)]
        l2 = [i.item_no for i in Material_sign.objects.filter(po=order_number)]
        if order_number not in l:
            return JsonResponse({'status': 'fail', 'msg': 'Po号不存在'})
        if item_no not in l1:
            return JsonResponse({'status': 'fail', 'msg': 'item号在po_detail中不存在'})
        if item_no not in l2:
            return JsonResponse({'status': 'fail', 'msg': 'item号在材料签收表中不存在'})
        try:
            material_sign = material_sign_modify(request)
            return JsonResponse({'status': 'success', 'msg': '修改成功'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
    elif 'view' in request.POST:
        detail_id = request.POST.get('detail_id')
        try:
            po_detail = Po_detail.objects.get(id=int(detail_id))
        except:
            return JsonResponse({'status': 'fail', 'msg': '查询结果不存在，请检查detailID'})
        order_number = po_detail.po
        item_no = po_detail.item_no
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po_detail不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        # material_detail签收信息
        try:
            material_sign_detail = Material_sign_detail.objects.filter(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign_detail'] = {}
            for i in material_sign_detail:
                try:
                    texture = obj_to_json(i.texture)
                except:
                    texture = {}
                try:
                    sender = obj_to_json(i.sender)
                except:
                    sender = {}
                try:
                    accessory_currency = obj_to_json(i.accessory_currency)
                except:
                    accessory_currency = {}
                try:
                    accessory_total_currency = obj_to_json(i.accessory_total_currency)
                except:
                    accessory_total_currency = {}
                try:
                    factory = obj_to_json(i.factory)
                except:
                    factory = {}
                try:
                    order_currency = obj_to_json(i.order_currency)
                except:
                    order_currency = {}
                try:
                    total_currency = obj_to_json(i.total_currency)
                except:
                    total_currency = {}
                try:
                    qc = obj_to_json(i.qc)
                except:
                    qc = {}
                try:
                    fqc = obj_to_json(i.fqc)
                except:
                    fqc = {}
                data['data']['material_sign_detail'][str(i.id)] = obj_to_json(i)
                data['data']['material_sign_detail'][str(i.id)]['texture'] = texture
                data['data']['material_sign_detail'][str(i.id)]['sender'] = sender
                data['data']['material_sign_detail'][str(i.id)]['accessory_currency'] = accessory_currency
                data['data']['material_sign_detail'][str(i.id)]['accessory_total_currency'] = accessory_total_currency
                data['data']['material_sign_detail'][str(i.id)]['factory'] = factory
                data['data']['material_sign_detail'][str(i.id)]['order_currency'] = order_currency
                data['data']['material_sign_detail'][str(i.id)]['total_currency'] = total_currency
                data['data']['material_sign_detail'][str(i.id)]['qc'] = qc
                data['data']['material_sign_detail'][str(i.id)]['fqc'] = fqc
        except:
            data['data']['material_sign_detail'] = {}
        return JsonResponse(data)


@login_required()
def material_sign_detail_view(request):  # 逻辑错误，修改
    if request.method == 'GET':
        data = json.dumps(basic_info_json(('Staff', 'Currency', 'Factory', 'Texture')))
        return render(request, 'order/material_sign_detail.html', locals())
    # 实现增删改查按钮
    if 'first' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # material_detail签收信息
        try:
            material_sign_detail = Material_sign_detail.objects.filter(po=order_number, item_no=item_no).order_by("id").first()
            try:
                texture = obj_to_json(material_sign_detail.texture)
            except:
                texture = {}
            try:
                sender = obj_to_json(material_sign_detail.sender)
            except:
                sender = {}
            try:
                accessory_currency = obj_to_json(material_sign_detail.accessory_currency)
            except:
                accessory_currency = {}
            try:
                accessory_total_currency = obj_to_json(material_sign_detail.accessory_total_currency)
            except:
                accessory_total_currency = {}
            try:
                factory = obj_to_json(material_sign_detail.factory)
            except:
                factory = {}
            try:
                order_currency = obj_to_json(material_sign_detail.order_currency)
            except:
                order_currency = {}
            try:
                total_currency = obj_to_json(material_sign_detail.total_currency)
            except:
                total_currency = {}
            try:
                qc = obj_to_json(material_sign_detail.qc)
            except:
                qc = {}
            try:
                fqc = obj_to_json(material_sign_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['material_sign_detail'] = obj_to_json(material_sign_detail)
            data['data']['material_sign_detail']['texture'] = texture
            data['data']['material_sign_detail']['sender'] = sender
            data['data']['material_sign_detail']['accessory_currency'] = accessory_currency
            data['data']['material_sign_detail']['accessory_total_currency'] = accessory_total_currency
            data['data']['material_sign_detail']['factory'] = factory
            data['data']['material_sign_detail']['order_currency'] = order_currency
            data['data']['material_sign_detail']['total_currency'] = total_currency
            data['data']['material_sign_detail']['qc'] = qc
            data['data']['material_sign_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前item无材料签收信息'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '无po_detail数据'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': '无po数据'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        return JsonResponse(data)
    elif 'last' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # material_detail签收信息
        m_id = int(request.POST.get('id'))
        try:
            material_sign_detail = Material_sign_detail.objects.filter(
                po=order_number, item_no=item_no, id__lt=m_id).order_by("-id").first()
            try:
                texture = obj_to_json(material_sign_detail.texture)
            except:
                texture = {}
            try:
                sender = obj_to_json(material_sign_detail.sender)
            except:
                sender = {}
            try:
                accessory_currency = obj_to_json(material_sign_detail.accessory_currency)
            except:
                accessory_currency = {}
            try:
                accessory_total_currency = obj_to_json(material_sign_detail.accessory_total_currency)
            except:
                accessory_total_currency = {}
            try:
                factory = obj_to_json(material_sign_detail.factory)
            except:
                factory = {}
            try:
                order_currency = obj_to_json(material_sign_detail.order_currency)
            except:
                order_currency = {}
            try:
                total_currency = obj_to_json(material_sign_detail.total_currency)
            except:
                total_currency = {}
            try:
                qc = obj_to_json(material_sign_detail.qc)
            except:
                qc = {}
            try:
                fqc = obj_to_json(material_sign_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['material_sign_detail'] = obj_to_json(material_sign_detail)
            data['data']['material_sign_detail']['texture'] = texture
            data['data']['material_sign_detail']['sender'] = sender
            data['data']['material_sign_detail']['accessory_currency'] = accessory_currency
            data['data']['material_sign_detail']['accessory_total_currency'] = accessory_total_currency
            data['data']['material_sign_detail']['factory'] = factory
            data['data']['material_sign_detail']['order_currency'] = order_currency
            data['data']['material_sign_detail']['total_currency'] = total_currency
            data['data']['material_sign_detail']['qc'] = qc
            data['data']['material_sign_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=material_sign_detail.po, item_no=material_sign_detail.item_no)
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '无po_detail数据'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': '无po数据'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        return JsonResponse(data)
    elif 'next' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # material_detail签收信息
        m_id = int(request.POST.get('id'))
        try:
            material_sign_detail = Material_sign_detail.objects.filter(
                po=order_number, item_no=item_no, id__gt=m_id).order_by("id").first()
            try:
                texture = obj_to_json(material_sign_detail.texture)
            except:
                texture = {}
            try:
                sender = obj_to_json(material_sign_detail.sender)
            except:
                sender = {}
            try:
                accessory_currency = obj_to_json(material_sign_detail.accessory_currency)
            except:
                accessory_currency = {}
            try:
                accessory_total_currency = obj_to_json(material_sign_detail.accessory_total_currency)
            except:
                accessory_total_currency = {}
            try:
                factory = obj_to_json(material_sign_detail.factory)
            except:
                factory = {}
            try:
                order_currency = obj_to_json(material_sign_detail.order_currency)
            except:
                order_currency = {}
            try:
                total_currency = obj_to_json(material_sign_detail.total_currency)
            except:
                total_currency = {}
            try:
                qc = obj_to_json(material_sign_detail.qc)
            except:
                qc = {}
            try:
                fqc = obj_to_json(material_sign_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['material_sign_detail'] = obj_to_json(material_sign_detail)
            data['data']['material_sign_detail']['texture'] = texture
            data['data']['material_sign_detail']['sender'] = sender
            data['data']['material_sign_detail']['accessory_currency'] = accessory_currency
            data['data']['material_sign_detail']['accessory_total_currency'] = accessory_total_currency
            data['data']['material_sign_detail']['factory'] = factory
            data['data']['material_sign_detail']['order_currency'] = order_currency
            data['data']['material_sign_detail']['total_currency'] = total_currency
            data['data']['material_sign_detail']['qc'] = qc
            data['data']['material_sign_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前条目无数据或已是第一条'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=material_sign_detail.po, item_no=material_sign_detail.item_no)
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '无po_detail数据'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': '无po数据'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        return JsonResponse(data)
    elif 'final' in request.POST:
        order_number = request.POST.get('po')
        item_no = request.POST.get('item_no')
        # material_detail签收信息
        try:
            material_sign_detail = Material_sign_detail.objects.filter(po=order_number, item_no=item_no).order_by("-id").first()
            try:
                texture = obj_to_json(material_sign_detail.texture)
            except:
                texture = {}
            try:
                sender = obj_to_json(material_sign_detail.sender)
            except:
                sender = {}
            try:
                accessory_currency = obj_to_json(material_sign_detail.accessory_currency)
            except:
                accessory_currency = {}
            try:
                accessory_total_currency = obj_to_json(material_sign_detail.accessory_total_currency)
            except:
                accessory_total_currency = {}
            try:
                factory = obj_to_json(material_sign_detail.factory)
            except:
                factory = {}
            try:
                order_currency = obj_to_json(material_sign_detail.order_currency)
            except:
                order_currency = {}
            try:
                total_currency = obj_to_json(material_sign_detail.total_currency)
            except:
                total_currency = {}
            try:
                qc = obj_to_json(material_sign_detail.qc)
            except:
                qc = {}
            try:
                fqc = obj_to_json(material_sign_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['material_sign_detail'] = obj_to_json(material_sign_detail)
            data['data']['material_sign_detail']['texture'] = texture
            data['data']['material_sign_detail']['sender'] = sender
            data['data']['material_sign_detail']['accessory_currency'] = accessory_currency
            data['data']['material_sign_detail']['accessory_total_currency'] = accessory_total_currency
            data['data']['material_sign_detail']['factory'] = factory
            data['data']['material_sign_detail']['order_currency'] = order_currency
            data['data']['material_sign_detail']['total_currency'] = total_currency
            data['data']['material_sign_detail']['qc'] = qc
            data['data']['material_sign_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '当前item无材料签收信息'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except:
            return JsonResponse({'status': 'fail', 'msg': '无po_detail数据'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except:
            return JsonResponse({'status': 'fail', 'msg': '无po数据'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except:
            data['data']['contract'] = {}
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        return JsonResponse(data)
    elif 'add' in request.POST:
        try:
            material_sign_detail = material_sign_detail_add(request)
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        except:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})
    elif 'delete' in request.POST:
        m_id = int(request.POST.get('id'))
        try:
            material_sign_detail = Material_sign_detail.objects.get(id=m_id)
            material_sign_detail.delete()
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '删除条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '删除遇到未知错误'})
        return JsonResponse({'status': 'success', 'msg': '删除成功'})
    elif 'modify' in request.POST:
        m_id = int(request.POST.get('id'))
        try:
            material_sign_detail = Material_sign_detail.objects.get(id=m_id)
            material_sign_detail_modify(request)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '修改条目不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '修改遇到未知错误'})
        return JsonResponse({'status': 'success', 'msg': '修改成功'})
    elif 'view' in request.POST:
        m_id = int(request.POST.get('id'))
        try:
            order_number = Material_sign_detail.objects.get(id=m_id).po
            item_no = Material_sign_detail.objects.get(id=m_id).item_no
        except:
            return JsonResponse({'status': 'fail', 'msg': '查询条目不存在材料信息'})
        # po_detail数据
        try:
            po_detail = Po_detail.objects.get(po=order_number, item_no=item_no)
            # 将python对象转化为json对象
            try:
                texture = obj_to_json(po_detail.texture)
            except:
                texture = {}
            try:
                currency = obj_to_json(po_detail.currency)
            except:
                currency = {}
            try:
                each_box = obj_to_json(po_detail.each_box)
            except:
                each_box = {}
            try:
                fac_delivery = obj_to_json(po_detail.fac_delivery)
            except:
                fac_delivery = {}
            try:
                fac_delivery_port = obj_to_json(po_detail.fac_delivery_port)
            except:
                fac_delivery_port = {}
            try:
                fmr = obj_to_json(po_detail.fmr)
            except:
                fmr = {}
            try:
                fqc = obj_to_json(po_detail.fqc)
            except:
                fqc = {}
            data = {}
            data['status'] = 'success'
            data['msg'] = '成功'
            data['data'] = {}
            data['data']['po_detail'] = obj_to_json(po_detail)
            data['data']['po_detail']['texture'] = texture
            data['data']['po_detail']['currency'] = currency
            data['data']['po_detail']['each_box'] = each_box
            data['data']['po_detail']['fac_delivery'] = fac_delivery
            data['data']['po_detail']['fac_delivery_port'] = fac_delivery_port
            data['data']['po_detail']['fmr'] = fmr
            data['data']['po_detail']['fqc'] = fqc
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po_detail不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # Po数据
        try:
            po = Po.objects.get(order_number=po_detail.po)
            try:
                customer = obj_to_json(po.customer)
            except:
                customer = {}
            try:
                delivery_condition = obj_to_json(po.delivery_condition)
            except:
                delivery_condition = {}
            try:
                port = obj_to_json(po.port)
            except:
                port = {}
            try:
                omr = obj_to_json(po.omr)
            except:
                omr = {}
            data['data']['po'] = obj_to_json(po)
            data['data']['po']['customer'] = customer
            data['data']['po']['delivery_condition'] = delivery_condition
            data['data']['po']['port'] = port
            data['data']['po']['omr'] = omr
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail', 'msg': '当前查询条目po不存在'})
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # 合同信息
        try:
            contract = Contract.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            try:
                factory = obj_to_json(contract.factory)
            except:
                factory = {}
            try:
                fac_currency = obj_to_json(contract.fac_currency)
            except:
                fac_currency = {}
            data['data']['contract'] = obj_to_json(contract)
            data['data']['contract']['factory'] = factory
            data['data']['contract']['fac_currency'] = fac_currency
        except ObjectDoesNotExist:
            data['data']['contract'] = {}
        except:
            return JsonResponse({'status': 'unknown', 'msg': '未知错误'})
        # material签收信息
        try:
            material_sign = Material_sign.objects.get(po=po_detail.po, item_no=po_detail.item_no)
            data['data']['material_sign'] = obj_to_json(material_sign)
        except:
            data['data']['material_sign'] = {}
        # material_detail签收信息
        m_id = request.POST.get('id')
        try:
            material_sign_detail = Material_sign_detail.objects.get(id=m_id)
            try:
                texture = obj_to_json(material_sign_detail.texture)
            except:
                texture = {}
            try:
                sender = obj_to_json(material_sign_detail.sender)
            except:
                sender = {}
            try:
                accessory_currency = obj_to_json(material_sign_detail.accessory_currency)
            except:
                accessory_currency = {}
            try:
                accessory_total_currency = obj_to_json(material_sign_detail.accessory_total_currency)
            except:
                accessory_total_currency = {}
            try:
                factory = obj_to_json(material_sign_detail.factory)
            except:
                factory = {}
            try:
                order_currency = obj_to_json(material_sign_detail.order_currency)
            except:
                order_currency = {}
            try:
                total_currency = obj_to_json(material_sign_detail.total_currency)
            except:
                total_currency = {}
            try:
                qc = obj_to_json(material_sign_detail.qc)
            except:
                qc = {}
            try:
                fqc = obj_to_json(material_sign_detail.fqc)
            except:
                fqc = {}
            data['data']['material_sign_detail'] = obj_to_json(material_sign_detail)
            data['data']['material_sign_detail']['texture'] = texture
            data['data']['material_sign_detail']['sender'] = sender
            data['data']['material_sign_detail']['accessory_currency'] = accessory_currency
            data['data']['material_sign_detail']['accessory_total_currency'] = accessory_total_currency
            data['data']['material_sign_detail']['factory'] = factory
            data['data']['material_sign_detail']['order_currency'] = order_currency
            data['data']['material_sign_detail']['total_currency'] = total_currency
            data['data']['material_sign_detail']['qc'] = qc
            data['data']['material_sign_detail']['fqc'] = fqc
        except:
            data['data']['material_sign_detail'] = {}
        return JsonResponse(data)
