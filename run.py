#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os


import parser
from creator import Creator
from slideshow import Slideshow


def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Runs the hashcode solution",
                                         formatter_class=argparse.RawTextHelpFormatter)

    total_score = 0
    # arg_parser.add_argument("", help="Strategy name")
    solution_path = "./solutions/"

    for filename in os.listdir("./problems"):
        slideshow = Slideshow()
        creator = Creator(slideshow)

        print("Load problem {}".format(filename))
        pictures = parser.load_data("./problems/" + filename)

        print("Add pictures to their sets")
        for pic in pictures:
            creator.add_picture_to_sets(pic)

        creator.fill_slideshow()

        solution = parser.create_solution_file(slideshow, solution_path + filename[:-4] + "_solution.txt")


if __name__ == '__main__':
    main()
