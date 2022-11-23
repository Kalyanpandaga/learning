from abc import ABC, abstractmethod
from typing import List

from lr_users.interactors.storage_interfaces.dtos import UserDetailsDTO


class UserProfileStorageInterface(ABC):
    @abstractmethod
    def get_users_details(self, user_ids: List[int]) -> \
            List[UserDetailsDTO]:
        pass

    @abstractmethod
    def get_existing_user_ids(self, user_ids: List[int]) -> \
            List[int]:
        pass
