from __future__ import annotations
from typing import Optional, Dict

from human_resource.constants import JobFamily, JobLevel


class ResourceType:
    """
    Resource type. Examples are
     - PM
     - Junior ML AS
     - Senior CV AS
    """

    def __init__(self, job_family: JobFamily, job_level: Optional[JobLevel] = None) -> None:
        self.job_family: JobFamily = job_family
        self.job_level: Optional[JobLevel] = job_level

    def to_json_data(self) -> Dict[str, str]:
        json_data: Dict[str, str] = dict(job_family=self.job_family.name)
        if self.job_level is not None:
            json_data.update(job_level=self.job_level.name)
        return json_data

    @staticmethod
    def create_from_json_data(json_data: Dict[str, str]) -> ResourceType:
        job_family: JobFamily = JobFamily[json_data["job_family"]]
        job_level: Optional[JobLevel] = None
        if "job_level" in json_data:
            job_level = JobLevel[json_data["job_level"]]

        return ResourceType(job_family, job_level)
