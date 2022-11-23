from typing import List

from lr_ride.adapters.dtos import UserDetailsDTO


class LRUsersServiceAdapter:
    @property
    def interface(self):
        from lr_users.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_users_details(self, user_ids: List[int]) -> List[UserDetailsDTO]:
        from lr_users.exceptions.custom_exceptions import \
            InvalidUserIdsException
        try:
            interface_dtos = self.interface.get_users_details(user_ids)
        except InvalidUserIdsException as exception:
            from lr_ride.exceptions.custom_exceptions import\
                InvalidUserIdsException
            raise InvalidUserIdsException(exception.user_ids)

        return [
            UserDetailsDTO(
                name=user_dto.name,
                user_id=user_dto.user_id,
            )
            for user_dto in interface_dtos
        ]
