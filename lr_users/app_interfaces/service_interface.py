from typing import List

from lr_users.interactors.get_user_details_interactor import \
    GetUsersDetailsInteractor
from lr_users.storages.user_profile_storage_implementation import \
    UserProfileStorageImplementation


class ServiceInterface:
    @staticmethod
    def get_users_details(user_ids: List[int]):
        user_storage = UserProfileStorageImplementation()
        user_details_interactor = \
            GetUsersDetailsInteractor(user_storage)
        user_details = user_details_interactor.get_users_details(user_ids)
        return user_details
    