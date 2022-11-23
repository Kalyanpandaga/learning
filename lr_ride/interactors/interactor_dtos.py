from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict

from lr_ride.adapters.dtos import UserDetailsDTO
from lr_ride.constants.enum import AssetTypeEnum, AssetSensitivityEnum, \
    OrderEnum, AppliedStatusEnum


@dataclass
class AssetTransportationRequestDetailsDTO:
    user_id: str
    from_location: str
    to_location: str
    start_datetime: datetime
    end_datetime: Optional[datetime]
    assets_quantity: int
    asset_type: AssetTypeEnum
    asset_sensitivity: AssetSensitivityEnum
    whom_to_deliver: str


@dataclass
class FilterByDTO:
    applied_status: AppliedStatusEnum


@dataclass
class MatchedRequestsBodyDetailsDTO:
    user_id: str
    sort_by: OrderEnum
    filter: Optional[FilterByDTO]
    from_location: str
    to_location: str
    datetime: datetime


@dataclass
class MatchedAssetTransportationRequestsWithUserDetailsDTO:
    requester_details: UserDetailsDTO
    from_location: str
    to_location: str
    start_datetime: datetime
    end_datetime: Optional[datetime]
    assets_quantity: int
    asset_type: AssetTypeEnum
    asset_sensitivity: AssetSensitivityEnum
    whom_to_deliver: str
    applied_status: AppliedStatusEnum


