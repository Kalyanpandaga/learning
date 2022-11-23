from lr_ride.interactors.interactor_dtos import \
    AssetTransportationRequestDetailsDTO
from lr_ride.interactors.storage_interfaces. \
    asset_transportation_request_storage_interface import \
    AssetTransportationRequestStorageInterface
from lr_ride.models.asset_transportation_request import \
    AssetTransportationRequest


class AssetTransportationRequestStorageImplementation(
    AssetTransportationRequestStorageInterface):
    def create_asset_transportation_request(
            self,
            asset_transportation_request_details: AssetTransportationRequestDetailsDTO):
        AssetTransportationRequest.objects.create(
            user_id=asset_transportation_request_details.user_id,
            from_location=asset_transportation_request_details.from_location,
            to_location=asset_transportation_request_details.to_location,
            start_datetime=asset_transportation_request_details.start_datetime,
            end_datetime=asset_transportation_request_details.end_datetime,
            assets_quantity=asset_transportation_request_details.assets_quantity,
            asset_type=asset_transportation_request_details.asset_type,
            asset_sensitivity=asset_transportation_request_details.asset_sensitivity,
            whom_to_deliver=asset_transportation_request_details.whom_to_deliver,
        )

