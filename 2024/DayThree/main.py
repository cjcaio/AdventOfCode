class AoC:
    def __init__(self):
        self.script = 'script.txt'

    def run(self):
        self.read_input()
        possible = self.look_for_m(self.input)
        possible = self.delimitate_possible_mul(possible)
        possible = self.look_for_comma_and_check_ints_in_parenthesis(possible)
        possible = self.get_only_nums(possible)
        answer = self.get_num_the_multiply(possible)

    def read_input(self):
        with open(self.script, "r") as f:
            self.input = f.read().splitlines()

    def look_for_m(self, input):
        possible = []
        for i in input:
            for j in range(len(i)):
                if i[j] == 'm':
                    if i[j+3] == '(':
                        possible.append(i[j:j+12])

        return possible

    def delimitate_possible_mul(self, possible):
        new_possible = []
        for i in possible:
            for j in range(len(i)):
                if i[j] == ')':
                    new_possible.append(i[0:j+1])

        return new_possible

    def look_for_comma_and_check_ints_in_parenthesis(self, possible):
        new_possible = []
        for i in possible:
            for j in range(len(i)):
                if i[j] == ',':
                   new_possible.append(i)

        return new_possible

    def get_only_nums(self, possible):
        new_possible = []
        for i in possible:
            for j in range(len(i)):
                if i[j] == '(' and i[-2] != ')':
                    new_possible.append(i[j+1:-1])

        for i in possible:
            for j in range(len(i)):
                if i[j] == ')':
                    new_possible.append(i[j+1:-1])

        return new_possible

    def get_num_the_multiply(self, possible):
        sum = 0
        for i in possible:
            num = int(i[0:i.index(',')]) * int(i[i.index(',')+1:])
            sum += num

        return sum

aoc = AoC()
aoc.run()