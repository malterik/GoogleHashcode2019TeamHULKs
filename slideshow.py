from picture import Picture
from slide import Slide


class Slideshow:

    def __init__(self, slides = None):
        if slides is not None:
            self.slides = sides
        else:
            self.slides = []

    def add_slide(self, slide: Slide):
        self.slides.append(slide)

    def lenght(self):
        return len(self.slides)

