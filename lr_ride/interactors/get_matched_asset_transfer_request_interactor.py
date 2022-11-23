from typing import List, Dict

from lr_ride.adapters.dtos import UserDetailsDTO
from lr_ride.adapters.service_adapter import get_service_adapter
from lr_ride.interactors.interactor_dtos import MatchedRequestsBodyDetailsDTO, \
    MatchedAssetTransportationRequestsWithUserDetailsDTO
from lr_ride.interactors.presenter_interfaces.\
    get_matched_asset_transportation_request_presenter_interface import \
    GetMatchedAssetTransportationRequestPresenterInterface
from lr_ride.interactors.storage_interfaces.\
    asset_transportation_request_storage_interface import \
    AssetTransportationRequestStorageInterface
from lr_ride.interactors.storage_interfaces.dtos import \
    MatchedAssetTransportationRequestsDetailsDTO


class GetMatchedAssetTransportationInteractor:
    def __init__(self,
                 asset_transportation_request_storage:
                 AssetTransportationRequestStorageInterface):
        self.asset_transportation_request_storage = \
            asset_transportation_request_storage

    def get_matched_asset_transportation_request_wrapper(
            self, matched_requests_body_details: MatchedRequestsBodyDetailsDTO,
            presenter: GetMatchedAssetTransportationRequestPresenterInterface):

        matched_asset_transportation_requests_with_user_details = \
            self.get_matched_asset_transportation_requests(
                matched_requests_body_details)

        return presenter.get_matched_asset_transportation_request_response(
            matched_asset_transportation_requests_with_user_details)

    def get_matched_asset_transportation_requests(
            self, matched_requests_body_details: MatchedRequestsBodyDetailsDTO) \
            -> MatchedAssetTransportationRequestsWithUserDetailsDTO:

        matched_asset_transportation_requests_details = \
            self.asset_transportation_request_storage.\
            get_matched_asset_transportation_requests(
                matched_requests_body_details)

        matched_asset_transportation_requests_user_ids = \
            self._get_get_asset_transportation_requests_user_ids(
                matched_asset_transportation_requests_details)

        matched_asset_transportation_requests_user_details = \
            self._get_users_details_from_user_id(
                matched_asset_transportation_requests_user_ids)

        mapping_user_details_with_user_id = \
            self._get_mapping_user_details_with_user_id(
                matched_asset_transportation_requests_user_details)

        matched_asset_transportation_requests_with_user_details = []
        for matched_asset_transportation_request_dto in \
                matched_asset_transportation_requests_details:
            requester_details = mapping_user_details_with_user_id[
                matched_asset_transportation_request_dto.user_id]

            matched_asset_transportation_requests_with_user_details.append(
                MatchedAssetTransportationRequestsWithUserDetailsDTO(
                    requester_details=requester_details,
                    from_location=matched_asset_transportation_request_dto.from_location,
                    to_location=matched_asset_transportation_request_dto.to_location,
                    start_datetime=matched_asset_transportation_request_dto.start_datetime,
                    end_datetime=matched_asset_transportation_request_dto.end_datetime,
                    assets_quantity=matched_asset_transportation_request_dto.assets_quantity,
                    asset_type=matched_asset_transportation_request_dto.asset_type,
                    asset_sensitivity=matched_asset_transportation_request_dto.asset_sensitivity,
                    whom_to_deliver=matched_asset_transportation_request_dto.whom_to_deliver,
                    applied_status=matched_asset_transportation_request_dto.applied_status
                )
            )

        return matched_asset_transportation_requests_with_user_details

    @staticmethod
    def _get_get_asset_transportation_requests_user_ids(
            matched_asset_transportation_requests_details:
            List[MatchedAssetTransportationRequestsDetailsDTO]):
        lr_user_ids = set()

        for matched_asset_transportation_request_dto in \
                matched_asset_transportation_requests_details:
            lr_user_ids.add(matched_asset_transportation_request_dto.user_id)

        return list(lr_user_ids)

    @staticmethod
    def _get_users_details_from_user_id(user_ids: List[str]) \
            -> List[UserDetailsDTO]:
        adapter = get_service_adapter()
        user_details = adapter.lr_users.get_users_details(user_ids)
        return user_details

    @staticmethod
    def _get_mapping_user_details_with_user_id(
            users_details: List[UserDetailsDTO]) \
            -> Dict[str, UserDetailsDTO]:

        mapping_user_details_with_user_id = {}

        for user in users_details:
            mapping_user_details_with_user_id[
                user.user_id
            ] = user

        return mapping_user_details_with_user_id


