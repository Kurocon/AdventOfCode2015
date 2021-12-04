from days import AOCDay, day


@day(2)
class Day2(AOCDay):
    print_debug = "c12"
    test_input = """2x3x4
1x1x10""".split("\n")

    def common(self, input_data):
        self.input_data = []
        for box in input_data:
            self.input_data.append(list(map(int, box.split('x'))))

    def part1(self, input_data):
        total = 0
        for l, w, h in self.input_data:
            ordered = sorted([l, w, h])
            area = 2 * l * w + 2 * w * h + 2 * h * l
            slack = ordered[0] * ordered[1]
            total += area + slack
        yield total

    def part2(self, input_data):
        total = 0
        for l, w, h in self.input_data:
            ordered = sorted([l, w, h])
            wrap = (ordered[0] * 2) + (ordered[1] * 2)
            slack = l * w * h
            total += wrap + slack
        yield total
