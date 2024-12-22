from multiprocessing.connection import answer_challenge


class AoC:
    def __init__(self):
        self.script = 'script.txt'
        self.input = []

    def read_input(self):
        with open(self.script, "r") as f:
            self.input = f.read().splitlines()

    def check_inc_dec(self, input):
        first_validator_lists = []
        for i in input:
            line_list = list(map(int, i.split()))  ## here i made this to turn each line in List type before checking
            last_num = 0
            pattern_check = []
            for j in range(len(line_list)):
                if j == 0:
                    if line_list[0] < line_list[1]:
                        pattern_check.append(1)
                        continue

                elif line_list[j] > last_num:
                    pattern_check.append(1)
                else:
                    pattern_check.append(0)
                last_num = line_list[j]
            keep_pattern = all(x == pattern_check[0] for x in pattern_check) ## its a bool - False -> the leves arent either ALL increasing or decreasing

            if keep_pattern:
                first_validator_lists.append(line_list)

        return first_validator_lists  ## return a MATRIX (list of lists) which passes the first validor


    def check_abs_difference(self, input):
        second_validator_lists = []
        for line_list in input:
            pattern_check = []
            for j in range(len(line_list) - 1):
                if 0< abs(line_list[j] - line_list[j+1]) <= 3:
                    pattern_check.append(1)
                else:
                    pattern_check.append(0)

            keep_pattern = all(x == pattern_check[0] for x in pattern_check)  ## its a bool - False -> the leves arent either ALL increasing or decreasing

            if keep_pattern:
                second_validator_lists.append(line_list)

        return second_validator_lists

    def get_sum_of_lists(self, input):
        sum = len(input)

        return sum

    def run(self):
        self.read_input()
        first_validator_lists = self.check_inc_dec(self.input)
        second_validator_lists = self.check_abs_difference(first_validator_lists)
        answer = self.get_sum_of_lists(second_validator_lists) ## answer to the challenge

        print(answer)



aoc = AoC()
aoc.run()