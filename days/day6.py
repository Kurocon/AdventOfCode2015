from collections import defaultdict

from days import AOCDay, day


@day(6)
class Day6(AOCDay):
    print_debug = "c12"
    test_input = """turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500""".split("\n")
    test_input2 = """turn on 0,0 through 0,0
toggle 0,0 through 999,999""".split("\n")

    grid = defaultdict(int)

    def common(self, input_data):
        self.grid = defaultdict(int)
        instrs = []
        for line in input_data:
            line = line.split(" ")
            if line[0] == "toggle":
                start = list(map(int, line[1].split(',')))
                end = list(map(int, line[3].split(',')))
                instrs.append(["toggle", *start, *end])
            elif line[0] == "turn":
                start = list(map(int, line[2].split(',')))
                end = list(map(int, line[4].split(',')))
                instrs.append([line[1], *start, *end])
        self.input_data = instrs

    def part1(self, input_data):
        for instr, startx, starty, endx, endy in self.input_data:
            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    if instr == "on":
                        self.grid[x, y] = 1
                    elif instr == "off":
                        self.grid[x, y] = 0
                    elif instr == "toggle":
                        self.grid[x, y] = 1 if self.grid[x, y] == 0 else 0
        yield sum(self.grid.values())

    def part2(self, input_data):
        for instr, startx, starty, endx, endy in self.input_data:
            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    if instr == "on":
                        self.grid[x, y] += 1
                    elif instr == "off":
                        self.grid[x, y] = max(self.grid[x, y] - 1, 0)
                    elif instr == "toggle":
                        self.grid[x, y] += 2
        yield sum(self.grid.values())
