from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'Order'
    verbose_name = '订单信息  '

    def ready(self):
        """
        在子类中重写此方法，以便在Django启动时运行代码。
        :return:
        """
        from .signals import po_update, po_detail_update, contract_update, product_send_update, omr_update, omr_po_detail_update
