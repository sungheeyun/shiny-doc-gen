import unittest
from typing import List, Dict, Any

from human_resource.resource_collection import ResourceCollection


class TestResourceCollection(unittest.TestCase):

    resource_collection_json_data_list: List[List[Dict[str, Any]]] = list()

    @classmethod
    def setUpClass(cls) -> None:
        cls.resource_collection_json_data_list.append(
            [
                {"job_family": "PM", "quantity": 1},
                {"job_family": "ML_AS", "job_level": "JUNIOR", "quantity": 2},
                {"job_family": "CV_AS", "job_level": "SENIOR", "quantity": 1},
            ]
        )

    def test_simple_resource_collection(self) -> None:
        for resource_collection_data in TestResourceCollection.resource_collection_json_data_list:
            resource_collection: ResourceCollection = ResourceCollection.create_from_json_data(resource_collection_data)
            self.assertEqual(resource_collection.to_json_data(), resource_collection_data)


if __name__ == "__main__":
    unittest.main()
