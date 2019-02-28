from slideshow import Slideshow
from slide import Slide
def score_solution(slideshow):
    total_points = 0
    t = 0
    return total_points

def create_solution_file(slideshow, solution_path):
    file = open(solution_path, "w")
    for slide in slideshow.slides:
        if slide.picture2 == None:
            line = "%d\n" % (slide.picture1)
        else:
            line = "%d %d\n" % (slide.picture1, slide.picture2)
        file.write(line)
    file.close()
    return
