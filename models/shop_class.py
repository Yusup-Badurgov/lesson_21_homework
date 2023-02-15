from models.store_class import Store


class Shop(Store):
    """
    Класс магазина
    """

    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def get_free_space(self, new_title):
        """
        Функция определения кол-ва свободного пространства в магазине
        :param new_title:
        :return:
        """
        #Проверка на наличие свободных мест в магазине
        if self.get_unique_items_count() >= 5:
            if new_title not in self.items:
                raise Exception
        return super().get_free_space()

    ###
    """ Hard Core 
    Здесь значение self.get_unique_items_count() задается жестко, можно ввести переменную, что позволит гибко настраивать
    кол-во свободных 'полок' в магазине и сделает задел для расширения """
    ###
