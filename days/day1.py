from days import AOCDay, day


@day(1)
class Day1(AOCDay):
    print_debug = "c12"
    test_input = """()())"""

    def common(self, input_data):
        pass

    def part1(self, input_data):
        floor = 0
        for i, c in enumerate(self.input_data):
            if c == "(":
                floor += 1
            elif c == ")":
                floor -= 1
        yield floor

    def part2(self, input_data):
        floor = 0
        for i, c in enumerate(self.input_data):
            if c == "(":
                floor += 1
            elif c == ")":
                floor -= 1
                if floor == -1:
                    yield i + 1
                    break
