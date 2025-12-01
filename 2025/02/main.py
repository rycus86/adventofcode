from shared.utils import *

import re


class Day02(Solution):
    ids: list[str]

    def setup(self):
        self.ids = ''.join(self.input_lines()).split(',')

    def part_1(self):
        for i in self.ids:
            left, right = map(int, i.split('-'))
            for n in range(left, right + 1):
                s = str(n)
                if len(s) % 2 == 0:
                    h = len(s) // 2
                    if s[0:h] == s[h:]:
                        self.add_result(n)

    def part_2(self):
        pattern = re.compile(r'^(\d+)\1+$')
        for i in self.ids:
            left, right = map(int, i.split('-'))
            for n in range(left, right + 1):
                s = str(n)
                if pattern.match(s):
                    self.add_result(n)


Day02(__file__).solve()
