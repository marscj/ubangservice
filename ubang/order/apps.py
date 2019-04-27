from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'ubang.order'

    def ready(self):
        import ubang.order.handler
