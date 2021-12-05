from collections import defaultdict
from itertools import permutations

from days import AOCDay, day


@day(9)
class Day9(AOCDay):
    print_debug = "c12"
    test_input = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".split("\n")

    destinations = defaultdict(dict)

    def common(self, input_data):
        self.destinations = defaultdict(dict)
        for line in input_data:
            line = line.split(" ")
            self.destinations[line[0]][line[2]] = int(line[4])
            self.destinations[line[2]][line[0]] = int(line[4])

    def path_length(self, path):
        return sum(self.destinations[path[i-1]][path[i]] for i in range(len(path)-1) if path[i] in self.destinations[path[i-1]])

    def part1(self, input_data):
        yield min(map(lambda path: self.path_length(path), permutations(sorted(self.destinations.keys()))))

    def part2(self, input_data):
        yield max(map(lambda path: self.path_length(path), permutations(sorted(self.destinations.keys()))))
