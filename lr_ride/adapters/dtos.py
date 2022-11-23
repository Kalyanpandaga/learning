from dataclasses import dataclass


@dataclass
class UserDetailsDTO:
    user_id: str
    name: str
