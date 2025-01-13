# Diplom_2
Тестирование API https://stellarburgers.nomoreparties.site/

Что было сделано в рамках данного задания:

1) Написаны тесты на проверку "Создания пользователя" **test_user_create.py&**
    1.1. Создать уникального пользователя.
    1.2. Создать пользователя, который уже зарегистрирован. 
    1.3. Создать пользователя и не заполнить одно из обязательных полей.
2) Написаны тесты на Авторизацию пользователя: **test_user_authorization.py**
   2.1. Выполнить логин под существующим пользователем.
   2.2. Выполнить логин с неверным логином и паролем.
3) Написаны тесты на Изменение данных пользователя: **test_user_change_info.py**
   3.1. Изменить данные пользователя с авторизацией.
   3.2. Изменить данные без авторизации.
4) Написаны тесты на Создание заказа: **test_orders_create.py**
   4.1. Создать заказ с авторизацией.
   4.2. Создать заказ без авторизации.
   4.3. Создать заказ с ингредиентами.
   4.4. Создать заказ без ингредиентов.
5) Написаны тесты на Создание заказ с неверным хешем ингредиентов. **test_orders_receiving.py**
   5.1. Получение заказов конкретного пользователя:
   5.2. Получить заказы авторизованного пользователя.
   5.3. Получить заказы неавторизованного пользователя.


Библиотеки используемые в рамках задания: pytest, allure-pytest, Faker, requests

Сформирован allure отчет