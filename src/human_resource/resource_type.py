from typing import Optional, Dict
from human_resource.enums import JobFamily, JobLevel


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

    def to_data(self) -> Dict[str, str]:
        data: Dict[str, str] = dict(job_family=self.job_family.name)
        if self.job_level is not None:
            data.update(job_level=self.job_level.name)
        return data
