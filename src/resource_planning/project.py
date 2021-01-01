class Project:
    """
    Project class containing the name and the description.
    """

    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description
