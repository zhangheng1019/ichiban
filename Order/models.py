import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete
# Create your models here.


class User_extension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension', verbose_name='用户')
    field_permission = models.TextField(blank=True, null=True, verbose_name='字段权限')  # 存储未拥有的字段权限
    # ------------以下为预留字段-------------
    # preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    # preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    # preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    # preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    # preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    # remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = "user_extension"
        verbose_name = '权限扩展'
        verbose_name_plural = verbose_name


@receiver(post_save, sender=User)
def create_user_extension(sender, instance, created, **kwargs):
    if created:
        User_extension.objects.create(user=instance)
    else:
        instance.extension.save()


class Package_texture(models.Model):
    """包装材质"""
    name = models.CharField(max_length=255, unique=True, verbose_name='包装材质中文名')
    edesc = models.CharField(max_length=255, blank=True, null=True, verbose_name='英文描述')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = "package_texture"
        verbose_name = '包装材质'
        verbose_name_plural = verbose_name


class Package_type(models.Model):
    """包装类型"""
    name = models.CharField(max_length=255, unique=True, verbose_name='类型名称')
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='类型编码')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = "package_type"
        verbose_name = '包装类型'
        verbose_name_plural = verbose_name


class Sea_rate(models.Model):
    """海关税率表"""
    tariff = models.CharField(max_length=200, unique=True, verbose_name='海关税则')
    rate = models.CharField(max_length=200, verbose_name='海关税率')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.tariff

    class Meta:
        ordering = ['rate']
        db_table = "sea_rate"
        verbose_name = '海关税率'
        verbose_name_plural = verbose_name


class Develop_function(models.Model):
    """开发产品用途"""
    func_name = models.CharField(max_length=200, unique=True, verbose_name='功能名称')
    func_desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='功能描述')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.func_name

    class Meta:
        ordering = ['func_name']
        db_table = "develop_function"
        verbose_name = '开发产品用途'
        verbose_name_plural = verbose_name


class Sketch_type(models.Model):
    """图稿开发的类型"""
    name = models.CharField(max_length=200, unique=True, verbose_name='类型名称')
    edesc = models.CharField(max_length=200, blank=True, null=True, verbose_name='类型英文描述')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = "sketch_type"
        verbose_name = '图稿开发类型'
        verbose_name_plural = verbose_name


class Sketch_design(models.Model):
    """图稿设计"""
    code = models.CharField(max_length=200, unique=True, verbose_name='图稿编号')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='图稿名称')
    developer = models.ForeignKey('Basic_info.Staff', related_name='sketch_design_develop_developer',
                                  on_delete=models.CASCADE, blank=True, null=True, verbose_name='开发人员')
    designer = models.ForeignKey('Basic_info.Staff', related_name='sketch_design_staff',
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name='设计师')
    category = models.ForeignKey('Basic_info.Category', related_name='sketch_category',
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name='开发系列')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发时间')
    customer = models.ForeignKey('Basic_info.Customer', related_name='sketch_customer',
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name='所属客户')
    texture = models.ForeignKey('Basic_info.Texture', related_name='sketch_design_texture',
                                on_delete=models.CASCADE, blank=True, null=True, verbose_name='主材质')
    sketch_type = models.ForeignKey('Order.Sketch_type', related_name='sketch_design_type',
                                    on_delete=models.CASCADE, blank=True, null=True, verbose_name='类型')
    photo1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='图片1所在路径')
    photo1_remark = models.TextField(blank=True, null=True, verbose_name='图片1备注')
    photo2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='图片2所在路径')
    photo2_remark = models.TextField(blank=True, null=True, verbose_name='图片2备注')
    photo3 = models.CharField(max_length=255, blank=True, null=True, verbose_name='图片3所在路径')
    photo3_remark = models.TextField(blank=True, null=True, verbose_name='图片3备注')
    # ----------以下字段在编辑页不展示----------
    sketch1_path = models.CharField(max_length=255, blank=True, null=True, verbose_name='图稿1所在路径')
    sketch2_path = models.CharField(max_length=255, blank=True, null=True, verbose_name='图稿2所在路径')
    sketch3_path = models.CharField(max_length=255, blank=True, null=True, verbose_name='图稿3所在路径')
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='记录插入时间')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['name']
        db_table = "sketch_design"
        verbose_name = '图稿设计'
        verbose_name_plural = verbose_name


class Sketch_develop(models.Model):
    """图稿开发"""
    season_info = (
        ('spring', '春季'),
        ('summer', '夏季'),
        ('autumn', '秋季'),
        ('winter', '冬季'),
    )
    sketch_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='图稿名称')  # 取自图稿设计
    number = models.CharField(max_length=200, unique=True, verbose_name='开发单号')
    receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='收到时间')
    category = models.ForeignKey('Basic_info.Category', related_name='sketch_develop_category',
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name='开发系列')
    developer = models.ForeignKey('Basic_info.Staff', related_name='sketch_develop_developer',
                                  on_delete=models.CASCADE, blank=True, null=True, verbose_name='开发人员')
    department = models.ForeignKey('Basic_info.Department', related_name='sketch_develop_department',
                                   on_delete=models.CASCADE, blank=True, null=True, verbose_name='开发部门')
    function = models.ForeignKey('Order.Develop_function', related_name='sketch_develop_func',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='开发用途')
    undertake = models.ForeignKey('Basic_info.Staff', related_name='sketch_develop_undertake',
                                  blank=True, null=True, on_delete=models.CASCADE, verbose_name='承办员')
    plan_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='完成期限')
    customer = models.ForeignKey('Basic_info.Customer', related_name='sketch_develop_customer',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='客户')
    season = models.CharField(max_length=60, blank=True, null=True, choices=season_info, verbose_name='开发季节')
    makesure_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发季样品底线确认日')
    explain = models.TextField(blank=True, null=True, verbose_name='开发说明')
    is_finish = models.CharField(max_length=30, choices=(('True', '已完成'), ('False', '未完成')),
                                 blank=True, null=True, default='False', verbose_name='是否完成')
    # -----------------以下为预留字段,在编辑页不展示-------------------
    last_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='最后操作时间')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.number

    class Meta:
        # 设置联合主键
        # unique_together = ('sketch_code', 'sketch_name', 'number', 'category', 'developer', 'customer')
        ordering = ['number']
        db_table = "sketch_develop"
        verbose_name = '图稿开发'
        verbose_name_plural = verbose_name


class Sketch_detail(models.Model):
    """图稿开发明细"""
    info = (
        ('True', '已完成'),
        ('False', '未完成')
    )
    number = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发单号')  # 关联Sketch_develop表
    item_number = models.CharField(max_length=200, verbose_name='开发item编号')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='中文品名')
    ename = models.CharField(max_length=200, blank=True, null=True, verbose_name='英文品名')
    customer_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人目标价')
    customer_currency = models.ForeignKey('Basic_info.Currency', related_name='sketch_custom_currency',
                                          blank=True, null=True, on_delete=models.CASCADE, verbose_name='客人货币类型')
    factory = models.ForeignKey('Basic_info.Factory', related_name='sketch_detail_factory',
                                blank=True, null=True, on_delete=models.CASCADE, verbose_name='生产工厂')
    factory_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂报价')
    factory_currency = models.ForeignKey('Basic_info.Currency', related_name='sketch_factory_currency',
                                         blank=True, null=True, on_delete=models.CASCADE, verbose_name='工厂货币类型')
    texture = models.ForeignKey('Basic_info.Texture', related_name='sketch_detail_texture',
                                blank=True, null=True, on_delete=models.CASCADE, verbose_name='材质')
    long = models.CharField(max_length=255, blank=True, null=True, verbose_name='长度')
    width = models.CharField(max_length=255, blank=True, null=True, verbose_name='宽度')
    height = models.CharField(max_length=255, blank=True, null=True, verbose_name='高度')
    size_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='尺寸单位')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='打样数量')
    fmr_undertake = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='sketch_detail_undertake_staff', verbose_name='承办员（FMR）')
    refer_data = models.CharField(max_length=200, blank=True, null=True, verbose_name='参考资料')
    refer_data_no = models.CharField(max_length=200, blank=True, null=True, verbose_name='参考资料编号')
    fmr_50 = models.CharField(max_length=200, blank=True, null=True, verbose_name='FMR样品50%完成')
    start_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开/雕模（工厂开工时间）')
    photo_src = models.CharField(max_length=255, blank=True, null=True, verbose_name='图片路径')
    fmr_plan_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='FMR需要完成日期')
    fmr_change_plan_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='FMR修改样预计完成日期')
    fmr_change_act_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='FMR修改样实际完成日期')
    receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品收到日期')
    sent_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品寄出日期')
    mould_min = models.CharField(max_length=255, blank=True, null=True, verbose_name='模具最小返回数（元）')
    other_fee = models.CharField(max_length=255, blank=True, null=True, verbose_name='其他费用（元）')
    express_fee = models.CharField(max_length=255, blank=True, null=True, verbose_name='快递费用（元）')
    is_customer_price = models.CharField(max_length=30, blank=True, null=True, choices=info, verbose_name='客人报价')
    is_finish = models.CharField(max_length=30, blank=True, null=True, choices=info, verbose_name='开发完成')
    product_explain = models.TextField(blank=True, null=True, verbose_name='产品说明')
    # ------------以下字段在编辑页不展示-------------
    sea_cuft_code = models.ForeignKey('Order.Sea_rate', to_field='tariff', on_delete=models.CASCADE, blank=True,
                                      null=True, related_name='sketch_detail_sea_tariff', verbose_name='海关税则')
    delay_reason = models.CharField(max_length=200, blank=True, null=True, verbose_name='延迟原因')
    case = models.CharField(max_length=60, blank=True, null=True, verbose_name='套几')
    first_sample_deadLine = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品第一次清线时间')
    first_sample_revised = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品第一次完成时间')
    mould_cost = models.CharField(max_length=255, blank=True, null=True, verbose_name='开模费')
    data_change_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='资料修改时间')
    status = models.TextField(blank=True, null=True, verbose_name='开发状态描述')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_number

    class Meta:
        unique_together = (("number", "item_number"),)
        ordering = ['item_number']
        db_table = "sketch_detail"
        verbose_name = '图稿开发明细'
        verbose_name_plural = verbose_name


class Sample_detail(models.Model):
    """样品详情"""
    season_info = (
        ('spring', '春季'),
        ('summer', '夏季'),
        ('autumn', '秋季'),
        ('winter', '冬季'),
    )
    item_no = models.CharField(max_length=100, unique=True, verbose_name='样品Item No')
    item_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发单item号')  # 关联Sketch_develop表
    parent_item = models.CharField(max_length=60, blank=True, null=True, verbose_name='父Item No')
    other_item = models.CharField(max_length=60, blank=True, null=True, verbose_name='其他No')
    sketch_no = models.CharField(max_length=60, blank=True, null=True, verbose_name='样品图稿编号')  # 关联Sketch_design表
    name = models.CharField(max_length=60, blank=True, null=True, verbose_name='中文品名')
    ename = models.CharField(max_length=60, blank=True, null=True, verbose_name='英文品名')
    category = models.ForeignKey('Basic_info.Category', related_name='sample_category',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='产品系列')
    texture = models.ForeignKey('Basic_info.Texture', related_name='sample_texture',
                                max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='材质')
    long = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品长度')
    width = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品宽度')
    height = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品高度')
    other = models.CharField(max_length=255, blank=True, null=True, verbose_name='篮子提手打开时高度')
    volume = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品材积')
    volume_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='材积单位')
    omr = models.ForeignKey('Basic_info.Staff', related_name='sample_omr',
                            max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='OMR')
    fmr = models.ForeignKey('Basic_info.Staff', related_name='sample_fmr',
                            max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='FMR')
    photo = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品图片路径')
    photo_remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='图片说明')
    sample_receive = models.CharField(max_length=255, blank=True, null=True, verbose_name='收到样品日期')
    company = models.ForeignKey('Basic_info.Company', related_name='sample_company',
                                max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='开发公司')
    desc = models.TextField(blank=True, null=True, verbose_name='备注说明')
    # ----------以下字段在编辑页不展示----------
    fac_volume = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂报材积')
    fac_volume_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='材积单位')
    customer = models.ForeignKey('Basic_info.Customer', related_name='sample_customer',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='所属客户')
    customer_dep = models.CharField(max_length=100, blank=True, null=True, verbose_name='客人部门')
    insert_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='资料录入时间')
    asst = models.CharField(max_length=255, blank=True, null=True, verbose_name='套几')
    check_mr = models.ForeignKey('Basic_info.Staff', related_name='sample_checker',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='审核人')
    check_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='审核时间')
    sea_rate = models.ForeignKey('Order.Sea_rate', blank=True, null=True, related_name='sample_sea_rate',
                                 on_delete=models.CASCADE, verbose_name='海关税则')
    is_delete = models.CharField(max_length=20, choices=(('True', '是'), ('False', '否')),
                                 default='False', blank=True, null=True, verbose_name='是否作废')
    min_order = models.CharField(max_length=255, blank=True, null=True, verbose_name='最低订购量')
    leadtime = models.CharField(max_length=255, blank=True, null=True, verbose_name='生产周期(天)')
    reroader_leadtime = models.CharField(max_length=255, blank=True, null=True, verbose_name='续单生产周期(天)')
    size40_perpc = models.CharField(max_length=255, blank=True, null=True, verbose_name='40尺柜单PC装量')
    size40_freight = models.CharField(max_length=255, blank=True, null=True, verbose_name='40尺柜国外海运费')
    high_size40_freight = models.CharField(max_length=255, blank=True, null=True, verbose_name='40尺高柜国外海运费')
    size45_freight = models.CharField(max_length=255, blank=True, null=True, verbose_name='45尺柜国外海运费')
    pack_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='货柜装箱数量')
    function = models.ForeignKey('Order.Develop_function', blank=True, null=True,
                                 related_name='sample_function', on_delete=models.CASCADE, verbose_name='功能')
    shape = models.TextField(blank=True, null=True, verbose_name='形状')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_no

    class Meta:
        ordering = ['item_no']
        db_table = "sample_detail"
        verbose_name = '样品详情'
        verbose_name_plural = verbose_name


class Item_note(models.Model):
    """样品item注释"""
    sample = models.CharField(max_length=255, verbose_name='样品Item No')  # 关联Sample_detail表
    code = models.CharField(max_length=200, verbose_name='注释编码')
    desc = models.TextField(blank=True, null=True, verbose_name='注释说明')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.code

    class Meta:
        unique_together = (("sample", "code"),)
        ordering = ['sample']
        db_table = "item_note"
        verbose_name = '样品item注释'
        verbose_name_plural = verbose_name


class Item_package(models.Model):
    """ITEM包装信息"""
    sample = models.CharField(max_length=255, verbose_name='样品Item No')  # 关联Sample_detail表
    type = models.ForeignKey('Order.Package_type', related_name='sample_package_type',
                             max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='包装类型')
    package_texture = models.ForeignKey('Package_texture', related_name='sample_package_texture',
                                        blank=True, null=True, on_delete=models.CASCADE, verbose_name='包装材质')
    long = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装长度')
    width = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装宽度')
    height = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装高度')
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装尺寸单位')
    net_weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='净重')
    gross_weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='毛重')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.sample)

    class Meta:
        ordering = ['sample']
        db_table = "item_package"
        verbose_name = '样品item包装信息'
        verbose_name_plural = verbose_name


class Factory_quote(models.Model):
    """工厂报价"""
    factory = models.ForeignKey('Basic_info.Factory', related_name='quote_factory',
                                max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='报价工厂')
    sample = models.CharField(max_length=255, verbose_name='样品Item No')  # 关联Sample_detail表
    factory_number = models.CharField(max_length=200, blank=True, null=True, verbose_name='工厂Item NO')
    cost = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂报价')
    currency = models.ForeignKey('Basic_info.Currency', related_name='fac_quote_currency',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='工厂报价的货币')
    pack_texture = models.ForeignKey('Order.Package_texture', related_name='fac_quote_pack_texture',
                                     blank=True, null=True, on_delete=models.CASCADE, verbose_name='单PCS包装材质')
    shipping_method = models.ForeignKey('Basic_info.Delivery', related_name='fac_quote_delivery',
                                        blank=True, null=True, on_delete=models.CASCADE, verbose_name='出口方式')
    shipping_port = models.ForeignKey('Basic_info.Export_port', on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='fac_quote_export_port', verbose_name='出货港口')
    sample_desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='品名')
    is_default_quote = models.CharField(max_length=60, choices=(('True', '是'), ('False', '否')),
                                        blank=True, null=True, default='False', verbose_name='是否默认报价')
    # ------------以下字段在编辑页不展示-------------
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='记录插入时间')
    quote_staff = models.ForeignKey('Basic_info.Staff', related_name='quote_staff', blank=True, null=True,
                                    on_delete=models.CASCADE, verbose_name='报价人')
    check_staff = models.ForeignKey('Basic_info.Staff', related_name='quote_check_staff', blank=True, null=True,
                                    on_delete=models.CASCADE, verbose_name='报价确认人')
    input_staff = models.ForeignKey('Basic_info.Staff', related_name='quote_input_staff', blank=True, null=True,
                                    on_delete=models.CASCADE, verbose_name='录入人员')
    is_check_ok = models.CharField(max_length=60, choices=(('True', '是'), ('False', '否')),
                                   blank=True, null=True, default='False', verbose_name='审核是否通过')
    not_reason = models.TextField(blank=True, null=True, verbose_name='审核不通过原因')
    check_date = models.DateTimeField(blank=True, null=True, verbose_name='审核时间')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.sample)

    class Meta:
        ordering = ['cost']
        db_table = "factory_quote"
        verbose_name = '工厂报价'
        verbose_name_plural = verbose_name


class Repeat_sample(models.Model):
    """复样总表"""
    number = models.CharField(max_length=250, unique=True, verbose_name='复样单号')
    customer = models.ForeignKey('Basic_info.Customer', related_name='repeat_sample_customer',
                                 max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='客户代码')
    receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='收到日期')
    fac_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂交期')
    undertaker = models.ForeignKey('Basic_info.Staff', related_name='repeat_sample_staff',
                                   blank=True, null=True, on_delete=models.CASCADE, verbose_name='承办人员')
    explain = models.TextField(blank=True, null=True, verbose_name='备注说明')
    # ----------以下字段在编辑页不展示----------
    supervisor1 = models.TextField(blank=True, null=True, verbose_name='备用')
    supervisor = models.TextField(blank=True, null=True, verbose_name='备用')
    advance_days = models.CharField(max_length=255, blank=True, null=True, verbose_name='复样单提前天数')
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='记录插入时间')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']
        db_table = "repeat_sample"
        verbose_name = '复样总表'
        verbose_name_plural = verbose_name


class Repeat_sample_detail(models.Model):
    """复样明细表"""
    number = models.CharField(max_length=255, verbose_name='复样单号')  # 关联Repeat_sample
    item_no = models.CharField(max_length=250, verbose_name='复样单item编号')
    specs = models.TextField(blank=True, null=True, verbose_name='产品规格')
    desc = models.TextField(blank=True, null=True, verbose_name='中文品名')
    edesc = models.TextField(blank=True, null=True, verbose_name='英文描述')
    customer_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人编号')
    texture = models.ForeignKey('Basic_info.Texture', related_name='repeat_sample_texture',
                                blank=True, null=True, on_delete=models.CASCADE, verbose_name='产品材质')
    samp_long = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品长度')
    samp_width = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品宽度')
    samp_height = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品高度')
    size_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='尺寸单位')
    fac_number = models.TextField(blank=True, null=True, verbose_name='工厂编号')
    sketch_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='图稿编号')  # 关联Sketch_design表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品数量')
    amount_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量单位')
    order_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单日期')
    factory = models.ForeignKey('Basic_info.Factory', related_name='sample_detail_factory',
                                blank=True, null=True, on_delete=models.CASCADE, verbose_name='工厂')
    actual_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='实际交期')
    cancle_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='取消日期')
    fac_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂交期')
    status = models.TextField(blank=True, null=True, verbose_name='状态')
    finish = models.CharField(max_length=100, choices=(('True', '已完成'), ('False', '未完成')),
                              blank=True, null=True, default='False', verbose_name='是否完成')
    finish_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='完成日期')
    sample_remark = models.TextField(max_length=4000, blank=True, null=True, verbose_name='样品单备注')
    # ----------以下字段在编辑页不展示----------
    new_no = models.TextField(blank=True, null=True, verbose_name='备用')
    sz_no = models.TextField(blank=True, null=True, verbose_name='备用')
    weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品重量')
    estimate_shipdate = models.TextField(blank=True, null=True, verbose_name='备用')
    project = models.TextField(blank=True, null=True, verbose_name='备用')
    color = models.TextField(blank=True, null=True, verbose_name='备用')
    season = models.TextField(blank=True, null=True, verbose_name='备用')
    type = models.TextField(blank=True, null=True, verbose_name='备用')
    peculiarity = models.TextField(blank=True, null=True, verbose_name='备用')
    to_tpe_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    to_hk_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    to_sz_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    to_usa_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    date1 = models.TextField(blank=True, null=True, verbose_name='备用')
    memo = models.TextField(blank=True, null=True, verbose_name='备用')
    net_weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    gross_weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    actual_qty = models.TextField(blank=True, null=True, verbose_name='备用')
    long = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    width = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    height = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    each = models.TextField(blank=True, null=True, verbose_name='备用')
    inner = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    middle = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    box = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    cno = models.TextField(blank=True, null=True, verbose_name='备用')
    qc1 = models.TextField(blank=True, null=True, verbose_name='备用')
    qc2 = models.TextField(blank=True, null=True, verbose_name='备用')
    qc3 = models.TextField(blank=True, null=True, verbose_name='备用')
    fqc = models.TextField(blank=True, null=True, verbose_name='备用')
    pum_id = models.TextField(blank=True, null=True, verbose_name='备用')
    is_resample = models.CharField(max_length=20, choices=(('True', '是'), ('False', '否')),
                                   blank=True, null=True, verbose_name='备用')
    sample_status = models.CharField(max_length=200, blank=True, null=True, verbose_name='复样单样品状态')
    request = models.TextField(blank=True, null=True, verbose_name='备用')
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='记录插入时间')
    is_omr_sure = models.CharField(max_length=200, choices=(('True', '已确认'), ('False', '未确认')),
                                   blank=True, null=True, verbose_name='OMR是否确认')
    omr_sure_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='OMR确认时间')
    fmr = models.ForeignKey('Basic_info.Staff', related_name='sample_detail_staff',
                            blank=True, null=True, on_delete=models.CASCADE, verbose_name='跟进的FMR')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_no

    class Meta:
        unique_together = (("number", "item_no"),)
        ordering = ['number']
        db_table = "repeat_sample_detail"
        verbose_name = '复样明细表'
        verbose_name_plural = verbose_name


class Sample_target(models.Model):
    """复样单修改与签名"""
    choice = (
        ('True', '是'),
        ('False', '否'),
    )
    number = models.CharField(max_length=255, blank=True, null=True, verbose_name='复样单号')  # 关联Repeat_sample
    item_no = models.CharField(max_length=250, blank=True, null=True, verbose_name='复样单item编号')
    change_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='修改日期')
    change_desc = models.TextField(blank=True, null=True, verbose_name='修改明细')
    omr_sure = models.CharField(max_length=20, choices=choice, default='False', verbose_name='OMR是否确认')
    omr_sure_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='OMR确认时间')
    fmr_sure = models.CharField(max_length=20, choices=choice, default='False', verbose_name='FMR是否确认')
    fmr_sure_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='FMR确认时间')
    omr_check = models.CharField(max_length=20, choices=choice, default='False', verbose_name='OMR是否检验')
    omr_check_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='OMR检验时间')
    fmr_check = models.CharField(max_length=20, choices=choice, default='False', verbose_name='FMR是否检验')
    fmr_check_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='FMR检验时间')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_no

    class Meta:
        unique_together = (("number", "item_no"),)
        ordering = ['item_no']
        db_table = "sample_target"
        verbose_name = '复样单修改与签名'
        verbose_name_plural = verbose_name


class Po(models.Model):
    """资讯部录单总表"""
    customer = models.ForeignKey('Basic_info.Customer', related_name='po_customer',
                                 max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='订单所属客户')
    customer_pono = models.CharField(max_length=250, blank=True, null=True, verbose_name='客人PO')
    cus_receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人收货日期')
    fina_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='最终交货日期')
    receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='接收到客人订单日期')
    order_number = models.CharField(max_length=250, unique=True, verbose_name='我司订单编号')
    fac_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂交货日期')
    produce_native_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='生产通知单日')
    delivery_condition = models.ForeignKey('Basic_info.Delivery', on_delete=models.CASCADE, blank=True,
                                           null=True, related_name='po_delivery_condition', verbose_name='客人交货条件')
    port = models.ForeignKey('Basic_info.Export_port', related_name='po_port',
                             max_length=255, blank=True, null=True, on_delete=models.CASCADE, verbose_name='客人出货港口')
    omr = models.ForeignKey('Basic_info.Staff', related_name='po_omr', blank=True, null=True,
                            on_delete=models.CASCADE, verbose_name='承办员')
    pay_type = models.CharField(max_length=60, blank=True, null=True, verbose_name='财务付款方式')
    # ----------以下字段在编辑页不展示----------
    special_remark = models.TextField(blank=True, null=True, verbose_name='订单总的注意事项说明')
    special_remark2 = models.TextField(blank=True, null=True, verbose_name='注意事项备用1')
    special_remark3 = models.TextField(blank=True, null=True, verbose_name='注意事项备用2')
    order_status = models.TextField(blank=True, null=True, verbose_name='订单状态')
    mai = models.TextField(blank=True, null=True, verbose_name='客人外箱正唛')
    ce_mai = models.TextField(blank=True, null=True, verbose_name='外箱侧唛')
    middle_mai = models.TextField(blank=True, null=True, verbose_name='中盒唛头')
    inner_mai = models.TextField(blank=True, null=True, verbose_name='内盒唛头')
    fen_pi = models.CharField(max_length=100, blank=True, null=True,
                              choices=(('True', '是'), ('False', '否')), verbose_name='备用')
    parent_pono = models.CharField(max_length=250, blank=True, null=True, verbose_name='未分批前的PoNO')
    supervise = models.TextField(blank=True, null=True, verbose_name='备用')
    supervise1 = models.TextField(blank=True, null=True, verbose_name='备用')
    product_send = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    product_receive = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    ship_style = models.CharField(max_length=255, blank=True, null=True, verbose_name='备用')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.order_number

    class Meta:
        ordering = ['order_number']
        db_table = "po"
        verbose_name = '资讯部录单总表'
        verbose_name_plural = verbose_name


class Po_detail(models.Model):
    """资讯部录单订单详情表"""
    po = models.CharField(max_length=255, verbose_name='我司Po订单编号')  # 和资讯Po表关联
    item_no = models.CharField(max_length=255, verbose_name='我司Item NO')
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人Item NO')
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='中文描述')
    edesc = models.CharField(max_length=255, blank=True, null=True, verbose_name='英文描述')
    fac_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂Item NO')
    texture = models.ForeignKey('Basic_info.Texture', related_name='po_detail_texture', blank=True, null=True, 
                                max_length=255, on_delete=models.CASCADE, verbose_name='材质')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量单位')
    costrate = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人要价')
    currency = models.ForeignKey('Basic_info.Currency', on_delete=models.CASCADE,
                                 max_length=255, blank=True, null=True, related_name='po_detail_currency', verbose_name='货币类型')
    each_box = models.ForeignKey('Order.Package_texture', related_name='po_detail_package',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='单一包装')
    outside_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装外盒数量')
    middle_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装中盒数量')
    inner_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装内盒数量')
    box_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装数量单位')
    for_profit_report = models.TextField(choices=(('True', '是'), ('False', '否')),
                                         blank=True, null=True, default='True', verbose_name='利润标志说明')
    special_remark = models.TextField(blank=True, null=True, verbose_name='注意事项')
    fac_delivery = models.ForeignKey('Basic_info.Delivery', on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='po_detail_fac_delivery', verbose_name='工厂交货条件')
    fac_delivery_port = models.ForeignKey('Basic_info.Export_port', on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='po_detail_fac_port', verbose_name='工厂出货港口')
    fmr = models.ForeignKey('Basic_info.Staff', blank=True, null=True, on_delete=models.CASCADE,
                            related_name='po_detail_fmr', verbose_name='FMR人员')
    fqc = models.ForeignKey('Basic_info.Staff', blank=True, null=True, on_delete=models.CASCADE,
                            related_name='po_detail_fqc', verbose_name='FQC人员')
    sale_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='消出货日期')
    # ------------以下为预留字段-------------
    cancle_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='订单取消日期')
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_no

    class Meta:
        unique_together = (("po", "item_no"),)
        ordering = ['item_no']
        db_table = "po_detail"
        verbose_name = '资讯部录单订单详情'
        verbose_name_plural = verbose_name


class Contract(models.Model):
    """合同"""
    po = models.CharField(max_length=255, verbose_name='我司Po订单编号')  # 和资讯Po表关联
    item_no = models.CharField(max_length=255, verbose_name='Item NO')  # 和资讯Po_detail表关联
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人货号')  # 取自Po表
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')  # 取自Po_detail表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人订购数量')  # 取自Po_detail表
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人数量单位')  # 取自Po_detail表
    oa_sure_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='OA确认日期')
    fac_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂订单数量')  # 取自Po_detail表
    fac_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂数量单位')  # 取自Po_detail表
    # 合同信息
    factory = models.ForeignKey('Basic_info.Factory', related_name='contract_factory',
                                blank=True, null=True, on_delete=models.CASCADE, verbose_name='生产工厂')
    fac_currency = models.ForeignKey('Basic_info.Currency', related_name='contract_fac_currency',
                                     on_delete=models.CASCADE, blank=True, null=True, verbose_name='工厂货币类型')
    fac_cost = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂价格')
    fac_total = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂合计金额')
    cancle_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='订单取消日期')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_no

    class Meta:
        unique_together = (("po", "item_no"),)
        ordering = ['po']
        db_table = "contract"
        verbose_name = '合同'
        verbose_name_plural = verbose_name


class Product_send(models.Model):
    """消出货"""
    po = models.CharField(max_length=255, verbose_name='我司Po订单编号')  # 和资讯Po表关联
    item_no = models.CharField(max_length=255, verbose_name='Item NO')  # 和资讯Po_detail表关联
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人货号')  # 取自资讯Po表
    fac_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂货号')  # 取自资讯Po表
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')  # 取自资讯Po表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='生产数量')  # 取自Po_detail表
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量单位')  # 取自Po_detail表
    fmr = models.ForeignKey('Basic_info.Staff', related_name='product_send_fmr',
                            blank=True, null=True, on_delete=models.CASCADE, verbose_name='FMR')
    qc1 = models.ForeignKey('Basic_info.Staff', blank=True, null=True, on_delete=models.CASCADE,
                            related_name='product_send_qc1', verbose_name='第一次检验人员')
    qc2 = models.ForeignKey('Basic_info.Staff', blank=True, null=True, on_delete=models.CASCADE,
                            related_name='product_send_qc2', verbose_name='第二次检验人员')
    qc3 = models.ForeignKey('Basic_info.Staff', blank=True, null=True, on_delete=models.CASCADE,
                            related_name='product_send_qc3', verbose_name='第三次检验人员')
    rqc1 = models.ForeignKey('Basic_info.Staff', blank=True, null=True, on_delete=models.CASCADE,
                             related_name='product_send_rqc1', verbose_name='第一次复检人员')
    rqc2 = models.ForeignKey('Basic_info.Staff', blank=True, null=True, on_delete=models.CASCADE,
                             related_name='product_send_rqc2', verbose_name='第二次复检人员')
    fqc = models.ForeignKey('Basic_info.Staff', blank=True, null=True, on_delete=models.CASCADE,
                            related_name='product_send_fqc', verbose_name='FQC人员')
    cancle_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='取消日期')
    sale_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='消出货日期')
    no_pass = models.CharField(max_length=100, choices=(('True', '是'), ('False', '否')),
                               blank=True, null=True, default='False', verbose_name='验货不通过放货')
    send_person = models.ForeignKey('Basic_info.Staff', blank=True, null=True,
                                    related_name='product_send_person', on_delete=models.CASCADE, verbose_name='放货人')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_no

    class Meta:
        unique_together = (("po", "item_no"),)
        ordering = ['item_no']
        db_table = "product_send"
        verbose_name = '消出货'
        verbose_name_plural = verbose_name


class OMR(models.Model):
    """OMR录单"""
    po = models.CharField(max_length=255, unique=True, verbose_name='我司Po订单编号')  # 和资讯Po表关联
    customer_pono = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人PO#')  # 取自资讯Po表
    receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='接单日期')  # 取自资讯Po表
    cus_receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='交货日期')  # 取自资讯Po表
    fac_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂交货期')  # 取自资讯Po表
    omr = models.CharField(max_length=255, blank=True, null=True, verbose_name='OMR')  # 取自资讯Po表  承办员
    special_remark = models.TextField(blank=True, null=True, verbose_name='注意事项')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.po

    class Meta:
        ordering = ['po']
        db_table = "omr"
        verbose_name = 'OMR录单'
        verbose_name_plural = verbose_name


class OMR_po_detail(models.Model):
    """OMR订单详情"""
    po = models.CharField(max_length=255, verbose_name='我司Po订单编号')  # 和资讯Po表关联
    item_no = models.CharField(max_length=255, verbose_name='Item NO')  # 和资讯Po_detail表关联
    customer_pono = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人PO#')  # 取自Po表
    receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='PO接单日期')  # 取自Po表
    cus_receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人收货日期')  # 取自Po表
    fac_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂交货期')  # 取自Po表
    omr = models.CharField(max_length=255, blank=True, null=True, verbose_name='OMR')  # 取自资讯Po表  承办员
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品描述')  # 取自Po_detail表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')  # 取自Contract表
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量单位')  # 取自Contract表
    oa_sure_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='OA确认日期')  # 取自Contract表
    factory = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单工厂')  # 取自Contract表
    texture = models.CharField(max_length=255, blank=True, null=True, verbose_name='材质')  # 取自Po_detail表
    port = models.CharField(max_length=255, blank=True, null=True, verbose_name='出货港口')  # 取自Po_detail表
    process = models.CharField(max_length=255, blank=True, null=True, verbose_name='进度')
    produce_record = models.CharField(max_length=255, blank=True, null=True, verbose_name='生产记录表送出日')
    mark_notice_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='唛头通知日期')
    label_sure_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='贴标确认日期')
    label_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='贴标送出日期')
    sample_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='测试样寄出日')
    sample_pass_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='测试样通过日')
    product_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='确认样寄交客户')
    product_sure_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='生产确认样确认')
    midterm_inspect = models.CharField(max_length=255, blank=True, null=True, verbose_name='期中验货日')
    booking_so = models.CharField(max_length=255, blank=True, null=True, verbose_name='Booking S/O')
    ichiban_inspect = models.CharField(max_length=255, blank=True, null=True, verbose_name='我司验货日')
    customer_inspect = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人验货日')
    pl_come_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='配料送交工厂')
    box_sure_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='彩盒确认日期')
    box_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='彩盒寄出日期')
    shipping_data = models.CharField(max_length=255, blank=True, null=True, verbose_name='shipping资料')
    special_remark = models.TextField(blank=True, null=True, verbose_name='注意事项')
    special_remark1 = models.TextField(blank=True, null=True, verbose_name='注意事项')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.po

    class Meta:
        unique_together = (("po", "item_no"),)
        ordering = ['po']
        db_table = "omr_po_detail"
        verbose_name = 'OMR订单详情'
        verbose_name_plural = verbose_name


class FMR(models.Model):
    """FMR"""
    po = models.CharField(max_length=255, verbose_name='我司Po订单编号')  # 和资讯Po表关联
    item_no = models.CharField(max_length=255, verbose_name='Item NO')  # 和资讯Po_detail表关联
    receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='接单日期')  # 取自Po表
    fac_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂交货期')  # 取自Po表
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='品名')  # 取自Po_detail表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品数量')  # 取自Po_detail表
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='计量单位')  # 取自Po_detail表
    factory = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂')  # 取自Contract表
    oa_sure_date = models.CharField(max_length=255, verbose_name='OA确认日期')  # 取自Contract表
    texture = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品材质')  # 取自Po_detail表
    process = models.ForeignKey('Basic_info.Texture_process', on_delete=models.CASCADE,
                                max_length=255, blank=True, related_name='fmr_texture_process', verbose_name='产品进度')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.po

    class Meta:
        unique_together = (("po", "item_no"),)
        ordering = ['po']
        db_table = "fmr"
        verbose_name = 'FMR'
        verbose_name_plural = verbose_name


class Material_sign(models.Model):
    """材料签收总表"""
    po = models.CharField(max_length=255, verbose_name='我司Po订单编号')  # 和资讯Po表关联
    item_no = models.CharField(max_length=255, verbose_name='Item NO')  # 和资讯Po_detail表关联
    omr = models.CharField(max_length=255, blank=True, null=True, verbose_name='承办人员')  # 取自Po表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品数量')  # 取自Po_detail表
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='计量单位')  # 取自Po_detail表
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')  # 取自Po_detail表
    customer_pono = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人PO#')  # 取自Po表
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人NO')  # 取自Po_detail表
    factory = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂')  # 取自Contract表
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_no

    class Meta:
        unique_together = (("po", "item_no"),)
        ordering = ['item_no']
        db_table = "material_sign"
        verbose_name = '材料签收总表'
        verbose_name_plural = verbose_name


class Material_sign_detail(models.Model):
    """材料签收明细"""
    po = models.CharField(max_length=255, verbose_name='我司Po订单编号')  # 和资讯Po表关联
    item_no = models.CharField(max_length=255, verbose_name='Item NO')  # 和资讯Po_detail表关联
    texture = models.ForeignKey('Basic_info.Texture', related_name='Material_sign_detail_texture',
                                on_delete=models.CASCADE, blank=True, null=True, verbose_name='材料明细')
    pc_count = models.CharField(max_length=255, blank=True, null=True, verbose_name='每PC用量')
    pc_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='PC用量单位')
    need_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='所需数量')
    need_qty_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='所需数量单位')
    name = models.TextField(blank=True, null=True, verbose_name='材料名称')
    provide_type = models.TextField(blank=True, null=True,
                                    choices=(('provide', '提供'), ('instead', '代购')), verbose_name='材料提供方式')
    provide_from = models.TextField(blank=True, null=True, verbose_name='材料来源地')
    is_order = models.TextField(blank=True, null=True,
                                choices=(('True', '是'), ('False', '否')), verbose_name='是否需订购')
    actual_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='实送数量')
    actual_qty_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='实送数量单位')
    send_material_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='送料日期')
    sender = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                               related_name='material_sign_detail_sender', verbose_name='经送人')
    special_remark = models.TextField(blank=True, null=True, verbose_name='备注说明')
    accessory_cost = models.CharField(max_length=255, blank=True, null=True, verbose_name='材料单价')
    accessory_currency = models.ForeignKey('Basic_info.Currency', on_delete=models.CASCADE, blank=True, null=True,
                                           related_name='material_sign_detail_accessory_currency',
                                           verbose_name='材料单价货币')
    accessory_cost_total = models.CharField(max_length=255, blank=True, null=True, verbose_name='材料总价')
    accessory_total_currency = models.ForeignKey('Basic_info.Currency', on_delete=models.CASCADE, blank=True, null=True,
                                                 related_name='material_sign_detail_acc_total_currency',
                                                 verbose_name='材料总价货币')
    deduct_invoice_no = models.TextField(blank=True, null=True, verbose_name='扣款发票号码')
    factory = models.ForeignKey('Basic_info.Factory', on_delete=models.CASCADE, blank=True, null=True,
                                related_name='accessory_category_factory', verbose_name='下单工厂')
    fac_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂订单数量')
    fac_qty_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量单位')
    price = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单单价')
    order_currency = models.ForeignKey('Basic_info.Currency', on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='material_sign_detail_order_currency', verbose_name='下单单价货币')
    total = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单总价')
    total_currency = models.ForeignKey('Basic_info.Currency', on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='material_sign_detail_total_currency', verbose_name='下单总价货币')
    order_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单日期')
    pay_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='交费期')
    is_shipment = models.TextField(blank=True, null=True,
                                   choices=(('True', '是'), ('False', '否')), verbose_name='是否消出货')
    qc = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                           related_name='material_sign_detail_qc', verbose_name='QC')
    fqc = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                            related_name='material_sign_detail_fqc', verbose_name='FQC')
    actual_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='实际出货期')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=25, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.item_no

    class Meta:
        ordering = ['item_no']
        db_table = "material_sign_detail"
        verbose_name = '材料签收明细表'
        verbose_name_plural = verbose_name
