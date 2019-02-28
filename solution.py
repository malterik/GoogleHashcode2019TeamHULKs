from slideshow import Slideshow
from slide import Slide
import numpy as np
def score_solution(slideshow, input_data):
    print(input_data)
    total_score = 0
    for i,slide in enumerate(slideshow.slides):
        p1_tags=[]
        p2_tags=[]
        if slide.picture2 == None: # horizontal image
            p1_tags = input_data[slide.picture1].tags
        else:
            p1_tags = list(set(input_data[slide.picture1].tags + input_data[slide.picture2].tags))

        if i + 1 < len(slideshow.slides):
            slide2 = slideshow.slides[i + 1]
            if slide2.picture2 == None: # horizontal image
                p2_tags = input_data[slide2.picture1].tags
            else:
                p2_tags = list(set(input_data[slide2.picture1].tags + input_data[slide2.picture2].tags))
        else:
            continue
        print("p1_tags")
        print(p1_tags)
        print("p2_tags")
        print(p2_tags)
        common_tags = len(list(set(p1_tags).intersection(p2_tags)))
        tags_in_1 = len(np.setdiff1d(p1_tags, p2_tags))
        tags_in_2 = len(np.setdiff1d(p2_tags, p1_tags))
        tempscore = min(common_tags, tags_in_1, tags_in_2)

    return total_score

