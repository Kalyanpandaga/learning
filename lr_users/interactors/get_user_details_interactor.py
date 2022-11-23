from typing import List

from lr_users.exceptions.custom_exceptions import InvalidUserIdsException
from lr_users.interactors.storage_interfaces.dtos import UserDetailsDTO
from lr_users.interactors.storage_interfaces.user_profile_storage_interface \
    import UserProfileStorageInterface


class GetUsersDetailsInteractor:
    def __init__(self, user_storage: UserProfileStorageInterface):
        self.user_storage = user_storage

    def get_users_details(self, user_ids: List[int]) -> List[UserDetailsDTO]:
        existing_user_ids = self.user_storage.get_existing_user_ids(user_ids)
        invalid_user_ids = list(set(user_ids)-set(existing_user_ids))
        if len(invalid_user_ids) > 0:
            raise InvalidUserIdsException(invalid_user_ids)

        user_details = self.user_storage.get_users_details(user_ids)
        return user_details



