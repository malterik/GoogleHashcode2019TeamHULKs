#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from parser import IO
from solution import create_solution_file
from slideshow import Slideshow
from slide import Slide
#  from simulate import score_solution


def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Scores the HashCode solution for the given problem",
                                         formatter_class=argparse.RawTextHelpFormatter)
    arg_parser.add_argument("problem", help="The problem file")
    arg_parser.add_argument("solution", help="The solution file")
    args = arg_parser.parse_args()
    problem_path = args.problem
    solution_path = args.solution
    
    reader = IO()
    data = reader.load_data(problem_path)
    print(data)
    s = Slideshow()
    slide1 = Slide()
    slide1.picture1 = 1
    slide2 = Slide()
    slide2.picture1 = 0
    slide2.picture2 = 2
    s.add_slide(slide1)
    s.add_slide(slide2)
    solution = create_solution_file(s, solution_path)

    print(solution)



if __name__ == '__main__':
    main()
