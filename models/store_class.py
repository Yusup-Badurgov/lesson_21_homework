from models.storage_class import Storage


class Store(Storage):
    """
    Класс склада
    """

    def __init__(self, items, capacity=100):
        self.__items = items
        self.__capacity = capacity

    @property
    def items(self):
        """
        Геттер для items
        :return:
        """
        ###
        """Дублирование кода. Метод полностью дублирует метод def get_items (self)"""
        ###
        return self.__items

    @property
    def capacity(self):
        """
        Геттер для capacity
        :return:
        """
        return self.__capacity

    def get_free_space(self, *args, **kwargs):
        """
        Функция получения кол-ва сободного места на складе
        :param args:
        :param kwargs:
        :return:
        """
        count = 0
        for k, v in self.get_items().items():
            count += v
        return self.capacity - count

    def add(self, new_title, new_capacity, *args, **kwargs):
        """
        Функция добавления товара на склад
        :param new_title:
        :param new_capacity:
        :param args:
        :param kwargs:
        :return:
        """
        if self.get_free_space(*args, **kwargs) >= new_capacity:
            if new_title in self.items:
                self.items[new_title] += new_capacity
            else:
                self.items[new_title] = new_capacity
        else:

            return

    def remove(self, rem_title, rem_capacity):
        """
        Функция удаления товара со склада
        :param rem_title:
        :param rem_capacity:
        :return:
        """
        if rem_title not in self.items or self.items[rem_title] < rem_capacity:
            return False
        self.items[rem_title] -= rem_capacity
        if self.items[rem_title] == 0:
            self.items.pop(rem_title)

    def get_items(self):
        """
        Функция получения словаря товар: количество
        :return:
        """

        ###
        """Дублирование кода. Метод полностью дублирует метод def items (self)"""
        ###
        return self.items

    def get_unique_items_count(self):
        """
        Функция получения кол-ва уникальных товаров
        :return:
        """
        return len(self.items)



