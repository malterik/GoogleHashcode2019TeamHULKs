import typing

from slideshow import Slideshow
from picture import Picture
from slide import Slide


class Creator:

    def __init__(self, slideshow: Slideshow):
        self.slideshow = slideshow
        self.current_slide = 0
        self.tag_sets : typing.Dict[str, set] = {}

    def choose_next(self):
        pass

    def add_picture_to_sets(self, picture: Picture):
        for tag in picture.tags:
            if tag not in self.tag_sets:
                self.add_set(tag)
            self.tag_sets[tag].add(picture)

    def add_set(self, tag: str):
        self.tag_sets[tag] = set()


