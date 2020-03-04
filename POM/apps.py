from django.apps import AppConfig


class PomConfig(AppConfig):
    name = 'POM'
    verbose_name = 'POM信息  '

    def ready(self):
        """
        在子类中重写此方法，以便在Django启动时运行代码。
        :return:
        """
        from .signals import point_update, point_update
