from typing import List, Dict, Any
import unittest
import os
import json

from pandas import DataFrame

from human_resource.resource_collection import ResourceCollection
from human_resource.resource_in_time import ResourceInTime
from human_resource.data_frame_conversion.resource_collection_converter import ResourceCollectionConverter
from human_resource.data_frame_conversion.resource_in_time_converter import ResourceInTimeConverter


DATA_DIR: str = os.path.join(os.curdir, "data")
RESOURCE_COLLECTION_TEST_DATA_JSON_FILE_PATH: str = os.path.join(DATA_DIR, "resource_collection_list.json")
RESOURCE_IN_TIME_TEST_DATA_JSON_FILE_PATH: str = os.path.join(DATA_DIR, "resource_in_time_list.json")


class TestResourceConversionDataframes(unittest.TestCase):
    resource_collection_json_data_list: List[List[Dict[str, Any]]] = list()
    resource_in_time_json_data_list: List[List[Dict[str, Any]]] = list()

    @classmethod
    def setUpClass(cls) -> None:
        with open(RESOURCE_COLLECTION_TEST_DATA_JSON_FILE_PATH) as fid:
            cls.resource_collection_json_data_list = json.load(fid)

        with open(RESOURCE_IN_TIME_TEST_DATA_JSON_FILE_PATH) as fid:
            cls.resource_in_time_json_data_list = json.load(fid)

    def test_resource_collection_conversion(self) -> None:
        for resource_collection_json_data in TestResourceConversionDataframes.resource_collection_json_data_list:
            resource_collection: ResourceCollection = ResourceCollection.create_from_json_data(
                resource_collection_json_data
            )
            resource_collection_dataframe: DataFrame = ResourceCollectionConverter.convert_to_dataframe(
                resource_collection
            )
            resource_collection_dataframe  # TODO MED insert assertions comparing with DataFrames

    def test_resource_in_time_conversion(self) -> None:
        for resource_in_time_json_data in TestResourceConversionDataframes.resource_in_time_json_data_list:
            resource_in_time: ResourceInTime = ResourceInTime.create_from_json_data(resource_in_time_json_data)
            resource_in_time_dataframe: DataFrame = ResourceInTimeConverter.convert_to_dataframe(resource_in_time)
            resource_in_time_dataframe


if __name__ == "__main__":
    unittest.main()
