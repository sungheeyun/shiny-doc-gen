from typing import Any
from abc import ABC, abstractmethod

from pandas import DataFrame


class DataFrameConverterBase(ABC):
    """
    Converters which converts resource class objects to pandas.DataFrame
    """

    @staticmethod
    @abstractmethod
    def convert_to_dataframe(resource_object: Any) -> DataFrame:
        assert False
