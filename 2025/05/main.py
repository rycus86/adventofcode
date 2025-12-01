from shared.utils import *


class Day05(Solution):
    ranges: list[tuple[int, int]]
    ingredients: list[int]

    def setup(self):
        self.ranges = list()
        self.ingredients = list()

        for line in self.input_lines():
            if not line:
                continue
            elif '-' in line:
                l, r = map(int, line.split('-'))
                self.ranges.append((l, r))
            else:
                self.ingredients.append(int(line))


    def part_1(self):
        for i in self.ingredients:
            for l, r in self.ranges:
                if l <= i <= r:
                    self.add_result(1)
                    break

    class Range:
        def __init__(self, left, right):
            self.left = left
            self.right = right
            if left > right:
                raise ValueError(f'{left} > {right}')

        def __repr__(self):
            return f'[{self.left}-{self.right}]'

        def __len__(self):
            return self.right - self.left + 1

        def overlaps(self, other: 'Day05.Range'):
            if other.right < self.left:
                return False
            elif other.left > self.right:
                return False
            else:
                return True

        def merge(self, other: 'Day05.Range'):
            self.left = min(self.left, other.left)
            self.right = max(self.right, other.right)

    def part_2(self):
        remaining_ranges = list(Day05.Range(l, r) for l, r in self.ranges)

        current_ranges = list()
        progressing = True

        while progressing:
            progressing = False

            for current in remaining_ranges:
                for r in current_ranges:
                    if current.overlaps(r):
                        r.merge(current)
                        progressing = True
                        break
                else:
                    current_ranges.append(current)

            if progressing:
                remaining_ranges = current_ranges
                current_ranges = list()

        return sum(len(r) for r in current_ranges)


Day05(__file__).solve()
