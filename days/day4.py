from days import AOCDay, day
import hashlib


@day(4)
class Day4(AOCDay):
    print_debug = "c12"
    test_input = """abcdef"""

    def common(self, input_data):
        pass

    def part1(self, input_data):
        i = 0
        while True:
            i += 1
            key = f"{self.input_data}{i}"
            hash = hashlib.md5(key.encode("utf-8")).hexdigest()
            if hash[0:5] == "00000":
                yield i
                break

    def part2(self, input_data):
        i = 0
        while True:
            i += 1
            key = f"{self.input_data}{i}"
            hash = hashlib.md5(key.encode("utf-8")).hexdigest()
            if hash[0:6] == "000000":
                yield i
                break
