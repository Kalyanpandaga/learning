from enum import Enum

from ib_common.constants import BaseEnumClass


class AssetTypeEnum(BaseEnumClass, Enum):
    laptop = 'LAPTOP'
    travel_bag = 'TRAVEL_BAG'
    package = 'PACKAGE'


class AssetSensitivityEnum(BaseEnumClass, Enum):
    highly_sensitive = 'HIGHLY_SENSITIVE'
    sensitive = 'SENSITIVE'
    normal = 'NORMAL'


class AppliedStatusEnum(BaseEnumClass, Enum):
    applied = 'APPLIED',
    not_applied = 'NOT_APPLIED'


class TravelMediumEnum(BaseEnumClass, Enum):
    bus = 'BUS',
    car = 'CAR',
    train = 'TRAIN'


class OrderEnum(BaseEnumClass, Enum):
    asc = 'ASC',
    desc = 'DESC'
