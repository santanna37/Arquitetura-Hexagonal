from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement = True, primary_key = True)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    age = Column(Integer, nullable = False)

    def __repr__(self):
        return f" Users [id = {self.id}, name = {self.first_name} {self.last_name}]"
