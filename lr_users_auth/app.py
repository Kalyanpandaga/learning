from django.apps import AppConfig


class LrUsersAuthAppConfig(AppConfig):
    name = "lr_users_auth"

    def ready(self):
        from lr_users_auth import signals # pylint: disable=unused-variable
