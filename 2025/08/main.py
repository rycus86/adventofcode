import math
import sys

from shared.utils import *


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'[{self.x}, {self.y}, {self.z}]'

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def distance(self, other: 'Box'):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)


class Day08(Solution):
    boxes: list[Box]
    distances: list[tuple[float, Box, Box]]

    def setup(self):
        self.boxes = list()
        self.distances = list()

        for line in self.input_lines():
            x, y, z = map(int, line.split(','))
            box = Box(x, y, z)

            for other in self.boxes:
                self.distances.append((box.distance(other), box, other))

            self.boxes.append(box)

        self.distances = list(sorted(self.distances, key=lambda d: d[0]))

    def part_1(self):
        circuit_count = 0
        circuits = dict()
        boxes_by_circuit = defaultdict(set)

        iterations = 10 if len(self.boxes) < 100 else 1000

        for _ in range(iterations):
            _, b1, b2 = self.distances.pop(0)

            c1, c2 = circuits.get(b1), circuits.get(b2)
            if c1 and c2:
                if c1 == c2:
                    continue
                else:
                    circuit_index = c1
                    to_move = boxes_by_circuit[c2]
                    for m in to_move:
                        circuits[m] = c1
                    boxes_by_circuit[c1].update(to_move)
                    boxes_by_circuit[c2].clear()

            elif c1 is None and c2 is None:
                circuit_count += 1
                circuit_index = circuit_count

            elif c1 is None:
                circuit_index = c2

            else:
                circuit_index = c1

            circuits[b1] = circuit_index
            circuits[b2] = circuit_index
            boxes_by_circuit[circuit_index].add(b1)
            boxes_by_circuit[circuit_index].add(b2)

        lengths = list(sorted(map(len, boxes_by_circuit.values()), reverse=True))
        return var_mul(*lengths[:3])

    def part_2(self):
        last_connection = None
        circuit_count = 0
        circuits = dict()
        boxes_by_circuit = defaultdict(set)

        while self.distances:
            _, b1, b2 = self.distances.pop(0)

            c1, c2 = circuits.get(b1), circuits.get(b2)
            if c1 and c2:
                if c1 == c2:
                    continue
                else:
                    circuit_index = c1
                    to_move = boxes_by_circuit[c2]
                    for m in to_move:
                        circuits[m] = c1
                    boxes_by_circuit[c1].update(to_move)
                    boxes_by_circuit[c2].clear()

            elif c1 is None and c2 is None:
                circuit_count += 1
                circuit_index = circuit_count

            elif c1 is None:
                circuit_index = c2

            else:
                circuit_index = c1

            circuits[b1] = circuit_index
            circuits[b2] = circuit_index
            boxes_by_circuit[circuit_index].add(b1)
            boxes_by_circuit[circuit_index].add(b2)

            last_connection = b1.x * b2.x

        return last_connection


Day08(__file__).solve()
