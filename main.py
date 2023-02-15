from models.request_class import Request
from models.shop_class import Shop
from models.store_class import Store


def default_values():
    """
    Функция задания начальных значений
    :return:
    """
    store_values = {
        "яблоки": 10,
        "груши": 25,
        "сливы": 18,
        "виноград": 15,
        "лимон": 11,
        "персики": 13
    }

    shop_values = {
        "яблоки": 2,
        "груши": 3,
        "сливы": 1,
        "виноград": 2
    }

    return Store(store_values), Shop(shop_values)


def storage_status():
    """
    Вывод текущего состояния по складам и получение строки команды
    """
    print(f"В склад хранится:")
    [print(v, k) for k, v in store.get_items().items()]
    print(f"\nВ магазин хранится:")
    [print(v, k) for k, v in shop.get_items().items()]
    command = input("\nВведите команду: ")
    user_request = Request(command)
    return user_request


def main(object_from, object_to, verification=None):
    """
    Главная функция перемещения товаров
    :param object_from: объект "откуда"
    :param object_to: объект "куда"
    :param verification: доп параметр нужен для проверки магазина на наличие товара при полном его заполнении
    :return:
    """
    try:
        # Проверка наличия необходимого товара и его количества на исходном складе
        if object_from.items[request.product] < request.amount:
            print(f"Недостаточно товара в {request.from_}")
            return
        print(f"Нужное количество есть в {request.from_}")
    except Exception:
        print(f"Нужного товара нет в {request.from_}")
        return
    try:
        # Проверка возможности перемещения товара в пункт назначения
        if object_to.get_free_space(request.product) >= request.amount:
            object_from.remove(request.product, request.amount)
            print(f"Курьер забрал {request.amount} {request.product} из {request.from_}")
            print(f"Курьер везет {request.amount} {request.product} из {request.from_} в {request.to_}")
            object_to.add(request.product, request.amount, verification)
            print(f"Курьер доставил {request.amount} {request.product} в {request.to_}")
        else:
            print(f"Нет свободного места для товара в {request.to_}")
    except Exception:
        print("Недостаточно места в магазин")


if __name__ == "__main__":
    store, shop = default_values()

    while True:
        try:
            request = storage_status()
        except Exception:
            print("Неверный запрос!!!")
            continue

        if request.from_ == "склад":
            main(store, shop, request.product)
        else:
            main(shop, store)
