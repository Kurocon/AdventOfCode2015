from days import AOCDay, day


@day(10)
class Day10(AOCDay):
    print_debug = "c12"
    test_input = """111221"""

    def common(self, input_data):
        pass

    def part1(self, input_data):
        inp = self.input_data
        for i in range(40):
            prev_c = None
            counter = 0
            new_inp = ""
            for c in inp:
                if c != prev_c:
                    if prev_c is not None:
                        new_inp += str(counter) + str(prev_c)
                    prev_c = c
                    counter = 1
                else:
                    counter += 1
            new_inp += str(counter) + str(prev_c)
            inp = new_inp
        yield len(inp)

    def part2(self, input_data):
        inp = self.input_data
        for i in range(50):
            prev_c = None
            counter = 0
            new_inp = ""
            for c in inp:
                if c != prev_c:
                    if prev_c is not None:
                        new_inp += str(counter) + str(prev_c)
                    prev_c = c
                    counter = 1
                else:
                    counter += 1
            new_inp += str(counter) + str(prev_c)
            inp = new_inp
        yield len(inp)
