from __future__ import annotations
from typing import Any
from abc import abstractmethod, ABC

from utils import classproperty


class JsonValueBaseClass(ABC):
    """
    Abstract base class. Every class in human_resource should subclass this class.
    """

    @abstractmethod
    def to_json_data(self) -> Any:
        assert False

    @staticmethod
    @abstractmethod
    def create_from_json_data(json_data: Any) -> JsonValueBaseClass:
        assert False

    @classproperty
    @abstractmethod
    def json_field_name(cls) -> str:
        assert False
