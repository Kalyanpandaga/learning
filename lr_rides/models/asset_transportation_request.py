import uuid

from django.core.exceptions import ValidationError
from django.db import models
from ib_common.models import AbstractDateTimeModel

from lr_rides.constants.enums import AssetTypeEnum, AssetSensitivityEnum, \
    AppliedStatusEnum
from lr_rides.constants.exception_messages import INVALID_ASSET_TYPE, \
    INVALID_ASSET_SENSITIVITY, INVALID_APPLIED_STATUS


def validate_asset_type(value):
    if value not in AssetTypeEnum.get_list_of_values():
        raise ValidationError(INVALID_ASSET_TYPE.format(value))


def validate_asset_sensitivity(value):
    if value not in AssetSensitivityEnum.get_list_of_values():
        raise ValidationError(INVALID_ASSET_SENSITIVITY.format(value))


def validate_applied_status(value):
    if value not in AppliedStatusEnum.get_list_of_values():
        raise ValidationError(INVALID_APPLIED_STATUS.format(value))


class AssetTransportationRequest(models.Model, AbstractDateTimeModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.CharField(max_length=36)
    from_location = models.CharField(max_length=250)
    to_location = models.CharField(max_length=250)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True)
    assets_quantity = models.IntegerField()
    asset_type = models.CharField(max_length=25,
                                  validators=[validate_asset_type])
    asset_sensitivity = models.CharField(max_length=20,
                                         validators=[validate_asset_sensitivity])
    whom_to_deliver = models.TextField()
    applied_status = models.CharField(
        max_length=25, default=AppliedStatusEnum.not_applied.value,
        validators=[validate_applied_status])

