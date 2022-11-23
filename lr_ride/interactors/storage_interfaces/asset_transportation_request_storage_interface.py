from abc import ABC, abstractmethod

from lr_ride.interactors.interactor_dtos import AssetTransportationRequestDetailsDTO


class AssetTransportationRequestStorageInterface(ABC):
    @abstractmethod
    def create_asset_transportation_request(
            self,
            asset_transfer_request_details: AssetTransportationRequestDetailsDTO):
        pass
