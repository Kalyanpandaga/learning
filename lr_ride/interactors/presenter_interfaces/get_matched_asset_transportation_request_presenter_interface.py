from abc import ABC, abstractmethod


class GetMatchedAssetTransportationRequestPresenterInterface(ABC):
    @abstractmethod
    def get_matched_asset_transportation_request_response(
            self,
            matched_asset_transportation_requests_with_user_details):
        pass
