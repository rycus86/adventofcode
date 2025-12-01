from shared.utils import *


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x},{self.y}'

    def area(self, other: 'Point'):
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)

    def to_area(self, other: 'Point') -> 'Area':
        return Area(self, other)

    def iter_line(self, other: 'Point'):
        if self.x == other.x:
            d = 1 if self.y < other.y else -1
            y = self.y
            while y != other.y:
                yield Point(self.x, y)
                y += d
        else:
            d = 1 if self.x < other.x else -1
            x = self.x
            while x != other.x:
                yield Point(x, self.y)
                x += d


class Area:
    def __init__(self, p1: Point, p2: Point):
        self.x1 = min(p1.x, p2.x)
        self.x2 = max(p1.x, p2.x)
        self.y1 = min(p1.y, p2.y)
        self.y2 = max(p1.y, p2.y)

    def is_strictly_inside(self, item: Point):
        return self.x1 < item.x < self.x2 and self.y1 < item.y < self.y2

    def __repr__(self):
        return f'[{self.x1},{self.y1} x {self.x2},{self.y2}]'


class Day09(Solution):
    tiles: list[Point]

    def setup(self):
        self.tiles = list()
        for line in self.input_lines():
            x, y = map(int, line.split(','))
            self.tiles.append(Point(x, y))

    def part_1(self):
        processed = list()
        largest_area = 0

        for t in self.tiles:
            for p in processed:
                a = t.area(p)
                if a > largest_area:
                    largest_area = a
            processed.append(t)

        return largest_area

    def part_2(self):
        processed = list()
        all_points = set()
        all_rectangles = list()

        prev_t = self.tiles[-1]
        for t in self.tiles:
            all_points.update(prev_t.iter_line(t))
            prev_t = t

            for p in processed:
                a = t.area(p)
                all_rectangles.append((a, t, p))

            processed.append(t)

        for area, p1, p2 in sorted(all_rectangles, key=lambda r: r[0], reverse=True):
            box = p1.to_area(p2)  # type: Area
            if any(box.is_strictly_inside(p) for p in all_points):
                continue

            return area


Day09(__file__).solve()
