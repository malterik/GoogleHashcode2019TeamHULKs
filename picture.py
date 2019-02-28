import typing


class Picture:

    def __init__(self, identifier: int, isHorizontal: bool, tags: typing.List):
        self.identifier = identifier
        self.tags = tags
        self.isHorizontal = isHorizontal

    def __repr__(self):
        return '\n' + str(self.identifier) + ', ' + str(self.isHorizontal) + ', ' + str(self.tags)

    def pop_from_all_sets(self, tag_sets: typing.Dict):
        #remove self from tag sets
        for tag in self.tags:
            tag_sets[tag].discard(self)
        #remove self from hori
        tag_sets['horizontal'].discard(self)
        tag_sets['vertical'].discard(self)



