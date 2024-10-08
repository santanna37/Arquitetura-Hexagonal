from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/clean_database".format(
            'mysql+pymysql',
            'root',
            'mypassword',
            'localhost',
            '3306',
            'clean_database'
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind = self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exec_vel, exc_tb):
        self.session.close()
