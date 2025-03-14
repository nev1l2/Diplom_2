import allure

from data import CodeResponse, QueryResponse
from helpers import generate_order_data
from methods.base_methods import BaseMethods
from methods.orders_methods import OrdersMethods


class TestOrderCreation:

    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_create_order_authorized(self, new_user, ingredients):
        order_data = generate_order_data(ingredients)
        response = OrdersMethods.create_order(new_user['access_token'], order_data)
        assert BaseMethods.check_status_code(response, CodeResponse.SUCCESS_CODE) and \
               BaseMethods.check_field_exists(response, 'order'), \
            f"Не удалось создать заказ. Код ответа: {response.status_code}, тело ответа: {response.json()}"

    @allure.title("Создание заказа неавторизованным пользователем")
    @allure.description("""
        Баг: API позволяет создать заказ неавторизованному пользователю.
        ОР код ответа 401 Unauthorized.
        ФР: код ответа 200, заказ создаётся.
    """)
    def test_create_order_unauthorized(self, ingredients):
        order_data = generate_order_data(ingredients)
        response = OrdersMethods.create_order("", order_data)
        assert BaseMethods.check_status_code(response, CodeResponse.SUCCESS_CODE) and \
               BaseMethods.check_response_field(response, 'success', QueryResponse.CREATE_ORDER_SUCCESS['success']), \
            (f"Ответ не соответствует ожидаемому."
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, new_user):
        response = OrdersMethods.create_order(new_user['access_token'], [])
        assert BaseMethods.check_status_code(response, CodeResponse.BAD_REQUEST_CODE) and \
               BaseMethods.check_response_field(response, 'message', QueryResponse.CREATE_ORDER_NO_INGREDIENTS['message']), \
            (f"Ответ не соответствует ожидаемому."
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredients(self, new_user):
        invalid_ingredients = ["53453gfdf34324fgfgfg", "3423fdfsdfho333o3oo3o234jjj"]
        response = OrdersMethods.create_order(new_user['access_token'], invalid_ingredients)
        assert BaseMethods.check_status_code(response, CodeResponse.SERVER_ERROR_CODE), \
            (f"Ответ не соответствует ожидаемому."
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")