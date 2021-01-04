from typing import Dict, Any
import os
import json

from resource_planner_outputter import ResourcePlannerOutputter
from resource_planning.resource_planner import ResourcePlanner


DATA_DIR_PATH: str = os.path.join(os.pardir, "data")
GL_STAFFING_PLAN_CONFIG_FILE_PATH: str = os.path.join(DATA_DIR_PATH, "gl_staffing_plan_2021_config.json")


if __name__ == "__main__":
    print(os.getcwd())
    with open(GL_STAFFING_PLAN_CONFIG_FILE_PATH) as fid:
        config_json_data: Dict[str, Any] = json.load(fid)

    data_directory_path: str = config_json_data["data_directory"]

    resource_planner_format_config_file_path: str = os.path.join(
        data_directory_path, config_json_data["format_config_file"]
    )

    with open(resource_planner_format_config_file_path) as fid:
        resource_planner_format_json_data: Any = json.load(fid)

    resource_planner_outputter: ResourcePlannerOutputter = ResourcePlannerOutputter(resource_planner_format_json_data)

    for data_file_name in config_json_data["resource_plan_file_list"]:
        json_data_file_path: str = os.path.join(data_directory_path, data_file_name)

        with open(json_data_file_path) as fid:
            project_planner_json_data: Dict[str, Any] = json.load(fid)

            resource_planner: ResourcePlanner = ResourcePlanner.create_from_json_data(project_planner_json_data)
            (
                per_project_pivot_table_dataframe,
                total_pivot_table_dataframe,
                hiring_pivot_table_dataframe,
            ) = resource_planner_outputter.process(resource_planner)
