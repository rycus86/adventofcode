from shared.utils import *


class Day11(Solution):
    graph: Graph

    def setup(self):
        rack = dict()
        for line in self.input_lines():
            start, end = line.split(':')
            devices = end.strip().split(' ')
            rack[start] = devices

        self.graph = Graph(rack)

    def part_1(self):
        queue = ['you']
        while queue:
            node = queue.pop(0)
            if node == 'out':
                self.add_result()
            else:
                queue.extend(self.graph.get_neighbours(node))

    def part_2(self):
        order = self.graph.topological_order()

        # going through dac then fft
        self.add_result(
            self.graph.count_paths('svr', 'dac', topological_order=order) *
            self.graph.count_paths('dac', 'fft', topological_order=order) *
            self.graph.count_paths('fft', 'out', topological_order=order)
        )

        # going through fft then dac
        self.add_result(
            self.graph.count_paths('svr', 'fft', topological_order=order) *
            self.graph.count_paths('fft', 'dac', topological_order=order) *
            self.graph.count_paths('dac', 'out', topological_order=order)
        )


Day11(__file__).solve()
