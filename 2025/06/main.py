from shared.utils import *


class Day06(Solution):

    def setup(self):
        pass

    def part_1(self):
        operands = list()
        operations = list()

        for _ in range(len(self.input_lines()[0].split())):
            operands.append(list())

        for line in self.input_lines():
            if '+' in line or '*' in line:
                operations = list(map(str.strip, line.split()))
            else:
                values = list(map(int, line.split()))
                for i, n in enumerate(values):
                    operands[i].append(n)

        for i, op in enumerate(operations):
            f = var_mul if '*' == op else var_sum
            self.add_result(f(*operands[i]))

    def part_2(self):
        ll = list(self.input_lines())
        h = len(ll)
        w = max(map(len, ll))
        for i, line in enumerate(ll):
            if len(line) < w:
                ll[i] += ' ' * (w - len(line))  # pad it with missing spaces

        operator = None
        operands = list()
        for p in range(w):
            operator = ll[-1][p].strip() or operator
            val = ''.join(c for y in range(h - 1) for c in ll[y][p] if c)
            if not val.strip():
                f = var_mul if '*' == operator else var_sum
                self.add_result(f(*operands))
                operands.clear()
            else:
                num = int(val)
                operands.append(num)
        else:
            f = var_mul if '*' == operator else var_sum
            self.add_result(f(*operands))


Day06(__file__).solve()
