import allure
import requests

from urls import Urls

class OrdersMethods:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(token, ingredients):
        headers = {'Authorization': token}
        data = {"ingredients": ingredients}
        return requests.post(Urls.URL_order_create, json=data, headers=headers)

    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_user_orders(token):
        headers = {'Authorization': token}
        return requests.get(Urls.URL_order_list_user, headers=headers)

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients():
        return requests.get(Urls.URL_ingredients_list)