from datetime import datetime

import factory

from lr_ride.adapters.dtos import UserDetailsDTO
from lr_ride.constants.enum import AssetTypeEnum, AssetSensitivityEnum, \
    OrderEnum, AppliedStatusEnum
from lr_ride.interactors.interactor_dtos import \
    AssetTransportationRequestDetailsDTO, MatchedRequestsBodyDetailsDTO, \
    FilterByDTO


class UserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UserDetailsDTO

    user_id = factory.Sequence(lambda n: 'user%d' % n)
    name = factory.Sequence(lambda n: 'user_name%d' % n)
