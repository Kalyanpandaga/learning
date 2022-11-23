from datetime import datetime
from unittest.mock import create_autospec

import pytest

from mock import Mock

from lr_ride.interactors.get_matched_asset_transfer_request_interactor import \
    GetMatchedAssetTransportationInteractor
from lr_ride.interactors.presenter_interfaces.\
    get_matched_asset_transportation_request_presenter_interface import \
    GetMatchedAssetTransportationRequestPresenterInterface
from lr_ride.interactors.storage_interfaces.\
    asset_transportation_request_storage_interface import \
    AssetTransportationRequestStorageInterface
from lr_ride.tests.common_fixtures.adapters import get_user_details_mock
from lr_ride.tests.factories.adapter_dtos import UserDetailsDTOFactory
from lr_ride.tests.factories.interactor_dtos import \
    MatchedRequestsBodyDetailsDTOFactory, \
    MatchedAssetTransportationRequestsWithUserDetailsDTOFactory
from lr_ride.tests.factories.storage_dtos import \
    MatchedAssetTransportationRequestsDetailsDTOFactory


class TestGetMatchedAssetTransportationInteractor:
    @pytest.fixture
    def common_mocks(self):
        asset_transfer_request_storage_mock = create_autospec(
            AssetTransportationRequestStorageInterface)
        presenter_mock = create_autospec(
            GetMatchedAssetTransportationRequestPresenterInterface)

        return asset_transfer_request_storage_mock, presenter_mock

    @pytest.fixture
    def setup_data(self):
        user_ids = ["user1", "user2"]

        asset_transfer_request_body_details = \
            MatchedRequestsBodyDetailsDTOFactory(
                user_id=user_ids[0],
                datetime=datetime(2022, 10, 15, 12, 15),
            )

        matched_request_details_1 = \
            MatchedAssetTransportationRequestsDetailsDTOFactory(
                user_id=user_ids[0])
        matched_request_details_2 = \
            MatchedAssetTransportationRequestsDetailsDTOFactory(
                user_id=user_ids[0])
        matched_request_details_3 = \
            MatchedAssetTransportationRequestsDetailsDTOFactory(
                user_id=user_ids[0])

        matched_asset_transportation_requests_details = [
            matched_request_details_1, matched_request_details_2,
            matched_request_details_3
        ]

        asset_transport_request_user_ids = ["user1"]

        user_details = [UserDetailsDTOFactory(user_id=user_id)
                        for user_id in asset_transport_request_user_ids]

        matched_asset_transportation_requests_with_user_details_details=[
            MatchedAssetTransportationRequestsWithUserDetailsDTOFactory(
                requester_details=user_details[0],
                from_location=matched_request_details_1.from_location,
                to_location=matched_request_details_1.to_location,
                start_datetime=matched_request_details_1.start_datetime,
                end_datetime=matched_request_details_1.end_datetime,
                assets_quantity=matched_request_details_1.assets_quantity,
                asset_type=matched_request_details_1.asset_type,
                asset_sensitivity=matched_request_details_1.asset_sensitivity,
                whom_to_deliver=matched_request_details_1.whom_to_deliver,
                applied_status=matched_request_details_1.applied_status
            ),
            MatchedAssetTransportationRequestsWithUserDetailsDTOFactory(
                requester_details=user_details[0],
                from_location=matched_request_details_2.from_location,
                to_location=matched_request_details_2.to_location,
                start_datetime=matched_request_details_2.start_datetime,
                end_datetime=matched_request_details_2.end_datetime,
                assets_quantity=matched_request_details_2.assets_quantity,
                asset_type=matched_request_details_2.asset_type,
                asset_sensitivity=matched_request_details_2.asset_sensitivity,
                whom_to_deliver=matched_request_details_2.whom_to_deliver,
                applied_status=matched_request_details_2.applied_status
            ),
            MatchedAssetTransportationRequestsWithUserDetailsDTOFactory(
                requester_details=user_details[0],
                from_location=matched_request_details_3.from_location,
                to_location=matched_request_details_3.to_location,
                start_datetime=matched_request_details_3.start_datetime,
                end_datetime=matched_request_details_3.end_datetime,
                assets_quantity=matched_request_details_3.assets_quantity,
                asset_type=matched_request_details_3.asset_type,
                asset_sensitivity=matched_request_details_3.asset_sensitivity,
                whom_to_deliver=matched_request_details_3.whom_to_deliver,
                applied_status=matched_request_details_3.applied_status
            )
        ]

        return asset_transfer_request_body_details, \
            matched_asset_transportation_requests_details, user_details, \
            asset_transport_request_user_ids, \
            matched_asset_transportation_requests_with_user_details_details

    def test_get_matched_asset_transportation_request(
            self, common_mocks, setup_data, mocker):
        asset_transfer_request_body_details, \
            matched_asset_transportation_requests_details, user_details, \
            asset_transport_request_user_ids, \
            matched_asset_transportation_requests_with_user_details_details =\
            setup_data

        asset_transfer_request_storage_mock, presenter_mock = common_mocks
        presenter_response = Mock()
        get_user_details_mock_object = get_user_details_mock(mocker)

        asset_transfer_request_storage_mock.\
            get_matched_asset_transportation_requests.return_value = \
            matched_asset_transportation_requests_details
        get_user_details_mock_object.return_value = user_details
        presenter_mock.get_matched_asset_transportation_request_response.\
            return_value = presenter_response

        interactor = GetMatchedAssetTransportationInteractor(
            asset_transfer_request_storage_mock)

        # act
        actual_response = \
            interactor.get_matched_asset_transportation_request_wrapper(
                asset_transfer_request_body_details, presenter_mock)

        # assert
        asset_transfer_request_storage_mock. \
            get_matched_asset_transportation_requests.assert_called_once_with(
                asset_transfer_request_body_details)

        get_user_details_mock_object.assert_called_once_with(
            asset_transport_request_user_ids)

        presenter_mock.get_matched_asset_transportation_request_response.\
            assert_called_once_with(
                matched_asset_transportation_requests_with_user_details_details)

        assert presenter_response == actual_response






