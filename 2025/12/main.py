from shared.utils import *


class Region:
    def __init__(self, width: int, height: int, quantities: list[int]):
        self.width = width
        self.height = height
        self.quantities = quantities

    def size(self):
        return self.width * self.height


class Day12(Solution):
    presents: list[Grid]
    regions: list[Region]

    def setup(self):
        self.presents = list()
        self.regions = list()

        lines = self.input_lines()
        while lines:
            line = lines.pop(0)
            if line.endswith(':'):  # present header
                present = [lines.pop(0), lines.pop(0), lines.pop(0)]
                self.presents.append(Grid(present))
                lines.pop(0)  # empty line
            elif ': ' in line:
                dim, q = line.split(': ')
                w, h = map(int, dim.split('x'))
                self.regions.append(Region(w, h, list(map(int, q.split(' ')))))

    def part_1(self):
        # just check if they can possibly fit
        box_sizes = {idx: sum(1 for _ in p.locate_all('#')) for idx, p in enumerate(self.presents)}
        for region in self.regions:
            total_box_size = sum(q * box_sizes[idx] for idx, q in enumerate(region.quantities))
            if total_box_size <= region.size():
                self.add_result()

    def part_2(self):
        pass  # none :)


Day12(__file__).solve()
