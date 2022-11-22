from lr_ride.interactors.storage_interfaces.asset_transportation_request_storage_interface import \
    AssetTransportationRequestStorageInterface


class CreateAssetTransferInteractor:
    def __init__(self,
                 asset_transportation_request_storage:
                 AssetTransportationRequestStorageInterface):
        self.asset_transportation_request_storage = \
            asset_transportation_request_storage

    def create_asset_transfer_interactor(self):
        pass
