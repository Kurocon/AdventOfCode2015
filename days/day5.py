from collections import Counter
import re

from days import AOCDay, day


@day(5)
class Day5(AOCDay):
    print_debug = "c12"
    test_input = """ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb""".split("\n")
    test_input2 = """qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy""".split("\n")

    DOUBLE = re.compile(r'(.)\1')
    DOUBLE_PAIR = re.compile(r'(.)(.).*\1\2')
    REPEAT = re.compile(r'(.)(.)\1')

    def is_nice_1(self, string):
        count = Counter(string)
        has_three_vowels = (count['a'] + count['e'] + count['i'] + count['o'] + count['u']) >= 3
        has_double_letter = bool(re.search(self.DOUBLE, string))
        has_no_bad_words = all(x not in string for x in ["ab", "cd", "pq", "xy"])
        return has_three_vowels and has_double_letter and has_no_bad_words

    def is_nice_2(self, string):
        has_double_pair = bool(re.search(self.DOUBLE_PAIR, string))
        has_repeat = bool(re.search(self.REPEAT, string))
        return has_double_pair and has_repeat

    def common(self, input_data):
        pass

    def part1(self, input_data):
        yield sum(self.is_nice_1(s) for s in self.input_data)

    def part2(self, input_data):
        yield sum(self.is_nice_2(s) for s in self.input_data)
