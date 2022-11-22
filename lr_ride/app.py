from django.apps import AppConfig


class LrRideAppConfig(AppConfig):
    name = "lr_ride"

    def ready(self):
        from lr_ride import signals # pylint: disable=unused-variable
