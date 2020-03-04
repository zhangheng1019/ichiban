from django.db import models

# Create your models here.
# ------------------内部推送POM---------------------------
class Point(models.Model):
    """触发点类型，用于触发事件"""
    point_form = (
        ('nothing', '无'),
        ('order', '订单'),
        ('POM', 'POM'),
        ('POMM', 'POMM'),
        ('POMC', 'POMC'),
    )

    source = models.CharField(max_length=255, blank=True, null=True, choices=point_form, verbose_name='触发点来源')
    name = models.TextField(blank=True, null=True, verbose_name='触发点名称')  # 工厂、材质、客户、接单日期、交货日期、其他...
    edesc = models.CharField(max_length=255, blank=True, null=True, verbose_name='触发点英文描述')
    code = models.TextField(blank=True, null=True, verbose_name='触发点编码')  # fac01
    date_info = models.TextField(blank=True, null=True, verbose_name='触发点日期条件')
    is_file = models.CharField(max_length=255, blank=True, null=True, choices=(('True', '是'), ('False', '否')),
                               default='False', verbose_name='是否需要上传附件')
    last_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='最后操作时间')
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
        db_table = "point"
        verbose_name = '触发点'
        verbose_name_plural = verbose_name


class PoPoint(models.Model):
    """
    订单相关因素--订单所有相关字段
    （po, po_detail, contract, product_send, omr, omr_po_detail）
    涵盖订单表、订单详情表、合同表、消出货表、omr表、omr详情表
    """
    # po
    customer = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户')
    customer_pono = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人po')
    cus_receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人收货日期')
    fina_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='最终交货日期')
    receive_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='接单日期')
    order_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='我司订单编号')
    fac_send_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂交货日期')
    produce_native_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='生产通知单日')
    delivery_condition = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人交货条件')
    port = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人出货港口')
    omr = models.CharField(max_length=255, blank=True, null=True, verbose_name='承办员')
    pay_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='财务付款方式')
    # po_detail
    item_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='我司Item No')
    customer_item = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人Item_no')
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='中文描述')
    edesc = models.CharField(max_length=255, blank=True, null=True, verbose_name='英文描述')
    fac_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂货号')
    texture = models.CharField(max_length=255, blank=True, null=True, verbose_name='材质')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量单位')
    costrate = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人要价')
    currency = models.CharField(max_length=255, blank=True, null=True, verbose_name='客人货币类型')
    each_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='单一包装材质')
    outside_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='外盒数量')
    middle_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='中盒数量')
    inner_box = models.CharField(max_length=255, blank=True, null=True, verbose_name='内盒数量')
    box_unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='包装数量单位')
    for_profit_report = models.CharField(max_length=255, blank=True, null=True, verbose_name='利润标说明')
    fac_delivery = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂交货条件')
    fac_delivery_port = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂出货港口')
    fmr = models.CharField(max_length=255, blank=True, null=True, verbose_name='FMR人员')
    fqc = models.CharField(max_length=255, blank=True, null=True, verbose_name='FQC人员')
    sale_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='消出货日期')
    # contract
    factory = models.CharField(max_length=255, blank=True, null=True, verbose_name='生产工厂')
    fac_currency = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂货币类型')
    fac_cost = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂价格')
    fac_total = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂合计金额')
    cancle_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='订单取消日期')
    # product_send
    qc1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='第一次检验人员')
    qc2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='第二次检验人员')
    qc3 = models.CharField(max_length=255, blank=True, null=True, verbose_name='第三次检验人员')
    rqc1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='第一次复检人员')
    rqc2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='第二次复检人员')
    no_pass = models.CharField(max_length=255, blank=True, null=True, verbose_name='验货不通过放货')
    send_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='放货人')
    # omr
    special_remark = models.TextField(blank=True, null=True, verbose_name='注意事项')
    # omr_po_detail
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
        db_table = "po_point"
        verbose_name = '订单相关因素'
        verbose_name_plural = verbose_name


class OtherPoint(models.Model):
    """其他因素筛选，用于筛选订单事件以外的条件"""
    point = models.TextField(blank=True, null=True, verbose_name='自定义触发点')
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='触发点中文描述')
    edesc = models.CharField(max_length=255, blank=True, null=True, verbose_name='触发点英文描述')
    code = models.TextField(blank=True, null=True, verbose_name='触发点编码')  # fac01
    last_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='最后操作时间')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.point

    class Meta:
        ordering = ['point']
        db_table = "other_point"
        verbose_name = '订单以外触发点'
        verbose_name_plural = verbose_name


class Event(models.Model):
    """事件，用于触发提醒"""
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='事件名称')
    edesc = models.CharField(max_length=255, blank=True, null=True, verbose_name='事件英文描述')
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='事件编码')
    last_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='最后操作时间')
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
        db_table = "event"
        verbose_name = '事件'
        verbose_name_plural = verbose_name


class PointEvent(models.Model):
    """触发点对应的事件，触发因素和时间是多对多关系"""
    point_category = models.CharField(max_length=255, blank=True, null=True, verbose_name='触发点类别')  # 客户、工厂、材质、时间
    other_point = models.ForeignKey('POM.OtherPoint', related_name='other_point', on_delete=models.CASCADE,
                                    blank=True, null=True, verbose_name='其他触发点')
    order_point = models.ForeignKey('POM.Point', related_name='point', on_delete=models.CASCADE,
                                    blank=True, null=True, verbose_name='订单触发点')  # A工厂
    event = models.ForeignKey('POM.Event', related_name='point_event', on_delete=models.CASCADE,
                              blank=True, null=True, verbose_name='事件')  # 防潮防火
    last_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='最后操作时间')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.order_point)

    class Meta:
        ordering = ['order_point']
        db_table = "point_event"
        verbose_name = '触发点对应事件'
        verbose_name_plural = verbose_name


class Remind(models.Model):
    """
    提醒事项，用于生成对用户的提醒，作为业务总表
    只有在订单创建、更改或者主管分配订单事项的时候，会自动匹配更改一次事项 -- 根据触发点匹配
    """
    is_or_not = (
        ('True', '是'),
        ('False', '否')
    )
    is_order = models.CharField(max_length=255, blank=True, null=True, choices=is_or_not,
                                default='True', verbose_name='是否订单相关')
    po = models.CharField(max_length=255, blank=True, null=True, verbose_name='我司po')
    item_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='Item No')
    event = models.ForeignKey('POM.Event', blank=True, null=True, related_name='remind_event',
                              on_delete=models.CASCADE, verbose_name='提醒事件')
    person = models.CharField(max_length=255, blank=True, null=True, verbose_name='被提醒人')  # 张三
    begin_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='开始提醒时间')  # 2020年1月12日
    end_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='结束提醒时间')  # 2020年1月22日
    rate = models.CharField(max_length=255, blank=True, null=True, verbose_name='提醒频次（天/次）')  # 5（相当于一共提醒两次）
    plan_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='应完成时间')  # 2020年1月22日
    actual_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='实际完成时间')  # 2020年1月23日
    status = models.CharField(max_length=255, blank=True, null=True, choices=(('True', '完成'), ('False', '未完成')),
                              default='False', verbose_name='事件状态')  # 未完成
    pomm = models.CharField(max_length=255, blank=True, null=True, verbose_name='一级监督者')  # 李四
    pomc = models.CharField(max_length=255, blank=True, null=True, verbose_name='二级监督者')  # 王五
    is_upload_file = models.CharField(max_length=255, blank=True, null=True, choices=is_or_not,
                                      default='False', verbose_name='是否需要上传附件')  # 否
    file_path = models.CharField(max_length=255, blank=True, null=True, verbose_name='附件路径')  # 如果上传附件勾选，则必须上传附件后才能提交
    last_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='最后操作时间')  # 2020-01-03 17:04
    manage_id = models.IntegerField(blank=True, null=True, verbose_name='延期事件的id')  # 用于员工对事件延期的时候记录被延期事件的id
    delay_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='延期日期')  # 用于员工对事件延期的时候记录延期日期
    # 不确定字段：是否罚款、罚款原因、罚款金额、罚款最后缴纳时间、罚款是否结清
    # is_punish = models.CharField(max_length=255, blank=True, null=True, choices=is_or_not,
    #                              default='False', verbose_name='是否罚款')
    # punish_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name='罚款原因')
    # punish_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='罚款金额')
    # punish_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='罚款最后缴纳时间')
    # is_punish_finish = models.CharField(max_length=255, blank=True, null=True, choices=is_or_not,
    #                                     default='False', verbose_name='罚款是否结清')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.person

    class Meta:
        ordering = ['person']
        db_table = "remind"
        verbose_name = '提醒事项'
        verbose_name_plural = verbose_name


# ---------------------工厂推送POM-------------------------
class FactoryAbility(models.Model):
    """工厂产能预测信息推送，用于记录工厂产能的基础信息"""
    item = models.ForeignKey('Order.Po_detail', blank=True, null=True, on_delete=models.CASCADE,
                             related_name='ability_item', verbose_name='工厂产能对应的item')
    factory = models.ForeignKey('Basic_info.Factory', related_name='ability_factory',
                                blank=True, null=True, on_delete=models.CASCADE, verbose_name='工厂')
    yields = models.CharField(max_length=255, blank=True, null=True, verbose_name='工厂日产量')
    per_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='人均产量')
    person = models.CharField(max_length=255, blank=True, null=True, verbose_name='人数')
    pass_rate = models.CharField(max_length=255, blank=True, null=True, verbose_name='合格率')
    formula = models.TextField(blank=True, null=True, verbose_name='产能计算公式')
    formula_expire_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='公式失效日期')
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return str(self.factory)

    class Meta:
        ordering = ['factory']
        db_table = "factory_ability"
        verbose_name = '工厂产能信息'
        verbose_name_plural = verbose_name


class FactoryProcess(models.Model):
    """工厂生产进度信息推送，用于记录工厂生产基础信息"""
    things = models.TextField(blank=True, null=True, verbose_name='事项')
    types = models.CharField(max_length=255, blank=True, null=True, default='按工厂', verbose_name='关联类型')
    remind_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='提醒日期')  # 10、15、20......
    date_by = models.CharField(max_length=255, blank=True, null=True, verbose_name='时间类型')  # 下单后、出货前.....
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.things

    class Meta:
        ordering = ['things']
        db_table = "factory_process"
        verbose_name = '工厂进度信息'
        verbose_name_plural = verbose_name


class TextureReminds(models.Model):
    """材质进度信息推送，用于记录材质进度基础信息"""
    texture_cate = models.CharField(max_length=255, blank=True, null=True, verbose_name='材质分类')
    things = models.TextField(blank=True, null=True, verbose_name='事项')
    remind_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='提醒日期')  # 10、15、20......
    date_by = models.CharField(max_length=255, blank=True, null=True, verbose_name='时间类型')  # 下单后、出货前.....
    # ------------以下为预留字段-------------
    preset1 = models.TextField(blank=True, null=True, verbose_name='预留字段1')
    preset2 = models.TextField(blank=True, null=True, verbose_name='预留字段2')
    preset3 = models.TextField(blank=True, null=True, verbose_name='预留字段3')
    preset4 = models.TextField(blank=True, null=True, verbose_name='预留字段4')
    preset5 = models.TextField(blank=True, null=True, verbose_name='预留字段5')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.things

    class Meta:
        ordering = ['remind_date']
        db_table = "texture_reminds"
        verbose_name = '材质进度信息'
        verbose_name_plural = verbose_name
