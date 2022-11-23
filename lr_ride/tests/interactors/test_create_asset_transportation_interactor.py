from datetime import datetime
from unittest.mock import create_autospec

import pytest

from lr_ride.interactors.create_asset_transfer_request_interactor import \
    CreateAssetTransportationInteractor
from lr_ride.interactors.storage_interfaces.\
    asset_transportation_request_storage_interface import \
    AssetTransportationRequestStorageInterface
from lr_ride.tests.factories.interactor_dtos import \
    AssetTransferRequestDetailsDTOFactory


class TestCreateAssetTransportationRequestInteractor:
    @pytest.fixture
    def common_mocks(self):
        asset_transfer_request_storage_mock = create_autospec(
            AssetTransportationRequestStorageInterface)

        return asset_transfer_request_storage_mock

    @pytest.fixture
    def setup_data(self):
        asset_transfer_request_details = \
            AssetTransferRequestDetailsDTOFactory(
                start_datetime=datetime(2022, 10, 15, 12, 15),
                end_datetime = datetime(2022, 10, 16, 12, 15)
            )

    def test_create_asset_transportation_request(self, common_mocks, setup_data):
        asset_transfer_request_details = setup_data
        asset_transfer_request_storage_mock = common_mocks

        interactor = CreateAssetTransportationInteractor(
            asset_transfer_request_storage_mock)

        interactor.create_asset_transportation_request_wrapper(
            asset_transfer_request_details)

        asset_transfer_request_storage_mock.\
            create_asset_transportation_request.assert_called_once_with(
                asset_transfer_request_details)







