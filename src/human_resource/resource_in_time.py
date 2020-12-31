from typing import Dict

from human_resource.resource_collection import ResourceCollection
from human_resource.period import Period


class ResourceInTime:
    """
    Contains how much resource are required (or acquired) for each period.
    """

    def __init__(self) -> None:
        self.period_resource_collection_dict: Dict[Period, ResourceCollection] = dict()

    def add_resource_collection(self, period: Period, resource_collection: ResourceCollection) -> None:
        assert period not in self.period_resource_collection_dict
        self.period_resource_collection_dict[period] = resource_collection
