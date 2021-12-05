from days import AOCDay, day


@day(7)
class Day7(AOCDay):
    print_debug = "c12"
    test_input = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""".split("\n")

    rules = {}

    def common(self, input_data):
        self.rules = {}
        for line in input_data:
            line = line.split(" -> ")
            self.rules[line[1]] = line[0]

    @staticmethod
    def f_not(x):
        return (~x) % 65536

    @staticmethod
    def f_and(x, y):
        return (x & y) % 65536

    @staticmethod
    def f_or(x, y):
        return (x | y) % 65536

    @staticmethod
    def f_rshift(x, y):
        return (x >> y) % 65536

    @staticmethod
    def f_lshift(x, y):
        return (x << y) % 65536

    def eval(self, wire):
        try:
            return int(wire)
        except ValueError:
            pass
        instr = self.rules[wire].split(" ")
        if len(instr) == 1:
            try:
                result = int(instr[0])
            except ValueError:
                result = self.eval(instr[0])
        elif len(instr) == 2:  # NOT
            result = self.f_not(self.eval(instr[1]))
        elif len(instr) == 3:
            if instr[1] == "AND":
                result = self.f_and(self.eval(instr[0]), self.eval(instr[2]))
            elif instr[1] == "OR":
                result = self.f_or(self.eval(instr[0]), self.eval(instr[2]))
            elif instr[1] == "LSHIFT":
                result = self.f_lshift(self.eval(instr[0]), self.eval(instr[2]))
            elif instr[1] == "RSHIFT":
                result = self.f_rshift(self.eval(instr[0]), self.eval(instr[2]))
            else:
                raise ValueError(f"Unknown instr {instr}")
        else:
            raise ValueError(f"Unknown instr {instr}")
        self.rules[wire] = str(result)
        return result

    def part1(self, input_data):
        yield self.eval('a')

    def part2(self, input_data):
        ares = self.part1(self.input_data).__next__()
        self.common(self.input_data)
        self.rules['b'] = str(ares)
        yield self.eval('a')
