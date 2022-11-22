from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from ib_common.date_time_utils.convert_string_to_local_date_time import \
    convert_string_to_local_date_time

from .validator_class import ValidatorClass
from ...constants.constants import DEFAULT_DATE_FORMAT
from ...interactors.interactor_dtos import AssetTransferRequestDetailsDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # user_id = Access the user id
    user_id = "jkdf_regl_jkdf_regl_jkdf_regl_jkdf_r"
    from_location = kwargs['request_data']['from_location']
    to_location = kwargs['request_data']['to_location']
    start_datetime = kwargs['request_data']['start_datetime']
    end_datetime = kwargs['end_datetime'].get('end_datetime')
    assets_quantity = kwargs['request_data']['assets_quantity']
    asset_type = kwargs['request_data']['asset_type']
    asset_sensitivity = kwargs['request_data']['asset_sensitivity']
    whom_to_deliver = kwargs['request_data']['whom_to_deliver']

    start_datetime = convert_string_to_local_date_time(start_datetime,
                                                       DEFAULT_DATE_FORMAT)
    if end_datetime is not None:
        end_datetime = convert_string_to_local_date_time(
            end_datetime, DEFAULT_DATE_FORMAT)

    asset_transfer_request_details = \
        AssetTransferRequestDetailsDTO(
            user_id=user_id,
            from_location=from_location,
            to_location=to_location,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            assets_quantity=assets_quantity,
            asset_type=asset_type,
            asset_sensitivity=asset_sensitivity,
            whom_to_deliver=whom_to_deliver
        )

    from lr_ride.storages.asset_transportation_request_storage_implementation import \
        AssetTransportationRequestStorageImplementation
    asset_transportation_request_storage = \
        AssetTransportationRequestStorageImplementation()

    from lr_ride.interactors.create_asset_transfer_request_interactor import \
        CreateAssetTransferInteractor
    interactor = CreateAssetTransferInteractor(
        asset_transportation_request_storage)

    return interactor.create_asset_transportation_request_wrapper(
        asset_transfer_request_details)


