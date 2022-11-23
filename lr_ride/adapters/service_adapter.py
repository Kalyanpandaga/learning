class ServiceAdapter:
    @property
    def lr_users(self):
        from lr_ride.adapters.lr_users_service_adapter import \
            LRUsersServiceAdapter
        return LRUsersServiceAdapter()


def get_service_adapter():
    return ServiceAdapter()

