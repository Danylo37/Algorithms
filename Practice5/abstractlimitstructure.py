from abc import ABC, abstractmethod
from Practice1.abstract_object import Employee


class AbstractStack(ABC):

    @abstractmethod
    def push(self, value: Employee) -> None:
        ...

    @abstractmethod
    def pop(self) -> Employee:
        ...

    @abstractmethod
    def top(self) -> Employee:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...


class AbstractQueue(ABC):

    @abstractmethod
    def enqueue(self, value: Employee) -> None:
        ...

    @abstractmethod
    def dequeue(self) -> Employee:
        ...

    @abstractmethod
    def top(self) -> Employee:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...


class AbstractDeque(ABC):

    @abstractmethod
    def push_first(self, value: Employee) -> None:
        ...

    @abstractmethod
    def push_last(self, value: Employee) -> None:
        ...

    @abstractmethod
    def pop_first(self) -> Employee:
        ...

    @abstractmethod
    def pop_last(self) -> Employee:
        ...

    @abstractmethod
    def top_first(self) -> Employee:
        ...

    @abstractmethod
    def top_last(self) -> Employee:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...
