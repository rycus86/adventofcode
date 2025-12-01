from shared.utils import *


class Day01(Solution):
    start: int
    password: int

    def setup(self):
        self.start = 50
        self.password = 0

    def part_1(self):
        for line in self.input_lines():
            direction, distance = line[0], int(line[1:])
            if direction == 'L':
                self.start = (self.start - distance) % 100
            elif direction == 'R':
                self.start = (self.start + distance) % 100
            if self.start == 0:
                self.password += 1

        return self.password

    def part_2(self):
        for line in self.input_lines():
            direction, distance = line[0], int(line[1:])

            if direction == 'L':
                travels = list(range(self.start - 1, self.start - distance - 1, -1))
                self.start = travels[-1]
                if self.start < 0:
                    self.start = self.start % 100
                self.password += sum(1 for i in travels if i % 100 == 0)

            elif direction == 'R':
                travels = list(range(self.start + 1, self.start + distance + 1, 1))
                self.start = travels[-1] % 100
                self.password += sum(1 for i in travels if i % 100 == 0)

        return self.password


Day01(__file__).solve()
