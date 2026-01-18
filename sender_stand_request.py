# Онищенко Виталий, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import data
import requests

# 1.Выполнить запрос на создание заказа.
def post_new_order(create_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=create_order,
                         headers=data.headers)
response = post_new_order(data.create_order)

# 2.Сохранить номер трека заказа.
track_order = response.json()["track"]

# 3.Выполнить запрос на получение заказа по треку заказа.
def get_order_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDER,
                        params={"t": track_order})