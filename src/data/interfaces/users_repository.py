from abc import ABC, abstractmethod
from typing import List
from src.domain.models.user import Users



class UsersRepositoryInterface(ABC):

    
    @abstractmethod
    def insert_users(self, first_name: str, last_name: str, age:int) -> None: pass

    @abstractmethod
    def select_user(self, first_name: str) -> List[Users]: pass
