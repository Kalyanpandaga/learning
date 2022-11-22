from enum import Enum

from ib_common.constants import BaseEnumClass


class AssetTypeEnum(Enum, BaseEnumClass):
    laptop = 'LAPTOP'
    travel_bag = 'TRAVEL_BAG'
    package = 'PACKAGE'


class AssetSensitivityEnum(Enum, BaseEnumClass):
    highly_sensitive = 'HIGHLY_SENSITIVE'
    sensitive = 'SENSITIVE'
    normal = 'NORMAL'


class AppliedStatusEnum(Enum, BaseEnumClass):
    applied = 'APPLIED',
    not_applied = 'NOT_APPLIED'


class TravelMediumEnum(Enum, BaseEnumClass):
    bus = 'BUS',
    car = 'CAR',
    train = 'TRAIN'
