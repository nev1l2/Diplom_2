import allure
import requests

from urls import Urls


class UserMethods:

    @staticmethod
    @allure.step("Регистрация пользователя: {email}")
    def register_user(email, password, name):
        data = {"email": email, "password": password, "name": name}
        return requests.post(Urls.URL_user_create, json=data)

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(email, password):
        data = {"email": email, "password": password}
        return requests.post(Urls.URL_user_login, json=data)

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def update_user(token, **data):
        headers = {'Authorization': token}
        return requests.patch(Urls.URL_user_change_info, json=data, headers=headers)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        headers = {'Authorization': token}
        return requests.delete(Urls.URL_user_delete, headers=headers)
