import allure
import pytest

from data import CodeResponse, QueryResponse
from methods.base_methods import BaseMethods
from methods.user_methods import UserMethods


class TestUserAuthorization:

    @allure.title("Успешная авторизация существующего пользователя")
    def test_login_user(self, create_user):
        email, password, _ = create_user
        response = UserMethods.login_user(email, password)
        assert BaseMethods.check_status_code(response, CodeResponse.SUCCESS_CODE) and \
               BaseMethods.check_field_exists(response, 'accessToken'), \
            f"Не удалось авторизоваться. Код ответа: {response.status_code}, тело ответа: {response.json()}"


    @allure.title("Авторизация с невалидными данными")
    @pytest.mark.parametrize("email,password", [
        ("kek@gmail.ru", "pas2231"),
        ("lol@mail.com", "qwerty72"),
    ])
    def test_login_with_invalid_data(self, create_user, email, password):
        response = UserMethods.login_user(email, password)
        assert BaseMethods.check_status_code(response, CodeResponse.UNAUTHORIZED_CODE) and \
               BaseMethods.check_response_field(response, 'message', QueryResponse.LOGIN_FAILED['message']), \
            (f"Ответ не соответствует ожидаемому."
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")