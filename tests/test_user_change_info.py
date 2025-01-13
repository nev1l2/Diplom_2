import allure
import pytest

from data import CodeResponse, QueryResponse
from helpers import generate_user_data
from methods.base_methods import BaseMethods
from methods.user_methods import UserMethods


class TestUserChangeInfo:

    @allure.title("Успешное изменение данных авторизованного пользователя")
    @pytest.mark.parametrize('update_field', ['email', 'name'])
    def test_update_authorized_user(self, new_user, update_field):
        new_data = generate_user_data()
        payload = {update_field: new_data[update_field]}
        response = UserMethods.update_user(new_user['access_token'], **payload)
        assert BaseMethods.check_status_code(response, CodeResponse.SUCCESS_CODE) and \
               BaseMethods.check_user_field(response, update_field, new_data[update_field]), \
            (f"Не удалось обновить {update_field} пользователя. "
             f"Получено: {response.status_code} {response.json()['user'][update_field]}. "
             f"Ожидалось: {CodeResponse.SUCCESS_CODE} {new_data[update_field]}")

    @allure.title("Изменение данных неавторизованного пользователя")
    @pytest.mark.parametrize("field", ["email", "name"])
    def test_update_unauthorized_user(self, field):
        new_data = generate_user_data()
        response = UserMethods.update_user("", **{field: new_data[field]})
        assert BaseMethods.check_status_code(response, CodeResponse.UNAUTHORIZED_CODE) and \
               BaseMethods.check_response_field(response, 'message', QueryResponse.UPDATE_USER_UNAUTHORIZED['message']), \
            (f"Ответ не соответствует ожидаемому."
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")