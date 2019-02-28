import typing


class Picture:

    def __init__(self, identifier: int, isHorizontal: bool, tags: typing.List):
        self.identifier = identifier
        self.tags = tags
        self.isHorizontal = isHorizontal

    def pop_from_all_sets(self):
        pass


