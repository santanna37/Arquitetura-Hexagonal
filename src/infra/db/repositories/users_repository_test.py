import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler 
from .users_repository import UsersRepository


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason = "Sensive_test")
def test_insert_user():
    first_name = 'first_name_test_insert'
    last_name = 'last_name'
    age = 34

    user_repository = UsersRepository()
    user_repository.insert_users(
        first_name = first_name, last_name = last_name, age = age)

    sql = ''' 
        SELECT * FROM users 
        WHERE first_name = '{}'
        AND last_name = '{}'
        '''.format(first_name,last_name)
    response = connection.execute(text(sql))
    registry = response.fetchall()

    print(registry)

    assert registry[0].first_name == first_name

    connection.execute(text(f''' DELETE FROM users WHERE id = {registry[0].id}'''))
    connection.commit()


@pytest.mark.skip(reason = "Sensive_test")
def test_select_user():
    first_name = 'first_nametest'
    last_name = 'last_nametest'
    age = 34

    sql = '''
        INSERT INTO  users (first_name, last_name, age) VALUES ('{}', '{}', '{}')
        '''.format(first_name, last_name, age)
    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(first_name)
    print('==========')
    print(response)

    assert response[0].first_name == first_name

    connection.execute(text(f''' DELETE FROM users WHERE id = {response[0].id}'''))
    connection.commit()
