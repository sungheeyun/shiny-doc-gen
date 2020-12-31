from enum import Enum


class JobFamily(Enum):
    PM = 1
    ML_AS = 2
    CV_AS = 3
    OPT_AS = 4
    SWE = 5


class JobLevel(Enum):
    JUNIOR = 1
    SENIOR = 2
