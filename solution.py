from slideshow import Slideshow
from slide import Slide
def score_solution(slideshow):
    total_points = 0
    t = 0
    return total_points

def create_solution_file(slideshow, solution_path):
    file = open(solution_path, "w")
    for slide in slideshow.slides:
        if slide.Picture2 == none:
            line = "%d\n" % (slide.Picture1)
        else:
            line = "%d %d\n" % (slide.Picture1, slide.Picture2)
        file.write(line)
    file.close()
    return
