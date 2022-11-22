import uuid

from django.db import models
from django.core.exceptions import ValidationError

from lr_rides.constants.enums import TravelMediumEnum
from lr_rides.constants.exception_messages import INVALID_TRAVEL_MEDIUM


def validate_travel_medium(value):
    if value in TravelMediumEnum.get_list_of_values():
        raise ValidationError(INVALID_TRAVEL_MEDIUM.format(value))


class RideTravelInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.CharField(max_length=36)
    from_location = models.CharField(max_length=250)
    to_location = models.CharField(max_length=250)
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField()
    travel_medium = models.CharField(max_length=20,
                                     validators=[validate_travel_medium])
    assets_quantity = models.IntegerField()

