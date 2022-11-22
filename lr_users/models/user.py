from django.db import models
from ib_common.models import AbstractDateTimeModel


class UserProfile(models.Model, AbstractDateTimeModel):
    user_id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=100)
