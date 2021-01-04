from typing import Dict, Any, List, Iterable, Tuple

from numpy import ndarray, diff, hstack
from pandas import DataFrame

from resource_planning.resource_planner import ResourcePlanner
from dataframe_conversion.resource_planner_converter import ResourcePlannerConverter
from dataframe_conversion.conversion_constants import (
    YEAR_DATAFRAME_COLUMN_NAME,
    QUARTER_DATAFRAME_COLUMN_NAME,
    RESOURCE_TYPE_DATAFRAME_COLUMN_NAME,
    QUANTITY_DATAFRAME_COLUMN_NAME,
    PROJECT_DATAFRAME_COLUMN_NAME,
    RESOURCE_STATUS_DATAFRAME_COLUMN_NAME,
)


def get_refined_order_list(order_list: Iterable, item_list: Iterable) -> list:
    unique_order_list = list(dict.fromkeys(order_list))
    unique_item_list = list(dict.fromkeys(item_list))
    return unique_order_list + [x for x in unique_item_list if x not in unique_order_list]


def replace_dataframe_contents(dataframe: DataFrame, contents: ndarray) -> DataFrame:
    return DataFrame(contents, index=dataframe.index, columns=dataframe.columns)


class ResourcePlannerOutputter:
    """
    Outputs the results of the resource planning.
    """

    def __init__(self, format_json_data: Dict[str, Any]) -> None:
        self.format_json_data: Dict[str, Any] = format_json_data

    def process(self, resource_planner: ResourcePlanner) -> Tuple[DataFrame, DataFrame, DataFrame]:
        resource_planner_dataframe: DataFrame = ResourcePlannerConverter.convert_to_dataframe(resource_planner)

        per_project_pivot_table_dataframe: DataFrame = resource_planner_dataframe.pivot_table(
            values=QUANTITY_DATAFRAME_COLUMN_NAME,
            index=[PROJECT_DATAFRAME_COLUMN_NAME, RESOURCE_TYPE_DATAFRAME_COLUMN_NAME],
            columns=[RESOURCE_STATUS_DATAFRAME_COLUMN_NAME, YEAR_DATAFRAME_COLUMN_NAME, QUARTER_DATAFRAME_COLUMN_NAME],
            aggfunc=sum,
            fill_value=0,
        )

        total_pivot_table_dataframe: DataFrame = resource_planner_dataframe.pivot_table(
            values=QUANTITY_DATAFRAME_COLUMN_NAME,
            index=[RESOURCE_TYPE_DATAFRAME_COLUMN_NAME],
            columns=[RESOURCE_STATUS_DATAFRAME_COLUMN_NAME, YEAR_DATAFRAME_COLUMN_NAME, QUARTER_DATAFRAME_COLUMN_NAME],
            aggfunc=sum,
            fill_value=0,
        )

        if "project_order" in self.format_json_data:
            per_project_pivot_table_dataframe = per_project_pivot_table_dataframe.reindex(
                get_refined_order_list(
                    self.format_json_data["project_order"], per_project_pivot_table_dataframe.index.get_level_values(0)
                ),
                level=0,
            )

        if "resource_type_order" in self.format_json_data:
            resource_type_order_list: List[str] = get_refined_order_list(
                self.format_json_data["resource_type_order"], total_pivot_table_dataframe.index
            )

            total_pivot_table_dataframe = total_pivot_table_dataframe.reindex(resource_type_order_list)
            per_project_pivot_table_dataframe = per_project_pivot_table_dataframe.reindex(
                resource_type_order_list, level=1
            )

        total_pivot_table_data_array: ndarray = total_pivot_table_dataframe.to_numpy()
        hiring_pivot_table_dataframe: DataFrame = replace_dataframe_contents(
            total_pivot_table_dataframe,
            hstack(
                (
                    diff(total_pivot_table_data_array[:, [0, -1]], axis=1),
                    diff(total_pivot_table_data_array, axis=1),
                )
            ),
        )

        per_project_pivot_table_dataframe.to_csv("per_project_pivot_table.csv")
        total_pivot_table_dataframe.to_csv("total_pivot_table.csv")
        hiring_pivot_table_dataframe.to_csv("hiring_pivot_table.csv")

        return per_project_pivot_table_dataframe, total_pivot_table_dataframe, hiring_pivot_table_dataframe
