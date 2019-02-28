import typing

from slideshow import Slideshow
from picture import Picture
from slide import Slide


class Creator:

    def __init__(self, slideshow: Slideshow):
        self.slideshow = slideshow
        self.current_slide = None
        self.tag_sets : typing.Dict[str, set] = {
                "horizontal": set(),
                "vertical": set()
                }

    def choose_next(self):
        pass

    def add_picture_to_sets(self, picture: Picture):
        for tag in picture.tags:
            if tag not in self.tag_sets:
                self.add_set(tag)
            self.tag_sets[tag].add(picture)
        if picture.isHorizontal:
            self.tag_sets["horizontal"].add(picture)
        else:
            self.tag_sets["vertical"].add(picture)

    def add_set(self, tag: str):
        self.tag_sets[tag] = set()

    def delete_odd_vertical(self):
        if len(self.tag_sets["vertical"]) % 2:
            pic = self.tag_sets["vertical"].pop()
            pic.pop_from_all_sets(self.tag_sets)

    def create_first_slide(self):
        self.delete_odd_vertical()
        current_pic = None
        if len(self.tag_sets["horizontal"]):
            current_pic = self.tag_sets["horizontal"].pop()
        else:
            current_pic = self.tag_sets["vertical"].pop()

        current_pic.pop_from_all_sets(self.tag_sets)

        current_slide = Slide()

        if current_pic.isHorizontal:
            current_slide.add_picture(current_pic)
        else:
            current_slide.add_picture(current_pic)
            second_image = self.tag_sets["vertical"].pop()
            second_image.pop_from_all_sets(self.tag_sets)
            current_slide.add_picture(second_image)

        self.current_slide = current_slide
        self.slideshow.add_slide(current_slide)
        print("created first slide")

    def fill_slideshow(self):
        counter = 1000
        while (len(self.tag_sets["horizontal"].union(self.tag_sets["vertical"]))) and counter > 0:
            print(len(self.tag_sets["horizontal"].union(self.tag_sets["vertical"])))
            # counter = counter - 1
            union = set()

            if self.current_slide.picture1 is not None:
                for tag in self.current_slide.picture1.tags:
                    if len(union):
                        break
                    union = self.tag_sets[tag].union(union)
            if self.current_slide.picture2 is not None:
                for tag in self.current_slide.picture2.tags:
                    if len(union):
                        break
                    union = self.tag_sets[tag].union(union)

            if len(union) == 0:
                return
            next_pic = union.pop()
            next_pic.pop_from_all_sets(self.tag_sets)

            next_slide = Slide()
            next_slide.add_picture(next_pic)

            if not next_pic.isHorizontal:
                second_image = self.tag_sets["vertical"].pop()
                second_image.pop_from_all_sets(self.tag_sets)
                next_slide.add_picture(second_image)

            self.slideshow.add_slide(next_slide)
            self.current_slide = next_slide



