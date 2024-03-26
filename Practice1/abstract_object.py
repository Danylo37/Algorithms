from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def get_info(self) -> str:
        pass

    @abstractmethod
    def get_message(self) -> str:
        pass

    def __repr__(self):
        pass
