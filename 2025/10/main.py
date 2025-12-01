from shared.utils import *

import math
import re


class Machine:
    lights: int
    buttons: list[int]
    button_indexes: tuple[tuple[int, ...], ...]
    joltages: tuple[int, ...]

    row_pattern = re.compile(r'^\[(.+)] (\(.+\)) \{(.+)}')

    def __init__(self, line):
        m = self.row_pattern.match(line)
        self.lights = sum(2**i if l == '#' else 0 for i, l in enumerate(m.group(1)))
        btn = m.group(2).split(' ')
        self.buttons = list(sum(map(lambda x: 2**int(x), b[1:-1].split(','))) for b in btn)
        self.button_indexes = tuple(tuple(map(int, b[1:-1].split(','))) for b in btn)
        self.joltages = tuple(map(int, m.group(3).split(',')))

    def __repr__(self):
        return f'M{self.lights} {self.buttons}{self.button_indexes} {{{self.joltages}}}'

    def solve_part1(self) -> int:
        iterations = list()
        for b in self.buttons:
            iterations.append((0, b, 0))

        states_tried = set()

        while iterations:
            pushes, button, state = iterations.pop(0)
            pushes, new_state = pushes + 1, state ^ button
            if new_state == self.lights:
                return pushes
            else:
                for b in self.buttons:
                    k = (new_state, b)
                    if k not in states_tried:
                        states_tried.add(k)
                        iterations.append((pushes, b, new_state))

        return -1

    def solve_using_scipy(self) -> int:
        # based on https://github.com/jad2192/advent_of_code_2025/blob/main/aoc2025/day10.py
        import numpy as np
        from scipy.optimize import linprog

        buttons = list(list(1 if idx in b else 0 for idx in range(len(self.joltages))) for b in self.button_indexes)

        # The coefficients of the linear objective function to be minimized.
        c = [1] * len(buttons)
        # The equality constraint matrix. Each row of A_eq specifies the coefficients of a linear equality constraint on x.
        a_eq = np.array(buttons).T
        # The equality constraint vector. Each element of A_eq @ x must equal the corresponding element of b_eq.
        b_eq = self.joltages
        # Linear programming: minimize a linear objective function subject to linear equality and inequality constraints.
        return int(linprog(c=c, A_eq=a_eq, b_eq=b_eq, integrality=c).fun)

    def solve_part2(self) -> int:
        # this is too slow unfortunately :(
        return self.try_combinations(tuple(sorted(self.button_indexes, key=lambda i: len(i), reverse=True)), self.joltages)

    def try_combinations(self, available_buttons: tuple[tuple[int, ...]], remaining_joltages: tuple[int, ...]):
        button, remaining_buttons = available_buttons[0], available_buttons[1:]
        start, l = min(remaining_joltages[idx] for idx in button), len(remaining_joltages)
        min_combinations, target = math.inf, (0,) * len(self.joltages)
        while start >= 0:
            jj = tuple(remaining_joltages[idx] - start * (1 if idx in button else 0) for idx in range(l))
            if jj == target:
                return start
            if not len(remaining_buttons):
                break
            min_combinations = min(min_combinations, start + self.try_combinations(remaining_buttons, jj))
            start = min(start - 1, min_combinations)

        return min_combinations


class Day10(Solution):
    machines: list[Machine]

    def setup(self):
        self.machines = list(map(Machine, self.input_lines()))

    def part_1(self):
        for m in self.machines:
            min_pushes = m.solve_part1()
            self.add_result(min_pushes)

    def part_2(self):
        for m in self.machines:
            # this was too slow unfortunately, used Reddit answers to find the Linear Algebra solution
            # min_pushes = m.solve_part2()
            min_pushes = m.solve_using_scipy()
            self.add_result(min_pushes)


Day10(__file__).solve()
