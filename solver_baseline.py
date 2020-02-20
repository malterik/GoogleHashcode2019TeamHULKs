from solution import *
from problem import *
import numpy as np
K = 2

class SolverBaseline():
    def __init__(self, problem : Problem):
        self.problem = problem

    def solve(self):
        solution_entries = []
        number_of_libraries = 0
        sorted_list = sorted(self.problem.libraries, key= lambda library : library.days_to_sign_up)
        for library in sorted_list:
            solution_entries.append(SolutionEntry(library.idx, K, library.books[0:K]))
            number_of_libraries += 1
        return Solution(number_of_libraries, solution_entries)

