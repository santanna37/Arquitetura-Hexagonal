from abc import ABC, abstractmethod
from typing import Dict

class UserFinder(ABC):
    @classmethod
    @abstractmethod  # Use os dois decoradores assim: primeiro @classmethod, depois @abstractmethod
    def find(cls, first_name: str) -> Dict: pass
