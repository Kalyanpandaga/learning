"""
# TODO: Update test case description
"""
from datetime import datetime

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from lr_ride.constants.enum import AppliedStatusEnum
from lr_ride.models.asset_transportation_request import \
    AssetTransportationRequest
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateAssetTransportRequestAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, api_user):
        user_id = api_user
        body = {
            'from_location': 'Khammam',
            'to_location': 'Hyderabad',
            'start_datetime': '2022-10-11 19:10',
            'end_datetime': '2022-11-11 19:10',
            'assets_quantity': 2,
            'asset_type': 'LAPTOP',
            'asset_sensitivity': 'HIGHLY_SENSITIVE',
            'whom_to_deliver': 'kalyan-999546735456'
        }
        start_datetime = datetime(2022, 10, 11, 19, 10)
        end_datetime = datetime(2022, 11, 11, 19, 10)
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

        created_asset_transportation_request_is_exists = \
            AssetTransportationRequest.objects.filter(
                user_id=user_id,
                from_location=body['from_location'],
                to_location=body['to_location'],
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                assets_quantity=body['assets_quantity'],
                asset_type=body['asset_type'],
                asset_sensitivity=body['asset_sensitivity'],
                whom_to_deliver=body['whom_to_deliver'],
                applied_status=AppliedStatusEnum.not_applied.value
            ).exists()

        assert created_asset_transportation_request_is_exists is True

