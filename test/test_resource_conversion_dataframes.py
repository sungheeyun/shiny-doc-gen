from typing import List, Dict, Any
import unittest
import os
import json

from pandas import DataFrame

from human_resource.resource_collection import ResourceCollection
from human_resource.data_frame_conversion.resource_collection_converter import ResourceCollectionConverter


DATA_DIR: str = os.path.join(os.curdir, "data")
RESOURCE_COLLECTION_TEST_DATA_JSON_FILE_PATH: str = os.path.join(DATA_DIR, "resource_collection_list.json")


class TestResourceConversionDataframes(unittest.TestCase):
    resource_collection_json_data_list: List[List[Dict[str, Any]]] = list()

    @classmethod
    def setUpClass(cls) -> None:
        with open(RESOURCE_COLLECTION_TEST_DATA_JSON_FILE_PATH) as fid:
            cls.resource_collection_json_data_list = json.load(fid)

    def test_resource_collection_conversion(self) -> None:
        for resource_collection_json_data in TestResourceConversionDataframes.resource_collection_json_data_list:
            resource_collection: ResourceCollection = ResourceCollection.create_from_json_data(
                resource_collection_json_data
            )
            resource_collection_dataframe: DataFrame = ResourceCollectionConverter.convert_to_dataframe(
                resource_collection
            )
            resource_collection_dataframe  # TODO MED insert assertions comparing with DataFrames


if __name__ == "__main__":
    unittest.main()
