import typing as ty
import numpy as np

from problem import *
from solution import *


class SolverState:
    passed_days = 0
    average_lib_value = 0
    beta = 1.3


def book_to_end_of_days(s_state: SolverState, library: Library, problem: Problem) -> int:
    d_hat = problem.number_of_days - s_state.passed_days - library.days_to_sign_up
    return min(library.books_per_day * d_hat, len(library.books))



def estimated_lib_value(s_state: SolverState, library: Library, problem: Problem) -> float:
    K = book_to_end_of_days(s_state, library, problem)
    if K == 0:
        return 0
    # value of best k books
    B = library.books[:K]
    V_hat = sum([problem.book_scores[book_id] for book_id in B])
    if V_hat == 0:
        return 0
    # opportuniy_cost
    op_cost = library.days_to_sign_up * s_state.average_lib_value / K * s_state.beta
    return V_hat - op_cost


def solve(problem: Problem) -> Solution:
    solution = Solution(0, [])
    s_state = SolverState()
    unreg_libs: ty.List[Library] = problem.libraries.copy()

    s_state.average_lib_value = np.mean(problem.book_scores)

    while problem.number_of_days - s_state.passed_days >= 0 and len(unreg_libs) > 0:
        i_star = np.argmax([estimated_lib_value(s_state, lib, problem) for lib in unreg_libs])
        lib_star = unreg_libs[i_star]
        # TODO: This is redundant
        K = book_to_end_of_days(s_state, lib_star, problem)
        # value of best k books
        B = lib_star.books[:K]

        s_state.passed_days += lib_star.days_to_sign_up
        # TODO: update average_lib_value
        unreg_libs.pop(i_star)
        for book in B:
            problem.book_scores[book] = 0
        #for lib in unreg_libs:
            #lib.books = list(np.setdiff1d(lib.books, B))
        print("Adding id: {} {} {}".format(lib_star.id, len(B), B))
        solution.libraries.append(SolutionEntry(lib_star.id, len(B), B))
        solution.number_of_libraries += 1
    return solution


