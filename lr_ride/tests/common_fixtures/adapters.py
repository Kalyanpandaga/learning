from lr_ride.tests.common_fixtures import get_mock


def get_user_details_mock(mocker, return_value=None, side_effect=None):
    from lr_ride.adapters.lr_users_service_adapter import LRUsersServiceAdapter
    func = LRUsersServiceAdapter.get_users_details
    return get_mock(mocker, func, return_value, side_effect)
