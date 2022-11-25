from lr_ride.interactors.interactor_dtos import AssetTransportationRequestDetailsDTO
from lr_ride.interactors.storage_interfaces.\
    asset_transportation_request_storage_interface import \
    AssetTransportationRequestStorageInterface


class CreateAssetTransportationInteractor:
    def __init__(self,
                 asset_transportation_request_storage:
                 AssetTransportationRequestStorageInterface):
        self.asset_transportation_request_storage = \
            asset_transportation_request_storage

    def create_asset_transportation_request_wrapper(
            self, asset_transfer_request_details):
        """
        remove
        """

        self.create_asset_transportation_request(asset_transfer_request_details)

    def create_asset_transportation_request(
            self,
            asset_transfer_request_details:
            AssetTransportationRequestDetailsDTO):

        self.asset_transportation_request_storage.\
            create_asset_transportation_request(asset_transfer_request_details)
