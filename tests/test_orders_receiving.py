import allure
import pytest

from data import CodeResponse, QueryResponse
from methods.base_methods import BaseMethods
from methods.orders_methods import OrdersMethods


@allure.feature("Получение заказов пользователя")
class TestOrdersReceiving:

    @allure.title("Успешное получение заказов авторизованным пользователем")
    def test_get_orders_authorized(self, new_user, create_new_order):
        create_new_order()
        response = OrdersMethods.get_user_orders(new_user['access_token'])
        assert BaseMethods.check_status_code(response, CodeResponse.SUCCESS_CODE) and \
       BaseMethods.check_field_exists(response, 'orders') and \
       len(response.json()['orders']) > 0, \
       f"Ошибка при получении заказов пользователя: " \
       f"Код ответа: {response.status_code}, " \
       f"Тело ответа: {response.json()}, " \
       f"Количество заказов: {len(response.json().get('orders', []))}"

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_orders_unauthorized(self):
        response = OrdersMethods.get_user_orders("")
        assert BaseMethods.check_status_code(response, CodeResponse.UNAUTHORIZED_CODE) and \
               BaseMethods.check_response_field(response, 'message', QueryResponse.GET_ORDERS_UNAUTHORIZED['message']), \
            (f"Ответ не соответствует ожидаемому."
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")