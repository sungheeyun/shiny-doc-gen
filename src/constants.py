from enum import Enum

from utils import classproperty


QUANTITY_JSON_FIELD_NAME: str = "quantity"
JOB_FAMILY_JSON_FIELD_NAME: str = "job_family"
JOB_LEVEL_JSON_FIELD_NAME: str = "job_level"


class JobFamily(Enum):
    PM = 1
    ML_AS = 2
    CV_AS = 3
    OPT_AS = 4
    SWE = 5


class JobLevel(Enum):
    JUNIOR = 1
    SENIOR = 2
