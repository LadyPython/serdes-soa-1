from abc import abstractmethod, ABC
from typing import Any


class BaseSerDes(ABC):
    def __init__(self):
        self.format = ""

    @abstractmethod
    def serialize(self, data) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def deserialize(self, data) -> Any:
        raise NotImplementedError
