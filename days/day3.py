from collections import defaultdict

from days import AOCDay, day


@day(3)
class Day3(AOCDay):
    print_debug = "c12"
    test_input = """^v^v^v^v^v"""

    houses = defaultdict(int)
    pos1 = (0, 0)
    pos2 = (0, 0)

    def common(self, input_data):
        # self.input_data = self.test_input
        self.houses = defaultdict(int)
        self.pos1 = (0, 0)
        self.pos2 = (0, 0)

    def part1(self, input_data):
        for instr in self.input_data:
            self.houses[self.pos1] += 1
            if instr == ">":
                self.pos1 = (self.pos1[0] + 1, self.pos1[1])
            elif instr == "<":
                self.pos1 = (self.pos1[0] - 1, self.pos1[1])
            elif instr == "^":
                self.pos1 = (self.pos1[0], self.pos1[1] + 1)
            elif instr == "v":
                self.pos1 = (self.pos1[0], self.pos1[1] - 1)
        yield len([x for x in self.houses.values() if x >= 1])

    def part2(self, input_data):
        for instr in self.input_data[::2]:
            self.houses[self.pos1] += 1
            if instr == ">":
                self.pos1 = (self.pos1[0] + 1, self.pos1[1])
            elif instr == "<":
                self.pos1 = (self.pos1[0] - 1, self.pos1[1])
            elif instr == "^":
                self.pos1 = (self.pos1[0], self.pos1[1] + 1)
            elif instr == "v":
                self.pos1 = (self.pos1[0], self.pos1[1] - 1)
        for instr in self.input_data[1::2]:
            self.houses[self.pos2] += 1
            if instr == ">":
                self.pos2 = (self.pos2[0] + 1, self.pos2[1])
            elif instr == "<":
                self.pos2 = (self.pos2[0] - 1, self.pos2[1])
            elif instr == "^":
                self.pos2 = (self.pos2[0], self.pos2[1] + 1)
            elif instr == "v":
                self.pos2 = (self.pos2[0], self.pos2[1] - 1)
        yield len([x for x in self.houses.values() if x >= 1])
