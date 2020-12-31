from typing import Dict, List, Any
from collections import defaultdict

from human_resource.resource_type import ResourceType


class ResourceCollection:
    """
    Resource collection. Examples are
    - 1 PM, 3 Senior CV ASs, 2 Junior ML ASs
    - 2 PMs, 3 Junior ML ASs
    """
    def __init__(self) -> None:
        self.resource_quantity_dict: Dict[ResourceType, int] = defaultdict(int)

    def add_resource(self, resource_type: ResourceType, quantity: int) -> None:
        self.resource_quantity_dict[resource_type] += quantity

    def to_data(self) -> List[Dict[str, Any]]:
        data: List[Dict[str, Any]] = list()
        for resource, quantity in self.resource_quantity_dict.items():
            resource_data: Dict[str, Any] = resource.to_data()
            resource_data.update(quantity=quantity)
            data.append(resource_data)

        return data
