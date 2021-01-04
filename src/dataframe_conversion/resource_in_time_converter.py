from typing import List

from pandas import DataFrame, concat

from dataframe_conversion.dataframe_converter_base import DataFrameConverterBase
from dataframe_conversion.decorators import reset_dataframe_index
from dataframe_conversion.conversion_constants import YEAR_DATAFRAME_COLUMN_NAME, QUARTER_DATAFRAME_COLUMN_NAME
from human_resource.resource_in_time import ResourceInTime
from dataframe_conversion.resource_collection_converter import ResourceCollectionConverter


class ResourceInTimeConverter(DataFrameConverterBase):
    @staticmethod
    @reset_dataframe_index
    def convert_to_dataframe(resource_in_time: ResourceInTime) -> DataFrame:
        dataframe_list: List[DataFrame] = list()
        for period, resource_collection in resource_in_time.period_resource_collection_dict.items():
            resource_collection_dataframe: DataFrame = ResourceCollectionConverter.convert_to_dataframe(
                resource_collection
            )

            assert YEAR_DATAFRAME_COLUMN_NAME not in resource_collection_dataframe.columns
            resource_collection_dataframe[YEAR_DATAFRAME_COLUMN_NAME] = period.year

            assert QUARTER_DATAFRAME_COLUMN_NAME not in resource_collection_dataframe.columns
            resource_collection_dataframe[QUARTER_DATAFRAME_COLUMN_NAME] = f"Q{period.quarter}"

            dataframe_list.append(resource_collection_dataframe)

        return concat(dataframe_list)
