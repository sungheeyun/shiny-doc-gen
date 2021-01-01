from typing import Dict, List

from pandas import DataFrame, concat

from human_resource.data_frame_conversion.dataframe_converter_base import DataFrameConverterBase
from human_resource.data_frame_conversion.decorators import reset_dataframe_index
from human_resource.resource_collection import ResourceCollection
from human_resource.constants import JobFamily, JobLevel, QUANTITY_JSON_FIELD_NAME


class ResourceCollectionConverter(DataFrameConverterBase):
    @staticmethod
    @reset_dataframe_index
    def convert_to_dataframe(resource_collection: ResourceCollection) -> DataFrame:
        dataframe_list: List[DataFrame] = list()
        for resource_type, quantity in resource_collection.resource_quantity_dict.items():
            data: Dict[str, list] = {
                JobFamily.json_field_name: [resource_type.job_family.name],
                QUANTITY_JSON_FIELD_NAME: [quantity],
            }
            if resource_type.job_level is not None:
                data[JobLevel.json_field_name] = [resource_type.job_level.name]
            dataframe_list.append(DataFrame(data=data))

        return concat(dataframe_list)
