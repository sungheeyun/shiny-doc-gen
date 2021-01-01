from typing import Any
import unittest
import os
import json

from resource_planning.resource_planner import ResourcePlanner


DATA_DIR: str = os.path.join(os.curdir, "data")
TEST_DATA_JSON_FILE_PATH: str = os.path.join(DATA_DIR, "resource_plan.json")


class TestResourcePlanner(unittest.TestCase):
    resource_plan_json_data_list: list = list()

    @classmethod
    def setUpClass(cls) -> None:
        with open(TEST_DATA_JSON_FILE_PATH) as fid:
            json_data: Any = json.load(fid)

        cls.resource_plan_json_data_list.append(json_data)

    def setUp(self) -> None:
        self.maxDiff = None

    def test_resource_plan(self) -> None:
        for resource_plan_json_data in TestResourcePlanner.resource_plan_json_data_list:
            resource_planner: ResourcePlanner = ResourcePlanner.create_from_json_data(resource_plan_json_data)
            new_resource_plan_json_data: Any = resource_planner.to_json_data()
            new_resource_plan_json_data
            # self.assertEqual(new_resource_plan_json_data, resource_plan_json_data)


if __name__ == '__main__':
    unittest.main()
