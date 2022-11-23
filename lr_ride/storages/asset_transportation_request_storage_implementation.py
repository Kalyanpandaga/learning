from typing import List

from lr_ride.interactors.interactor_dtos import \
    AssetTransportationRequestDetailsDTO, MatchedRequestsBodyDetailsDTO
from lr_ride.interactors.storage_interfaces. \
    asset_transportation_request_storage_interface import \
    AssetTransportationRequestStorageInterface
from lr_ride.interactors.storage_interfaces.dtos import \
    MatchedAssetTransportationRequestsDetailsDTO
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

    def get_matched_asset_transportation_requests(
            self, matched_requests_body_details: MatchedRequestsBodyDetailsDTO)\
            -> List[MatchedAssetTransportationRequestsDetailsDTO]:

        request_user_id = matched_requests_body_details.user_id
        sort_by = matched_requests_body_details.sort_by
        filter_by_dto = matched_requests_body_details.filter
        from_location = matched_requests_body_details.from_location
        to_location = matched_requests_body_details.to_location
        datetime = matched_requests_body_details.datetime

        user_asset_transportation_requests = \
            AssetTransportationRequest.objects.filter(
                user_id=request_user_id,
                from_location=from_location,
                to_location=to_location
            )

        if filter_by_dto is not None:
            applied_status = filter_by_dto.applied_status
            user_asset_transportation_requests.filter(
                applied_status=applied_status)

        user_asset_transportation_requests.filter()
