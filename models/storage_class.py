from abc import ABC, abstractmethod


class Storage(ABC):
    """
    Базовый абстрактный класс
    """
    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass


    @abstractmethod
    def get_unique_items_count(self):
        pass

