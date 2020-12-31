class Period:
    """
    Quater-Year. Examples are
    - Q1-2020
    - Q3-2021
    """

    def __init__(self, year: int, quarter: int) -> None:
        self.year: int = year
        self.quarter: int = quarter
