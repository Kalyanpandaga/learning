from datetime import datetime

import pytest

from lr_ride.constants.enum import AppliedStatusEnum
from lr_ride.interactors.interactor_dtos import MatchedRequestsBodyDetailsDTO
from lr_ride.models.asset_transportation_request import \
    AssetTransportationRequest
from lr_ride.storages.asset_transportation_request_storage_implementation import \
    AssetTransportationRequestStorageImplementation
from lr_ride.tests.factories.interactor_dtos import \
    AssetTransferRequestDetailsDTOFactory


@pytest.mark.django_db
class TestCreateAssetTransportationRequests:
    def test_create_asset_transportation_requests(self):

        # arrange
        storage = AssetTransportationRequestStorageImplementation()
        asset_transportation_request_details = \
            AssetTransferRequestDetailsDTOFactory(
                start_datetime=datetime(2022, 10, 15, 12, 15),
                end_datetime=None
            )

        # act
        storage.create_asset_transportation_request(
            asset_transportation_request_details)

        # assert
        created_asset_transportation_request_is_exists = \
            AssetTransportationRequest.objects.filter(
                user_id=asset_transportation_request_details.user_id,
                from_location=asset_transportation_request_details.from_location,
                to_location=asset_transportation_request_details.to_location,
                start_datetime=asset_transportation_request_details.start_datetime,
                end_datetime=asset_transportation_request_details.end_datetime,
                assets_quantity=asset_transportation_request_details.assets_quantity,
                asset_type=asset_transportation_request_details.asset_type,
                asset_sensitivity=asset_transportation_request_details.asset_sensitivity,
                whom_to_deliver=asset_transportation_request_details.whom_to_deliver,
                applied_status=AppliedStatusEnum.not_applied.value
            ).exists()

        assert created_asset_transportation_request_is_exists is True






