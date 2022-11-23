class InvalidUserIdsException(Exception):
    def __init__(self, user_ids):
        self.user_ids = user_ids
