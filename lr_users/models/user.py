from django.db import models


class UserProfile(models.Model):
    user_id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=100)
