import allure
import pytest

from helpers import generate_user_data, generate_order_data
from methods.orders_methods import OrdersMethods
from methods.user_methods import UserMethods


@pytest.fixture
def create_user():
    user_data = generate_user_data()
    with allure.step("Создание тестового пользователя"):
        response = UserMethods.register_user(**user_data)
    assert response.status_code == 200, f"Не удалось создать пользователя. Код ответа: {response.status_code}"
    yield user_data['email'], user_data['password'], user_data['name']
    with allure.step("Удаление тестового пользователя"):
        response = UserMethods.login_user(user_data['email'], user_data['password'])
        UserMethods.delete_user(response.json()['accessToken'])


@pytest.fixture
def auth_token(create_user):
    email, password, _ = create_user
    with allure.step("Получение токена авторизации"):
        response = UserMethods.login_user(email, password)
    assert response.status_code == 200, f"Не удалось получить токен. Код ответа: {response.status_code}"
    return response.json()['accessToken']


@pytest.fixture
def new_user():
    user_data = generate_user_data()

    with allure.step("Создание тестового пользователя"):
        response = UserMethods.register_user(**user_data)
    assert response.status_code == 200, f"Не удалось создать пользователя. Код ответа: {response.status_code}"

    with allure.step("Получение токена авторизации"):
        login_response = UserMethods.login_user(user_data['email'], user_data['password'])
    assert login_response.status_code == 200, f"Не удалось получить токен. Код ответа: {login_response.status_code}"

    access_token = login_response.json()['accessToken']
    user = {
        "email": user_data['email'],
        "password": user_data['password'],
        "name": user_data['name'],
        "access_token": access_token
    }

    yield user

    with allure.step("Удаление тестового пользователя"):
        UserMethods.delete_user(access_token)


@pytest.fixture
def create_new_order(new_user, ingredients):
    def _create_order():
        order_data = generate_order_data(ingredients)
        with allure.step("Создание тестового заказа"):
            response = OrdersMethods.create_order(new_user['access_token'], order_data)
        assert response.status_code == 200, f"Не удалось создать заказ. Код ответа: {response.status_code}"
        return response.json()

    return _create_order

@pytest.fixture
def ingredients():
    response = OrdersMethods.get_ingredients()
    assert response.status_code == 200, f"Не удалось получить ингредиенты. Код ответа: {response.status_code}"
    return response.json()['data']
