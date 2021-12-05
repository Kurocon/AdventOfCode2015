import ast

from days import AOCDay, day


@day(8)
class Day8(AOCDay):
    print_debug = "c12"
    test_input = """\"\"
\"abc\"
\"aaa\\\"aaa\"
\"\\x27\"""".split("\n")

    def common(self, input_data):
        pass

    def part1(self, input_data):
        tot_char = 0
        tot_mem = 0
        for line in self.input_data:
            tot_char += len(line)
            tot_mem += len(ast.literal_eval(line))
        yield tot_char - tot_mem

    def part2(self, input_data):
        tot_char = 0
        tot_enc = 0
        for line in self.input_data:
            new_line = "\"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\""
            tot_char += len(line)
            tot_enc += len(new_line)
        yield tot_enc - tot_char
