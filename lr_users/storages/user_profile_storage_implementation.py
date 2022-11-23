from typing import List

from lr_users.interactors.storage_interfaces.dtos import UserDetailsDTO
from lr_users.interactors.storage_interfaces.user_profile_storage_interface \
    import UserProfileStorageInterface
from lr_users.models.user_profile import UserProfile


class UserProfileStorageImplementation(UserProfileStorageInterface):
    def get_existing_user_ids(self, user_ids: List[int]) -> \
            List[int]:
        existing_user_ids = \
            UserProfile.objects.filter(id__in=user_ids).values('user_id')

        return [user_id_details['user_id']
                for user_id_details in existing_user_ids]

    def get_users_details(self, user_ids: List[int]) -> \
            List[UserDetailsDTO]:
        users = UserProfile.objects.filter(id__in=user_ids)
        user_details = []
        for user in users:
            user_details.append(
                UserDetailsDTO(
                    user_id=user.id,
                    name=user.name,
                )
            )
        return user_details
