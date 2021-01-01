from typing import List, Dict, Any, Set
import unittest

from human_resource.period import Period
from human_resource.resource_collection import ResourceCollection
from human_resource.resource_in_time import ResourceInTime


class TestResourceInTime(unittest.TestCase):

    resource_in_time_json_data_list: List[List[Dict[str, Any]]] = list()

    @classmethod
    def setUpClass(cls) -> None:
        cls.resource_in_time_json_data_list.append(
            [
                {
                    "period": "Q4-2020",
                    "resource_collection": [
                        {"job_family": "PM", "quantity": 1},
                        {"job_family": "ML_AS", "job_level": "JUNIOR", "quantity": 2},
                    ],
                },
                {
                    "period": "Q1-2021",
                    "resource_collection": [
                        {"job_family": "PM", "quantity": 1},
                        {"job_family": "ML_AS", "job_level": "JUNIOR", "quantity": 3},
                        {"job_family": "ML_AS", "job_level": "SENIOR", "quantity": 1},
                    ],
                },
                {"period": "Q2-2021", "resource_collection": "same"},
                {"period": "Q3-2021", "resource_collection": "same"},
                {"period": "Q4-2021", "resource_collection": "same"},
            ]
        )

        cls.resource_in_time_json_data_list.append(
            [
                {
                    "period": "Q4-2020",
                    "resource_collection": [
                        {"job_family": "PM", "quantity": 1},
                        {"job_family": "ML_AS", "job_level": "JUNIOR", "quantity": 2},
                    ],
                }
            ]
        )

        cls.resource_in_time_json_data_list.append(
            [
                {
                    "period": "Q4-2020",
                    "resource_collection": [
                        {"job_family": "PM", "quantity": 1},
                        {"job_family": "ML_AS", "job_level": "JUNIOR", "quantity": 2},
                    ],
                }
            ]
        )

        cls.resource_in_time_json_data_list.append(
            [
                {
                    "period": "Q1-2021",
                    "resource_collection": [
                        {"job_family": "PM", "quantity": 1},
                        {"job_family": "ML_AS", "job_level": "JUNIOR", "quantity": 3},
                        {"job_family": "ML_AS", "job_level": "SENIOR", "quantity": 1},
                    ],
                },
                {
                    "period": "Q2-2021",
                    "resource_collection": [
                        {"job_family": "PM", "quantity": 1},
                        {"job_family": "ML_AS", "job_level": "JUNIOR", "quantity": 3},
                        {"job_family": "ML_AS", "job_level": "SENIOR", "quantity": 2},
                    ],
                },
                {"period": "Q3-2021", "resource_collection": "same"},
                {"period": "Q4-2021", "resource_collection": "same"},
            ]
        )

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
