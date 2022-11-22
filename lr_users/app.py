from django.apps import AppConfig

class LrUsersAppConfig(AppConfig):
    name = "lr_users"

    def ready(self):
        from lr_users import signals # pylint: disable=unused-variable
