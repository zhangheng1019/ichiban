from django.db import models

# Create your models here.


class Claim_category(models.Model):
    """索赔类型"""
    name = models.CharField(max_length=255, verbose_name='索赔类型名称')
    code = models.CharField(max_length=255, unique=True, verbose_name='索赔类型编码')
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
        ordering = ['code']
        db_table = "claim_category"
        verbose_name = '索赔类型'
        verbose_name_plural = verbose_name


class Type(models.Model):
    """索赔费用分类"""
    desc = models.CharField(max_length=200, verbose_name='类别描述')
    edesc = models.CharField(max_length=200, blank=True, null=True, verbose_name='英文描述')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.desc

    class Meta:
        ordering = ['desc']
        db_table = "type"
        verbose_name = '索赔费用分类'
        verbose_name_plural = verbose_name


class Finance_bill(models.Model):
    """财务传票"""
    option = (
        ('True', '是'),
        ('False', '否'),
    )
    # 古代公司传票
    bill_number = models.CharField(max_length=255, unique=True, verbose_name='传票编号')
    out_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='外编号')
    place = models.ForeignKey('Basic_info.Area', on_delete=models.CASCADE, related_name='finance_bill_place',
                              blank=True, null=True, verbose_name='地点')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='日期')
    extra_bill = models.CharField(max_length=255, blank=True, null=True, verbose_name='附单据')
    is_check = models.CharField(max_length=40, blank=True, null=True, choices=option, default='False', verbose_name='核对')
    is_pay = models.CharField(max_length=40, blank=True, null=True, choices=option, default='False', verbose_name='结算')
    # 传票细节
    detail_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='细节id')  # 应该就是一个自增长的ID值
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name='摘要')
    code = models.ForeignKey('Basic_info.Code', on_delete=models.CASCADE, blank=True, null=True, 
                             related_name='finance_bill_code', verbose_name='编码')
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name='科目')
    child_subject = models.CharField(max_length=255, blank=True, null=True, verbose_name='子科目')
    inner_subject = models.CharField(max_length=255, blank=True, null=True, verbose_name='内细目')
    currency = models.ForeignKey('Basic_info.Currency', on_delete=models.CASCADE, blank=True, null=True, 
                                 related_name='finance_bill_currency', verbose_name='币种')
    borrow = models.CharField(max_length=255, blank=True, null=True, verbose_name='借方')
    lend = models.CharField(max_length=255, blank=True, null=True, verbose_name='贷方')
    rate_of_exchange = models.CharField(max_length=255, blank=True, null=True, verbose_name='兑换比率')
    is_receipt = models.CharField(max_length=40, blank=True, null=True, choices=option, default='False', verbose_name='结算')
    head_quarter = models.ForeignKey('Basic_info.Head_quarter', on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='finance_bill_head', verbose_name='总部')
    area = models.ForeignKey('Basic_info.Area', on_delete=models.CASCADE, blank=True, null=True,
                             related_name='finance_bill_area', verbose_name='地区')
    department = models.ForeignKey('Basic_info.Department', on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='finance_bill_department', verbose_name='部门')
    handle = models.ForeignKey('Basic_info.Staff', on_delete=models.CASCADE, blank=True, null=True,
                               related_name='finance_bill_handle', verbose_name='经手人')
    explain = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注说明')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.bill_number

    class Meta:
        ordering = ['bill_number']
        db_table = "finance_bill"
        verbose_name = '财务传票'
        verbose_name_plural = verbose_name


class Ship_payment(models.Model):
    """大货付款"""
    # 客户和工厂资料
    customer = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户编码')  # 取自Po表
    factory = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂全称')  # 取自Contract表
    # 订单信息
    po = models.CharField(max_length=255, verbose_name='我司po')  # 关联Po表
    po_detail = models.CharField(max_length=255, verbose_name='我司item no')  # 关联po_detail表
    customer_po = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户po')  # 取自Po表
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户货号')  # 取自Po_detail表
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='品名与规格')  # 取自Po_detail表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')  # 取自Po_detail表
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='单位')  # 取自Po_detail表
    final_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='实际交货期')  # 取自Po表
    qc1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='QC')  # 取自Product_send表的qc1
    omr = models.CharField(max_length=255, blank=True, null=True, verbose_name='承办员')  # 取自Po表
    cus_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人单价')  # 取自Po_detail表
    cus_currency = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人单价货币单位')  # 取自Po_detail表
    cus_total = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人总价')  # 单价 * 数量
    cus_total_currency = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人总价货币单位')  # 取自Po_detail表，和currency一致
    fac_cost = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂单价')  # 取自Contract表
    fac_cost_currency = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂单价货币单位')  # 取自Contract表
    fac_total = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂总价')  # 取自Contract表
    fac_total_currency = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂总价货币单位')  # 取自Contract表
    # 进出口公司信息
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司代码')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='进出口公司')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='户口抬头')
    account_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='户口账号')
    bank = models.CharField(max_length=255, blank=True, null=True, verbose_name='开户银行')
    # 添加付款明细（添加按钮）
    invoice_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='发票号码')
    currency = models.ForeignKey('Basic_info.Currency', related_name='ship_payment_currency',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='付款货币')
    explain = models.CharField(max_length=255, blank=True, null=True, verbose_name='附加说明')
    pay_amount = models.FloatField(blank=True, null=True, verbose_name='付款金额')
    remit_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='汇款单号码')
    pay_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='付款日期')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.po_detail)

    class Meta:
        ordering = ['po_detail']
        db_table = "ship_payment"
        verbose_name = '大货付款'
        verbose_name_plural = verbose_name


class Accessory_pay(models.Model):
    """材料配件付款"""
    # 客户和工厂资料
    customer = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户编码')  # 取自Po表
    factory = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂全称')  # 取自Contract表
    # 订单信息（po_detail + 材料签收表--po_detail被材料签收关联着）
    po = models.CharField(max_length=255, verbose_name='我司po')  # 关联Po表
    po_detail = models.CharField(max_length=255, verbose_name='我司item no')  # 关联po_detail表
    customer_po = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户po')  # 取自Po表
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户货号')  # 取自Po_detail表
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='品名与规格')  # 取自Po_detail表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='订购数量')  # 取自Po_detail表
    unit = models.CharField(max_length=200, blank=True, null=True, verbose_name='计量单位')  # 取自Material_sign表
    send_material_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='实际送料日期')  # 取自Material_sign_detail表
    provide_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='材料提供方式')  # 取自Material_sign_detail表
    omr = models.CharField(max_length=200, blank=True, null=True, verbose_name='MR')  # 取自Material_sign表
    accessory_cost = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价')  # 取自Material_sign_detail表
    accessory_cost_total = models.CharField(max_length=255, blank=True, null=True, verbose_name='总价')  # 取自Material_sign_detail表
    currency = models.CharField(max_length=255, blank=True, null=True, verbose_name='货币')  # 取自Material_sign_detail表
    sale_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='消出货日期')  # 取自Product_send表
    # 进出口公司信息
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司代码')  # 取自Export_company表
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='进出口公司')  # 取自Export_company表
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='户口抬头')  # 取自Export_company表
    account_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='户口账号')  # 取自Export_company表
    bank = models.CharField(max_length=255, blank=True, null=True, verbose_name='开户银行')  # 取自Export_company表
    # 付款信息
    invoice_no = models.CharField(max_length=255, verbose_name='付款发票号码')
    explain = models.CharField(max_length=255, blank=True, null=True, verbose_name='附加说明')
    pay_currency = models.ForeignKey('Basic_info.Currency', related_name='accessory_pay_currency',
                                     blank=True, null=True, on_delete=models.CASCADE, verbose_name='付款货币')
    pay_remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    pay_amount = models.FloatField(blank=True, null=True, verbose_name='付款金额')  # 单价 * 数量
    remit_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='汇款单号码')
    pay_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='付款日期')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.po_detail)

    class Meta:
        unique_together = (('po', 'po_detail'),)
        ordering = ['po_detail']
        db_table = "accessory_pay"
        verbose_name = '材料配件付款'
        verbose_name_plural = verbose_name


class Claim_payment(models.Model):
    """索赔扣款"""
    # 客户和工厂资料
    customer = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户编码')  # 取自Po表
    factory = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂全称')  # 取自Contract表
    mr = models.CharField(max_length=255, blank=True, null=True, verbose_name='MR')  # 取自Po表
    explain = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注说明')
    # 订单信息
    po = models.CharField(max_length=255, verbose_name='我司po')  # 关联Po表
    po_detail = models.CharField(max_length=255, verbose_name='我司item no')  # 关联po_detail表
    customer_po = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户po')  # 取自Po表
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人货号')  # 取自Po表
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='品名与规格')  # 取自Po_detail表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')  # 取自Po_detail表
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='单位')  # 取自Po_detail表
    final_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='实际交货期')  # 取自Po表
    qc1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='QC')  # 取自Product_send表的qc1
    # 索赔摘要（无需存储在当前模型）
    pay_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='付清日期')  # 取自Claim_detail表
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔日期')  # 取自Claim_detail表
    claim_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔金额')  # 取自Claim_detail表
    fac_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔工厂金额')  # 取自Claim_detail表
    currency = models.ForeignKey('Basic_info.Currency', related_name='claim_payment_currency',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='货币币种')  # 取自Claim_detail表
    invoice_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='结算发票号码')  # 取自Claim_detail表
    claim_remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')  # 取自Claim_detail表
    # 扣款摘要（无需存储在当前模型）
    clear_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='付清日期')  # 取自Deduction_detail表
    deduction_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔日期')  # 取自Deduction_detail表
    deduction_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔金额')  # 取自Deduction_detail表
    deduction_fac_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔工厂金额')  # 取自Deduction_detail表
    deduction_currency = models.ForeignKey('Basic_info.Currency', related_name='claim_payment_deduction_currency',
                                           blank=True, null=True, on_delete=models.CASCADE, verbose_name='货币币种')  # 取自Deduction_detail表
    deduction_invoice_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='结算发票号码')  # 取自Deduction_detail表
    category_remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类备注')  # 取自Deduction_detail表
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.po_detail)

    class Meta:
        unique_together = (('po', 'po_detail'),)
        ordering = ['po_detail']
        db_table = "claim_payment"
        verbose_name = '索赔扣款'
        verbose_name_plural = verbose_name


class Claim_detail(models.Model):
    """索赔明细"""
    claim_payment = models.ForeignKey('Finance.Claim_payment', related_name='claim_detail_claim_payment',
                                      blank=True, null=True, on_delete=models.CASCADE, verbose_name='索赔扣款')
    claim_category = models.ForeignKey('Finance.Claim_category', related_name='claim_detail_category',
                                       blank=True, null=True, on_delete=models.CASCADE, verbose_name='赔款种类')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔日期')
    count = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔数量')
    currency = models.ForeignKey('Basic_info.Currency', related_name='claim_detail_currency',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='货币币种')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔金额')
    type = models.ForeignKey('Finance.Type', related_name='claim_detail_type', blank=True, null=True,
                             on_delete=models.CASCADE, verbose_name='分类')
    category_remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类备注')
    claim_detail_explain = models.TextField(blank=True, null=True, verbose_name='索赔明细说明')
    currency1 = models.ForeignKey('Basic_info.Currency', related_name='claim_detail_currency1', blank=True, null=True,
                                  on_delete=models.CASCADE, verbose_name='货币币种')
    fac_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='索赔工厂金额')
    to_rmb = models.CharField(max_length=255, blank=True, null=True, verbose_name='对人民币汇率')
    fac_claim_detail = models.TextField(blank=True, null=True, verbose_name='索赔工厂金额明细')
    invoice_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='结算发票号码')
    pay_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='付清日期')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.invoice_no

    class Meta:
        ordering = ['invoice_no']
        db_table = "claim_detail"
        verbose_name = '索赔明细'
        verbose_name_plural = verbose_name


class Deduction_detail(models.Model):
    """索赔扣款明细资料"""
    claim_payment = models.ForeignKey('Finance.Claim_payment', related_name='deduction_detail_claim_payment',
                                      blank=True, null=True, on_delete=models.CASCADE, verbose_name='索赔扣款')
    method = models.CharField(max_length=255, blank=True, null=True, verbose_name='材料提供方式')
    material_from = models.CharField(max_length=255, blank=True, null=True, verbose_name='材料来源地')
    is_order = models.CharField(max_length=255, blank=True, null=True, verbose_name='是否需要订购')
    factory = models.ForeignKey('Basic_info.Factory', related_name='deduction_detail_factory', blank=True, null=True,
                                on_delete=models.CASCADE, verbose_name='下单工厂')
    fac_order_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='订购数量')
    qty_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量单位')
    total = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣款总额')  # 订购数量 * 实送数量
    order_cost = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单单价')
    order_currency = models.ForeignKey('Basic_info.Currency', related_name='deduction_detail_order_currency',
                                       blank=True, null=True, on_delete=models.CASCADE, verbose_name='货币币种')
    deducted_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣款日期')
    fac_actual_qty = models.CharField(max_length=255, blank=True, null=True, verbose_name='实送数量')
    fac_actual_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量单位')
    invoice_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣款发票号')
    material = models.CharField(max_length=255, blank=True, null=True, verbose_name='材料')  # 取自Claim_payment表product字段
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.material)

    class Meta:
        ordering = ['material']
        db_table = "deduction_detail"
        verbose_name = '索赔扣款明细'
        verbose_name_plural = verbose_name


class Accessory_deduction(models.Model):
    """材料配件扣款"""
    # 客户和工厂资料
    customer = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户编码')  # 取自Po表
    factory = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂全称')  # 取自Contract表
    mr = models.CharField(max_length=255, blank=True, null=True, verbose_name='MR')  # 取自Po表
    explain = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注说明')
    # 订单信息（po_detail + 材料签收表--po_detail被材料签收关联着）
    po = models.CharField(max_length=255, verbose_name='我司po')  # 关联Po表
    po_detail = models.CharField(max_length=255, verbose_name='我司item no')  # 关联po_detail表
    customer_po = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户po')  # 取自Po表
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人货号')  # 取自Po表
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='品名')  # 取自Po_detail表
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')  # 取自Po_detail表
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='单位')  # 取自Po_detail表
    final_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='实际交货期')  # 取自Po表
    qc1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='QC')  # 取自Product_send表的qc1
    # 扣款摘要
    pay_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣款日期')
    deduction_clear_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='付清日期')
    type = models.ForeignKey('Finance.Type', related_name='accessory_deduction_type',
                             blank=True, null=True, on_delete=models.CASCADE, verbose_name='扣款类型')
    count = models.FloatField(blank=True, null=True, verbose_name='扣款数量')
    deduction_amount = models.FloatField(blank=True, null=True, verbose_name='扣款金额')
    fac_amount = models.FloatField(blank=True, null=True, verbose_name='扣款工厂金额')
    currency = models.ForeignKey('Basic_info.Currency', related_name='accessory_deduction_currency',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='货币币种')
    fac_total_amount = models.FloatField(blank=True, null=True, verbose_name='扣款工厂总金额')
    invoice_no = models.CharField(max_length=255, verbose_name='结算发票号码')
    category_remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类备注')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.po_detail

    class Meta:
        unique_together = (('po', 'po_detail'),)
        ordering = ['po_detail']
        db_table = "accessory_deduction"
        verbose_name = '财务配件扣款'
        verbose_name_plural = verbose_name


class Accessory_deduction_detail(models.Model):
    """添加扣配件款明细"""
    # 配件扣款主信息（po_detail + 材料签收表--po_detail被材料签收关联着）
    deduction_detail = models.ForeignKey('Finance.Accessory_deduction', related_name='Accessory_deduction_detail',
                                         on_delete=models.CASCADE, verbose_name='所属配件扣款单')
    # 扣款明细信息
    pay_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣款日期')
    reason = models.TextField(blank=True, null=True, verbose_name='扣款原因')
    count = models.FloatField(blank=True, null=True, verbose_name='扣款数量')
    price = models.FloatField(blank=True, null=True, verbose_name='扣款单价')
    currency = models.ForeignKey('Basic_info.Currency', related_name='accessory_deduction_detail_currency',
                                 blank=True, null=True, on_delete=models.CASCADE, verbose_name='货币币种')
    total_amount = models.FloatField(blank=True, null=True, verbose_name='扣款总金额')  # 数量 * 单价
    deduction_no = models.TextField(blank=True, null=True, verbose_name='扣款发票号码')
    deduction_clear_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣完日期')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.deduction_detail)

    class Meta:
        ordering = ['deduction_detail']
        db_table = "accessory_deduction_detail"
        verbose_name = '财务配件扣款明细'
        verbose_name_plural = verbose_name
