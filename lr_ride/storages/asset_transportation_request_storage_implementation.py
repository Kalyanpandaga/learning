from lr_ride.interactors.interactor_dtos import AssetTransferRequestDetailsDTO
from lr_ride.interactors.storage_interfaces.\
    asset_transportation_request_storage_interface import \
    AssetTransportationRequestStorageInterface


class AssetTransportationRequestStorageImplementation(
        AssetTransportationRequestStorageInterface):
    def create_asset_transportation_request(
            self,
            asset_transfer_request_details: AssetTransferRequestDetailsDTO):
        pass
