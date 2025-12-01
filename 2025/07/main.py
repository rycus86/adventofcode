from shared.utils import *
from functools import cache


class Day07(Solution):
    grid: Grid

    def setup(self):
        self.grid = self.input_grid()

    def part_1(self):
        sx, sy = self.grid.locate('S')
        assert self.grid.get(sx, sy + 1) == '.'
        self.grid.set_inplace(sx, sy+1, '|')

        for ri, row in enumerate(self.grid.rows[1:]):
            y = ri + 1
            for x in range(self.grid.width):
                value = self.grid.get(x, y)
                if value == '^' and self.grid.get(x, y-1) in '|S':
                    # split, mark the new beams, and set the splitter as visited: '*'
                    self.grid.set_inplace(x-1, y, '|')
                    self.grid.set_inplace(x+1, y, '|')
                    self.grid.set_inplace(x, y, '*')
                elif value == '.' and self.grid.get(x, y-1) in '|S':
                    self.grid.set_inplace(x, y, '|')

        # count the number of visited splitters
        return sum(1 for _ in self.grid.locate_all('*'))

    def part_2(self):
        sx, sy = self.grid.locate('S')
        return self.count_timelines(sx, sy)

    @cache
    def count_timelines(self, x, y):
        if y + 1 == self.grid.height:
            return 1

        v = self.grid.get(x, y+1)
        if v == '^':
            return self.count_timelines(x-1, y+1) + self.count_timelines(x+1, y+1)
        else:
            return self.count_timelines(x, y+1)


Day07(__file__).solve()
