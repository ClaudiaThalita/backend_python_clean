from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet

faker = Faker()

def test_by_pet_id():
    """ Testing pet_id method in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}

    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # Testing Input

    assert pet_repo.select_pet_param["pet_id"] == attributes["pet_id"]

    # Testing Output

    assert response["Success"] is True
    assert response["Data"]

def test_by_user_id():
    """ Testing pet_id method in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.random_number(digits=2)}

    response = find_pet.by_user_id(user_id=attributes["user_id"])

    # Testing Input

    assert pet_repo.select_pet_param["user_id"] == attributes["user_id"]

    # Testing Output

    assert response["Success"] is True
    assert response["Data"]

def test_by_pet_id_and_user_id():
    """ Testing pet_id method in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.random_number(digits=2),"pet_id": faker.random_number(digits=2)}


    response = find_pet.by_pet_id_and_user_id(pet_id=attributes["pet_id"],user_id=attributes["user_id"])

    # Testing Input

    assert pet_repo.select_pet_param["user_id"] == attributes["user_id"]
    assert pet_repo.select_pet_param["pet_id"] == attributes["pet_id"]

    # Testing Output

    assert response["Success"] is True
    assert response["Data"]

def test_register_by_id_fail():
    """ Testing registry method in fail """
    
    user_repo = PetRepositorySpy()
    find_pet = FindPet(user_repo)

    attributes = { "id": faker.name()}

    response = find_pet.by_pet_id(
        pet_id=attributes["id"]
    )

    print(response)

    # Testing inputs
    assert user_repo.insert_pet_param == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None  

def test_by_user_id_fail():
    """ Testing registry method in fail """
    
    user_repo = PetRepositorySpy()
    find_pet = FindPet(user_repo)

    attributes = { "id": faker.name()}

    response = find_pet.by_user_id(
        user_id=attributes["id"]
    )

    print(response)

    # Testing inputs
    assert user_repo.insert_pet_param == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None 

def test_by_pet_id_and_user_id_fail():
    """ Testing registry method in fail """
    
    user_repo = PetRepositorySpy()
    find_pet = FindPet(user_repo)

    attributes = { "pet_id": faker.name(), "user_id": faker.name()}

    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"],user_id=attributes["user_id"]
    )

    print(response)

    # Testing inputs
    assert user_repo.insert_pet_param == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None  