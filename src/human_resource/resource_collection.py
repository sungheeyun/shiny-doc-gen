from __future__ import annotations
from typing import Dict, List, Any
from collections import defaultdict

from utils import classproperty
from json_value_base_class import JsonValueBaseClass
from human_resource.resource_type import ResourceType
from constants import QUANTITY_JSON_FIELD_NAME


class ResourceCollection(JsonValueBaseClass):
    """
    Resource collection. Examples are
    - 1 PM, 3 Senior CV ASs, 2 Junior ML ASs
    - 2 PMs, 3 Junior ML ASs
    """

    @classproperty
    def json_field_name(cls) -> str:
        return "resource_collection"

    def __init__(self) -> None:
        self.resource_quantity_dict: Dict[ResourceType, int] = defaultdict(int)

    def add_resource(self, resource_type: ResourceType, quantity: int) -> None:
        self.resource_quantity_dict[resource_type] += quantity

    def to_json_data(self) -> List[Dict[str, Any]]:
        json_data: List[Dict[str, Any]] = list()
        for resource, quantity in self.resource_quantity_dict.items():
            resource_data: Dict[str, Any] = resource.to_json_data()
            resource_data.update({QUANTITY_JSON_FIELD_NAME: quantity})
            json_data.append(resource_data)

        return json_data

    @staticmethod
    def create_from_json_data(json_data: List[Dict[str, Any]]) -> ResourceCollection:
        resource_collection: ResourceCollection = ResourceCollection()
        for resource_quantity_data in json_data:
            resource_quantity_data_copy: Dict[str, Any] = resource_quantity_data.copy()
            quantity: int = resource_quantity_data_copy.pop(QUANTITY_JSON_FIELD_NAME)
            resource_type: ResourceType = ResourceType.create_from_json_data(resource_quantity_data_copy)
            resource_collection.add_resource(resource_type, quantity)

        return resource_collection
