"""
# TODO: Update test case description
"""
from datetime import datetime

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from ib_users.models import UserAccount

from lr_ride.constants.enum import AppliedStatusEnum
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters import get_user_details_mock
from ...factories.adapter_dtos import UserDetailsDTOFactory
from ...factories.models import AssetTransportationRequestFactory


class TestCase01GetMatchedAssetTransportRequestsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def required_data_setup(self, api_user):
        user_id = 'bc0fec43-ce34-4cde-81d5-36869493018d'
        user = UserAccount.objects.create(
            username='test', user_id=user_id
        )
        self.api_user = user
        user_ids = [str(api_user.user_id), 'user2']
        request_object1 = \
            AssetTransportationRequestFactory(
                user_id=user_ids[0],
                from_location='khammam',
                to_location='hyderabad',
                start_datetime=datetime(2022, 10, 11, 7, 12),
                end_datetime=datetime(2022, 10, 11, 9, 12),
                applied_status=AppliedStatusEnum.not_applied.value
            )

        request_object2 = \
            AssetTransportationRequestFactory(
                user_id=user_ids[0],
                from_location='warangal',
                to_location='hyderabad',
                start_datetime=datetime(2022, 10, 11, 7, 12),
                end_datetime=datetime(2022, 10, 11, 9, 12)
            )

        request_object3 = \
            AssetTransportationRequestFactory(
                user_id=user_ids[0],
                from_location='khammam',
                to_location='hyderabad',
                start_datetime=datetime(2022, 10, 11, 8, 12),
                applied_status=AppliedStatusEnum.not_applied.value,
                end_datetime=None,
            )

        request_object4 = \
            AssetTransportationRequestFactory(
                user_id=user_ids[0],
                from_location='khammam',
                to_location='hyderabad',
                start_datetime=datetime(2022, 10, 11, 7, 50),
                end_datetime=None,
            )

        request_object5 = \
            AssetTransportationRequestFactory(
                user_id=user_ids[0],
                from_location='khammam',
                to_location='hyderabad',
                start_datetime=datetime(2022, 10, 11, 12, 12),
                end_datetime=datetime(2022, 10, 11, 11, 12)
            )

        request_object6 = \
            AssetTransportationRequestFactory(
                user_id=user_ids[0],
                from_location='khammam',
                to_location='hyderabad',
                start_datetime=datetime(2022, 10, 11, 7, 12),
                end_datetime=datetime(2022, 10, 11, 9, 12),
                applied_status=AppliedStatusEnum.applied.value
            )
        request_object7 = \
            AssetTransportationRequestFactory(
                user_id=user_ids[1],
                from_location='khammam',
                to_location='hyderabad',
                start_datetime=datetime(2022, 10, 11, 7, 12),
                end_datetime=datetime(2022, 10, 11, 9, 12)
            )
        request_users_details = [
            UserDetailsDTOFactory(user_id=user_ids[0])
        ]

        return request_users_details

    def setupUser(self):
        pass

    @pytest.mark.django_db
    def test_case(self, snapshot, required_data_setup, mocker):
        request_users_details = required_data_setup

        get_user_details_mock_object = get_user_details_mock(mocker)
        get_user_details_mock_object.return_value = request_users_details

        body = {
            'sort_by': 'ASC',
            'filter': {
                'applied_status': 'NOT_APPLIED'
            },
            'from_location': 'khammam',
            'to_location': 'hyderabad',
            'datetime': '2022-10-11 8:12'
        }

        path_params = {}
        query_params = {'limit': 3, 'offset': 0}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)







