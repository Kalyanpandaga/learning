from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class AssetTransferRequestDetailsDTO:
    user_id: str
    from_location: str
    to_location: str
    start_datetime: datetime
    end_datetime: Optional[datetime]
    assets_quantity: int
    asset_type: str
    asset_sensitivity: str
    whom_to_deliver: str

