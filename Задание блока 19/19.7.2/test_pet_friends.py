from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Космо', animal_type='Черный',
                                     age='5', pet_photo='images/blackcat.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "5", "images/blackcat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][5]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Космо2', animal_type='Белый', age=1):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert len(my_pets['pets']) > 0, "There is no my pets"
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['name'] == name


# тест 1 Проверка добавления питомца с корректными данными без фото
def test_add_new_pet_without_photo_with_valid_data(name='Лолита', animal_type='Лысый', age='3'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    assert result['pet_photo'] == ''


# тест 2 Проверка на изменение фото питомца
def test_add_pet_new_photo(pet_photo='images/blackcat.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
    assert status == 200
    assert result['pet_photo'] != ''


# тест 3 "Проверка на загрузку фото питомца несоответствующего формата
def test_add_pet_new_photo(pet_photo='images/cat.xlsx'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
    assert status != 200


# тест 4 Проверка возвращения статуса 403 api при вводе неверного логина
def test_get_api_key_for_invalid_user_email(email='koryaga@mail.ru', password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403


# тест 5 Проверка возвращения статуса 403 api при вводе неверного пароля
def test_get_api_key_for_invalid_user_password(email=valid_email, password='DT##$fgs'):
    status, result = pf.get_api_key(email, password)
    assert status == 403


# тест 6 Проверка на добавление питомца с отрицательным возрастом
def test_add_new_pet_with_negative_age(name='Sputnik', animal_type='туземец',
                                       age='-100', pet_photo='images/cosmo.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200

# тест 7 Проверка на добавление питомца со слишком большим возрастом
def test_add_new_pet_with_too_old_age(name='SputniKV', animal_type='антиковид',
                                       age='999', pet_photo='images/cosmo.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200


# тест 8 "Проверка на добавление питомца без возраста
def test_add_new_pet_with_invalid_age(name='Cool', animal_type='Joke',
                                       age='', pet_photo='images/cosmo.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200


# Тест 9 Проверка введения имени более 50 симоволов
def test_add_new_pet_with_long_name(name='sadghdgafhhshdhdghsdghdshdhsgdhsgdhsdsdsadasgdhasgdhdgsahdahdgahdsghda',
                                    animal_type='',
                                    age='10', pet_photo='images/cosmo.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200


# тест 10 Проверка удаления питомца с пустым ID
def test_try_unsuccessful_delete_empty_pet_id():

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = ''
    status, _ = pf.delete_pet(auth_key, pet_id)
    assert status == 400 or 404

