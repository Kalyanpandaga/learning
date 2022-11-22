"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateAssetTransportRequestAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'from_location': 'string',
            'to_location': 'string',
            'start_datetime': 'string',
            'end_datetime': 'string',
            'assets_quantity': 1,
            'asset_type': 'LAPTOP',
            'asset_sensitivity': 'HIGHLY_SENSITIVE',
            'whom_to_deliver': 'string'
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
