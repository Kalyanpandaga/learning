from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from lr_ride.constants.enum import AssetTypeEnum, AssetSensitivityEnum, \
    AppliedStatusEnum


@dataclass
class MatchedAssetTransportationRequestsDetailsDTO:
    user_id: str
    from_location: str
    to_location: str
    start_datetime: datetime
    end_datetime: Optional[datetime]
    assets_quantity: int
    asset_type: AssetTypeEnum
    asset_sensitivity: AssetSensitivityEnum
    whom_to_deliver: str
    applied_status: AppliedStatusEnum
