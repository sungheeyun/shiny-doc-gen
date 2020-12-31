import unittest

from human_resource.resource_collection import ResourceCollection
from human_resource.resource_type import ResourceType
from human_resource.enums import JobFamily, JobLevel


class TestResourceCollection(unittest.TestCase):
    def test_simple_resource_collection(self) -> None:
        resource_collection: ResourceCollection = ResourceCollection()

        resource_collection.add_resource(ResourceType(JobFamily.PM), 1)
        resource_collection.add_resource(
            ResourceType(JobFamily.ML_AS, JobLevel.JUNIOR), 2
        )
        resource_collection.add_resource(
            ResourceType(JobFamily.CV_AS, JobLevel.SENIOR), 1
        )

        self.assertEqual(
            resource_collection.to_data(),
            [
                {"job_family": "PM", "quantity": 1},
                {"job_family": "ML_AS", "job_level": "JUNIOR", "quantity": 2},
                {"job_family": "CV_AS", "job_level": "SENIOR", "quantity": 1},
            ],
        )


if __name__ == "__main__":
    unittest.main()
