from datetime import datetime

import factory

from lr_ride.constants.enum import AssetTypeEnum, AssetSensitivityEnum
from lr_ride.interactors.interactor_dtos import AssetTransportationRequestDetailsDTO


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
