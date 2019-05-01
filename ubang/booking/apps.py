from django.apps import AppConfig


class BookingConfig(AppConfig):
    name = 'ubang.booking'

    def ready(self):
        from .import handler