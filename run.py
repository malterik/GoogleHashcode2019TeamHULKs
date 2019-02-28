#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os


import parser
from creator import Creator
from Slideshow import Slideshow


def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Runs the hashcode solution",
                                         formatter_class=argparse.RawTextHelpFormatter)

    total_score = 0
    arg_parser.add_argument("strategy_name", help="Strategy name")

    slideshow = Slideshow()
    creator = Creator(slideshow)

    for filename in os.listdir("./problems"):
        print("Load problem {}".format(filename))
        pictures = parser.load_data(filename)

        print("Add pictures to their sets")
        for pic in pictures:
            creator.add_picture_to_sets(pic)



    #     args = arg_parser.parse_args()
    #     strategy_name = args.strategy_name

    #     city = load_problem("./problems/%s" % filename)
    #     solution = strategies.__dict__[strategy_name](city)

    #     score = score_solution(solution)
    #     print("Score %s: %s" % (filename, score))
    #     save_solution("./solutions/%s_%s.out" % (filename, strategy_name), solution)
    #     total_score = total_score + score

    # print("TotalScore: %s" % total_score)

if __name__ == '__main__':
    main()
