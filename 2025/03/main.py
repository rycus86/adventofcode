from shared.utils import *


class Day03(Solution):
    banks: list[str]

    def setup(self):
        self.banks = list(self.input_lines())

    def part_1(self):
        for bank in self.banks:
            self.add_result(int(self.pick_next(bank, 2)))

    def part_2(self):
        for bank in self.banks:
            self.add_result(int(self.pick_next(bank, 12)))

    def pick_next(self, bank: str, remaining):
        if remaining == 0:
            return ''

        max_val = max(bank)
        max_pos = bank.index(max_val)
        tail = bank[max_pos:]
        tail_len = len(tail)

        if tail_len == remaining:
            return bank[max_pos:]
        elif tail_len < remaining:
            return self.pick_next(bank[:max_pos], remaining - tail_len) + tail
        else:
            return max_val + self.pick_next(bank[max_pos+1:], remaining - 1)

Day03(__file__).solve()
