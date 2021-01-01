from __future__ import annotations
from typing import Match
import re

from utils import classproperty
from human_resource.base_class import JasonValueBaseClass


class Period(JasonValueBaseClass):
    """
    Quater-Year. Examples are
    - Q1-2020
    - Q3-2021
    """

    @classproperty
    def json_field_name(cls) -> str:
        return "period"

    def __init__(self, year: int, quarter: int) -> None:
        self.year: int = year
        self.quarter: int = quarter

    def __lt__(self, other: Period) -> bool:
        return (self.year, self.quarter) < (other.year, other.quarter)

    def __eq__(self, other) -> bool:
        return (self.year, self.quarter) == (other.year, other.quarter)

    def __hash__(self) -> int:
        return hash((self.year, self.quarter))

    def __repr__(self) -> str:
        return self.to_json_data()

    def to_json_data(self) -> str:
        return f"Q{self.quarter}-{self.year}"

    @staticmethod
    def create_from_json_data(json_data: str) -> Period:
        match: Match = re.match(r"^Q(\d)-(\d\d\d\d)$", json_data)
        assert match is not None

        year: int = int(match.group(2))
        quarter: int = int(match.group(1))

        return Period(year, quarter)
