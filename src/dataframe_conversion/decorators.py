from functools import wraps
from typing import Callable

from pandas import DataFrame


def reset_dataframe_index(func: Callable[..., DataFrame]) -> Callable[..., DataFrame]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> DataFrame:
        dataframe: DataFrame = func(*args, **kwargs)
        dataframe.index = range(dataframe.shape[0])
        return dataframe
    return wrapper
