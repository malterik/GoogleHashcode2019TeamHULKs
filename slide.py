from picture import Picture


class Slide:

    def __init__(self, picture1: Picture = None, picture2: Picture = None):
        self.picture1 = picture1
        self.picture2 = picture2

    def add_picture(self, picture: Picture, position: int = None):
        if position == 1:
            self.picture1 = picture
            return
        elif position == 2:
            self.picture2 = picture
            return

        if self.picture1 is None:
            self.picture1 = picture1
            return
        elif self.picture2 is None:
            self.picture2 = picture2
            return
        raise Exception("No slots empty for picture")

