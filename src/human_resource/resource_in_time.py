from __future__ import annotations
from typing import Dict, List, Any, Optional, Union
from copy import copy

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

    def to_json_data(self) -> List[Dict[str, Any]]:
        json_data: List[Dict[str, Any]] = list()
        sorted_period_list: List[Period] = sorted(self.period_resource_collection_dict)
        for period in sorted_period_list:
            resource_collection: ResourceCollection = self.period_resource_collection_dict[period]
            json_data.append(
                {
                    Period.json_field_name: period.to_json_data(),
                    ResourceCollection.json_field_name: resource_collection.to_json_data(),
                }
            )

        return json_data

    @staticmethod
    def create_from_json_data(json_data: List[Dict[str, Any]]) -> ResourceInTime:
        period_data_dict: Dict[Period, List[Dict[str, Any]]] = dict()
        for period_resource_collection_data in json_data:
            assert Period.json_field_name in period_resource_collection_data, list(
                period_resource_collection_data.keys()
            )
            assert ResourceCollection.json_field_name in period_resource_collection_data, (
                ResourceCollection.json_field_name,
                list(period_resource_collection_data.keys()),
            )
            period: Period = Period.create_from_json_data(period_resource_collection_data[Period.json_field_name])

            assert period not in period_data_dict, period
            period_data_dict[period] = period_resource_collection_data[ResourceCollection.json_field_name]

        resource_in_time: ResourceInTime = ResourceInTime()

        sorted_period_list: List[Period] = sorted(period_data_dict.keys())
        previous_resource_collection: Optional[ResourceCollection] = None
        for period in sorted_period_list:
            resource_collection_data: Union[str, List[Dict[str, Any]]] = period_data_dict[period]
            if resource_collection_data == "same":
                assert previous_resource_collection is not None
                resource_collection = copy(previous_resource_collection)
            else:
                resource_collection = ResourceCollection.create_from_json_data(resource_collection_data)
            resource_in_time.add_resource_collection(period, resource_collection)
            previous_resource_collection = resource_collection

        return resource_in_time
