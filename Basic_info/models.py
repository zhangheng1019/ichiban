from django.db import models
from django.contrib.auth.models import *
# Create your models here.


class Texture(models.Model):
    """产品材质"""
    name = models.CharField(max_length=200, unique=True, verbose_name='中文名')
    code = models.CharField(max_length=60, unique=True, verbose_name='材质编码')
    ename = models.CharField(max_length=200, blank=True, null=True, verbose_name='英文名')
    desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='中文描述')
    edesc = models.TextField(blank=True, null=True, verbose_name='英文描述')
    lastdate = models.DateTimeField(auto_now=True, verbose_name='最后操作时间')
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
        db_table = "texture"
        verbose_name = '产品材质'
        verbose_name_plural = verbose_name


class Texture_process(models.Model):
    """保存产品进度情况"""
    texture = models.ForeignKey('Basic_info.Texture', related_name='texture_process_texture',
                                blank=True, null=True, on_delete=models.CASCADE, verbose_name='材质ID')
    texture_process = models.CharField(max_length=200, blank=True, null=True, verbose_name='进度中文描述')
    not_in_process = models.CharField(max_length=200, blank=True, null=True, verbose_name='进度未完成部分中文描述')
    ahead_days = models.FloatField(blank=True, null=True, verbose_name='进度完成所需时间')
    code = models.CharField(max_length=200, unique=True, verbose_name='产品进度英文代码')
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
        ordering = ['ahead_days']
        db_table = "texture_process"
        verbose_name = '产品进度情况'
        verbose_name_plural = verbose_name


class Material_cate(models.Model):
    """配件的材料组成"""
    category = models.CharField(max_length=255, verbose_name='类别的英文代码')
    desc = models.CharField(max_length=255, verbose_name='类别的中文描述')
    child_cate_edesc = models.CharField(max_length=255, verbose_name='子类别的英文描述')
    child_cate = models.CharField(max_length=255, verbose_name='子类别的中文描述')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']
        db_table = "material_cate"
        verbose_name = '配件类别'
        verbose_name_plural = verbose_name


class Material(models.Model):
    """产品材料"""
    option = (
        ('True', '是'),
        ('False', '否'),
    )
    po = models.ForeignKey('Order.Po', related_name='material_po', blank=True, null=True,
                           on_delete=models.CASCADE, verbose_name='我公司PoNO')
    po_detail = models.ForeignKey('Order.Po_detail', on_delete=models.CASCADE, blank=True, null=True,
                                  related_name='material_po_detail', verbose_name='po_detail')
    to_factory_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='配送至工厂日期')
    fac_qty = models.FloatField(blank=True, null=True, verbose_name='工厂订单数量')
    qty_unit = models.ForeignKey('Basic_info.Unit', on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='material_fac_qty_unit', verbose_name='数量单位')
    fac_order_qty = models.FloatField(blank=True, null=True, verbose_name='订单数量')
    fac_actual_qty = models.FloatField(blank=True, null=True, verbose_name='实送数量')
    sender = models.CharField(max_length=255, blank=True, null=True, verbose_name='经送人')
    send_remark = models.TextField(blank=True, null=True, verbose_name='经送说明')
    fac_remark = models.TextField(blank=True, null=True, verbose_name='工厂说明')
    method = models.CharField(max_length=255, blank=True, null=True, verbose_name='材料提供方式')
    material_from = models.CharField(max_length=255, blank=True, null=True, verbose_name='材料来源地')
    is_order = models.CharField(max_length=255, choices=option, default='False', verbose_name='是否需要订购')
    deducted_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣款日期')
    invoice_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣款发票号')
    mat_cost = models.FloatField(default=0, verbose_name='材料单价')
    currency = models.ForeignKey('Basic_info.Currency', related_name='material_currency', blank=True, null=True,
                                 on_delete=models.CASCADE, verbose_name='货币币种')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='材料名称')
    belong = models.ForeignKey('Basic_info.Material_cate', related_name='material_category',
                               blank=True, null=True, on_delete=models.CASCADE, verbose_name='所属材料类别')
    factory = models.ForeignKey('Basic_info.Factory', related_name='material_factory', blank=True, null=True,
                                on_delete=models.CASCADE, verbose_name='下单工厂')
    order_cost = models.FloatField(default=0, verbose_name='下单单价')
    order_currency = models.ForeignKey('Basic_info.Currency', related_name='material_order_currency', blank=True, null=True,
                                       on_delete=models.CASCADE, verbose_name='货币币种')
    order_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单日期')
    delivery_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='要求交期')
    actual_delivery_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='实际交期')
    special_remark = models.TextField(blank=True, null=True, verbose_name='配件的注意事项说明')
    qc = models.ForeignKey('Basic_info.Staff', related_name='material_qc', blank=True, null=True,
                           on_delete=models.CASCADE, verbose_name='QC')
    fqc = models.ForeignKey('Basic_info.Staff', related_name='material_fqc', blank=True, null=True,
                            on_delete=models.CASCADE, verbose_name='FQC')
    is_complate = models.CharField(max_length=255, choices=option, default='False', verbose_name='是否完成')
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
        db_table = "material"
        verbose_name = '产品材料'
        verbose_name_plural = verbose_name


class Position(models.Model):
    """职务表"""
    job = models.CharField(max_length=200, unique=True, verbose_name='职务名称')
    code = models.CharField(max_length=200, blank=True, null=True, verbose_name='职务代码')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.job

    class Meta:
        ordering = ['job']
        db_table = "position"
        verbose_name = '职务设置'
        verbose_name_plural = verbose_name


class Currency(models.Model):
    """货币设置"""
    name = models.CharField(max_length=60, unique=True, verbose_name='货币名')
    code = models.CharField(max_length=60, unique=True, verbose_name='货币符号')
    to_rmb = models.FloatField(blank=True, null=True, verbose_name='对人命币汇率')
    to_us = models.FloatField(blank=True, null=True, verbose_name='对美元汇率')
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
        db_table = "currency"
        verbose_name = '货币设置'
        verbose_name_plural = verbose_name


class Category(models.Model):
    """保存产品系列信息资料表"""
    code = models.CharField(max_length=200, unique=True, verbose_name='系列代号')
    parent_category = models.CharField(max_length=20, blank=True, null=True, verbose_name='产品系列上级系列id')
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
        ordering = ['code']
        db_table = "category"
        verbose_name = '系列设置'
        verbose_name_plural = verbose_name


class Unit(models.Model):
    """计量单位设置"""
    name = models.CharField(max_length=200, unique=True, verbose_name='单位名称')
    sign = models.CharField(max_length=200, unique=True, verbose_name='单位符号')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.sign

    class Meta:
        ordering = ['name']
        db_table = "unit"
        verbose_name = '计量单位设置'
        verbose_name_plural = verbose_name


class Area(models.Model):
    """地区设置"""
    name = models.CharField(max_length=200, unique=True, verbose_name='地区中文名')
    code = models.CharField(max_length=200, unique=True, verbose_name='地区编码')
    desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='地区描述')
    fmr = models.ForeignKey('Basic_info.Staff', related_name='area_fmr',
                            blank=True, null=True, on_delete=models.CASCADE, verbose_name='负责的FMR')
    qc = models.ForeignKey('Basic_info.Staff', related_name='area_qc',
                           blank=True, null=True, on_delete=models.CASCADE, verbose_name='负责的QC')
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
        ordering = ['code']
        db_table = "area"
        verbose_name = '地区设置'
        verbose_name_plural = verbose_name


class Department(models.Model):
    """部门设置"""
    name = models.CharField(max_length=200, unique=True, verbose_name='部门名称')
    charge_id = models.CharField(max_length=30, blank=True, null=True, verbose_name='主管ID')
    charge_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='主管名')
    last_dept = models.CharField(max_length=200, blank=True, null=True, verbose_name='上级部门')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=60, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = "department"
        verbose_name = '部门设置'
        verbose_name_plural = verbose_name


class Head_quarter(models.Model):
    """总部设置"""
    name = models.CharField(max_length=200, unique=True, verbose_name='总部名字')
    code = models.CharField(max_length=200, unique=True, verbose_name='总部代码')
    city = models.CharField(max_length=200, blank=True, null=True, verbose_name='总部所在城市')
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
        db_table = "head_quarter"
        verbose_name = '总部设置'
        verbose_name_plural = verbose_name


class Company(models.Model):
    """公司设置"""
    name = models.CharField(max_length=200, unique=True, verbose_name='公司名字')
    code = models.CharField(max_length=200, unique=True, verbose_name='公司代号')
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
        db_table = "company"
        verbose_name = '公司设置'
        verbose_name_plural = verbose_name


class Delivery(models.Model):
    """出货条件"""
    code = models.CharField(max_length=100, unique=True, verbose_name='条件代号')
    desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='中文描述')
    edesc = models.CharField(max_length=200, blank=True, null=True, verbose_name='英文描述')
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
        ordering = ['code']
        db_table = 'delivery'
        verbose_name = '出货条件'
        verbose_name_plural = verbose_name


class Export_port(models.Model):
    """POE港口设置"""
    name = models.CharField(max_length=200, unique=True, verbose_name='港口中文名称')
    ename = models.CharField(max_length=200, unique=True, verbose_name='港口英文名称')
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
        db_table = 'export_port'
        verbose_name = 'POE港口设置'
        verbose_name_plural = verbose_name


class Export_type(models.Model):
    """出货方式"""
    name = models.CharField(max_length=200, unique=True, verbose_name='方式名称')
    desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='中文描述')
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
        db_table = 'export_type'
        verbose_name = '出货方式'
        verbose_name_plural = verbose_name


class Customer(models.Model):
    """客人信息"""
    code = models.CharField(max_length=200, unique=True, verbose_name='客户编码')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='客户名')
    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='客人联系电话')
    fax = models.CharField(max_length=200, blank=True, null=True, verbose_name='传真')
    street = models.CharField(max_length=100, blank=True, null=True, verbose_name='所住街道名')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='所住城市')
    province = models.CharField(max_length=100, blank=True, null=True, verbose_name='所住省名')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='所住国家')
    post_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='所住地的邮编')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='邮箱地址')
    join_date = models.DateTimeField(blank=True, null=True, verbose_name='成为我司客人的时间')
    contact = models.CharField(max_length=200, blank=True, null=True, verbose_name='联系人')
    avg_profit = models.CharField(max_length=30, blank=True, null=True,
                                  choices=(('True', '是'), ('False', '否')), verbose_name='是否平分利润')
    is_agree = models.CharField(max_length=30, blank=True, null=True,
                                choices=(('True', '是'), ('False', '否')), verbose_name='是否一定要签合约')
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
        ordering = ['code']
        db_table = "customer"
        verbose_name = '客人信息'
        verbose_name_plural = verbose_name


class Customer_mark(models.Model):
    """客户唛头"""
    code = models.ForeignKey('Basic_info.Customer', on_delete=models.CASCADE, blank=True, null=True,
                             related_name='mark_customer', verbose_name='客户代码')
    request = models.TextField(blank=True, null=True, verbose_name='客户要求')
    zhenmai = models.TextField(blank=True, null=True, verbose_name='正唛')
    cemai = models.TextField(blank=True, null=True, verbose_name='侧唛')
    neimai = models.TextField(blank=True, null=True, verbose_name='内唛')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.code)

    class Meta:
        ordering = ['code']
        db_table = "customer_mark"
        verbose_name = '客户唛头'
        verbose_name_plural = verbose_name


class Export_country(models.Model):
    """出口国家"""
    name = models.CharField(max_length=200, unique=True, verbose_name='国家中文名')
    code = models.CharField(max_length=200, unique=True, verbose_name='国家编码')
    ename = models.CharField(max_length=200, blank=True, null=True, verbose_name='国家英文名')
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
        db_table = "export_country"
        verbose_name = '出口国家'
        verbose_name_plural = verbose_name


class Export_company(models.Model):
    """进出口公司信息"""
    name = models.CharField(max_length=200, verbose_name='进出口公司名字')
    code = models.CharField(max_length=200, unique=True, verbose_name='进出口公司代码')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='户口抬头')
    account_no = models.CharField(max_length=200, blank=True, null=True, verbose_name='户口账号')
    bank = models.CharField(max_length=200, blank=True, null=True, verbose_name='户口银行')
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
        db_table = "export_company"
        verbose_name = '进出口公司'
        verbose_name_plural = verbose_name


class Staff(models.Model):
    """员工信息"""
    name = models.CharField(max_length=60, verbose_name='员工中文名')
    ename = models.CharField(max_length=60, blank=True, null=True, verbose_name='英文名')
    emp_ename = models.CharField(max_length=60, blank=True, null=True, verbose_name='职员英文缩写')
    emp_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='考勤卡号')
    id_card = models.CharField(max_length=30, blank=True, null=True, verbose_name='身份证号')
    company = models.ForeignKey('Basic_info.Company', on_delete=models.CASCADE, blank=True, null=True,
                                related_name='staff_comp', verbose_name='所属公司')
    sex = models.CharField(max_length=30, blank=True, null=True,
                           choices=(('male', '男'), ('female', '女')), verbose_name='性别')
    birthday = models.CharField(max_length=255, blank=True, null=True, verbose_name='出生日期')
    is_marry = models.CharField(max_length=30, blank=True, null=True,
                                choices=(('True', '已婚'), ('False', '未婚')), verbose_name='婚否')
    graduate_school = models.CharField(max_length=100, blank=True, null=True, verbose_name='毕业学校')
    graduate_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='毕业时间')
    major = models.CharField(max_length=100, blank=True, null=True, verbose_name='所学专业')
    education = models.CharField(max_length=50, blank=True, null=True, verbose_name='学历')
    hometown = models.CharField(max_length=100, blank=True, null=True, verbose_name='家乡')
    addr = models.CharField(max_length=100, blank=True, null=True, verbose_name='详细地址')
    home_tel = models.CharField(max_length=100, blank=True, null=True, verbose_name='家乡联系电话')
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='联系电话')
    department = models.ForeignKey('Basic_info.Department', on_delete=models.CASCADE, related_name='staff_dep',
                                   blank=True, null=True, verbose_name='所属部门')
    position = models.ForeignKey('Basic_info.Position', on_delete=models.CASCADE, related_name='staff_position',
                                 blank=True, null=True, verbose_name='职务')
    offer_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='应聘日期')
    join_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='入职日期')
    staff_form = models.CharField(max_length=255, blank=True, null=True, verbose_name='聘用形式')
    become_real_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='转正日期')
    contract_end_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='合同终止日期')
    quit_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='离职时间')
    quit_reason = models.CharField(max_length=100, blank=True, null=True, verbose_name='离职原因')
    quit_extend_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='离职延时时间')
    quit_remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='离职补充说明')
    clear = models.CharField(max_length=30, blank=True, null=True, verbose_name='离职时财务是否结清')
    math_score = models.FloatField(max_length=30, blank=True, null=True, verbose_name='数学成绩')
    english_score = models.FloatField(max_length=30, blank=True, null=True, verbose_name='英语成绩')
    level = models.CharField(max_length=30, blank=True, null=True, verbose_name='备用')
    titled = models.CharField(max_length=30, blank=True, null=True, verbose_name='职称')
    email = models.CharField(max_length=60, blank=True, null=True, verbose_name='email地址')
    charge = models.CharField(max_length=30, blank=True, null=True, verbose_name='直接主管')
    agent_charge = models.CharField(max_length=60, blank=True, null=True, verbose_name='代理主管')
    manager = models.CharField(max_length=60, blank=True, null=True, verbose_name='经理')
    agent_manager = models.CharField(max_length=60, blank=True, null=True, verbose_name='公司代理经理')
    table = models.CharField(max_length=255, blank=True, null=True, verbose_name='表')
    field = models.CharField(max_length=255, blank=True, null=True, verbose_name='字段')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = "staff"
        verbose_name = '员工信息'
        verbose_name_plural = verbose_name


class EmployeeRelationship(models.Model):
    """员工的上司和下属关系关联表"""
    staff = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                              related_name='staff_name', verbose_name='员工')
    leader = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                               related_name='leader_staff', verbose_name='直接上司')
    branch = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                               related_name='branch_staff', verbose_name='直接下属')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.staff)

    class Meta:
        ordering = ['staff']
        db_table = "employee_relationship"
        verbose_name = '员工上下级信息'
        verbose_name_plural = verbose_name


class Factory(models.Model):
    """工厂信息"""
    code = models.CharField(max_length=200, unique=True,  verbose_name='工厂代码')
    contact = models.CharField(max_length=100, blank=True, null=True, verbose_name='联系人')
    name = models.CharField(max_length=200, verbose_name='工厂中文全名')
    ename = models.TextField(blank=True, null=True, verbose_name='工厂英文名')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='所在国家')
    province = models.CharField(max_length=100, blank=True, null=True, verbose_name='所在省份')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='所在城市')
    fax = models.CharField(max_length=100, blank=True, null=True, verbose_name='传真')
    tel = models.CharField(max_length=100, blank=True, null=True, verbose_name='电话')
    area = models.ForeignKey('Basic_info.Area', on_delete=models.CASCADE, blank=True, null=True,
                             related_name='fac_area', verbose_name='所在地区代号')
    street = models.CharField(max_length=100, blank=True, null=True, verbose_name='所在街道')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='邮箱地址')
    post_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='所在地邮编')
    export_company_code = models.ForeignKey('Basic_info.Export_company', on_delete=models.CASCADE, blank=True, null=True,
                                            related_name='fac_company', verbose_name='进出口公司代码')
    fac_remark = models.TextField(blank=True, null=True, verbose_name='备注')
    # ----------以下字段不在编辑页展示----------
    fac_texture = models.ForeignKey('Basic_info.Texture', to_field='name', on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='fac_texture', verbose_name='生产材质')
    fac_master = models.CharField(max_length=100, blank=True, null=True, verbose_name='工厂负责人')
    fac_assess = models.CharField(max_length=200, blank=True, null=True, verbose_name='工厂地址经纬度')
    arrive_type = models.TextField(blank=True, null=True, verbose_name='送达方式')
    insert_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='记录插入时间')
    is_check = models.CharField(max_length=20, blank=True, null=True,
                                choices=(('True', '是'), ('False', '否')), verbose_name='是否已经被QC验厂通过')
    fmr = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                            related_name='fmr_staff', verbose_name='评估工厂的FMR人员')
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
        db_table = "factory"
        verbose_name = '工厂信息'
        verbose_name_plural = verbose_name


class Code(models.Model):
    """编码设置"""
    category_code = models.CharField(max_length=100, unique=True, verbose_name='类别编码')
    first = models.CharField(max_length=60, blank=True, null=True, verbose_name='一类')
    second = models.CharField(max_length=60, blank=True, null=True, verbose_name='二类')
    third = models.CharField(max_length=60, blank=True, null=True, verbose_name='三类')
    department = models.ForeignKey('Basic_info.Department', on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='code_dep', verbose_name='所属部门')
    area = models.ForeignKey('Basic_info.Area', on_delete=models.CASCADE, blank=True, null=True,
                             related_name='code_area', verbose_name='所属地区')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.category_code

    class Meta:
        ordering = ['category_code']
        db_table = "code"
        verbose_name = '编码设置'
        verbose_name_plural = verbose_name


class Status(models.Model):
    """产品状态设置"""
    name = models.CharField(max_length=60, verbose_name='产品所属状态描述')
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
        db_table = "status"
        verbose_name = '产品状态设置'
        verbose_name_plural = verbose_name


class Matrial_process(models.Model):
    """材质生产进度"""
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='进度名称')
    p_code = models.CharField(max_length=200, blank=True, null=True, verbose_name='进度编码')
    m_code = models.ForeignKey('Basic_info.Texture', on_delete=models.CASCADE, blank=True, null=True,
                               related_name='mat_process_code', verbose_name='材料编码')
    next_process = models.CharField(max_length=200, blank=True, null=True, verbose_name='下一进度名称')
    produce_days = models.CharField(max_length=30, blank=True, null=True, verbose_name='正常生产天数')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.m_code)

    class Meta:
        ordering = ['m_code']
        db_table = "matrial_process"
        verbose_name = '材质生产进度'
        verbose_name_plural = verbose_name
