#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import logging
import glob
import tqdm
import time

import parser
import scoring
from colorlog import ColorLog
from solution import *
from problem import *
from solver_baseline import *

logger = ColorLog()
logger.setLevel(logging.DEBUG)


def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Runs the hashcode solution",
                                         formatter_class=argparse.RawTextHelpFormatter)

    # arg_parser.add_argument("", help="Strategy name")
    arg_parser.add_argument("--solution-path", default="./solutions/")
    arg_parser.add_argument("--problem-path", default="./problems/")

    arg_parser.add_argument(
        "problem", nargs="?", default="*", help="The problem name to score")

    args = arg_parser.parse_args()

    solution_path = args.solution_path
    problem_path = args.problem_path

    total_score = 0

    problem_files = sorted(glob.glob(problem_path + args.problem))

    if not problem_files:
        logger.warning("No problem files found! Exiting...")
        exit(0)

    t = tqdm.tqdm(problem_files, postfix={"last": 0, "total": total_score})
    for filepath in t:
        basename = os.path.splitext(os.path.basename(filepath))[0]
        t.set_description(basename)
        problem_data = parser.load_data(filepath)

        solver_baseline = SolverBaseline(problem_data)
        solution = solver_baseline.solve()
        # compute solution
        libraries = [SolutionEntry(1, 3, [5, 2, 3]), SolutionEntry(0, 5, [0, 1, 2, 3, 4])]
        solution2 = Solution(2, libraries)

        score = scoring.score_solution(solution, problem_data)
        total_score += score
        t.set_postfix(last = score, total = total_score)
        parser.create_solution_file(
            solution, solution_path + basename + "_solution.txt")

    logger.info("Total Score: {}".format(total_score))


if __name__ == '__main__':
    main()
