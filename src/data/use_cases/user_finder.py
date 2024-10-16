#PylintW0238:unused-private-member
#pylint: disable=unused-private-member

from typing import Dict
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UserFinder(UserFinderInterface):
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = user_repository
        

    def find(self, first_name:str) -> Dict: pass
    