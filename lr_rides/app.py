from django.apps import AppConfig


class LrRidesAppConfig(AppConfig):
    name = "lr_rides"

    def ready(self):
        from lr_rides import signals # pylint: disable=unused-variable
