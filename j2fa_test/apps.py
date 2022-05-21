from django.apps import AppConfig


class J2FaTestConfig(AppConfig):
    name = 'j2fa_test'

    def ready(self):
        from . import signals

