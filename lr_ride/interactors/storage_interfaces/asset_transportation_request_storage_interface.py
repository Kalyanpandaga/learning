from abc import ABC, abstractmethod
from typing import List

from lr_ride.interactors.interactor_dtos import \
    AssetTransportationRequestDetailsDTO, MatchedRequestsBodyDetailsDTO
from lr_ride.interactors.storage_interfaces.dtos import \
    MatchedAssetTransportationRequestsDetailsDTO


class AssetTransportationRequestStorageInterface(ABC):
    @abstractmethod
    def create_asset_transportation_request(
            self,
            asset_transfer_request_details: AssetTransportationRequestDetailsDTO):
        pass

    def get_matched_asset_transportation_requests(
            self, matched_requests_body_details: MatchedRequestsBodyDetailsDTO) \
            -> List[MatchedAssetTransportationRequestsDetailsDTO]:
        pass

