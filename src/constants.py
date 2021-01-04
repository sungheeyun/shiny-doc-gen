from enum import Enum, auto

QUANTITY_JSON_FIELD_NAME: str = "quantity"
JOB_FAMILY_JSON_FIELD_NAME: str = "job_family"
JOB_LEVEL_JSON_FIELD_NAME: str = "job_level"


class JobFamily(Enum):
    PM = auto()
    ML_AS = auto()
    CV_AS = auto()
    OPT_AS = auto()
    SWE = auto()
    OP_AS = auto()


class JobLevel(Enum):
    JUNIOR = auto()
    SENIOR = auto()
