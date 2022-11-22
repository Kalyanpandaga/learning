import abc

from lr_users_auth.interactors.storage_interfaces.dtos import TokensDTO
from lr_users_auth.adapters.dtos import UserAuthTokensDTO

class LoginPresenterInterface:

    @abc.abstractmethod
    def raise_invalid_credentials_exception(self):
        pass

    @abc.abstractmethod
    def raise_user_account_deactivated_exception(self):
        pass

    @abc.abstractmethod
    def get_response_for_login(self, token_dto: TokensDTO):
        pass