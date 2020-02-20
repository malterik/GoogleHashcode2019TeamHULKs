#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import numpy as np
import typing as ty

import parser
from problem import *
from solution import *


class ScanningLibrary:
    books_to_scan: ty.List[int] = []
    books_per_day: int = 0

    def __init__(self, books_to_scan: ty.List[int], books_per_day: int):
        self.books_to_scan = books_to_scan
        self.books_per_day = books_per_day


class SimulationState:
    active_sign_up_id: int = None
    active_sign_up_remaining: int = 0
    scanning_libraries: ty.List[ScanningLibrary] = []


def score_solution(solution: Solution, problem: Problem):
    current_sign_up = None
    total_score = 0
    signed_up_counter = 0
    google_library = [False] * len(problem.book_scores)
    sim_state = SimulationState()
    for t in range(0, problem.number_of_days):
        if sim_state.active_sign_up_remaining == 0:
            if sim_state.active_sign_up_id is not None:
                books_to_scan = list(solution.libraries[signed_up_counter].books_to_scan)
                books_per_day = problem.libraries[solution.libraries[signed_up_counter].id].books_per_day
                sim_state.scanning_libraries.append(
                    ScanningLibrary(books_to_scan, books_per_day))
                signed_up_counter += 1
            if signed_up_counter < len(solution.libraries):
                sim_state.active_sign_up_id = solution.libraries[signed_up_counter].id
                sim_state.active_sign_up_remaining = problem.libraries[
                    sim_state.active_sign_up_id].days_to_sign_up - 1
            else:
                sim_state.active_sign_up_remaining = None
        elif sim_state.active_sign_up_remaining is not None:
            sim_state.active_sign_up_remaining -= 1
        for lib in sim_state.scanning_libraries:
            for i in range(0, lib.books_per_day):
                if len(lib.books_to_scan) > 0:
                    book_id = lib.books_to_scan.pop(0)
                    google_library[book_id] = True
    for id, scanned in enumerate(google_library):
        if scanned:
            total_score += problem.book_scores[id]

            # computing the total score of this solution
    return total_score


def main():
    "Implement direct scoring"


if __name__ == "__main__":
    main()
