from datetime import datetime

import factory

from lr_ride.constants.enum import AssetTypeEnum, AssetSensitivityEnum, \
    OrderEnum, AppliedStatusEnum
from lr_ride.interactors.interactor_dtos import \
    AssetTransportationRequestDetailsDTO, MatchedRequestsBodyDetailsDTO, \
    FilterByDTO, MatchedAssetTransportationRequestsWithUserDetailsDTO
from lr_ride.tests.factories.adapter_dtos import UserDetailsDTOFactory


class AssetTransferRequestDetailsDTOFactory(factory.Factory):
    class Meta:
        model = AssetTransportationRequestDetailsDTO

    user_id = factory.Sequence(lambda n: 'user%d' % n)
    from_location = factory.Sequence(lambda n: 'from_location%d' % n)
    to_location = factory.Sequence(lambda n: 'to_location%d' % n)
    start_datetime = factory.LazyFunction(datetime.now)
    end_datetime = factory.LazyFunction(datetime.now)
    assets_quantity = factory.Sequence(lambda n: n)
    asset_type = factory.Iterator(AssetTypeEnum.get_list_of_values())
    asset_sensitivity = factory.Iterator(
        AssetSensitivityEnum.get_list_of_values())
    whom_to_deliver = factory.Sequence(lambda n: 'whom_to_delever%d' % n)


class FilterByDTOFactory(factory.Factory):
    class Meta:
        model = FilterByDTO

    applied_status = factory.Iterator(AppliedStatusEnum.get_list_of_values())


class MatchedRequestsBodyDetailsDTOFactory(factory.Factory):
    class Meta:
        model = MatchedRequestsBodyDetailsDTO

    user_id = factory.Sequence(lambda n: 'user%d' % n)
    sort_by = factory.Iterator(OrderEnum.get_list_of_values())
    filter = factory.SubFactory(FilterByDTOFactory)
    from_location = factory.Sequence(lambda n: 'from_location%d' % n)
    to_location = factory.Sequence(lambda n: 'to_location%d' % n)
    datetime = factory.LazyFunction(datetime.now)


class MatchedAssetTransportationRequestsWithUserDetailsDTOFactory(
        factory.Factory):

    class Meta:
        model = MatchedAssetTransportationRequestsWithUserDetailsDTO

    requester_details = factory.SubFactory(UserDetailsDTOFactory)
    from_location = factory.Sequence(lambda n: 'from_location%d' % n)
    to_location = factory.Sequence(lambda n: 'to_location%d' % n)
    start_datetime = factory.LazyFunction(datetime.now)
    end_datetime = factory.LazyFunction(datetime.now)
    assets_quantity = factory.Sequence(lambda n: n)
    asset_type = factory.Iterator(AssetTypeEnum.get_list_of_values())
    asset_sensitivity = factory.Iterator(
        AssetSensitivityEnum.get_list_of_values())
    whom_to_deliver = factory.Sequence(lambda n: 'whom_to_delever%d' % n)
    applied_status = factory.Iterator(AppliedStatusEnum.get_list_of_values())
