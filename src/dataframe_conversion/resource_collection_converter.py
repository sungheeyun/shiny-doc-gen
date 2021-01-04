from typing import Dict, List

from pandas import DataFrame, concat

from dataframe_conversion.dataframe_converter_base import DataFrameConverterBase
from dataframe_conversion.decorators import reset_dataframe_index
from human_resource.resource_collection import ResourceCollection
from constants import JOB_FAMILY_JSON_FIELD_NAME, JOB_LEVEL_JSON_FIELD_NAME
from dataframe_conversion.conversion_constants import (
    QUANTITY_DATAFRAME_COLUMN_NAME,
    RESOURCE_TYPE_DATAFRAME_COLUMN_NAME,
)


class ResourceCollectionConverter(DataFrameConverterBase):
    @staticmethod
    @reset_dataframe_index
    def convert_to_dataframe(resource_collection: ResourceCollection) -> DataFrame:
        dataframe_list: List[DataFrame] = list()
        for resource_type, quantity in resource_collection.resource_quantity_dict.items():
            data: Dict[str, list] = {
                QUANTITY_DATAFRAME_COLUMN_NAME: [quantity],
                RESOURCE_TYPE_DATAFRAME_COLUMN_NAME: [resource_type.resource_type_str],
                JOB_FAMILY_JSON_FIELD_NAME: [resource_type.job_family.name],
            }
            if resource_type.job_level is not None:
                data[JOB_LEVEL_JSON_FIELD_NAME] = [resource_type.job_level.name]
            dataframe_list.append(DataFrame(data=data))

        if dataframe_list:
            return concat(dataframe_list)
        else:
            return DataFrame()
