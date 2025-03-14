import allure
import pytest

from data import CodeResponse, QueryResponse
from helpers import generate_user_data
from methods.base_methods import BaseMethods
from methods.user_methods import UserMethods


class TestUserCreation:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_new_user_success(self):
        data = generate_user_data()
        response = UserMethods.register_user(**data)
        assert BaseMethods.check_status_code(response, CodeResponse.SUCCESS_CODE) and \
               BaseMethods.check_field_exists(response, QueryResponse.REGISTER_SUCCESS), \
            f"Ошибка при создании пользователя. Код ответа: {response.status_code}, тело ответа: {response.json()}"

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, create_user):
        email, password, name = create_user
        response = UserMethods.register_user(email=email, password=password, name=name)
        assert BaseMethods.check_status_code(response, CodeResponse.FORBIDDEN_CODE) and \
               BaseMethods.check_response_field(response, 'message', QueryResponse.REGISTER_USER_EXISTS['message']), \
            (f"Ответ не соответствует ожидаемому."
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")

    @allure.title("Создание пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_user_without_required_field(self, field):
        data = generate_user_data()
        data[field] = ""
        response = UserMethods.register_user(**data)
        assert BaseMethods.check_status_code(response, CodeResponse.FORBIDDEN_CODE) and \
               BaseMethods.check_response_field(response, 'message', QueryResponse.REGISTER_MISSING_FIELD['message']), \
            (f"Ответ при попытке создать пользователя без {field}. "
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")