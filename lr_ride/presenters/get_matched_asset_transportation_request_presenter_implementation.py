from typing import Dict, List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from lr_ride.interactors.interactor_dtos import \
    MatchedAssetTransportationRequestsWithUserDetailsDTO
from lr_ride.interactors.presenter_interfaces.\
    get_matched_asset_transportation_request_presenter_interface import \
    GetMatchedAssetTransportationRequestPresenterInterface


class GetMatchedAssetTransportationRequestPresenterImplementation(
        HTTPResponseMixin,
        GetMatchedAssetTransportationRequestPresenterInterface):
    def get_matched_asset_transportation_request_response(
            self,
            matched_asset_transportation_requests_with_user_details:
            List[MatchedAssetTransportationRequestsWithUserDetailsDTO]):
        matched_asset_transportation_requests_details = []

        for matched_request in \
                matched_asset_transportation_requests_with_user_details:
            requested_user_details = self._get_requester_details(
                matched_request.requester_details)

            matched_request_details = {
                "Requester_details": requested_user_details,
                "from_location": matched_request.from_location,
                "to_location": matched_request.to_location,
                "start_date": matched_request.start_datetime,
                "end_date": matched_request.end_datetime,
                "assets_quantity": matched_request.assets_quantity,
                "asset_type": matched_request.asset_type,
                "asset_sensitivity": matched_request.asset_sensitivity,
                "whom_to_deliver": matched_request.whom_to_deliver,
                "applied_status": matched_request.applied_status
            }
            matched_asset_transportation_requests_details.append(
                matched_request_details
            )

        return self.prepare_200_success_response(
            matched_asset_transportation_requests_details)

    @staticmethod
    def _get_requester_details(requester_details_dto) -> Dict[str, str]:
        requester_details = {
            "user_id": requester_details_dto.user_id,
            "user_name": requester_details_dto.name
        }

        return requester_details

