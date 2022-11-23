from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from ib_common.date_time_utils.convert_string_to_local_date_time import \
    convert_string_to_local_date_time

from .validator_class import ValidatorClass
from ...constants.constants import DEFAULT_DATE_FORMAT
from ...interactors.interactor_dtos import MatchedRequestsBodyDetailsDTO, \
    FilterByDTO
from ...presenters.get_matched_asset_transportation_request_presenter_implementation import \
    GetMatchedAssetTransportationRequestPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    sort_by = kwargs['request_data']['sort_by']
    filter_by = kwargs['request_data'].get('filter')
    from_location = kwargs['request_data']['from_location']
    to_location = kwargs['request_data']['to_location']
    datetime = kwargs['request_data']['start_datetime']

    datetime = convert_string_to_local_date_time(datetime,
                                                 DEFAULT_DATE_FORMAT)
    if filter_by is not None:
        filter_by_dto = FilterByDTO(applied_status=filter_by.applied_status)
    else:
        filter_by_dto = None
    matched_requests_body_details = \
        MatchedRequestsBodyDetailsDTO(
            user_id=user_id,
            sort_by=sort_by,
            filter=filter_by_dto,
            from_location=from_location,
            to_location=to_location,
            datetime=datetime,
        )

    from lr_ride.storages.asset_transportation_request_storage_implementation\
        import AssetTransportationRequestStorageImplementation
    asset_transportation_request_storage = \
        AssetTransportationRequestStorageImplementation()

    from lr_ride.interactors.get_matched_asset_transfer_request_interactor \
        import GetMatchedAssetTransportationInteractor
    interactor = GetMatchedAssetTransportationInteractor(
        asset_transportation_request_storage)

    presenter = GetMatchedAssetTransportationRequestPresenterImplementation()

    return interactor.get_matched_asset_transportation_request_wrapper(
        matched_requests_body_details, presenter)
