from __future__ import annotations
from typing import Any, List, Dict, Set

from json_value_base_class import JsonValueBaseClass
from resource_planning.project import Project
from human_resource.resource_in_time import ResourceInTime


class ResourcePlanner(JsonValueBaseClass):
    """
    Resource planner containing resource current and required resource for each project
    in quarterly time frame.
    """

    def json_field_name(cls) -> str:
        assert False

    def __init__(self) -> None:
        self.project_resource_plan_list: List[Dict[str, Any]] = list()
        self.project_name_set: Set[str] = set()

    def add_project_resource_plan(
        self, project: Project, current_resource: ResourceInTime, required_resource: ResourceInTime
    ) -> None:
        assert project.name not in self.project_name_set, (self.project_name_set, project.name)
        self.project_name_set.add(project.name)
        self.project_resource_plan_list.append(
            dict(project=project, current_resource=current_resource, required_resource=required_resource)
        )

    def to_json_data(self) -> Any:
        project_resource_plan_json_data_list: List[Dict[str, Any]] = list()
        for project_resource_plan_dict in self.project_resource_plan_list:
            project: Project = project_resource_plan_dict["project"]
            project_resource_plan_json_data_list.append(
                dict(
                    project_name=project.name,
                    description=project.description,
                    current_resource=project_resource_plan_dict["current_resource"].to_json_data(),
                    required_resource=project_resource_plan_dict["required_resource"].to_json_data(),
                )
            )

        return dict(project_list=project_resource_plan_json_data_list)

    @staticmethod
    def create_from_json_data(json_data: Any) -> ResourcePlanner:
        resource_planner: ResourcePlanner = ResourcePlanner()

        for project_resource_plan_json_data in json_data["project_list"]:
            project: Project = Project(
                project_resource_plan_json_data["project_name"], project_resource_plan_json_data["description"]
            )
            current_resource: ResourceInTime = ResourceInTime.create_from_json_data(
                project_resource_plan_json_data["current_resource"]
            )
            required_resource: ResourceInTime = ResourceInTime.create_from_json_data(
                project_resource_plan_json_data["required_resource"]
            )

            resource_planner.add_project_resource_plan(project, current_resource, required_resource)

        return resource_planner
