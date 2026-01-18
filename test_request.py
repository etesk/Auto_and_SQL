# Онищенко Виталий 39-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# Функция для позитивной проверки
def positive_assert(track_order):
    order_response = sender_stand_request.get_order_track(track_order)
    assert order_response.status_code == 200

# Автотест
def test_get_order_track_response():
    positive_assert(sender_stand_request.track_order)