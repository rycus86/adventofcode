from shared.utils import *


class Day04(Solution):
    grid: Grid

    def setup(self):
        self.grid = self.input_grid()

    def part_1(self):
        for x, y in self.grid.locate_all('@'):
            if list(self.grid.nearby_cells(x, y, include_diagonals=True).values()).count('@') < 4:
                self.add_result()


    def part_2(self):
        making_progress = True
        while making_progress:
            making_progress = False

            for x, y in self.grid.locate_all('@'):
                if list(self.grid.nearby_cells(x, y, include_diagonals=True).values()).count('@') < 4:
                    self.grid.set(x, y, '.')
                    self.add_result()
                    making_progress = True


Day04(__file__).solve()
