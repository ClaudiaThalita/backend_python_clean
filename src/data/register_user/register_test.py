from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """ Testing registry method """

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.name()}
    # crio o dicionario com os valores
    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )
    #tento atribuir em register_user.register, os valores que eu criei no dicionario acima, na classe de registro

    
    print(response)
    # Testing inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]
    #verifico se o que eu criei, e o que eu inseri estão iguais.

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """ Testing registry method in fail """

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.random_number(digits=2), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    print(response)

    # Testing inputs
    assert user_repo.insert_user_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None