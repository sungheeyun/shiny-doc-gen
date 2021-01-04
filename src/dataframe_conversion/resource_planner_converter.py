from typing import List

from pandas import DataFrame, concat

from dataframe_conversion.dataframe_converter_base import DataFrameConverterBase
from dataframe_conversion.decorators import reset_dataframe_index
from dataframe_conversion.resource_in_time_converter import ResourceInTimeConverter
from dataframe_conversion.conversion_constants import (
    RESOURCE_STATUS_DATAFRAME_COLUMN_NAME,
    PROJECT_DATAFRAME_COLUMN_NAME,
)
from human_resource.resource_in_time import ResourceInTime
from resource_planning.resource_planner import ResourcePlanner
from resource_planning.project import Project


class ResourcePlannerConverter(DataFrameConverterBase):
    @staticmethod
    @reset_dataframe_index
    def convert_to_dataframe(resource_planner: ResourcePlanner) -> DataFrame:
        dataframe_list: List[DataFrame] = list()
        for project_resource_plan_dict in resource_planner.project_resource_plan_list:
            project: Project = project_resource_plan_dict["project"]
            current_resource: ResourceInTime = project_resource_plan_dict["current_resource"]
            required_resource: ResourceInTime = project_resource_plan_dict["required_resource"]

            current_resource_dataframe: DataFrame = ResourceInTimeConverter.convert_to_dataframe(current_resource)
            required_resource_dataframe: DataFrame = ResourceInTimeConverter.convert_to_dataframe(required_resource)

            assert RESOURCE_STATUS_DATAFRAME_COLUMN_NAME not in current_resource_dataframe.columns
            assert RESOURCE_STATUS_DATAFRAME_COLUMN_NAME not in required_resource_dataframe.columns

            current_resource_dataframe[RESOURCE_STATUS_DATAFRAME_COLUMN_NAME] = "current"
            required_resource_dataframe[RESOURCE_STATUS_DATAFRAME_COLUMN_NAME] = "required"

            project_resource_plan_dataframe: DataFrame = concat(
                (current_resource_dataframe, required_resource_dataframe)
            )

            assert PROJECT_DATAFRAME_COLUMN_NAME not in project_resource_plan_dataframe.columns
            project_resource_plan_dataframe[PROJECT_DATAFRAME_COLUMN_NAME] = project.name

            dataframe_list.append(project_resource_plan_dataframe)

        return concat(dataframe_list)
