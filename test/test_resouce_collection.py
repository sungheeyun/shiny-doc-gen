import unittest
from typing import List, Dict, Any
import json
import os

from human_resource.resource_collection import ResourceCollection


DATA_DIR: str = os.path.join(os.curdir, "data")
TEST_DATA_JSON_FILE_PATH: str = os.path.join(DATA_DIR, "resource_collection_list.json")


class TestResourceCollection(unittest.TestCase):

    resource_collection_json_data_list: List[List[Dict[str, Any]]] = list()

    @classmethod
    def setUpClass(cls) -> None:
        with open(TEST_DATA_JSON_FILE_PATH) as fid:
            cls.resource_collection_json_data_list = json.load(fid)

    def test_simple_resource_collection(self) -> None:
        for resource_collection_data in TestResourceCollection.resource_collection_json_data_list:
            resource_collection: ResourceCollection = ResourceCollection.create_from_json_data(resource_collection_data)
            self.assertEqual(resource_collection.to_json_data(), resource_collection_data)


if __name__ == "__main__":
    unittest.main()
