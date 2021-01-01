from enum import Enum

from utils import classproperty


QUANTITY_JSON_FIELD_NAME: str = "quantity"


class JobFamily(Enum):
    PM = 1
    ML_AS = 2
    CV_AS = 3
    OPT_AS = 4
    SWE = 5

    @classproperty
    def json_field_name(cls) -> str:
        return "job_family"


class JobLevel(Enum):
    JUNIOR = 1
    SENIOR = 2

    @classproperty
    def json_field_name(cls) -> str:
        return "job_level"
