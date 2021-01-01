from typing import List, Dict, Any, Set
import unittest
import json
import os

from human_resource.period import Period
from human_resource.resource_collection import ResourceCollection
from human_resource.resource_in_time import ResourceInTime


DATA_DIR: str = os.path.join(os.curdir, "data")
TEST_DATA_JSON_FILE_PATH: str = os.path.join(DATA_DIR, "resource_in_time_list.json")


class TestResourceInTime(unittest.TestCase):

    resource_in_time_json_data_list: List[List[Dict[str, Any]]] = list()

    @classmethod
    def setUpClass(cls) -> None:
        with open(TEST_DATA_JSON_FILE_PATH) as fid:
            cls.resource_in_time_json_data_list = json.load(fid)

    def test_resource_in_time(self):
        for resource_in_time_json_data in TestResourceInTime.resource_in_time_json_data_list:
            resource_in_time: ResourceInTime = ResourceInTime.create_from_json_data(resource_in_time_json_data)

            skip_period_json_data_set: Set[str] = set()
            skip_resource_in_period_json_data_list: List[Dict[str, Any]] = list()
            for resource_in_period_json_data in resource_in_time_json_data:
                if resource_in_period_json_data[ResourceCollection.json_field_name] == "same":
                    skip_period_json_data_set.add(resource_in_period_json_data[Period.json_field_name])
                    skip_resource_in_period_json_data_list.append(resource_in_period_json_data)

            resource_in_time_json_data_copy = resource_in_time_json_data.copy()
            for skip_resource_in_period_json_data in skip_resource_in_period_json_data_list:
                resource_in_time_json_data_copy.remove(skip_resource_in_period_json_data)

            derived_resource_in_time_json_data: List[Dict[str, Any]] = resource_in_time.to_json_data()
            skip_resource_in_period_json_data_list = list()
            for resource_in_period_json_data in derived_resource_in_time_json_data:
                if resource_in_period_json_data[Period.json_field_name] in skip_period_json_data_set:
                    skip_resource_in_period_json_data_list.append(resource_in_period_json_data)

            for skip_resource_in_period_json_data in skip_resource_in_period_json_data_list:
                derived_resource_in_time_json_data.remove(skip_resource_in_period_json_data)

            self.assertEqual(derived_resource_in_time_json_data, resource_in_time_json_data_copy)

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
